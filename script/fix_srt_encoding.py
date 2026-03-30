#!/usr/bin/env python3
"""
fix_srt_encoding.py
-------------------
Fix SRT subtitle files containing Chinese characters so they display
correctly in media players (IINA, VLC, etc.) on macOS.

Problems fixed
--------------
1. Missing UTF-8 BOM
   Symptom : subtitles don't appear at all, even though the file looks
             fine when opened in a text editor.
   Cause   : the file is valid UTF-8 but has no BOM (byte-order mark,
             EF BB BF). macOS media players use the BOM to confirm the
             encoding when Chinese characters are present; without it
             they silently skip the subtitle track.
   Fix     : prepend the UTF-8 BOM.

2. Out-of-order timestamps
   Symptom : subtitles don't appear, or only show briefly then stop.
   Cause   : credit/header blocks at the top of the file carry late
             timestamps (e.g. 00:45:xx), while the actual dialogue
             starts at 00:00:xx. Players expect timestamps to be
             monotonically increasing and abort the track on the
             first backwards jump.
   Fix     : sort all blocks by start timestamp and renumber them
             sequentially (1, 2, 3 …).

3. Wrong encoding (non-UTF-8 files)
   Symptom : subtitles show garbled characters (mojibake).
   Cause   : the file is encoded in a Chinese legacy encoding —
             CP950 / Big5 / GB18030 / UTF-16 — instead of UTF-8.
   Fix     : detect the actual encoding, decode, and re-save as
             UTF-8 with BOM.

4. Double-decoded / mojibake UTF-8
   Symptom : subtitles show garbled characters even though the file
             appears to be UTF-8.
   Cause   : the bytes were decoded with the wrong encoding at some
             point (e.g. CP950 bytes interpreted as GB18030), producing
             valid-looking but wrong UTF-8.
   Fix     : re-encode with the incorrect encoding and decode again
             with the correct one to recover the original characters.

Usage
-----
    python3 fix_srt_encoding.py <folder_path>
    python3 fix_srt_encoding.py <folder_path> --pattern "S02E0[89]"
    python3 fix_srt_encoding.py <folder_path> --dry-run

Examples
--------
    python3 fix_srt_encoding.py "/Users/me/Downloads/拉字至上第一季"
    python3 fix_srt_encoding.py ~/Downloads/subtitles --pattern "S01"
"""

import os
import sys
import glob
import re
import argparse

# Chinese characters used to verify correct decoding
CHINESE_VERIFY = ['翻譯', '字幕', '拉字', '制作', '影視', '第一', '第二', '劇情', '片名']

TS_RE = re.compile(r'(\d{2}:\d{2}:\d{2},\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2},\d{3})')

def is_valid_chinese(text):
    """Check if text contains recognizable Traditional Chinese subtitle content."""
    return any(kw in text for kw in CHINESE_VERIFY)

def ts_to_ms(ts):
    """Convert SRT timestamp string to milliseconds."""
    h, m, rest = ts.split(':')
    s, ms = rest.split(',')
    return int(h)*3600000 + int(m)*60000 + int(s)*1000 + int(ms)

def sort_srt_blocks(text):
    """Sort SRT blocks by start timestamp and renumber sequentially.
    Returns (sorted_text, was_changed)."""
    blocks = [b.strip() for b in text.strip().split('\n\n') if b.strip()]
    parsed = []
    for block in blocks:
        lines = block.split('\n')
        if len(lines) < 2:
            continue
        m = TS_RE.search(lines[1])
        if not m:
            continue
        parsed.append((ts_to_ms(m.group(1)), block))

    sorted_blocks = sorted(parsed, key=lambda x: x[0])
    was_changed = any(a != b for a, b in zip(parsed, sorted_blocks))

    if not was_changed:
        return text, False

    output = []
    for i, (_, block) in enumerate(sorted_blocks, 1):
        lines = block.split('\n')
        lines[0] = str(i)
        output.append('\n'.join(lines))
    return '\n\n'.join(output) + '\n', True

def try_decode_raw_bytes(raw_bytes):
    """Try to decode raw bytes using various Chinese encodings. Returns (content, encoding)."""
    encodings = ['cp950', 'big5hkscs', 'big5', 'gb18030', 'utf-16', 'utf-16-le', 'utf-16-be']
    
    for enc in encodings:
        try:
            content = raw_bytes.decode(enc)
            return content, enc
        except (UnicodeDecodeError, Exception):
            continue
    return None, None

def try_fix_double_decoded(utf8_content):
    """Fix content that was incorrectly decoded (e.g., CP950 bytes decoded as GB18030).
    Returns (fixed_content, src_enc, target_enc) or (None, None, None)."""
    encodings = ['gb18030', 'cp950', 'big5hkscs', 'big5']
    
    for src_enc in encodings:
        for target_enc in encodings:
            if src_enc == target_enc:
                continue
            try:
                original_bytes = utf8_content.encode(src_enc, errors='strict')
                correct_content = original_bytes.decode(target_enc, errors='strict')
                if is_valid_chinese(correct_content):
                    return correct_content, src_enc, target_enc
            except Exception:
                continue
    
    # Try with errors='ignore' as fallback
    for src_enc in encodings:
        for target_enc in encodings:
            if src_enc == target_enc:
                continue
            try:
                original_bytes = utf8_content.encode(src_enc, errors='ignore')
                correct_content = original_bytes.decode(target_enc, errors='ignore')
                if is_valid_chinese(correct_content):
                    return correct_content, src_enc, f'{target_enc} (lossy)'
            except Exception:
                continue
    
    return None, None, None

UTF8_BOM = b'\xef\xbb\xbf'

def fix_srt_file(filepath):
    """Fix encoding of a single SRT file. Returns (status, message)."""
    # First try reading as raw bytes
    with open(filepath, 'rb') as f:
        raw_bytes = f.read()
    
    # Already has UTF-8 BOM — check if valid and contains Chinese
    if raw_bytes.startswith(UTF8_BOM):
        try:
            content = raw_bytes[3:].decode('utf-8')
            if is_valid_chinese(content):
                content, reordered = sort_srt_blocks(content)
                if reordered:
                    with open(filepath, 'wb') as f:
                        f.write(UTF8_BOM + content.encode('utf-8'))
                    return 'fixed', 'UTF-8 with BOM (reordered timestamps)'
                return 'skip', 'Already correct UTF-8 with BOM'
        except UnicodeDecodeError:
            pass  # BOM present but not valid UTF-8 after it — fall through

    # Check if it's valid UTF-8 without BOM
    try:
        content = raw_bytes.decode('utf-8')

        # UTF-8 with Chinese but missing BOM (and maybe out-of-order timestamps)
        if is_valid_chinese(content):
            content, reordered = sort_srt_blocks(content)
            notes = []
            if reordered:
                notes.append('reordered timestamps')
            notes.append('added BOM')
            with open(filepath, 'wb') as f:
                f.write(UTF8_BOM + content.encode('utf-8'))
            return 'fixed', 'UTF-8 → ' + ', '.join(notes)

        # Try to fix double-decoded content
        fixed, src_enc, target_enc = try_fix_double_decoded(content)
        if fixed:
            fixed, reordered = sort_srt_blocks(fixed)
            with open(filepath, 'wb') as f:
                f.write(UTF8_BOM + fixed.encode('utf-8'))
            return 'fixed', f'{src_enc} → {target_enc} → UTF-8 with BOM'

        return 'skip', 'UTF-8 (no Chinese detected, skipping)'

    except UnicodeDecodeError:
        pass  # Not UTF-8, try other encodings

    # Try direct decoding from raw bytes
    content, enc = try_decode_raw_bytes(raw_bytes)
    if content:
        content, _ = sort_srt_blocks(content)
        with open(filepath, 'wb') as f:
            f.write(UTF8_BOM + content.encode('utf-8'))
        return 'fixed', f'{enc} → UTF-8 with BOM'

    return 'fail', 'Could not determine encoding'

def main():
    parser = argparse.ArgumentParser(
        description='Fix SRT subtitle encoding to UTF-8 for Chinese subtitles'
    )
    parser.add_argument('folder', help='Folder containing SRT files')
    parser.add_argument('--pattern', default=None,
                        help='Regex pattern to filter filenames (e.g., "S02E0[89]")')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would be done without making changes')
    args = parser.parse_args()
    
    folder = os.path.expanduser(args.folder)
    if not os.path.isdir(folder):
        print(f"Error: folder not found: {folder}")
        sys.exit(1)
    
    # Find all SRT files
    srt_files = sorted(glob.glob(os.path.join(folder, '*.srt')) +
                       glob.glob(os.path.join(folder, '*.SRT')))
    
    # Filter by pattern if given
    if args.pattern:
        srt_files = [f for f in srt_files if re.search(args.pattern, os.path.basename(f))]
    
    if not srt_files:
        print(f"No SRT files found in: {folder}")
        sys.exit(0)
    
    print(f"Found {len(srt_files)} SRT file(s) in: {folder}")
    if args.dry_run:
        print("[DRY RUN - no changes will be made]")
    print("-" * 70)
    
    fixed = skipped = failed = 0
    
    for filepath in srt_files:
        filename = os.path.basename(filepath)
        
        if args.dry_run:
            print(f"  {filename}")
            continue
        
        status, message = fix_srt_file(filepath)
        
        if status == 'fixed':
            print(f"✓ {filename}\n  └─ {message}")
            fixed += 1
        elif status == 'skip':
            print(f"○ {filename}\n  └─ {message}")
            skipped += 1
        else:
            print(f"✗ {filename}\n  └─ {message}")
            failed += 1
    
    print("-" * 70)
    print(f"Fixed: {fixed}  |  Skipped: {skipped}  |  Failed: {failed}")

if __name__ == '__main__':
    main()
