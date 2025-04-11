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
<script src="https://gist.github.com/parkr/c08ee0f2726fd0e3909d.js"> </script>
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

