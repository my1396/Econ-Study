---
layout: post
title: Embedding Gists with Jekyll on GitHub Pages
tag: programming
update: 2025-04-10
toc: true
---

Github gists can be embedded into Jekyll pages using the `gist` tag.



## Configuring Jekyll

Follow the installation guide indicated [here](https://github.com/jekyll/jekyll-gist). The steps are listed here for reference just in case.

Steps are as follows:

1. Append `jekyll-gist` to your `Gemfile`.

    ```
    gem 'jekyll-gist'
    ```

2. Add the package to the `_config.yml` file .

    ```
    plugins:
      - jekyll-gist
    ```



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

Now we can embed existing Gists using the `gist` Liquid template tag and the gist ID.

Use the tag as follows in your Jekyll pages, posts and collections:

Basic syntax:

```liquid
{% raw %}{% gist <gist_id> <optional_file_name> %}{% endraw %}
```

Use example:

```liquid
{% raw %}{% gist c08ee0f2726fd0e3909d %}{% endraw %}
```

This will create the following script tag:

```html
<script src="https://gist.github.com/username/c08ee0f2726fd0e3909d.js"> </script>
```

You may optionally specify a `filename` after the `gist_id`:

```liquid
{% raw %}{% gist c08ee0f2726fd0e3909d test.md %}{% endraw %}
```

This will produce the correct URL to show just the specified file in your post rather than the entire Gist.

It will be rendered as

{% gist 9edcb9c13ecc2aa657e4e24a41cbeef8 R_style_embrace_opt.R %}



___

**References**:

<https://w0lfram1te.com/embedding-gists-with-jekyll-and-github-pages>

<https://stackoverflow.com/a/36298409/10108921>

