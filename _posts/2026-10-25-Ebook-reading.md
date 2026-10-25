---
layout: post
title: Ebook reading
tag: life
update: 2026-10-25
---

## Sony Digital Paper

Model: DPT-CP1 10"

As of December 2025, support for the Digital Paper devices and the Digital Paper Application (DPA) software will be discontinued. No further software updates will be available after Digital Paper DPA v1.4.7 is released in June 2024.

[Help Guide](https://helpguide.sony.net/dpt/rp1/v1/en/index.html)

Sort by "Date Modified"

1. Press Home button
2. Tap "All Documents"
3. Select [Date Read] or [Date Modified] to reorder your files.

Turn off the power (Shutdown)

1. Press and hold the ⏻ (Power) button for about 3 seconds.
2. Tap [Yes] to turn off the Digital Paper device.

**Sleep mode**

To extend battery life and prevent unintentional operation of the touchscreen, set the Digital Paper device to sleep mode by pressing the ⏻  (Power) button. The standby screen appears.  
To wake the device, press the ⏻  (Power) button again.



## Books

中文书籍里内嵌字体无法正常显示

以《曾国藩家书》为例：calibre ebook-viewer 中宋体、楷体显示正常，Apple Books 中全书统一为无衬线字体。

**原因**

- 书里其实没有内嵌字体（epub 中没有 `.ttf`/`.otf` 文件），CSS 只写了 Kindle 的字体名，如 `font-family: STKai, "MKai PRC", Kai, "楷体";`，正文没有指定字体。
- calibre 会按字体名去找系统字体（Mac 上恰好有 `Kai`），正文用默认衬线字体（宋体），所以显示正常。
- Apple Books 默认忽略 CSS 中的 `font-family`；书中没有声明 `specified-fonts` 时，即使选「原始」也不按 CSS 排版，正文默认用苹方（无衬线）。
- 声明 `specified-fonts` 后，iPad 上宋体正常（`Songti SC` 为系统字体），但楷体仍不显示：Books 无法通过 CSS 使用 iPad 上的楷体，只能把字体文件放进 epub。

**修改**（Mac、iPad 已验证）

脚本：`script/embed_epub_font.py`，用 `uv` 运行（自动安装 fonttools），原书不会被修改：

```bash
uv run script/embed_epub_font.py "book.epub"              # 输出 book-AppleBooks.epub
uv run script/embed_epub_font.py "book.epub" -o out.epub
uv run script/embed_epub_font.py --help                   # 其他选项
```

默认把霞鹜文楷（`~/Library/Fonts/LXGWWenKai-Regular.ttf`，OFL 授权）裁剪后嵌入楷体段落，下面是脚本做的事。

1. 解包：`unzip book.epub -d book`
2. 新增 `META-INF/com.apple.ibooks.display-options.xml`：

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <display_options>
      <platform name="*">
        <option name="specified-fonts">true</option>
      </platform>
    </display_options>
    ```

3. 裁剪字体，只保留楷体段落（`.kindle-cn-kai` 等）中出现的字符。本书共 3,702 个字符，字体从 25 MB 减到 1.7 MB：

    ```bash
    uvx --from fonttools pyftsubset ~/Library/Fonts/LXGWWenKai-Regular.ttf \
      --text-file=kai_chars.txt \
      --output-file=book/fonts/LXGWWenKai-Regular-subset.ttf \
      --layout-features='*' --name-IDs='*' --name-languages='*' --no-hinting
    ```

4. 修改 `stylesheet.css`：

    ```css
    /* 文件开头（新增）：自定义字体名，避免与系统字体重名 */
    @font-face {
      font-family: "EmbedKai";
      src: url(fonts/LXGWWenKai-Regular-subset.ttf);
    }
    /* 楷体段落：内嵌字体放在第一位，原字体名作为后备 */
    font-family: "EmbedKai", STKai, "MKai PRC", Kai, "楷体";
    /* 黑体标题：iPad 上没有 Hei，补上苹方 */
    font-family: "MYing Hei S", Hei, "黑体", "PingFang SC", sans-serif;
    /* 正文（新增）：用系统自带的宋体 */
    body { font-family: "Songti SC", STSong, serif; }
    ```

5. 在 `content.opf` 的 `<manifest>` 中登记字体：

    ```xml
    <item id="embed-font" href="fonts/LXGWWenKai-Regular-subset.ttf" media-type="application/x-font-ttf"/>
    ```

6. 重新打包，`mimetype` 必须是第一个文件且不压缩：

    ```bash
    cd book
    zip -X0 ../new.epub mimetype
    zip -X9r ../new.epub . -x mimetype -x '.*'
    ```

7. Books 中删除旧版本（书籍 ID 相同，不删会沿用旧版缓存）→ 退出并重开 Books → 导入新版本 → 「Aa」中选「原始」。iPad 通过 iCloud 同步或 AirDrop 获取新版本。

注：

- 只嵌入了楷体；宋体、苹方用 Mac/iPad 系统自带字体。Mac 上楷体段落也会显示为霞鹜文楷，而不是系统的 `Kai`。
- 楷体段落中的粗体由系统模拟加粗。
- 其他书的 CSS 类名、字体名可能不同；脚本按 `font-family` 中的关键字（默认 `kai`、`楷`）查找要替换的规则，可用 `--match` 修改。


