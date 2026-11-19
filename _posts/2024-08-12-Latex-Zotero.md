---
layout: post
title: "LaTeX Bibliography Manager – Zotero"
tag: programming
update: 2025-08-01
---


<a class="top-link hide" href="#" id="js-top">↑</a>

<img src="{{site.baseurl}}/images/zotero_icon.png" alt="" style="display: inline; height: 2em; vertical-align: middle;" /> Zotero is a free and open-source reference management software to manage bibliographic data. 
It is powerful in reading literature, making annotations and markdown notes. 
It is available for Windows, macOS, and Linux.

**Highlighted features:**

- 🔥🔥 You can link your notes to pdfs directly. This is convenient if you want to locate the references and read more about the topic in context. → Use [Better Notes](#zotero-better-notes)

- 🔥 [PDF viewer](#zotero-attanger-pdf-viewer) is much more powerful than Preview. → You can change the background color; select text and insert directly to notes; citations are linked to pdfs; hover over hyperlinks to see the referenced object, Figure/Table/Eqn/bibliography, etc. 

- You can [sync your Zotero library](#zotero-sync) across multiple devices using a cloud service. → All your pdf attachments are available on all your devices with unlimited storage. 

**Useful resources:**

- [Zotero documentation](https://www.zotero.org/support/quick_start_guide)
- [Zotero 中文社区](https://zotero-chinese.com/user-guide/plugins/better-notes)
- [Libguides: Geneva Graduate Institute](https://libguides.graduateinstitute.ch/zotero/tags)

--------------------------------------------------------------------------------

## Quick Start

**Change PDF background color / theme**

There are built-in themes for the pdf viewer, including light, dark, and sepia, etc. 

<img src="{{site.baseurl}}/images/zotero theme.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:50%;" />


The [**Ethereal Style**](#zotero-ethereal-style) add-on provides more themes, including a green background theme. 

Click the pdf icon <i class="bi bi-file-pdf env-red" style="font-size:1.5em; vertical-align: middle;"></i> to choose your preferred background color for the pdf viewer. If the icon is not visible, reload the pdf.
You can customize your own background color by clicking the color palette 🎨 at the bottom of the menu.

<img src="{{site.baseurl}}/images/zotero pdf background.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

Dark themes will invert images, making it hard to read, whereas light themes do not touch the images. 
I personally like the green background theme.

--------------------------------------------------------------------------------

**Add text box**

<img src="https://l3lab.net/posts/tutorial-zotero-obsidian-annotations/2024-08-04-annotations-with-zotero-version-7/six-annotation-types-min.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

Click the **Add Text** icon, then choose your preferred color and font size using the dropdown menu. Then go to the pdf and click where you want to add the text box. You can resize the text box by dragging the corners. The font size will scale with the text box. Note you cannot change the font color after you add the text box. 


The following GIF shows how to add annotations / sticky notes. Similar to adding a text box. First choose color/style, then click on the pdf to add the annotation.

<img src="https://dkou0skpxpnwz.cloudfront.net/accounts/176650/images/gif_notas.gif" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

--------------------------------------------------------------------------------

**Underlining and highlighting**

Supported by the native Zotero pdf viewer

<img src="https://dkou0skpxpnwz.cloudfront.net/accounts/176650/images/gif_sublinhar.gif" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

When you select text, a menu will pop up, allowing you to highlight or underline the text. Default is to highlight. If you want to underline, click the underline icon, then choose the color you want. 

<img src="{{site.baseurl}}/images/zotero underline.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

You can also highlight sections of your PDF that aren't text, by using the **Select Area** tool.

**Use Colors Purposefully**

| Color | Meaning |
| ----- | ------- |
| Yellow | Running text |
| Red    | Important    |
| Orange | TODO / follow up |
| Green  | Resources: article/book/package/URL |
| Blue   | Code; Examples   |

You can define meanings for each color

<img src="{{site.baseurl}}/images/ethereal style annotation color.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

ref:

- [Annotation with Zotero](https://l3lab.net/posts/tutorial-zotero-obsidian-annotations/2024-08-04-annotations-with-zotero-version-7/)
- [Annotation colors](https://plugins.muisedestiny.xyz/docs/style#annotation-colors)

--------------------------------------------------------------------------------

**Add new items**

- **Add by Identifier**: Click the magic wand icon 🪄 in the toolbar > Paste DOI, ISBN or arXiv ID of the citation > Press Enter.

--------------------------------------------------------------------------------

**Attachment**

You can attach pdf files to your Zotero items. 

- <img src="{{site.baseurl}}/images/stored files1.svg" alt="" style="display: inline; height: 1.5em; vertical-align: bottom;" /> <img src="{{site.baseurl}}/images/stored files2.svg" alt="" style="display: inline; height: 1.5em; vertical-align: bottom;" /> Stored files: Default option. The file will be copied to the Zotero data directory. → Supported by Zotero cloud storage; limited to 300 MB free space.
  
  <img src="{{site.baseurl}}/images/zotero stored files.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

  The pdfs are stored in the Zotero data directory `/Users/<username>/Zotero/storage` with random alphanumeric folder names for each item, making it <span class="env-orange">hard to identify the files</span>. 

- <img src="{{site.baseurl}}/images/linked files1.svg" alt="" style="display: inline; height: 1.5em; vertical-align: bottom;" /> <img src="{{site.baseurl}}/images/linked files2.svg" alt="" style="display: inline; height: 1.5em; vertical-align: bottom;" /> **Linked files:** create a link to the file on your computer. → Used when you use a third party cloud service (Google Drive, etc.) to sync your pdf files across multiple devices.
  
  <img src="{{site.baseurl}}/images/zotero linked files.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

  For syncing to work on your multiple devices, you need to set the set the [linked attachment base directory](https://www.zotero.org/support/preferences/advanced#linked_attachment_base_directory) so that the files can be found by Zotero on each computer. 
  
  The base directory <u>stores your linked files</u>. <span class="env-green">It can be different on each computer.</span> For example, if the folder with your linked files is at `/Users/Sarah/Dropbox/PDFs` on your laptop and at `C:\Users\Sarah\Dropbox\PDFs` on your work computer, set those paths as the base directory on each respective machine. The directories serve as the root for all linked files, so Zotero will look for the linked files in the same relative path but different root paths on each computer.

  The base directory needs to be consistent with the `Destination Path` in your linked file manager plugin, such as `Attanger` or `ZotMoov`.

  - `Destination Path`: supported by plugins; controls where the attachments are stored.
  - `Base Directory`: tells Zotero where to look for the attachments.

  See [Here](#zotero-base-directory) for details on how to set the base directory.

  Limitations:

  - Cannot be used within a group library; group members may not have access to the same file location.

**refs:**

- [Stored vs. Linked Files](https://www.zotero.org/support/attaching_files)
- [添加附件](https://zotero-chinese.com/user-guide/add-attachments)


--------------------------------------------------------------------------------

### Tags

Tags are keywords that characterize the references. Some tags are automatically downloaded with the references, but you can also add tags manually. These tags can be used for topics, of course, but you can also use

- workflow tags: to-read, to-assess
- methodology tags: panel, time-series, asset-pricing, writing
- evaluation tags: seminal, working-paper, review

You can tag references, but also attached files or notes.

--------------------------------------------------------------------------------

**Configuration**

It is <span class="env-orange">NOT</span> recommended to keep the tags that are automatically downloaded. Each source has its own keyword system, so there will not be any logic to your tags. 

- To disable the automatic download of tags, go to the Settings menu → General → Miscellaneous and uncheck "Automatically tag items with keywords and subject headings". 

  <img src="{{site.baseurl}}/images/zotero automatic tag.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:60%;" />

- You can delete all these automatic tags by clicking on the <i class="codicon codicon-filter" aria-hidden="true" style="font-size:1.5em; vertical-align: middle;"></i> button next to "Filter Tags" and selecting "Delete Automatic Tags in This Library".
  
  <img src="{{site.baseurl}}/images/zotero delete automatic tags.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:40%;" />


--------------------------------------------------------------------------------

**Add Tags**

1. Find the citation you want to tag and click it.
2. In the information panel on the right, scroll to "Tags" or click the "Tags" icon, which looks like a luggage tag, in the right navigation.
   <img src="{{site.baseurl}}/images/Zotero_-_Tags_-_Desktop_-_Tags_Icon.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />
3. Click the "Add" button, a plus icon, the Tags section.
   <img src="{{site.baseurl}}/images/Zotero_-_Tags_-_Desktop_-_Add_-_7.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />
4. Start typing the tag name you want to add.
   <img src="{{site.baseurl}}/images/Zotero_-_Tags_-_Desktop_-_Add_-_List_-_7.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />
   - If you already have used that tag, it will appear in the list below the search bar. Click the tag name to add it.
   - If this is a new tag, finish typing out your tag and either click off the text box or hit Enter.


Keyboard shortcut: <kbd>⌃</kbd> + <kbd>T</kbd>

<div class="note">
<span class="env-green">Three types of tags:</span>
- No prefix → Color-coded tag, shows as icon under `Tags` column
- Start with `#` → Name tag, shows under `#Tags` column
- Start with `/` → Status tag, shows under `Status` column

See [HERE](#zotero-types-of-tags) for their differences.
</div>

--------------------------------------------------------------------------------

**Color code your tags**

To color code your tags, right click on a tag in the lower left pane.  Choose **Assign Color** from the menu.  Click on the color box to choose one of the nine color options for your tag.

<img src="https://d2jv02qf7xgjwx.cloudfront.net/accounts/46117/images/Add_tags_step_3.jpg" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:60%;" />

Once you have chosen a color for your tag, the tag will display with that color in the lower left pane, and in the center pane of your library you will see a colored dot next to all items that have that particular tag.

<img src="http://lgimages.s3.amazonaws.com/data/imagemanager/74010/tag2.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

--------------------------------------------------------------------------------

**Principles for tag names:**

- Use lower case unless it is a proper noun.
- Plural vs singular: choose one and be consistent.

--------------------------------------------------------------------------------

**Show tag info in item view**

Supported by Ethereal Style plugin

<a id="zotero-types-of-tags"></a>
<span class="env-green">Three types of tags:</span>

| Naming Convention | Column Name in Item View | Description | Use Case |
| ----------------- | ------------------------ | ----------- | -------- |
| `#<tag-name>` | `#Tags` | Tags will display as text; most informative | Explicitly show category of the reference, e.g., `#methodology`, `#topic`, `#evaluation` |
| `#<level1>/<level2>` | `#Tags` | Hierarchical Topic Classification | `#finance/asset-pricing`, `#finance/monetary-policy`, `#finance/green-finance` |
| `<tag-name>`  | `Tags`  | **ONLY** <span class="env-green">color-coded tags will display</span> as colored dots | Significance of the reference, e.g., `seminal`, `working-paper`, ⭐️|
| `/<tag-name>` | `Status` | Will show color and text | Use for workflow, e.g., `/to-read`, `/reading`, `/done` |


Keyboard shortcut: Use <kbd>⌃</kbd> + <kbd>T</kbd> to add a tag. It can be any type, use `#` for name tags, `/` for status tags, and no prefix for plain (color-coded) tags.

`Status` column is most convenient. You can click on the cell to change the status of the reference. Click `Create` to create a new status tag.

Use ⭐️, ⭐️️⭐️, ⭐️⭐️⭐️ to indicate the significance of the reference. Add them as `️️⭐️` and <u>assign colors</u> to them so that they will show up in the `Tags` column in the item view.


<img src="https://plugins.muisedestiny.xyz/images/style/tutorial/status-menu.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

--------------------------------------------------------------------------------

**Tag Selector**

The Zotero Tag Selector is the panel located at the bottom-left corner of the Zotero window that lets you filter, organize, and bulk-manage your library using keywords.

- Nested tag view (show as a **list**) → Supported by the Ethereal Style plugin
  
  Click <kbd><i class="bi bi-chevron-expand" style="-webkit-text-stroke: 0.8px; display: inline; height: 1.5em; vertical-align: bottom;"></i></kbd> to sort tags by name.
  
  <img src="{{site.baseurl}}/images/zoterostyle-嵌套标签.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:40%;" />
  
- Normal tag view → Supported by native Zotero

  <img src="{{site.baseurl}}/images/zotero normal tag view.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:100%;" />


**refs:**

- [How do I use tags in Zotero](https://libanswers.memphis.edu/faq/410374)
- [Tagging](https://guides.library.oregonstate.edu/c.php?g=359201&p=2426089)
- [Ethereal Style: Tags](https://plugins.muisedestiny.xyz/docs/style#tags)



--------------------------------------------------------------------------------

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

<a id="zotero-sync"></a>

### Sync Settings

Use Zotero's [sync](https://www.zotero.org/support/sync#zotero_file_storage) feature to keep your library up to date across multiple devices and back it up to the cloud.

- **Data Syncing**
  
  Data syncing merges library items, notes, links, tags, etc. — everything except attachment files — between your local computer and the Zotero servers, allowing you to work with your data from any computer with Zotero installed and to view your library online on [zotero.org](https://zotero.org). Data syncing is <span class="env-green">free and unlimited</span>, and it can be used without file syncing.

  <img src="https://drive.google.com/thumbnail?id=1qK7_3vzro-jzE9VcmfAYI1bB5w2ckuo9&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

  -   **Sync automatically:** When check, Zotero will start a sync every time you make a change to your library. You can manually start a sync by clicking the sync button (circular green arrow) in the upper-right corner of the Zotero window.

  -   **Sync full-text content:** When checked, Zotero will sync the extracted text contents of your PDFs and other files, allowing you to perform searches across devices regardless of whether files have been downloaded to a particular device. This also allows for full-text searches in the [web library](https://www.zotero.org/mylibrary "/mylibrary").
      
      <span class="env-green">**Uncheck "Sync full-text content" and "Sync attachment files in My Library"**</span> to avoid your Zotero cloud storage being quickly filled up.
      
      Zotero's cloud file storage only provides <span class="env-orange">**300 MB**</span> free space, and syncing full-text content can quickly use up your storage quota. One pdf file is around 3--5 MB, that means you can only sync ~70 files before you run out of free storage. You can buy more storage at $20/year for 2 GB.
      
      <img src="https://drive.google.com/thumbnail?id=1xFpYvjdtYDpcmHEDq-c7uWyTH_oRoOOr&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

      A workaround is to use <span class="env-green">`Attanger`</span> or `ZotMoov` to manage your attachments in a local folder synced by cloud services or NAS. This way, you get unlimited storage for your attachments.
      See the next section on "Sync local pdf files" for details.


- **File Syncing**
  
  I use NAS to sync my Zotero attachments across multiple devices. So here I **uncheck** "Sync attachment files in My Library using Zotero".

  Zotero cloud storage is the default option to sync attachments. But it has limited space. An alternative is to use WebDAV.
  
  `Download files` has two options (relevant only if you use Zotero to sync your attachments):
  
  -   **At sync time:** Download all attachment files not already in your local Zotero file storage on your computer each time Zotero syncs.

  -   **As needed:** Only download attachment files when the user attempts to open the file. Useful for reducing the amount of hard disk space Zotero uses for attachments.
  
  [List of WebDAV providers](https://www.zotero.org/support/kb/webdav_services)

  -   **Zotero:**
      -   Sync file attachments using [Zotero File Storage](https://www.zotero.org/support/sync#zotero_file_storage "/support/sync#zotero_file_storage").
      
      -   Each Zotero user is given **300 MB** of free Zotero Storage for attached files.
        
  
  -   **WebDAV:**
      
      WebDAV is a protocol that allows you to store files on a remote server. E.g., 4shared, CloudMe. They provide some free storage space, but might have limitations on file size or number of files per folder.
      
      -   Sync file attachments using [WebDAV storage](https://www.zotero.org/support/sync#webdav "/support/sync#webdav").

      -   Enter the URL for your WebDAV server (note that `/zotero` is added to the end of the URL automatically), your username, and your password.

      -   Click "Verify Server" to check whether Zotero can connect with the server for file syncing.

**ref:**

- [Zotero documents: Syncing](https://www.zotero.org/support/sync#data_syncing)
- [使用坚果云 WebDAV 同步](https://b23.tv/0NH8VyM)

--------------------------------------------------------------------------------

### Sync local pdf files

**Issue:** Zotero cloud storage only provides 300 MB free space. If you manage pdf using Zotero, we will quickly run out of space.

**Fix:** Follow the steps below to get <span class="env-green">unlimited attachment Zotero storage</span> using cloud services or NAS. You can use this approach to sync your Zotero attachments across multiple devices without using Zotero's cloud storage.

**Prerequisites:** 

- a sync service and
- Zotero linked file manager plugin, such as <span class="env-green">`Attanger`</span> or `ZotMoov`. 

**Step by step instructions:**

1. **Create a folder for storing and syncing Zotero attachments.**
   
   This folder will be synced to multiple devices using cloud services or NAS. PDF attachments will be stored in this folder.
   
   I use NAS to sync my Zotero directory, so I create a folder `~/Documents/Zotero` on my local computer.
   
   Alternatively, if you use cloud services, such as Google Drive, Dropbox, OneDrive, etc., you can create the folder within the local sync folder of these services.
   An example is `~/Google Drive/Zotero`.

   <a id="zotero-base-directory"></a>

2. Change your **Base Directory** to your local sync folder.

   Zotero > Preferences > Advanced > Files and Folders > Change your "Base Directory" to your local sync folder.

   <img src="{{site.baseurl}}/images/Zotero base directory.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

3. In your linked file manager plugin, such as `Attanger` or `ZotMoov`, set the **`Destination Path`** to be the same as your Base Directory.
   
   <img src="{{site.baseurl}}/images/Zotero Attanger.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />
   
   This way, all your pdf attachments are stored in your local sync folder, and synced to other devices using your cloud services or NAS.

   See [Attanger](#attanger) for detailed instructions on how to set up synced folders.

**ref:**

- ![img](https://www.gstatic.com/youtube/img/watch/yt_favicon_ringo2.png) [Youtube video: Zotero + Google Drive Sync](https://www.youtube.com/watch?v=BBSEDaUDGOM&list=WL&index=1) start from 8:11

--------------------------------------------------------------------------------

<span style="display:block; font-size:2.5em; font-weight:bold; margin:1em 0;">Plugins</span>

## Better Bib(La)Tex 

Useful links:

- [Better BibTeX Homepage](https://retorque.re/zotero-better-bibtex/index.html)
- [GitHub repo](https://github.com/retorquere/zotero-better-bibtex)

--------------------------------------------------------------------------------

How to [install](https://retorque.re/zotero-better-bibtex/installation/) the BBT plugin

1. Download `.xpi` file from the GitHub [releases page](https://github.com/retorquere/zotero-better-bibtex/releases).
2. Go to Zotero > Tools > Plugins > Click on the gear in the top-right corner <i class="codicon codicon-settings-gear dynamic-setting-icon" aria-hidden="true" style="font-size:1.5em; vertical-align: middle;"></i> > choose ‘Install Plugin From File…’ > Select the `.xpi` file you downloaded

You can use the same method to install other Zotero plugins.

<img src="https://drive.google.com/thumbnail?id=1qtP45q_HrQHaxQDZOqVzkdB9wfUcH36Z&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

--------------------------------------------------------------------------------

<span class="env-green">**How to export bibtex items**</span>

1. Select the references you want to export in Zotero
2. Right-click > Better BibTeX > Copy <span class="env-green">BibTeX</span> to Clipboard
3. Paste the content into a `.bib` file


Q: Difference btw BibTeX and BibLaTeX?  
A: Slightly different keys. E.g., BibLaTeX uses `journaltitle` instead of `journal`, `date` instead of `year`, etc. Usually, BibTeX is preferred.

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

If you want your keys to update after a pattern change, you will have to select your items, right-click > <span class="env-green">Better BibTeX</span> > <span class="env-green">Select `Refresh BibTeX key`</span>. This will not affect keys you have pinned.

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
  
  <a id="zotero-attanger-pdf-viewer"></a>
  What I like about <span class="env-green">**Zotero pdf viewer**</span>: 
  
  - Add quotes linked to bibliography entries in Better Notes.
    
    You can select figure and add to Better Notes too.
  
  - Add comment on highlighted text. ← Not possible on Preview.
  - Hover over hyperlink to see the referenced object, Figure/Table/Eqn/bibliography, etc. ← Not possible on Preview.
  - Other basic annotation functions, such as highlight, underline, sticky notes. ← Supported by Preview.
  - You can set pdf viewer themes, like changing background color to sepia, dark mode, etc. Attanger supports more themes. ← Not possible on Preview.
  
  See [HERE](https://www.zotero.org/support/pdf_reader) for documentation of PDF reader in Zotero.

- Mac Preview: annotation saved in the pdf file. The annotations are visible everywhere, such as web browsers, etc.

**Annotation direction:**

Preview → Zotero ✅  
Zotero → Preview ❌


--------------------------------------------------------------------------------

### Configuration

**Attanger settings:**

- `Source Path` (源路径): This can be set to the `~/Downloads` folder where Zotero will retrieve newly added files and attach it to ZOtero Item/Collection.
  
  This is the local directory where your browser downloads files to.

- `Attach Path` (附加类型): Leave it as `Link`. This is the default.

<a id="Attanger-destination-path"></a>

- <span class="env-green">**`Destination Path`**</span> (靶路径): This is the directory to move files to. Set it to your [`Base Directory`](#base-directory).
  
  This is the local directory to move the attachments to. I set it to <span class="env-green">`~/Documents/Zotero`</span>.
  
  I sync this file using NAS. You can use any cloud services instead, such as Google Drive, Dropbox, OneDrive, etc.

--------------------------------------------------------------------------------

### How to use

After configuring Attanger, when you download a pdf file from the web, it will first be saved to your `Source Path` (e.g., `~/Downloads`).

Then, in Zotero, right click on the item you want to attach the pdf to, and choose `Attanger` > <span class="env-green">`Attach New File`</span>. It will identify the latest file in your `Source Path`, move it to your `Destination Path`, and attach it to the Zotero item.

For *existing attachments*, the pdf files are still stored in the default Zotero storage folder (`~/Zotero/storage`) with random alphanumeric folder names.
If you want to move these attachments to your `Destination Path`, you can select the items, right click, and choose `Attanger` > <span class="env-green">`Move Attachment`</span>. The pdf files will be moved to the destination path.

<img src="https://drive.google.com/thumbnail?id=1NNffhdffd9CD4i1T-GJB0BAydHIE3V2D&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

If you renamed a collection, you can use <span class="env-green">`Move Attachment`</span> to move the attachments to the new path. This way, the attachments will be organized in a folder structure consistent with your Zotero library structure.


Note that linked files that are managed/tracked by Attanger will show a link ∞ on top of the file icon <img src="{{site.baseurl}}/images/link.png" alt="" style="display: inline; height: 1.5em; vertical-align: middle;" />.

ref:

- [US Berkeley Library: ZotMoov](https://guides.lib.berkeley.edu/zotero/zotfile)
- [Zotero hacks: reliably setup unlimited storage for you personal academic library, @Ilya Kashnitsky](https://ikashnitsky.phd/2024/zotero7/)

--------------------------------------------------------------------------------

<a id="zotero-ethereal-style"></a>

## Ethereal Style

This plugin customizes the appearance of the Zotero interface to make it cleaner and more visually appealing.

⇧ + <kbd>P</kbd> to start a command palette to quickly access various functions provided by Ethereal Style.

<img src="{{site.baseurl}}/images/zotero style command palette.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

**Column Settings**

<img src="{{site.baseurl}}/images/zotero column-menu.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />


**Highlight features:**

- Title: As the background of title, reading progress visually reflect the distribution of your reading time of each page for the PDF under a item, the darker the color the longer the reading time.
  
  <img src="{{site.baseurl}}/images/zotero column setting title.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:60%;" />

  - Tags: Show `#Tags` color in dots
  - Emoji: Show `Tags` if it is an emoji

- Publication Tags (影响因子与期刊标签)
  
  Need to set up `easyscholar` API key.

**refs:**

- [Ethereal Style Documentation](https://plugins.muisedestiny.xyz/docs/style)
- [Notion: Ethereal Style 中文教程](https://www.notion.so/Zotero-Style-bc2aebbbb6df4b7baa858e376e4fc5be)
- [Zotero Documentation: Ethereal Style](https://zotero-chinese.github.io/user-guide/plugins/style?utm_source=chatgpt.com)

--------------------------------------------------------------------------------

<a id="zotero-better-notes"></a>

## Better Notes

[Better Notes](https://github.com/windingwind/zotero-better-notes) allows you to make notes in Markdown format while reading PDFs in Zotero. My favorite feature: you can select text in the PDF viewer and right click to add it as a note to the item. The citation key is automatically added. When you click on the citation, it will take you to the corresponding page in the PDF.

Q: How to add quotes from PDF to notes?  
A: The trick is that you need to select and open the target Notes as a side panel to make the "Add to Note" option appear when you right click on the selected text in the PDF viewer.

<img src="https://drive.google.com/thumbnail?id=1FEfrSepemYvM0Z4yAjm1tWCCyFCtQoml&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

When you have seen this window, you can then click the three dots `...` on the status bar of the Notes. This allows you to select "Open Note in New Tab". The "Add to Note" options will still work this way. Otherwise, if you open the note directly, the "Add to Note" option will not appear when you right click on the selected text in the PDF viewer.

Click "Add to Note". The selected text will be added to the note, with the citation key automatically added. 

<img src="https://drive.google.com/thumbnail?id=1W5pzuN19mVC6Y9vd-bFROZxOO51LdgSb&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:50%;" />

Hierarchy of Better Notes: It can be placed under an item, or a collection, or the whole library.


--------------------------------------------------------------------------------

**Magic Key**

Type `/` to open a menu of commands, where you can e.g., insert a citation, typset text, insert math block.


Q: How to insert inline math?  
A: Type `$` to open the inline math, then type your math formula, and type `$` again to close the equation. Hit <kbd>Enter</kbd> to render the equation.

Q: How to insert a math block?  
A: Type <span class="env-green">`$$` followed by a **space**</span> to create a block. Or use the Magic Key `/` to open the command menu, and choose "Insert math block". Then you can type your math formula in the block.



**Tool bar**

<img src="https://drive.google.com/thumbnail?id=1NYPMNAXJViRfRwNI_dDG2ZPN8_H30B4E&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />


| Number | Function                         |
| ------ | -------------------------------- |
| 1      | Format text (bold, italic, etc.) |
| 2      | Change text color                |
| 3      | Highlight text                   |
| 4      | Clear Format                     |
| 5      | Insert link                      |
| 6      | Insert Citation                  |
| 7      | Find and Replace                 |

Export Notes: Click the three dots `...` on tool bar > `Export Current Notes...` > Choose the format you want to export, e.g., LaTeX.


Ref:

- [Zotero的 Better Notes！写综述必备](https://b23.tv/ORpXg57) starts from 03:30
- [Zotero 插件 Better Notes 超好用笔记插件](https://b23.tv/HiTxTmo) starts from 13:50
  
  This video also shows installation.



--------------------------------------------------------------------------------

## Useful plugins

[Zotero plugin collection](https://www.zotero.org/support/plugins)

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

- [delitemwithatt](https://github.com/redleafnew/delitemwithatt): Delete item with attachments. By default, when you delete an item, the attachments are not deleted. This plugin allows you to delete the attachments together with the item.

- [Scihub](https://github.com/ethanwillis/zotero-scihub) Download pdf from Sci-Hub or Sch-Net.
  
  By default, it will download pdfs when you add a new item in the library. You can disable this feature in the plugin settings.

  Right-click, a context menu titiled "Update Scihub PDF", click it to download the pdf.

- [Publication Rankings](https://github.com/ben-AI-cybersec/zotero-publication-rankings)
  
  Right-click column headers and enable the "Ranking" column
  
  - SJR ranking (all-encompassing): Q1 (top 25%, SJR > 1); should aim for SJR value 2 and 3
  
  - ABS Rankings (business): 4* (top 2.6%); 4 (top 5%); 3 (top 25%); 2 (top 55%); 1 (bottom 45%)
  
  <img src="https://github.com/ben-AI-cybersec/zotero-publication-rankings/raw/main/assets/Rankings_Text.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

**AI plugins** (not tested yet):

- [Aria](https://github.com/lifan0127/ai-research-assistant)

AI research assistant:

- [Monnlight](https://www.themoonlight.io/en): 3 papers per week

--------------------------------------------------------------------------------

## VS Code Plugins

To use Zotero with VS Code, use an extension to link your Zotero library with VS Code. There are two extensions available: Zotero Cite and VSCode Zotero. I personally prefer Zotero Cite because it has a better search bar.

### Zotero Cite

<img src="https://xing.gallerycdn.vsassets.io/extensions/xing/zotero-cite/0.9.16/1788363541686/Microsoft.VisualStudio.Services.Icons.Default" alt="" style="display: inline; height: 2em; vertical-align: middle;" />
[Zotero Cite](https://marketplace.visualstudio.com/items?itemName=XING.zotero-cite) by Xing

Zotero Cite has a search bar that is well integrated with Zotero. It shows all your libraries and references. You can search for your references in the graphical interface.

<img src="{{site.baseurl}}/images/vscode zotero cite search bar.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />


**Configuration**

1. Add keyboard shortcut (⌃⌘R) to insert citations and bibliographies

   ```json
   // Zotero Cite keybindings
   {
     "key": "ctrl+cmd+r",
     "command": "zotero-cite.citeSmart",
     "when": "editorTextFocus && !editorReadonly"
   },
   ```

   The `when` condition means it only fires while you're typing in an editor you can change.

2. Specify your bib file in `.vscode/settings.json` (project settings):

   ```json
   {
     "zotero-cite.defaultBibName": "bibli.bib"
   }
   ```

   <span class="env-orange">One drawback:</span> not intelligent enough to locate my bib file. It defaults to `ref.bib`. You need to specify your bib file in `.vscode/settings.json` as shown above. Otherwise, it will create a new `ref.bib` file in your project root directory.

--------------------------------------------------------------------------------

### VSCode Zotero

<img src="https://jinvim.gallerycdn.vsassets.io/extensions/jinvim/vscode-zotero/1.4.8/1793069270649/Microsoft.VisualStudio.Services.Icons.Default" alt="" style="display: inline; height: 2em; vertical-align: middle;" /> [VSCode Zotero](https://marketplace.visualstudio.com/items?itemName=jinvim.vscode-zotero) extension by Jinvim allows you to insert citations and bibliographies into your LaTeX document using Zotero.

Advantage: Locate `*.bib` intelligently.  
Drawback: Library search is not as good as Zotero Cite. The search bar does not have a preview of existing libraries.

- <span class="env-green">Search Library</span> (`zotero.searchLibrary`): <kbd>ctrl</kbd> + <kbd>cmd</kbd> + <kbd>R</kbd>
  
  This will start a search in the Command Palette. Find your references, hit <kbd>Enter</kbd>, the cite key together with the citation command will be inserted at the cursor position in your LaTeX document. `bib` entry will be automatically added to `*.bib` file of your project if it does not exist already. See [below](#Zotero-bib-file) for locations the extension searches for `*.bib` file.

  <img src="https://raw.githubusercontent.com/jinvim/vscode-zotero/refs/heads/main/resources/fig1.gif" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" /> 

  1. Items in local Zotero library will be shown in Quick Picks.
  2. Search for the item you want to cite, select it, hit <kbd>Enter</kbd>. 
     
     - The key of the selected item will be inserted at the cursor position in your LaTeX document.

     - The bib entry will be automatically added to `*.bib` file of your project.
       
       <a id="Zotero-bib-file"></a>
       The extension <span class="env-green">searches `*.bib` file in the following order</span>:
       
       1.  `*.bib` file in `quarto` or `latex` file header (for quarto, this includes `_quarto.yml`)
       2.  `bibliography.bib` or `references.bib` file in the workspace root directory
       3.  Any `*.bib` file in the workspace root directory.
       4.  If none of above is available, ask user to provide path, or create a new one (you still need to add the file to `quarto` or `latex` header).


- Open Zotero entry under cursor: <kbd>ctrl</kbd> + <kbd>cmd</kbd> + <kbd>o</kbd>
  
  This will open the citation's linked pdf file.

- Tidy up `.bib` file: <kbd>ctrl</kbd> + <kbd>cmd</kbd> + <kbd>t</kbd>
  
  This clear unused entries; add missing bib entries that are used in the manuscript but not in the `.bib` file; sort entries alphabetically

--------------------------------------------------------------------------------



## MS Word

Install Zotero Word plugin following this [guide](https://www.zotero.org/support/word_processor_plugin_manual_installation#word_for_mac).

After installation, you will see a Zotero tab in Word. You can use it to insert citations and bibliographies into your Word document.

<img src="{{site.baseurl}}/images/word zotero.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

- Add/Edit Citation: Add a new citation or edit an existing citation in your document at the cursor location.
- Add/Edit Bibliography: Add a new bibliography or edit an existing bibliography in your document <span class="env-green">at the cursor location</span>.
- Document Preferences: Set the citation style and other preferences for your document.

More usage instructions can be found in [Using the Zotero Word Plugin](https://www.zotero.org/support/word_processor_plugin_usage)

--------------------------------------------------------------------------------

### Shared Library

Zotero groups provide a powerful way to share bibliography with coauthors. There is NO limit on how many members may join your groups, and your full storage subscription is always available to your personal and group libraries.

Use case scenario: If your coauthor wants to edit the item type or authors, they can do so in the group library. The changes in the Share Library will be reflected in your paper references. It is NOT suggested to make changes directly in the docx as it will be overwritten by the Zotero data when you refresh. Zotero data is the root, docx retrieves data from Zotero. So if you want to make changes, do it in the Zotero library.

Create a [New Group](https://www.zotero.org/groups/new). Follow instructions, then your **Group Libraries** will show under your personal library.

<img src="{{site.baseurl}}/images/Zotero groups.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:40%;" />


On the Group Settings page, select "Members Settings" to invite members to your group.

<img src="{{site.baseurl}}/images/zotero group page.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

Users must log in to the [zotero.org](https://zotero.org) website to join a group.

ref:

- [Zotero document: Groups](https://www.zotero.org/support/groups)


--------------------------------------------------------------------------------

## FAQ

Q: How to copy a bibliography entry?  
A: Edit > Copy Bibliography (⇧⌘C). You need to follow the steps in [Quick-Copy format](#copy-bibliography) to set the default style.

--------------------------------------------------------------------------------

Q: Better BibTeX export has no `year` field even though the item has a date. [↩](https://forums.zotero.org/discussion/48645/bibtex-export-date-and-year)  
A: Exporting through BBT as "<span class="env-green">Copy BibTeX to lipboard</span>" instead of "Copy BibLaTeX to lipboard" uses 'year' instead of 'date'.

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

--------------------------------------------------------------------------------

Q: How to rotate a pdf page?  
A: Got to **thumbnail view**, right click on the page you want to rotate, and choose "Rotate Left" or "Rotate Right". 

--------------------------------------------------------------------------------

Q: Differences between `Based Directory` and `Data Directory`?  
A: `Base Directory` is the root folder for storing linked files. `Data Directory` is the whole Zotero database. You will see many `zotero.sqlite.*` files which contains item metadata, notes, tags, etc. 

- [Base Directory](https://www.zotero.org/support/preferences/advanced#linked_attachment_base_directory): you can customize it to any folder you want. I set it to `~/Documents/Zotero`.
- [Data Directory](https://www.zotero.org/support/zotero_data): defaults to `/Users/<username>/Zotero`.

