---
layout: post
title: "LaTeX Bibliography Manager – Zotero"
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


