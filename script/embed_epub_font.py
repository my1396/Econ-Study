#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["fonttools"]
# ///
"""
embed_epub_font.py
------------------
Embed a subsetted font into an EPUB so Apple Books (Mac / iPad / iPhone)
displays the typeface the book's CSS asks for, e.g. 楷体 paragraphs in
Chinese books converted from Kindle format.

Problem
-------
Symptom : the book shows 宋体/楷体 correctly in calibre ebook-viewer, but
          in Apple Books every paragraph uses the same font, even with
          「Aa」→「原始」 selected.
Cause   : the EPUB contains no font files. Its CSS only names fonts, e.g.
              font-family: STKai, "MKai PRC", Kai, "楷体";
          calibre looks these names up among the installed system fonts;
          Apple Books ignores CSS fonts unless the book opts in with
          `specified-fonts`, and on iPad/iPhone cannot use these fonts
          even then.

Fixes applied
-------------
1. Add META-INF/com.apple.ibooks.display-options.xml with
   specified-fonts = true, so Books honours the book's CSS fonts.
2. Find CSS rules whose font-family matches --match (default: kai, 楷),
   collect the characters used by elements with those selectors, and
   subset --font to just those characters (25 MB -> ~2 MB).
3. Add the subset to fonts/, register it in the OPF manifest, add an
   @font-face rule, and prepend the embedded family to the matched
   font-family declarations (the original names stay as fallbacks).
4. Append "PingFang SC", sans-serif to font-family declarations matching
   --sans-match (default: hei, 黑), so 黑体 headings use 苹方 on iPad/iPhone,
   where Kindle names like "MYing Hei S", Hei, "黑体" don't exist.
5. Append `body { font-family: --body-font }` so body text uses 宋体
   instead of Books' default sans-serif (苹方). Rules on the book's own
   body classes still take precedence.
6. Repack with `mimetype` as the first, uncompressed entry.

Usage
-----
    uv run embed_epub_font.py <book.epub> [-o out.epub] [options]

Options
-------
    --font PATH        font to embed (.ttf/.otf/.ttc);
                       default ~/Library/Fonts/LXGWWenKai-Regular.ttf
    --font-number N    face index inside a .ttc collection (default 0)
    --match WORD ...   font-family keywords to replace (default: kai 楷)
    --family NAME      CSS family name for the embedded font (default EmbedKai)
    --sans-match WORD ...
                       font-family keywords that get "PingFang SC", sans-serif
                       appended (default: hei 黑); pass no words to skip
    --body-font CSS    body font stack; "" to skip
                       (default: "Songti SC", STSong, serif)
    --all-chars        subset to every character in the book instead of
                       only the matched elements

Examples
--------
    uv run embed_epub_font.py "曾国藩家书.epub"
    uv run embed_epub_font.py book.epub -o book-AppleBooks.epub --all-chars
    uv run embed_epub_font.py book.epub --match hei 黑 --family EmbedHei \\
        --font ~/Library/Fonts/SourceHanSansSC-Regular.otf --sans-match \\
        --body-font ""

Without uv: install fonttools in a virtual environment and run the script
with that environment's python3.
"""

import argparse
import os
import re
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from urllib.parse import unquote

try:
    from fontTools import subset
    from fontTools.ttLib import TTFont
except ImportError:
    sys.exit("fontTools not found. Run with `uv run embed_epub_font.py ...` "
             "or install it: pip install fonttools")


DISPLAY_OPTIONS = """<?xml version="1.0" encoding="UTF-8"?>
<display_options>
  <platform name="*">
    <option name="specified-fonts">true</option>
  </platform>
</display_options>
"""
DISPLAY_OPTIONS_PATH = "META-INF/com.apple.ibooks.display-options.xml"
CSS_RULE = re.compile(r"([^{}]+)\{([^{}]*)\}")
FONT_FAMILY = re.compile(r"(font-family\s*:\s*)([^;}]+)", re.I)
GENERIC_FAMILY = re.compile(r"\b(serif|sans-serif|monospace|cursive|fantasy|system-ui)\b")
SANS_FALLBACK = '"PingFang SC", sans-serif'
FONT_MEDIA_TYPES = {".ttf": "application/x-font-ttf",
                    ".otf": "application/vnd.ms-opentype"}


def find_opf(root: Path) -> Path:
    container = ET.parse(root / "META-INF" / "container.xml").getroot()
    for el in container.iter():
        if el.tag.endswith("rootfile"):
            return root / el.get("full-path")
    sys.exit("No rootfile in META-INF/container.xml")


def read_manifest(opf: Path):
    """Return (css files, xhtml files) listed in the OPF manifest."""
    css, xhtml = [], []
    for el in ET.parse(opf).getroot().iter():
        if not el.tag.endswith("}item"):
            continue
        path = opf.parent / unquote(el.get("href", ""))
        media = el.get("media-type", "")
        if media == "text/css":
            css.append(path)
        elif media in ("application/xhtml+xml", "text/html"):
            xhtml.append(path)
    return css, xhtml


def parse_selector(selector: str):
    """Reduce a selector to (tag, classes) of the element it targets.

    Returns None when the selector is too complex to match by tag/class
    (attribute selectors, *, ids only), in which case all characters
    are used.
    """
    last = re.split(r"[\s>+~]+", selector.strip())[-1]
    last = re.sub(r"::?[\w-]+(\([^)]*\))?", "", last)
    if not last or "[" in last or "*" in last:
        return None
    tag = re.match(r"^[A-Za-z][\w-]*", last)
    classes = set(re.findall(r"\.([\w-]+)", last))
    if not tag and not classes:
        return None
    return (tag.group(0).lower() if tag else None, classes)


def has_generic_family(value: str) -> bool:
    unquoted = re.sub(r"\"[^\"]*\"|'[^']*'", "", value.lower())
    return bool(GENERIC_FAMILY.search(unquoted))


def patch_css(css_files, keywords, family, sans_keywords):
    """Prepend `family` to matching font-family declarations, and append
    SANS_FALLBACK to declarations matching `sans_keywords`.

    Returns (files containing `family`, target selectors, need_all_chars).
    """
    modified, targets, need_all = [], [], False

    for css in css_files:
        text = css.read_text(encoding="utf-8")

        def patch_rule(m):
            nonlocal need_all
            selectors, body = m.group(1), m.group(2)
            fm = FONT_FAMILY.search(body)
            if selectors.strip().startswith("@") or not fm:
                return m.group(0)
            raw = fm.group(2)
            value = raw.strip()
            low = value.lower()

            if any(k in low for k in sans_keywords) and not has_generic_family(value):
                value = f"{value}, {SANS_FALLBACK}"
            if any(k in low for k in keywords):
                for sel in selectors.split(","):
                    parsed = parse_selector(sel)
                    if parsed is None:
                        need_all = True
                    else:
                        targets.append(parsed)
                if family not in value:
                    value = f'"{family}", {value}'

            if value == raw.strip():
                return m.group(0)
            trail = raw[len(raw.rstrip()):]
            body = body[:fm.start(2)] + value + trail + body[fm.end(2):]
            return f"{selectors}{{{body}}}"

        new_text = CSS_RULE.sub(patch_rule, text)
        if new_text != text:
            css.write_text(new_text, encoding="utf-8")
        if f'"{family}"' in new_text:
            modified.append(css)
    return modified, targets, need_all


def collect_chars(xhtml_files, targets, all_chars):
    """Characters inside elements matched by `targets` (or the whole book)."""
    chars = set(chr(c) for c in range(0x20, 0x7F))
    for f in xhtml_files:
        try:
            root = ET.parse(f).getroot()
        except ET.ParseError:
            print(f"  ! {f.name}: not well-formed XHTML, using all its text")
            raw = f.read_text(encoding="utf-8", errors="ignore")
            chars |= set(re.sub(r"<[^>]+>", "", raw))
            continue
        for el in root.iter():
            if all_chars:
                if el.tag.endswith("}body"):
                    chars |= set("".join(el.itertext()))
                continue
            tag = el.tag.split("}")[-1].lower()
            classes = set((el.get("class") or "").split())
            if any((t is None or t == tag) and cls <= classes
                   for t, cls in targets):
                chars |= set("".join(el.itertext()))
    return chars - set("\n\r\t")


def subset_font(font_path: Path, font_number: int, chars, out_dir: Path):
    font = TTFont(font_path, fontNumber=font_number)
    cmap = font.getBestCmap()
    missing = sorted(c for c in chars if ord(c) not in cmap and not c.isspace())

    opts = subset.Options()
    opts.layout_features = ["*"]
    opts.name_IDs = ["*"]
    opts.name_languages = ["*"]
    opts.hinting = False
    subsetter = subset.Subsetter(opts)
    subsetter.populate(text="".join(chars))
    subsetter.subset(font)

    ext = ".otf" if "CFF " in font or "CFF2" in font else ".ttf"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{font_path.stem}-subset{ext}"
    font.save(out)
    return out, missing


def add_font_face(css_files, font_file: Path, family):
    for css in css_files:
        text = css.read_text(encoding="utf-8")
        if f'font-family: "{family}";' in text:
            continue
        url = Path(os.path.relpath(font_file, css.parent)).as_posix()
        rule = f'@font-face {{\n  font-family: "{family}";\n  src: url({url});\n}}\n'
        css.write_text(rule + text, encoding="utf-8")


def add_body_font(css: Path, body_font):
    text = css.read_text(encoding="utf-8")
    rule = f"body {{\n  font-family: {body_font};\n}}\n"
    if rule not in text:
        css.write_text(text.rstrip("\n") + "\n\n" + rule, encoding="utf-8")


def register_font(opf: Path, font_file: Path):
    text = opf.read_text(encoding="utf-8")
    href = Path(os.path.relpath(font_file, opf.parent)).as_posix()
    if f'href="{href}"' in text:
        return
    item_id, n = "embed-font", 1
    while f'id="{item_id}"' in text:
        n += 1
        item_id = f"embed-font{n}"
    m = re.search(r"\s*</(\w+:)?manifest>", text)
    if not m:
        sys.exit("No </manifest> in OPF")
    prefix = m.group(1) or ""
    item = (f'\n    <{prefix}item id="{item_id}" href="{href}" '
            f'media-type="{FONT_MEDIA_TYPES[font_file.suffix]}"/>')
    opf.write_text(text[:m.start()] + item + text[m.start():], encoding="utf-8")


def ensure_display_options(root: Path):
    path = root / DISPLAY_OPTIONS_PATH
    if not path.exists():
        path.write_text(DISPLAY_OPTIONS, encoding="utf-8")
        return
    text = path.read_text(encoding="utf-8")
    opt = re.compile(r'(<option name="specified-fonts">)\s*\w+\s*(</option>)')
    if opt.search(text):
        text = opt.sub(r"\1true\2", text)
    elif '<platform name="*">' in text:
        text = text.replace('<platform name="*">', '<platform name="*">\n'
                            '    <option name="specified-fonts">true</option>', 1)
    else:
        print(f"  ! {DISPLAY_OPTIONS_PATH} exists; add specified-fonts manually")
        return
    path.write_text(text, encoding="utf-8")


def repack(root: Path, out: Path):
    out.unlink(missing_ok=True)
    if not (root / "mimetype").exists():
        (root / "mimetype").write_text("application/epub+zip", encoding="ascii")
    with zipfile.ZipFile(out, "w") as z:
        z.write(root / "mimetype", "mimetype", compress_type=zipfile.ZIP_STORED)
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if not d.startswith((".", "__MACOSX"))]
            for name in sorted(filenames):
                path = Path(dirpath) / name
                arc = path.relative_to(root).as_posix()
                if arc == "mimetype" or name.startswith("."):
                    continue
                z.write(path, arc, compress_type=zipfile.ZIP_DEFLATED)


def main():
    parser = argparse.ArgumentParser(
        description="Embed a subsetted font into an EPUB for Apple Books")
    parser.add_argument("epub", type=Path, help="input EPUB (left unchanged)")
    parser.add_argument("-o", "--output", type=Path,
                        help="output EPUB (default: <input>-AppleBooks.epub)")
    parser.add_argument("--font", type=Path,
                        default=Path("~/Library/Fonts/LXGWWenKai-Regular.ttf").expanduser())
    parser.add_argument("--font-number", type=int, default=0)
    parser.add_argument("--match", nargs="+", default=["kai", "楷"])
    parser.add_argument("--family", default="EmbedKai")
    parser.add_argument("--sans-match", nargs="*", default=["hei", "黑"])
    parser.add_argument("--body-font", default='"Songti SC", STSong, serif')
    parser.add_argument("--all-chars", action="store_true")
    args = parser.parse_args()

    if not args.epub.is_file():
        sys.exit(f"Not found: {args.epub}")
    if not args.font.is_file():
        sys.exit(f"Font not found: {args.font}")
    out = args.output or args.epub.with_name(f"{args.epub.stem}-AppleBooks.epub")
    if out.resolve() == args.epub.resolve():
        sys.exit("Output must differ from input")
    keywords = [k.lower() for k in args.match]
    sans_keywords = [k.lower() for k in args.sans_match]

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        with zipfile.ZipFile(args.epub) as z:
            z.extractall(root)
        opf = find_opf(root)
        css_files, xhtml_files = read_manifest(opf)

        modified, targets, need_all = patch_css(css_files, keywords, args.family,
                                               sans_keywords)
        if not modified:
            sys.exit(f"No CSS font-family matches {args.match}; nothing to embed")
        print(f"CSS rules matched: {len(targets)} selector(s) in "
              f"{', '.join(c.name for c in modified)}")

        all_chars = args.all_chars or need_all
        if need_all and not args.all_chars:
            print("  ! complex selector found, subsetting to all characters")
        chars = collect_chars(xhtml_files, targets, all_chars)

        font_file, missing = subset_font(args.font, args.font_number, chars,
                                         opf.parent / "fonts")
        print(f"Subset {args.font.name}: {len(chars)} chars -> "
              f"{font_file.stat().st_size / 1e6:.1f} MB")
        if missing:
            print(f"  ! {len(missing)} chars not in font (fall back to the "
                  f"next font in the stack): {''.join(missing[:40])}")

        add_font_face(modified, font_file, args.family)
        if args.body_font:
            add_body_font(modified[0], args.body_font)
        register_font(opf, font_file)
        ensure_display_options(root)
        repack(root, out)

    print(f"Saved: {out} ({out.stat().st_size / 1e6:.1f} MB)")
    print("In Books: delete the old copy first, import this file, "
          "then choose 「Aa」→「原始」.")


if __name__ == "__main__":
    main()
