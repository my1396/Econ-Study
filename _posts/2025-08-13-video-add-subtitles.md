---
layout: post
title: 视频添加字幕
tag: programming
update: 2025-10-24
---

### macos

[mkvtoolnix](https://formulae.brew.sh/formula/mkvtoolnix) is a set of free, open-source tools to edit MKV files. 

Useful features:

- Add subtitles to mkv files using the MKVMerge tool.
  
  It performs soft subs, which means it embeds subtitles as a separate, selectable track within an MKV file, allowing viewers to turn them on or off. 

Limits: only supports MKV video files.

[Download](https://mkvtoolnix.download/downloads.html)

Q: What's the difference between soft subs and hard subs?  
A: Hard subs permanently burns the subtitles into the video itself and cannot be turned off. 


Q: How can I merge multiple video, audio, or subtitle files into a single MKV file?  
A: Refer to [the official document](https://mkvtoolnix.org/how-can-i-merge-multiple-video-audio-or-subtitle-files-into-a-single-mkv-file/).

### Windows

[mkvtoolnix-batch-tool](https://github.com/iPzard/mkvtoolnix-batch-tool) can embed subtitle files into videos in a batch. [<span class="env-orange">Only for Windows OS</span>]

The following file types are supported.

**Video**:

-   *AVI*, *M4V*, *MKV*, *MOV*, *MP4*, *MPG*, *MPEG*, *OGG*, *OGM*, *WEBM*, *WMV*

**Subtitle**:

-   *ASS*, *IDX*, *PGS*, *SMI*, *SRT*, *SSA*, *SUB*, *SUP*, *VTT*

