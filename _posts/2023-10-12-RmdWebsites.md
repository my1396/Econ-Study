---
layout: post
title: R Markdown Websites
tag: programming
update: 2023-10-12
---

<a class="top-link hide" href="#" id="js-top">↑</a>

**How-to tutorials**


- Course website with Rmd \
  Github repo: <https://github.com/ryantibs/timeseries-f23/tree/main> \
  Website: <https://www.stat.berkeley.edu/~ryantibs/timeseries-f23/> \
  Setup Tutorial: <https://bookdown.org/yihui/blogdown/github-pages.html> \
  `Bookdown` Books: <https://rstudio4edu.github.io/rstudio4edu-book/book-dress.html>



An R Markdown website must have at least have the following two files:

- an `index.Rmd` file 

  - homepage of your website, contain links to all your blogs. Each blog is a separate `.html` file. You create a link to it in `index.Rmd` by referring to their names. All generated `.html` files should be located in `docs` folder (the folder is specified in `_site.yml`).
  - If you want to link to a downloadable file, such as data or code files, have to write their names in `_site.yml`.

- a `_site.yml` file (which can be empty): one configure file provides the global YAML header for the site.

  - YAML in `_site.yml` will apply it to all R Markdown files for the website, e.g. setting the output format here will tell R Markdown to use that format across the website.
  - Set navigation bar
  - Set the theme, how to highlight your codes, ...

  ```yml
  name: "EK360E-website"
  output_dir: "docs"
  include: ["w1.rmd", "w2.rmd", "w3.Rmd", "w4.Rmd", "w5.Rmd", "sitemap.xml",
            "FF_factors.Rmd"]
  navbar:
    title: "Course Website"
    left:
      - text: "Home"
        href: index.html
      - text: "About"
        href: about.html
  output:
    html_document:
      theme: cosmo
      highlight: textmate
      css: "style.css"
  ```

  



How to build your website? Two options:

- Execute the `rmarkdown::render_site` function from within the directory containing your files to build `_site`, a directory of files ready to deploy as a standalone static website.

- If you create an RStudio Project for your directory, RStudio will add a `Build` tab to the IDE that you can use to build and preview your site.

  <img src="https://drive.google.com/thumbnail?id=1jnBv4cZfqBuJIuJU15LojKqC1L3vrIJM&sz=w1000" alt="build rmd website" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />



What is `_bookdown.yml`?

A configuration file for **bookdown**.



How to host your website on GitHub?

GitHub Pages has a [new feature](https://github.com/blog/2228-simpler-github-pages-publishing) which allows you to use a `docs/` folder in the master branch of your repo to publish a static website. This allows you to track the source files for your book and the published HTML files in the same branch, eliminating the need for that pesky `gh-pages` branch.



















