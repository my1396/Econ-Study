---
layout: post
title: LaTeX Workshop
tag: life
update: 2025-08-01
---

Latex-Workshop GitHub: <https://github.com/James-Yu/LaTeX-Workshop/wiki/Install#usage>

Configure LateX Workshop by Paul Wintz: <https://paulwintz.com/latex-in-vscode/> 👍

Integrating Overleaf with VS Code: <https://www.youtube.com/watch?v=SaMRCYbsAek>

Snippets: <https://github.com/James-Yu/LaTeX-Workshop/wiki/Snippets#Handy-mathematical-snippets>


**Aesthetic themes** for LaTeX Workshop PDF viewer:

```json
"latex-workshop.view.pdf.color.dark.backgroundColor": "#F5F5DC",
"latex-workshop.view.pdf.color.dark.pageColorsBackground": "#F5F5DC",
```

This changes the background color and the spacing btw pages in the PDF viewer to beige in dark mode, which is easier on the eyes.

By default, LaTeX Workshop auto builds the pdf on every save. This can be too frequent and distracting.
I set `"files.autoSave": "onFocusChange"` so that the pdf only rebuilds when I switch away from the tex file, not on every keystroke.

The following works in `markdown` inside math environment

| Prefix | Command |
| ------ | ------- |
| `__`   | `_{$1}` |
| `**`   | `^{$1}` |
| `...`  | `\dots` |

Environment snippets works directly in `tex`, you type `B`, a drop-down list will show up for you to choose.

- The prefixes start with `B` and are followed by an abbreviation of the environment name.
- The unnumbered versions of the environments are prefixed with `BS`, e.g., `BSEQ` for `equation*`.
- In `tex`, these cmds work in both math and text environments.
- However, it is more restrictive in markdown, where these cmds work only inside math environments (`$...$`)



| Prefix                                | Environment name |
| ------------------------------------- | ---------------- |
| <span class="env-green">`BEQ`</span>  | `equation`       |
| `BSEQ`                                | `equation*`      |
| `BAL`                                 | `align`          |
| `BSAL`                                | `align*`         |
| `BGA`                                 | `gather`         |
| `BSGA`                                | `gather*`        |
| `BMU`                                 | `multline`       |
| `BSMU`                                | `multline*`      |
| `BIT`                                 | `itemize`        |
| `BEN`                                 | `enumerate`      |
| <span class="env-green">`BSPL`</span> | `split`          |
| `BCAS`                                | `cases`          |
| `BFR`                                 | `frame`          |
| `BFI`                                 | `figure`         |
| `BTA`                                 | `table`          |



[`@` suggestsion](https://github.com/James-Yu/latex-workshop/wiki/Intellisense#-suggestions)

LaTeX-Workshop provides an independent intellisense mechanism triggered by `@`. For example, you can type `@a` for `\alpha`. It works for most Greeks and have some useful mathematical helpers.

| Prefix | Command               |
| ------ | --------------------- |
| `@(`   | `\left( $1 \right)`   |
| `@{`   | `\left\{ $1 \right\}` |
| `@[`   | `\left[ $1 \right]`   |
| `@^`   | `\Hat{$1}`            |
| `@_`   | `\bar{$1}`            |



___

## Build the document

You can define several compiling toolchains to build LaTeX projects using [**LaTeX recipes**](https://github.com/James-Yu/latex-workshop/wiki/Compile#latex-recipes) and then call the command *Build with recipe* to choose the appropriate toolchain for actually building the project. Alternatively, you can directly select the appropriate recipe from the *TeX* badge <i class="fa-brands fa-tex" style="font-size: 1.5em"></i>.

Below are some commonly used examples:

```json
"latex-workshop.latex.recipes": [
  {
    "name": "latexmk",
    "tools": [
      "latexmk"
    ]
  },
  {
    "name": "pdflatex -> bibtex -> pdflatex * 2",
    "tools": [
      "pdflatex",
      "bibtex",
      "pdflatex",
      "pdflatex"
    ]
  }
]
```

-   The first one simply relies on the `latexmk` command. This is the **default** recipe to use when building a project.

-   The second one run the following sequence of commands `pdflatex` → `bibtex` → `pdflatex` → `pdflatex`.

-   Many of my projects use <span style="color: #008B45;">`xelatex`</span> instead of `pdflatex` to support Unicode characters and OpenType fonts. The recipe is similar to the second one, but it uses `xelatex` instead of `pdflatex`.

You can change the default recipe by setting the [`latex-workshop.latex.recipe.default`](https://github.com/James-Yu/LaTeX-Workshop/wiki/Compile#latex-workshoplatexrecipedefault). Recipes are referred to by their names as defined in `latex-workshop.latex.recipes`. Note there are two special values:

-   `"first"`: Use the first recipe defined in [`latex-workshop.latex.recipes`](https://github.com/James-Yu/LaTeX-Workshop/wiki/Compile#latex-recipes).
-   `"lastUsed"`: Use the last used recipe by the command *LaTeX Workshop: 
    
    Build with recipe*. This is useful when you have multiple recipes defined and you want to use the last one you used without having to select it again.

```json
// set the default recipe to the last used one
"latex-workshop.latex.recipe.default": "lastUsed"
```

--------------------------------------------------------------------------------

## View PDF

- **Forward/Direct synctex** (source to pdf) can either be activated by selecting 'Navigate, select, and edit' > 'SyncTeX from cursor' in the side bar, or by the shortcut `cmd`+`option`+`j` (on Mac).
  
    ```json
    // enable 
    "latex-workshop.synctex.afterBuild.enabled": true
    ```

    The setting syncs PDF with cursor position after compiling., defaults to `false`.

- **Backward/Reverse** synctex (pdf to source) is activated by pointing at the relevant element of the pdf preview. When using the internal viewer, the default keybinding to point at an element in the pdf preview is `cmd+click`. It can be changed to `double-click` using the setting [`latex-workshop.view.pdf.internal.synctex.keybinding`](https://github.com/James-Yu/latex-workshop/wiki/View#latex-workshopviewpdfinternalsynctexkeybinding).
  
  ```json
  "latex-workshop.view.pdf.internal.synctex.keybinding": "double-click"
  ```

--------------------------------------------------------------------------------

## Output Directory

By default, LaTeX builds with LaTeX Workshop puts output files in the directory containing your `.tex` file. This quickly creates a cluttered mess, due to the numerous auxiliary files generated by the LaTeX build process. To avoid clutter and allow for build files to be quickly deleted, change the out directory. I use the following setting:

```json
"latex-workshop.latex.outDir": "%DIR%/out_dir",
```

After changing `"latex-workshop.latex.outDir"`, LaTeX Workshop's `"Clean up auxiliary files"` command no longer deletes auxiliary files unless you also change this setting:

```json
"latex-workshop.latex.clean.subfolder.enabled": true,
```

(Note: The "Clean up auxiliary files" command misses some file types, so for a full clean you should just delete all of the files in the folder manually.)

--------------------------------------------------------------------------------

## Overleaf Integration

Overleaf Workshop Extension: <https://github.com/iamhyc/overleaf-workshop>

Overleaf is nice for collaboration, but you will loss the LaTeX Workshop features. E.g., snippets, better synctex (with highlighter of precise location), etc.

A workaround is to use [GitHub integration](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git-integration) to sync Overleaf projects to your computer. Using Git incurs some overhead with pushing, pushing, and (possibly) merging, but it may be worth the upsides of editing Overleaf documents with the exact same tools as any of your local LaTeX documents.

**Log in with Cookies**

<img src="https://raw.githubusercontent.com/iamhyc/Overleaf-Workshop/master/docs/assets/demo01-login.gif" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

1. Find Overleaf cookies:

   <img src="https://drive.google.com/thumbnail?id=1GMargv1kBL1PgZEeZrn31QZQcDoY-_vE&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

   Go to [Overleaf homepage](https://www.overleaf.com/project) in Chrome > Open the browser developer tools (F12), go to <span class="env-green">"Network"</span> tab > In the Filter field, type "project" > Click the project under "Name" column > Go to <span class="env-green">"Headers"</span> tab > Scroll down to "Request Headers" section > Copy the value of <span class="env-green">"Cookie"</span>.

2. In VS code:

   Go to the Overleaf Workshop extension, click "log in with cookies", paste the cookies you copied from the browser, and click "Log in".

When the login is successful, you will see your Overleaf projects listed in the extension sidebar. And you will see the server status at the bottom left corner of VS Code.

<img src="https://drive.google.com/thumbnail?id=11DjiuuRo0RpFmWOqtQWSxQChnkNlyTRV&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />


**Highlight features:**

- Sync with Overleaf Cloud
  
  User cursor indicator will show your position.

- Chat with Collaborators (copy line reference)
  
  <img src="https://raw.githubusercontent.com/iamhyc/Overleaf-Workshop/master/docs/assets/demo06-chat.gif" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

- **On-the-fly Compiling and Previewing**

  Real-time PDF preview as you type.

  - Cmd + Option + B (on macOS) to compile, and
  - Cmd + Option + V to preview 

  The [compiling](https://github.com/overleaf-workshop/Overleaf-Workshop/blob/master/docs/wiki.md#compile-the-project) is done on Overleaf servers. The pdf output together with all auxiliary files will be in a folder named `/.output/` in your project.
  
  Your lock latex compiler, such as Latex Workshop, <span class="env-orange">won't</span> work here.

**Caveats:**

- Do <span class="env-orange">NOT</span> use the Overleaf Workshop "Open Projects Locally" feature. 
  
  ❗️ Using a local version leads to major issues, including edit conflicts and data loss. See this [GitHub issue](https://github.com/iamhyc/Overleaf-Workshop/issues/180).

--------------------------------------------------------------------------------

Overleaf pdf viewer supports three **themes**: `default` (white), `light` (warm yellow, easy on eyes 👍), and `dark`. You can change the theme via clicking the theme button (the square) on the title bar in the Overleaf PDF viewer.  
P.S. If you cannot see the theme button, please make sure the PDF viewer is wide enough.

<img src="https://drive.google.com/thumbnail?id=1dJ3METG2LREwSDj3w4rLzj2vARE-RVg4&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

--------------------------------------------------------------------------------

**SyncTeX and Reverse SyncTeX**

The SyncTeX and Reverse SyncTeX are supported in the Overleaf PDF viewer.

-   **SyncTeX, Jump to PDF**: Also called forward sync. 
    
    Put your cursor in the expected position in the document editor, then press `Cmd`+`Option`+`J` (Mac) to jump to the corresponding position in the PDF.

    At first the keybinding did not work for me. To fix it, I need to change the `when` condition of the command `overleaf-workshop.compileManager.syncCode`.

    Open Keyboard Shortcuts (`⌘`+`K`, `⌘`+`S`), search for `overleaf-workshop.compileManager.syncCode`. Right click the command, select `Change When Expression`, and change it to: "editorTextFocus && resourceScheme == 'overleaf-workshop'".

    The final keybinding looks like this:
    
    ```json
    {
      "key": "alt+cmd+j",
      "command": "overleaf-workshop.compileManager.syncCode",
      "when": "editorTextFocus && resourceScheme == 'overleaf-workshop'"
    }
    ```

-   **Reverse SyncTeX, Jump to Code**: backward sync. Double click on the text on PDF to jump to the corresponding position in the editor.


Q: Editor stops responding when compiling tex for preview.   
A: Disable auto build on save. This way, you can have a smooth editing experience and only compile when you need to preview. Use `⌥`+`⌘`+`B` to compile when needed.

```json
"overleaf-workshop.compileOnSave.enabled": false
```

### GitHub Integration

Left side bar > Integrations <i class="bi bi-file-code-fill" style="font-size: 1.5em"></i> > GitHub <i class="fa-brands fa-github" style="font-size: 1.5em"></i>

This will create a GitHub repository and link it to your Overleaf project. You can then clone the repository to your local machine and use Git to sync changes between your local machine and Overleaf.

**Cloning the repository to your computer**

1. On GitHub, navigate to the main page of the repository.
2. Click the green  **<i class="bi bi-code"></i> Code** button > Copy the URL for the repository.
3. Open Terminal > Go to your local folder where you want to clone the repository, then run:

   ```bash
   git clone <repository URL>
   ``` 


**Synchronizing changes**

Synchronization between GitHub and Overleaf does NOT happen automatically. Synchronization options are shown by clicking the **GitHub** option within **Integrations**.

<img src="https://drive.google.com/thumbnail?id=1S54nTbx3W-l05m1r62v0AenZLw66H4Mw&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

- GitHub ahead of Overleaf: Pull changes from GitHub to Overleaf.
- Overleaf ahead of GitHub: Push changes from Overleaf to GitHub.


**Resolving merge conflicts**

Merging conflicts happen when your collaborator changed a line in Overleaf and you **changed the same line** in the GitHub repository, Overleaf may not be able to choose which version to keep.

Suggested practice: Always pull changes from GitHub to Overleaf before pushing changes from Overleaf to GitHub. This way, you can resolve any conflicts locally on your computer before pushing the changes to GitHub.


ref: [GitHub synchronization](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization)



