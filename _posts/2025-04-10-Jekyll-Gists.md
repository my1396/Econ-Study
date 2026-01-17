---
layout: post
title: Embedding Gists with Jekyll on GitHub Pages
tag: programming
update: 2025-04-10
toc: true
---

Github gists can be embedded into Jekyll pages using HTML `<script>` tags. We only need to find the correct URL for the gist.


## Configuring Jekyll

**Note**: The `jekyll-gist` plugin is <span class="env-orange">NO longer</span> needed when using HTML embedding. You can embed gists directly using HTML `<script>` tags, which works with any Jekyll setup including GitHub Pages.


___

## Adding the Gist to the Post

Understanding the Gist URL 

<img src="https://drive.google.com/thumbnail?id=1NdYdSiP5ENpMG8Zx_Dt1U59p7fBCAEeB&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

- Using the Copy Link Button 

  `<script src="https://gist.github.com/my1396/9edcb9c13ecc2aa657e4e24a41cbeef8.js"></script>`
  
  which follows the pattern

  `https://gist.github.com/<USER_NAME>/<GIST_ID>.js`

- Raw file content
  
  `https://gist.githubusercontent.com/my1396/9edcb9c13ecc2aa657e4e24a41cbeef8/raw/aa040ca7f108732717cf0f01fc3f54257731d98a/R_style_embrace_opt.R`
  
  which follows the pattern

  `https://gist.githubusercontent.com/<USER_NAME>/<GIST_ID>/raw/<GIST_REVISION_ID>/<GIST_FILE_NAME>`
  
  Note that when you make changes to the Gist, you will get a new `<GIST_REVISION_ID>`, the URL changes too.
  
  When you refer to the Gist, use the following pattern.
  
  `https://gist.github.com/<USER_NAME>/<GIST_ID>/raw/<GIST_FILE_NAME>`

Ref: <https://stackoverflow.com/a/18835385>

Now we can embed existing Gists using HTML script tags.

### Method 1: Embed Entire Gist

One Gist may contain multiple files. See an example [HERE](https://gist.github.com/jmooring/23932424365401ffa5e9d9810102a477).

To embed an entire gist, use:

```html
<script src="https://gist.github.com/username/c08ee0f2726fd0e3909d.js"></script>
```

### Method 2: Embed Specific File from Gist

To embed just a specific file from a gist, add `?file=filename` to the URL:

```html
<script src="https://gist.github.com/username/c08ee0f2726fd0e3909d.js?file=test.md"></script>
```

### Example

Here's an example embedding a specific R file:

<script src="https://gist.github.com/my1396/9edcb9c13ecc2aa657e4e24a41cbeef8.js?file=R_style_embrace_opt.R"></script>


___

**References**:

<https://w0lfram1te.com/embedding-gists-with-jekyll-and-github-pages>
<https://stackoverflow.com/a/36298409/10108921>
