---
layout: post
tag: programming
title: Run Python in Rstudio
---

<a class="top-link hide" href="#" id="js-top">↑</a>


The `reticulate` package provides an interface to embed Python sessions within R sessions.

Specify Python interpreter

1. run `which -a python python3` in the terminal to check executable paths.
2. configure a default version of Python to be used with RStudio.
   - use Preferences (`cmd`+`,`).
   - choose one of the *Conda Environments*. Easy to manage packages afterwards.