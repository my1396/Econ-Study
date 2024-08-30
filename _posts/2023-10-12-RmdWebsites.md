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

  - The `yml` file is simply a text file (use `File > New file > Text File` in RStudio). Save it as `_site.yml` or it won’t work. 
  
  - YAML in `_site.yml` will apply it to all R Markdown files for the website, e.g. setting the output format here will tell R Markdown to use that format across the website.

  - Set navigation bar
  
  - Set the theme, how to highlight your codes, ...
  
    At the time of writing the available themes that you might want to try are `cerulean`, `cosmo`, `flatly`, `journal`, `lumen`, `paper`, `readable`, `sandstone`, `simplex`, , `spacelab`, `united`, `yeti`.
  
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

- In the console: Execute the `rmarkdown::render_site` function from within the directory containing your files to build `_site`, a directory of files ready to deploy as a standalone static website.

- If you create an RStudio Project for your directory, RStudio will add a `Build` tab to the IDE that you can use to build and preview your site. Build tab > Build Website.

  <img src="https://drive.google.com/thumbnail?id=1jnBv4cZfqBuJIuJU15LojKqC1L3vrIJM&sz=w1000" alt="build rmd website" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

  

Q: I don't see the `Build` tab.

A: Restart for the `Build` and `git` tabs to show.

<img src="https://drive.google.com/thumbnail?id=1F0sIvmi07aHNxknjJt90Qfw9aqgC7cuM&sz=w1000" alt="Build tab" style="display: block; margin-right: auto; margin-left: auto; zoom:100%;" />



What is `_bookdown.yml`?

A configuration file for **bookdown**.



How to host your website on GitHub?

GitHub Pages has a [new feature](https://github.com/blog/2228-simpler-github-pages-publishing) which allows you to use a `docs/` folder in the master branch of your repo to publish a static website. This allows you to track the source files for your book and the published HTML files in the same branch, eliminating the need for that pesky `gh-pages` branch.

1. Create an empty text file `.nojekyll` and save it at the root of the site. This tells Github not to try and build the site with jekyll (the default for Github).
2. On [GitHub.com](https://github.com/), link you local project to a remote repo, then go Settings $\rightarrow$ Pages $\rightarrow$ Branch $\rightarrow$ Set to deploy from `main` branch and `/docs` folder.
3. Wait for a couple of minutes (but not long, Github needs to recognize the website), your webpages will be live at your GitHub project domain.



**Troubleshoot**: RPC failed; HTTP 400 curl 22 The requested URL returned error: 400 Bad Request.

Cause:  A large push can exceed the default buffer size.

Solution: Increase the buffer size by running the following command:

```bash
git config http.postBuffer 524288000
```

This sets the buffer size to 500 MB. You can adjust the size as needed.



### **Basic Workflow**

1. add content (text, code, images, etc) in an RMarkdown file. This is like a single blog.

2. knit the RMarkdown file to preview

3. update `_site.yml` (perhaps, if it is a new file you want to embed on your website);

   update `_index.Rmd` (if you need to update the home page)

4. build the website

   - Build tab > Build Website or
   - In the console: `rmarkdown::render_site()`

5. repeat, repeat, repeat

6. commit and push your website to GitHub, it’s live!



### Reference

@Jules32, Github Repository, <https://jules32.github.io/rmarkdown-website-tutorial/basic_workflow.html>











