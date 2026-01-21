---
layout: post
title: "LaTeX Bibliography Manager Zotero"
tag: programming
update: 2025-08-01
---


<a class="top-link hide" href="#" id="js-top">↑</a>

Zotero is a free and open-source reference management software to manage bibliographic data. 
It is available for Windows, macOS, and Linux.


## Install plugin

### Better Bib(La)Tex 

Useful links:

- [Better BibTeX Homepage](https://retorque.re/zotero-better-bibtex/index.html)
- [GitHub repo](https://github.com/retorquere/zotero-better-bibtex)

--------------------------------------------------------------------------------

How to [install](https://retorque.re/zotero-better-bibtex/installation/)

1. Download `.xpi` file from the GitHub [releases page](https://github.com/retorquere/zotero-better-bibtex/releases).
2. Go to Zotero > Tools > Plugins > Click on the gear in the top-right corner and choose ‘Install Plugin From File…’ > Select the `.xpi` file you downloaded

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

## Cite Keys

The default key pattern is `auth.lower + shorttitle(3, 3) + year`:

1. last name of first author without spaces, in lowercase because of the .lower filter
2. The first `n` (default: 3) words of the title, apply capitalization to first `m` (default: 3) of those.
3. year of publication if any,
4. a letter postfix (a, b, c, etc) in case of a clash (this part is always added, you can’t disable it, although you can change it to Zotero-style numeric)

Changing a pattern will only affect items created/changed after you changed the pattern; existing keys are not automatically regenerated when you change the pattern.

If you want your keys to update after a pattern change you will have to select your items, right-click, and select `Refresh`. This will not affect keys you have pinned.