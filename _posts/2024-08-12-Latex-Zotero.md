---
layout: post
title: "LaTeX Bibliography Manager – Zotero"
tag: programming
update: 2025-08-01
---


<a class="top-link hide" href="#" id="js-top">↑</a>

<img src="{{site.baseurl}}/images/zotero_icon.png" alt="" style="display: inline; height: 2em; vertical-align: middle;" /> Zotero is a free and open-source reference management software to manage bibliographic data. 
It is available for Windows, macOS, and Linux.

## General Settings

- Disable automatic download pdfs and snapshots
  
  Preferences > File Handling > Uncheck 
  
  - "Automatically attach associated PDFs and other files when saving items"
  - "Automatically take snapshots when creating items from web pages"

<a id="base-directory"></a>

- **Base Directory**
  
  Base Directory is useful when you want to store all your attachments in a specific folder, rather than the default Zotero storage folder, i.e., `~/Zotero/storage`. 

  The problem with the default Zotero storage folder is that it use random alphanumeric folder names for each item, making it hard to identify the files.

  To change the Base Directory, go to Zotero > Preferences > Advanced > Files and Folders > Change your "Base Directory" to your desired folder to store attachments. [↩](https://www.zotero.org/support/preferences/advanced#files_and_folders)

  My Base Directory is set to `/Users/menghan/Documents/Zotero`.

  <hr>

  This setting let you access all your attachments on multiple computers even if they are stored in different locations on each computer, as long as you set the Base Directory to the correct sync folder on each computer.

  **Use scenario:** You have two computers, A and B. 
  
  A is a Mac, and set the Base Directory to `/Users/Sarah/Dropbox/PDFs` on A.

  B is a Windows PC, and set the Base Directory to `C:\Users\Sarah\Dropbox\PDFs` on B.

  If you add a pdf attachment within the base directory, Zotero stores a relative path to that base direcotry rather than an absolute path.
  
  <hr>
  Note that this setting does not control where files are stored — only whether linked files within the specified folder are referenced by absolute or relative paths.

  If you want to keep the actual pdfs in the base directory, you can use `Attanger` or `ZotMoov` plugin to move the attachments to the base directory.

  When you set up `Attanger` or `ZotMoov`, make sure the [`Destination Path`](#Attanger-destination-path) is consistent with your `Base Directory`.
  

--------------------------------------------------------------------------------

### Sync Settings

Use Zotero's [sync](https://www.zotero.org/support/sync#zotero_file_storage) feature to keep your library up to date across multiple devices and back it up to the cloud.

- **Data Syncing**

  <img src="https://drive.google.com/thumbnail?id=1qK7_3vzro-jzE9VcmfAYI1bB5w2ckuo9&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

  -   **Sync automatically:** When check, Zotero will start a sync every time you make a change to your library. You can manually start a sync by clicking the sync button (circular green arrow) in the upper-right corner of the Zotero window.

  -   **Sync full-text content:** When checked, Zotero will sync the extracted text contents of your PDFs and other files, allowing you to perform searches across devices regardless of whether files have been downloaded to a particular device. This also allows for full-text searches in the [web library](https://www.zotero.org/mylibrary "/mylibrary").
      
      <span class="env-green">**Uncheck "Sync full-text content" and "Sync attachment files in My Library"**</span> to avoid your Zotero cloud storage being quickly filled up.
      
      Zotero's cloud file storage only provides <span class="env-orange">**300 MB**</span> free space, and syncing full-text content can quickly use up your storage quota. One pdf file is around 3--5 MB, that means you can only sync ~70 files before you run out of free storage. You can buy more storage at $20/year for 2 GB.
      
      <img src="https://drive.google.com/thumbnail?id=1xFpYvjdtYDpcmHEDq-c7uWyTH_oRoOOr&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

      A workaround is to use `Attanger` or `ZotMoov` to manage your attachments in a local folder synced by cloud services or NAS. This way, you get unlimited storage for your attachments.
      See the next section on "Sync local pdf files" for details.


- **File Syncing**
  
  I use NAS to sync my Zotero attachments across multiple devices. So here I uncheck "Sync attachment files in My Library using Zotero".

  Zotero cloud storage is the default option to sync attachments. But it has limited space. An alternative is to use WebDAV.
  
  [List of WebDAV providers](https://www.zotero.org/support/kb/webdav_services)

  -   **Zotero:**
      -   Sync file attachments using [Zotero File Storage](https://www.zotero.org/support/sync#zotero_file_storage "/support/sync#zotero_file_storage").
      
      -   Each Zotero user is given **300 MB** of free Zotero Storage for attached files.
        
  
  -   **WebDAV:**
      -   Sync file attachments using [WebDAV storage](https://www.zotero.org/support/sync#webdav "/support/sync#webdav").

      -   Enter the URL for your WebDAV server (note that `/zotero` is added to the end of the URL automatically), your username, and your password.

      -   Click "Verify Server" to check whether Zotero can connect with the server for file syncing.
      
      -   [使用坚果云 WebDAV 同步](https://b23.tv/0NH8VyM)
  
  -   **Download files:**
      -   **At sync time:** Download all attachment files not already in your local Zotero file storage on your computer each time Zotero syncs.

      -   **As needed:** Only download attachment files when the user attempts to open the file. Useful for reducing the amount of hard disk space Zotero uses for attachments.

--------------------------------------------------------------------------------

### Sync local pdf files

**Issue:** Zotero cloud storage only provides 300 MB free space. If you manage pdf using Zotero, we will quickly run out of space.

**Fix:** Follow the steps below to get <span class="env-green">unlimited attachment Zotero storage</span> using cloud services or NAS. You can use this approach to sync your Zotero attachments across multiple devices without using Zotero's cloud storage.

**Prerequisites:** 

- a sync service and
- Zotero linked file manager plugin, such as `Attanger` or `ZotMoov`. 

**Step by step instructions:**

1. **Create a folder for storing and syncing Zotero attachments.**
   
   This folder will be synced to multiple devices using cloud services or NAS. PDF attachments will be stored in this folder.
   
   I use NAS to sync my Zotero directory, so I create a folder `~/Documents/Zotero` on my local computer.
   
   But if you use cloud services, such as Google Drive, Dropbox, OneDrive, etc., you can create the folder within the local sync folder of these services.
   An example is `~/Google Drive/Zotero`.

2. Change your **Base Directory** to your local sync folder.

   Zotero > Preferences > Files and Folders > Change your "Base Directory" to your local sync folder.

3. In your linked file manager plugin, such as `Attanger` or `ZotMoov`, set the **`Destination Path`** to be the same as your Base Directory.

   This way, all your pdf attachments are stored in your local sync folder, and synced to other devices using your cloud services or NAS.

   See [Attanger](#attanger) for detailed instructions on how to set up synced folders.

**ref:**

- ![img](https://www.gstatic.com/youtube/img/watch/yt_favicon_ringo2.png) [Youtube video: Zotero + Google Drive Sync](https://www.youtube.com/watch?v=BBSEDaUDGOM&list=WL&index=1) start from 8:11

--------------------------------------------------------------------------------

<span style="display:block; font-size:2.5em; font-weight:bold; margin:1em 0;">Plugins</span>

--------------------------------------------------------------------------------

## Better Bib(La)Tex 

Useful links:

- [Better BibTeX Homepage](https://retorque.re/zotero-better-bibtex/index.html)
- [GitHub repo](https://github.com/retorquere/zotero-better-bibtex)

--------------------------------------------------------------------------------

How to [install](https://retorque.re/zotero-better-bibtex/installation/) BBT plugin

1. Download `.xpi` file from the GitHub [releases page](https://github.com/retorquere/zotero-better-bibtex/releases).
2. Go to Zotero > Tools > Plugins > Click on the gear in the top-right corner <i class="codicon codicon-settings-gear dynamic-setting-icon" aria-hidden="true" style="font-size:1.5em; vertical-align: middle;"></i> > choose ‘Install Plugin From File…’ > Select the `.xpi` file you downloaded

You can use the same method to install other Zotero plugins.

<img src="https://drive.google.com/thumbnail?id=1qtP45q_HrQHaxQDZOqVzkdB9wfUcH36Z&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

--------------------------------------------------------------------------------

**How to export bibtex items**

1. Select the references you want to export in Zotero
2. Right click > Better BibTeX > Copy <span class="env-green">BibTeX</span> to Clipboard
3. Paste the content into a `.bib` file

--------------------------------------------------------------------------------

### Quick-Copy format

If you just want to quickly add references to a paper, you can use the Quick-Copy feature.

1. Go to Preferences (⌘,) > Better BibTeX > Quick-Copy
2. Set Quick-Copy format.
   
   [Possible options:](https://retorque.re/zotero-better-bibtex/preferences/export/index.html#quick-copy)
   - Default Output Format: LaTeX citation
   - Cite Keys


--------------------------------------------------------------------------------

Edit > Copy **Citation** (⇧⌘A) to copy the citation in the selected format.

> Piergallini, “Corporate Finance and Interest Rate Policy.”

--------------------------------------------------------------------------------

<a id="copy-bibliography"></a>
Edit > Copy **Bibliography** (⇧⌘C) 

The default style is Chicago Manual of Style 18th edition (shortened notes and bibliography).

> Piergallini, Alessandro. “Corporate Finance and Interest Rate Policy.” Preprint, SSRN, 2024. https://doi.org/10.2139/ssrn.5009544.

You can change the default style in Preferences > Export > Quick Copy > Item Format. 

<img src="https://drive.google.com/thumbnail?id=16tjFqgw5jylCLWzdXcUpePu-x47hHcyS&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

I change the Item Format `Better BibTeX`. So when I do <span class="env-green">⇧⌘C</span>, it will copy the bibliography in BibTeX format.

```
@article{piergallini2024corporate,
  title={Corporate Finance and Interest Rate Policy},
  author={Piergallini, Alessandro},
  year={2024},
  publisher={SSRN}
}
```

A <span class="env-orange">side effect</span> after setting `Better BibTeX` as the Item Format is that you cannot copy citations using shortcut ⇧⌘A anymore. And the Edit menu does not have the `Copy Citation` option anymore.

A workaround is to right click on the item and choose "Create Bibliography from Item..."

<img src="https://drive.google.com/thumbnail?id=1Cj09Jv7vn3N24eRYiRDzAhg5kCIr-V2u&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:30%;" />


--------------------------------------------------------------------------------

### Cite Keys

Citekeys are generated according to a user-defined formula composed of functions and filters. Broadly, 

- **Functions** grab text from your item, and 
  
  Examples of functions (field markers): `auth`, `title`, `year`, `shorttitle(n, m)`, etc.


- **Filters** transform that text. 
  
  Examples of filters: `.lower`, `.upper`, `.abbr`, etc.

  - `.lower`: convert to lowercase
  - `.upper`: convert to uppercase
  - `.abbr`: abbreviate names. 
    - `journal.abbr` would use the first letters abbreviations of each word in the journal name, using uppercase letters by default.
      
      For example, `Journal of Fish Biology` produces `JoFB`.
    - `title.abbr` would from the title `An awesome paper on JabRef` produce `AAPoJ`

  Note that you can have multiple filters chained together, e.g., `journal.lower.abbr`. For examples, `Journal of Fish Biology` would become `jofb`.


[Cite key formatting syntax](https://docs.jabref.org/setup/citationkeypatterns)

--------------------------------------------------------------------------------

The default key pattern is `auth.lower + shorttitle(3, 3) + year`:

1. last name of first author without spaces, in lowercase because of the .lower filter
2. The <span class="env-green">first `n` (default: 3) words</span> of the title, apply <span class="env-green">capitalization to first `m` (default: 3)</span> of those.
3. year of publication if any,
4. a letter postfix (a, b, c, etc) in case of a clash (this part is always added, you can’t disable it, although you can change it to Zotero-style numeric)

Changing a pattern will only affect items created/changed after you changed the pattern; existing keys are <span class="env-orange">NOT automatically updated</span> when you change the pattern.

If you want your keys to update after a pattern change, you will have to select your items, right-click > Better BibTeX > Select `Refresh BibTeX key`. This will not affect keys you have pinned.

Taking the following reference as an example:

> Zhang, Peng, Olivier Deschenes, Kyle Meng, and Junjie Zhang. “Temperature Effects on Productivity and Factor Reallocation: Evidence from a Half Million Chinese Manufacturing Plants.” Journal of Environmental Economics and Management 88 (March 2018): 1–17. https://doi.org/10.1016/j.jeem.2017.11.001.

| Cite Key Pattern                     | Resulting Cite Key                     |
| ------------------------------------ | -------------------------------------- |
| `auth.lower + shorttitle(3, 3) + year` | `zhangTemperatureEffectsProductivity2018` |
| `auth + shorttitle(3, 3) + year`     | `ZhangTemperatureEffectsProductivity2018` |
| `auth + year`                        | `Zhang2018`                            |
| `auth + year + shorttitle(2, 2)`     | `Zhang2018TemperatureEffects`          |


### Generating cite keys

Editing the formula does not update any citation keys. A new formula takes effect for items changed from that point forward. 

If you want to apply your new formula to existing items, select the items, right-click, and choose `Better BibTeX` → "Refresh BibTeX key".


--------------------------------------------------------------------------------

## Attanger

Same function as [ZotMoov](https://github.com/wileyyugioh/zotmoov). They are used to automatically move pdf attachments and link them. Previously, Zotfile does the same job, but it is no longer compatible with Zotero 7+.

[Attanger](https://github.com/MuiseDestiny/zotero-attanger) puts your literature at one local directory following your library structure, with meaningful file names which help you identify the files quickly. You can use any cloud services or NAS to sync the local directory to multiple devices.

This way, you use Zotero as a pdf viewer and make annotations, which will be synced to all your devices. <span class="env-orange">One drawback</span> is that the annotations made using Zotero pdf viewer are not visible if you open the pdf using other pdf readers, such as Adobe Acrobat or Preview on macOS.

If you add annotation using Preview, when you open it using Zotero pdf viewer, the annotations are visible. But if you add annotation using Zotero pdf viewer, when you open it using Preview, the annotations are not visible.

- Zotero pdf viewer: annotation saved in Zotero. As long as you have Zotero installed, you can see the annotations.

  <img src="https://www.zotero.org/static/images/blog/6.0/pdf-reader.jpg" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />
  
  Let me try to use Zotero pdf viewer as my main pdf reader when I do literature review.
  See how it goes and decide if I want to stick to it or go back to Preview.

  What I like about Zotero pdf viewer: 
  
  - Add quotes linked to bibliography entries in Better Notes.
    
    You can select figure and add to Better Notes too.
  
  - Add comment on highlighted text. ← Not possible on Preview.
  - Hover over hyperlink to see the referenced object, Figure/Table/Eqn/bibliography, etc. ← Not possible on Preview.
  - Other basic annotation functions, such as highlight, underline, sticky notes. ← Supported by Preview.
  - You can set pdf viewer themes, like changing background color to sepia, dark mode, etc. ← Not possible on Preview.
  
  See [HERE](https://www.zotero.org/support/pdf_reader) for documentation of PDF reader in Zotero.

- Mac Preview: annotation saved in the pdf file. The annotations are visible everywhere, such as web browsers, etc.

**Annotation direction:**

Preview → Zotero ✅  
Zotero → Preview ❌


--------------------------------------------------------------------------------

**Attanger settings:**

- `Source Path` (源路径): This can be set to the `~/Downloads` folder where Zotero will retrieve newly added files and attach it to ZOtero Item/Collection.
  
  This is the local directory where your browser downloads files to.

- `Attach Path` (附加类型): Leave it as `Link`. This is the default.

<a id="Attanger-destination-path"></a>

- <span class="env-green">**`Destination Path`**</span> (靶路径): This is the directory to move files to. Set it to your [`Base Directory`](#base-directory).
  
  This is the local directory to move the attachments to. I set it to <span class="env-green">`~/Documents/Zotero`</span>.
  
  I sync this file using NAS. You can use any cloud services instead, such as Google Drive, Dropbox, OneDrive, etc.

--------------------------------------------------------------------------------

After configuring Attanger, when you download a pdf file from the web, it will first be saved to your `Source Path` (e.g., `~/Downloads`).

Then, in Zotero, right click on the item you want to attach the pdf to, and choose `Attanger` > `Attach New File`. It will identify the latest file in your `Source Path`, move it to your `Destination Path`, and attach it to the Zotero item.

For *existing attachments*, the pdf files are still stored in the default Zotero storage folder (`~/Zotero/storage`) with random alphanumeric folder names.
If you want to move these attachments to your `Destination Path`, you can select the items, right click, and choose `Attanger` > `Move Attachment`. The pdf files will be moved to the destination path.

<img src="https://drive.google.com/thumbnail?id=1NNffhdffd9CD4i1T-GJB0BAydHIE3V2D&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

Note that linked files that are managed/tracked by Attanger will show a link ∞ on top of the file icon <img src="{{site.baseurl}}/images/link.png" alt="" style="display: inline; height: 1.5em; vertical-align: middle;" />.

ref:

- [US Berkeley Library: ZotMoov](https://guides.lib.berkeley.edu/zotero/zotfile)
- [Zotero hacks: reliably setup unlimited storage for you personal academic library, @Ilya Kashnitsky](https://ikashnitsky.phd/2024/zotero7/)

--------------------------------------------------------------------------------

## Ethereal Style

This plugin customizes the appearance of the Zotero interface to make it cleaner and more visually appealing.

⇧P to start a command palette to quickly access various functions provided by Ethereal Style.

Highlight features:

- Title: As the background of title, reading progress visually reflect the distribution of your reading time of each page for the PDF under a item, the darker the color the longer the reading time.


[Ethereal Style 中文教程](https://www.notion.so/Zotero-Style-bc2aebbbb6df4b7baa858e376e4fc5be)

--------------------------------------------------------------------------------

## Useful plugins

[Zotero plugins collection](https://www.zotero.org/support/plugins)

- [Add-on Market](https://github.com/syt2/zotero-addons?tab=readme-ov-file): Plugin manager.
  
  By default, you need to download the `.xpi` file from GitHub releases page and install it manually. But with this add-on, you can search and install plugins directly from Zotero interface.
  
  You can also update and remove plugins directly from this add-on. 

  Click click and choose "Homepage" to go to the GitHub repo of the plugin.
  
  <img src="https://drive.google.com/thumbnail?id=1wESPOKeoVtHGWEbAMIS-Fg6_QZYkijwQ&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

- [Better BibTeX](https://retorque.re/zotero-better-bibtex/index.html)

  Set Citation keys to `auth + year`.

- [Attanger](https://github.com/MuiseDestiny/zotero-attanger): Organize pdf files in your selected folder.
  
  自动更改文件名称、移动文件到指定文件夹。
  
  一个附加功能是，通过同步文件夹实现多设备同步附件。🔥

  Need to set up the `Source Path` and `Destination Path` in the settings for it to work.

- [Better Notes](https://github.com/windingwind/zotero-better-notes): Making notes while reading PDFs in Zotero. 
  
  You can select text in the PDF viewer and right click to add it as a note to the item. The citation key is automatically added. When you click on the citation, it will take you to the corresponding page in the PDF. 👍
  
  You can export notes as latex format.

  Support some simple markdown syntax and keyboard shortcuts.

- [Linter](https://github.com/northword/zotero-format-metadata): Format item metadata.

  It will retrieve metadat, and rename pdf files to be identifiable.

- [Ethereal Style](https://github.com/MuiseDestiny/zotero-style): customize appearance of Zotero interface


**AI plugins** (not tested yet):

- [Aria](https://github.com/lifan0127/ai-research-assistant)

--------------------------------------------------------------------------------

## FAQ

Q: How to copy a bibliography entry?  
A: Edit > Copy Bibliography (⇧⌘C). You need to follow the steps in [Quick-Copy format](#copy-bibliography) to set the default style.


Q: Better BibTeX export has no `year` field even though the item has a date. [↩](https://forums.zotero.org/discussion/48645/bibtex-export-date-and-year)  
A: Exporting through BBT as "Copy BibTeX to lipboard" instead of "Copy BibLaTeX to lipboard" uses 'year' instead of 'date'.

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


