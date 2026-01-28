---
layout: post
title: "LaTeX Bibliography Manager – Zotero"
tag: programming
update: 2025-08-01
---


<a class="top-link hide" href="#" id="js-top">↑</a>

Zotero is a free and open-source reference management software to manage bibliographic data. 
It is available for Windows, macOS, and Linux.

## General Settings

- Disable automatic download pdfs
  
  Preferences > File Handling > Uncheck "Automatically attach associated PDFs and other files when saving items"

### Sync Settings

Use Zotero's [sync](https://www.zotero.org/support/sync#zotero_file_storage) feature to keep your library up to date across multiple devices and back it up to the cloud.

- **Data Syncing**
  
  <img src="https://www.zotero.org/support/_media/preferences_sync_settings_user.png?w=600&tok=44ddef" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

  -   **Sync automatically:** When check, Zotero will start a sync every time you make a change to your library. You can manually start a sync by clicking the sync button (circular green arrow) in the upper-right corner of the Zotero window.

  -   **Sync full-text content:** When checked, Zotero will sync the extracted text contents of your PDFs and other files, allowing you to perform searches across devices regardless of whether files have been downloaded to a particular device. This also allows for full-text searches in the [web library](https://www.zotero.org/mylibrary "/mylibrary").


- **File Syncing**
  
  [使用坚果云 WebDAV 同步](https://b23.tv/0NH8VyM)
  
  [List of WebDAV providers](https://www.zotero.org/support/kb/webdav_services)

  -   **Zotero:**
    
    -   Sync file attachments using [Zotero File Storage](https://www.zotero.org/support/sync#zotero_file_storage "/support/sync#zotero_file_storage").
    -   Each Zotero user is given **300 MB** of free Zotero Storage for attached files.
  
  -   **WebDAV:**
    -   Sync file attachments using [WebDAV storage](https://www.zotero.org/support/sync#webdav "/support/sync#webdav").

    -   Enter the URL for your WebDAV server (note that `/zotero` is added to the end of the URL automatically), your username, and your password.

    -   Click "Verify Server" to check whether Zotero can connect with the server for file syncing.

  -   **Download files:**
    -   **At sync time:** Download all attachment files not already in your local Zotero file storage on your computer each time Zotero syncs.

    -   **As needed:** Only download attachment files when the user attempts to open the file. Useful for reducing the amount of hard disk space Zotero uses for attachments.

--------------------------------------------------------------------------------

## Plugins

### Better Bib(La)Tex 

Useful links:

- [Better BibTeX Homepage](https://retorque.re/zotero-better-bibtex/index.html)
- [GitHub repo](https://github.com/retorquere/zotero-better-bibtex)

--------------------------------------------------------------------------------

How to [install](https://retorque.re/zotero-better-bibtex/installation/) BBT plugin

1. Download `.xpi` file from the GitHub [releases page](https://github.com/retorquere/zotero-better-bibtex/releases).
2. Go to Zotero > Tools > Plugins > Click on the gear in the top-right corner <i class="codicon codicon-settings-gear dynamic-setting-icon" aria-hidden="true" style="font-size:1.5em; vertical-align: middle;"></i> > choose ‘Install Plugin From File…’ > Select the `.xpi` file you downloaded

You can use the same method to install other Zotero plugins.

--------------------------------------------------------------------------------

How to export bibtex items

1. Select the references you want to export in Zotero
2. Right click > Better BibTeX > Copy BibTeX to Clipboard
3. Paste the content into a `.bib` file

--------------------------------------------------------------------------------

Quick-Copy format

1. Go to Preferences (⌘,) > Better BibTeX > Quick-Copy
2. Set Quick-Copy format
   
   - Default Output Format: LaTeX citation
   - Cite Keys

--------------------------------------------------------------------------------

### Cite Keys

Citekeys are generated according to a user-defined formula composed of functions and filters. Broadly, functions grab text from your item, and filters transform that text. 

The default key pattern is `auth.lower + shorttitle(3, 3) + year`:

1. last name of first author without spaces, in lowercase because of the .lower filter
2. The first `n` (default: 3) words of the title, apply capitalization to first `m` (default: 3) of those.
3. year of publication if any,
4. a letter postfix (a, b, c, etc) in case of a clash (this part is always added, you can’t disable it, although you can change it to Zotero-style numeric)

Changing a pattern will only affect items created/changed after you changed the pattern; existing keys are not automatically regenerated when you change the pattern.

If you want your keys to update after a pattern change you will have to select your items, right-click, and select `Refresh`. This will not affect keys you have pinned.

Taking the following reference as an example:

> Zhang, Peng, Olivier Deschenes, Kyle Meng, and Junjie Zhang. “Temperature Effects on Productivity and Factor Reallocation: Evidence from a Half Million Chinese Manufacturing Plants.” Journal of Environmental Economics and Management 88 (March 2018): 1–17. https://doi.org/10.1016/j.jeem.2017.11.001.

| Cite Key Pattern                     | Resulting Cite Key                     |
| ------------------------------------ | -------------------------------------- |
| `auth.lower + shorttitle(3, 3) + year` | `zhangTemperatureEffectsProductivity2018` |
| `auth + shorttitle(3, 3) + year`     | `ZhangTemperatureEffectsProductivity2018` |
| `auth + year`                        | `Zhang2018`                            |
| `auth + year + shorttitle(2, 2)`     | `Zhang2018TemperatureEffects`          |


### Generating cite keys

Editing the formula does not update any citation keys. A new formula takes effect for items changed from that point forward. If you want to apply your new formula, select the items, right-click, and choose `Better BibTeX` → "Refresh BibTeX key".

--------------------------------------------------------------------------------

## Other useful plugins


[Zotero plugins collection](https://www.zotero.org/support/plugins)

- [Add-on Market](https://github.com/syt2/zotero-addons?tab=readme-ov-file): Plugin manager

- [Better Notes](https://github.com/windingwind/zotero-better-notes): Making notes while reading PDFs in Zotero; you can select text in the PDF viewer and right click to add it as a note to the item. The citation key is automatically added. When you click on the citation, it will take you to the corresponding page in the PDF. 👍
  
  You can export notes as latex format.

  Support some simple markdown syntax and keyboard shortcuts.

- [Linter](https://github.com/northword/zotero-format-metadata): format item metadata
- [Attanger](https://github.com/MuiseDestiny/zotero-attanger): organize pdf files in your selected folder.
  
  自动更改文件名称、移动文件到指定文件夹。
  
  一个附加功能是，通过同步文件夹实现多设备同步附件。

- [Zotero Ethereal Style](https://github.com/MuiseDestiny/zotero-style): customize appearance of Zotero interface



--------------------------------------------------------------------------------

## FAQ

Q: How to copy a bibliography entry?  
A: Edit > Copy Bibliography (⇧⌘C).


Q: BibTeX export has no `year` field even though the item has a date. [↩](https://forums.zotero.org/discussion/48645/bibtex-export-date-and-year)  
A: Exporting through BBT as "Better BibTeX" instead of "Better BibLaTeX" uses 'year' instead of 'date'.

<img src="https://drive.google.com/thumbnail?id=1so9BOTBQziGVSSThi2nwlQgpO-ZiwDEm&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />


BibLaTeX exporter: ❌

```
@article{Schlenker2010, |
  title        = {Robust Negative Impacts of Climate Change on {{African}} Agriculture},
  author       = {Schlenker, Wolfram and Lobell, David B},
  date         = {2010-01},
  journaltitle = {Environmental Research Letters},
  volume       = {5},
  number       = {1},
  pages        = {014010},
  issn         = {1748-9326},
  doi          = {10.1088/1748-9326/5/1/014010},
  url          = {http://stacks.iop.org/1748-9326/5/i=1/a=014010},
  urldate      = {2019-01-06}
}
```

BibTeX exporter: ✅

```
@article{Schlenker2010,
  title = {Robust Negative Impacts of Climate Change on {{African}} Agriculture},
  author = {Schlenker, Wolfram and Lobell, David B},
  year = {2010},
  month = jan,
  journal = {Environmental Research Letters},
  volume = {5},
  number = {1},
  pages = {014010},
  issn = {1748-9326},
  doi = {10.1088/1748-9326/5/1/014010},
  urldate = {2019-01-06}
}
```


