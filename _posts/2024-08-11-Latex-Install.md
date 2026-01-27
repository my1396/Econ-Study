---
layout: post
title: Install LaTeX on MacOS
tag: programming
update: 2025-07-01
---

I install LaTeX on my Mac following instruction on [TeXShop](https://pages.uoregon.edu/koch/texshop/obtaining.html) website. 

TeXShop is a front end to TeX and LaTeX, but when TeXShop typesets, it calls command line programs in an underlying TeX distribution. This distribution must be obtained separately. The TeX distribution contains the actual typesetting programs by Knuth and others, various fonts used by TeX, and a vast array of support style files and other auxiliary files.

Just install the full distribution (about 2800 packages) to avoid missing packages. It' a pain to install missing packages one by one. 

- The standard TeX distribution is called <span class="env-green">**TeX Live**</span>. ✅
  
  TeX Live is a *free* comprehensive TeX system that includes all the major TeX-related engines (TeX, pdfLaTeX, XeTeX, and LuaTeX), macro packages (`amsmath`, `booktabs`, etc. common packages used for formating your manuscript), and fonts.

- *BasicTeX* is a small subset of TeX Live. 
  
  This causes you lots of troubles installing packages manually later on. ❌

--------------------------------------------------------------------------------

## MacTeX Installer

Use MacTeX to install everything in one step automatically. 傻瓜式一键安装所有。 ✅

The package installs TeX Live, the complete reference edition of TeX produced in cooperation by TeX User Groups across the world. 
It also installs Ghostscript and several GUI utilities for TeX including TeXShop, so it is not necessary to get the front end separately. 
One of the GUI programs it installs is "TeX Live Utility," which can keep TeX Live up to date. Everything is completely configured and ready to use once the installer finishes its job.

- MacTeX is a large download, about six gigabytes. 
  
  To obtain it, click on the following link: [MacTeX.pkg](https://mirror.ctan.org/systems/mac/mactex/MacTeX.pkg).

- This package is free, and uses Apple's standard installer; installation takes eight to ten minutes and is automatic.

--------------------------------------------------------------------------------

## Homebrew Installation

You can install LaTeX using Homebrew as well. This method is more lightweight, but you need to be familiar with the Unix command line. 轻量化但是需要熟悉命令行。需要用户自行配置 PATH environment variable。

On Apple Silicon (M chips), homebrew files are symlinked into `/opt/homebrew` and its executable binaries are symlinked into `/opt/homebrew/bin`.

**Configure TeXShop for Homebrew**

This step is to create a symbolic link so LaTeX executables become easily accessible.

> Failed to configure PATH will result in build errors like "pdflatex not found".
>
> In VS Code, you may see errors like:
> "Recipe terminated with fatal error: spawn pdflatex ENOENT". Source: LaTeX Workshop.

Many tools and scripts expect LaTeX binary to be found at `/Library/TeX/texbin`, however, when installed via Homebrew, the binaries are located at `/opt/homebrew/bin`.

Hence, we need to create a symbolic link from `/Library/TeX/texbin` (symbolic link) to `/opt/homebrew/bin` (target).

```bash
cd /Library/TeX
sudo ln -s /opt/homebrew/bin texbin
```

After changing the PATH, <span class="env-green">relaunch VS Code</span> to make sure it picks up the new PATH settings.

Note that you <span class="env-orange">cannot</span> just reload the window, you must completely quit VS Code and relaunch it.

Q: What is the difference between reloading the window and relaunching VS Code?  
A: Reloading the window is like a soft restart. When you install new extensions or change `settings.json`, reloading the window is sufficient. However, <span class="env-green">a full restart is required</span> if you need VS Code to pick up <span class="env-green">system-wide changes</span>, such as new environment variables added to your operating system's `$PATH`.

--------------------------------------------------------------------------------

## Package Management

If you have installed TeX Live, it comes with a comprehensive set of LaTeX packages. However, if there is a package you don't have it locally, TeX Live includes a package manager called `tlmgr` (TeX Live Manager) that allows you to install, update, and manage LaTeX packages.

```bash
# To install a package
tlmgr install <package-name1> <package-name2> ...

# To remove a package
tlmgr remove <package-name1> <package-name2> ...

# To update all installed packages
tlmgr update --all
```