---
layout: post
title: VS Code Extension – LaTeX Workshop
tag: programming
update: 2025-08-01
---

<a class="top-link hide" href="#" id="js-top">↑</a>

[**LaTeX Workshop**](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) is a popular LaTeX extension for Visual Studio Code, providing a comprehensive set of features for LaTeX editing, compiling, and previewing. In the following, I summarize some useful settings and tips for using LaTeX Workshop effectively.

**Highlight features:**

- **Writing assistance**
  - AI prompts from GitHub Copilot
    
    This is the most important reason I use VS Code for LaTeX editing, rather than Overleaf (online LaTeX editor) or [TexShop](https://pages.uoregon.edu/koch/texshop/). It is also what distinguishes VS Code from the other LaTeX editors.

    With an university email, you can get [GitHub Copilot Pro](https://docs.github.com/en/copilot/how-tos/manage-your-account/get-free-access-to-copilot-pro) for free. It is a powerful tool to help me to write academic papers, create reports, and prepare teaching materials. ✅

    See <a href="{{site.baseurl}}/2023/10/12/GitHub101.html#github-education">HERE</a> for more details about GitHub Copilot Education benefits.

- **Editing**
  - Intellisense for code autocompletion
  - Snippets for quickly insert commonly used commands and environments



**Useful resources:**

- Latex-Workshop GitHub repo: <https://github.com/James-Yu/LaTeX-Workshop/wiki/Install#usage>
- Configure LateX Workshop by Paul Wintz: <https://paulwintz.com/latex-in-vscode/> 👍
- Integrating Overleaf with VS Code: <https://www.youtube.com/watch?v=SaMRCYbsAek>
- Snippets: <https://github.com/James-Yu/LaTeX-Workshop/wiki/Snippets#Handy-mathematical-snippets>


--------------------------------------------------------------------------------

## Installation

Full installation instructions can be found [HERE](https://github.com/James-Yu/LaTeX-Workshop/wiki/Install#installation-and-basic-settings).


The only requirement is a compatible LaTeX distribution in the system PATH. For example, [TeX Live](https://www.tug.org/texlive/). We **strongly recommend**TeX Live.

> After installing TeX Live, you must add the directory of TeX Live binaries to your PATH environment variable.  
> 
> If VS Code cannot find executables of TeX, it means that **the setting of your system is broken**.

💡 Just install the full TeX Live distribution to avoid missing packages. It' a pain to install missing packages one by one.

- [MiKTeX](https://miktex.org/) is another lightweight distribution with a convenient automatic on-demand package install. Note, however, that **for MiKTeX to work correctly with Latex Workshop, you need to install [Perl](https://strawberryperl.com/)**.





--------------------------------------------------------------------------------

## Dark Theme

**Aesthetic themes** for LaTeX Workshop PDF viewer:

```json
"latex-workshop.view.pdf.color.dark.pageColorsBackground": "#F5F5DC", // The background color of the document
"latex-workshop.view.pdf.color.dark.backgroundColor": "#F5F5DC",      // The background color of the viewer, space btw pages
```

This sets the background color and the spacing btw pages in the PDF viewer to **beige** in dark mode, which is easier on the eyes.

❌ <span class="env-orange">A caveat</span> is that this interferes with text color and image color in the document. E.g., If you use colored text `\textcolor{red}{...}`, the text won't appear red. The colored images <span class="env-orange">won't</span> appear in their original colors either.

> Update: 26-01-08  
> Set page background color using LaTeX command instead of LaTeX Workshop settings to avoid the interference with textcolor. 
> ```latex
> \usepackage{graphicx}
> \pagecolor[HTML]{F5F5DC} % beige background for easier reading on screen, remove for print
> ```
> Insert in the preamble to set the page background color to beige.   
> This works both in the internal and external PDF viewer.  
> For printing, just comment out the line.



In the documentation, when you see "Reload vscode to apply the changes", you can do this quickly by pressing `Cmd`+`Shift`+`P` (Mac) to open the command palette, typing `Developer: Reload Window`, and pressing `Enter`.

By default, LaTeX Workshop auto builds the pdf on every save. This can be too frequent and distracting.
I set <span class="env-green">`"files.autoSave": "onFocusChange"`</span> so that the pdf only rebuilds when I switch away from the tex file, not on every keystroke.

--------------------------------------------------------------------------------

## Snippets


Environment snippets works directly in `tex`, you type `B`, a drop-down list will show up for you to choose.

- The prefixes start with `B` and are followed by an abbreviation of the environment name.
- The unnumbered versions of the environments are prefixed with `BS`, e.g., `BSEQ` for `equation*`.
- In `tex`, these cmds work in both math and text environments.
- However, it is more restrictive in `markdown`, where these cmds work only inside math environments (`$...$`)


### Mathematical symbols

| Prefix | Command |
| ------ | ------- |
| `__`   | `_{$1}` |
| `**`   | `^{$1}` |
| `...`  | `\dots` |


### Environments

Commands start with <span class="env-green">`B`</span> for inserting LaTeX environments.

| Prefix                                | Environment name |
| ------------------------------------- | ---------------- |
| <span class="env-green">`BEQ`</span>  | `equation`       |
| `BSEQ`                                | `equation*`      |
| <span class="env-green">`BAL`</span>  | `align`          |
| `BSAL`                                | `align*`         |
| <span class="env-green">`BSPL`</span> | `split`          |
| `BCAS`                                | `cases`          |
| `BGA`                                 | `gather`         |
| `BSGA`                                | `gather*`        |
| `BMU`                                 | `multline`       |
| `BSMU`                                | `multline*`      |
| `BIT`                                 | `itemize`        |
| `BEN`                                 | `enumerate`      |
| `BFR`                                 | `frame`          |
| <span class="env-green">`BFI`</span>  | `figure`         |
| <span class="env-green">`BTA`</span>  | `table`          |

**How to surround some selected text with an environment:**

1. In editing mode, select the text you want to surround.
2. Insert the environment by typing either
   
   - ✅ `\<envname>`, e.g., `\equation`, or
     
     This will surround the selected text with `\begin{envname}` and `\end{envname}`.
     
     <img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/surround-envname.gif" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />
   
   - `\beginend`
     
     This will surround the selected text with `\begin{}` and `\end{}`, and enter the multi-cursor mode. Type your desired environment name in `\begin{}` and the same name will be automatically filled in the `\end{}`.

     <img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/surround-beginend.gif" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

--------------------------------------------------------------------------------

Q: How to select the current environment, e.g., a table environment?  
A: Place the cursor inside the environment, then press `Cmd`+`Shift`+`P` (Mac) to open the command palette, type `Latex Workshop: Select Current Environment`, and press `Enter`. This will select the entire environment, including the `\begin{}` and `\end{}` lines.

<img src="https://drive.google.com/thumbnail?id=1508qMUl5GtzJ0OBamc3wYtJN4T93Hx77&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

- `LaTeX Workshop: Select the current environment content` only selects the content inside the environment, excluding the `\begin{}` and `\end{}` lines.
- `LaTeX Workshop: Navigate to matching begin/end` moves the cursor to the matching `\begin{}` or `\end{}` of the current environment.
- **Changing from one environment to another.** [↩︎](https://github.com/James-Yu/latex-workshop/wiki/Environments#changing-between--and-beginend)
  
  1. Place the cursor inside the environment you want to change.
  2. `LaTeX Workshop: Select the current environment name` to select the environment name.
  3. `LaTeX Workshop: Add a multi-cursor to the current environment name` to add a multi-cursor to both the `\begin{}` and `\end{}` lines.
  4. Type the new environment name to replace the old one.

--------------------------------------------------------------------------------

### [`@` Suggestsions](https://github.com/James-Yu/latex-workshop/wiki/Intellisense#-suggestions)

LaTeX-Workshop provides an independent intellisense mechanism triggered by `@`. For example, you can type `@a` for `\alpha`. It works for most Greeks and have some useful mathematical helpers.

**Mathmetical helpers:**

| Prefix | Command               |
| ------ | --------------------- |
| `@(`   | `\left( $1 \right)`   |
| `@{`   | `\left\{ $1 \right\}` |
| `@[`   | `\left[ $1 \right]`   |
| `@^`   | `\Hat{$1}`            |
| `@_`   | `\bar{$1}`            |

**Inserting Greek letters:**

| Prefix | Command    |
| ------ | ---------- |
| `@a`   | `\alpha`   |
| `@b`   | `\beta`    |
| `@g`   | `\gamma`   |
| `@d`   | `\delta`   |
| `@e`   | `\epsilon` |

___

### Font cmds

Select the text you want to change the font of, then type the prefixes listed below.
<span style="color: #00CC66;"></span>

| Prefix | Command         | Font face                |
| ------ | --------------- | ------------------------ |
| `FBF`  | `\textbf{ $1 }` | **Bold face**            |
| `FIT`  | `\textit{ $1 }` | *Italic face*            |
| `FTT`  | `\texttt{ $1 }` | <tt>Typewriter face</tt> |

More font cmds can be found [HERE](https://github.com/James-Yu/latex-workshop/wiki/Snippets#font-commands-and-snippets).

--------------------------------------------------------------------------------



## Build the document

### LaTeX recipes

You can define several compiling <span class="env-green">toolchains</span> to build LaTeX projects using [**LaTeX recipes**](https://github.com/James-Yu/latex-workshop/wiki/Compile#latex-recipes) and then call the command *Build with recipe* to choose the appropriate toolchain for actually building the project. Alternatively, you can directly select the appropriate recipe from the *TeX* badge <i class="fa-brands fa-tex" style="font-size: 1.5em"></i>.

Below are some commonly used examples:

```json
// Sequence of tools to run for building
"latex-workshop.latex.recipes": [
  {
    "name": "latexmk 🔃",
    "tools": [
      "latexmk"
    ]
  },
  {
    "name": "pdflatex ➞ bibtex ➞ pdflatex*2",
    "tools": [
      "pdflatex",
      "bibtex",
      "pdflatex",
      "pdflatex"
    ]
  },
  {
    "name": "pdflatex ➞ pdflatex",
    "tools": [
      "pdflatex",
      "pdflatex"
    ]
  },
  {
    "name": "xelatex",
    "tools": [
      "xelatex"
    ]
  }
]，
```

Each recipe is an object in the configuration list, consisting of a `name` field and a list of `tools` to be invoked in the recipe. Tools are defined separately in `latex-workshop.latex.tools` (see <a href="#latex-tools">below</a>).

-   The first one simply relies on the `latexmk` command. ✅

    `latexmk` is a Perl script that **automates** the process of building LaTeX documents. It automatically determines the sequence of commands needed to build the document, including handling bibliography and cross-references.

    It is <span class="env-green">intelligent</span>. It determines the minimum necessary compilations based on the changes made to the document. This recipe is fast and efficient for most use cases. 👍

    This is the **default** recipe to use when building a project for the first time.

    <span class="env-green">If you want a different default recipe, put it as the first element</span> of the `latex-workshop.latex.recipes` array.

-   The second one run the following sequence of commands `pdflatex` → `bibtex` → `pdflatex` → `pdflatex`.

    This is a full-fledged build process that handles bibliography and cross-references properly. It is suitable for final compilation before sharing or printing the document.

    **Use scenario:**
    
    - First time building a new document
    - When you have added new citations or references
    - Changed bibliography style of the `.bib` file

-   The third one runs `pdflatex` twice. 
    
    This is useful when you want to run a fast build without bibliography. E.g., when you are just editing regular text and do not need to update citations or references.

-   Many of my projects use <span class="env-green">`xelatex`</span> instead of `pdflatex` to support <span class="env-green">Unicode</span> characters and OpenType fonts. 
    
    This recipe is similar to the second one, but it uses `xelatex` instead of `pdflatex`.

--------------------------------------------------------------------------------

**Set the default recipe to use**

You can change the **default recipe** by setting the [`latex-workshop.latex.recipe.default`](https://github.com/James-Yu/LaTeX-Workshop/wiki/Compile#latex-workshoplatexrecipedefault). Recipes are referred to by their **names** as defined in `latex-workshop.latex.recipes`. 

Note there are two special values:

-   `"first"`: Use the first recipe defined in [`latex-workshop.latex.recipes`](https://github.com/James-Yu/LaTeX-Workshop/wiki/Compile#latex-recipes).
  
    This is the default value.

-   `"lastUsed"`: Use the last used recipe by the command *LaTeX Workshop: 
    
    Build with recipe*. This is useful when you have multiple recipes defined and you want to use the last one you used without having to select it again.

```json
// Set the default recipe to the last used one
"latex-workshop.latex.recipe.default": "lastUsed"
```

--------------------------------------------------------------------------------

### LaTeX tools {#latex-tools}

Each `tool` appearing in the `tools` field of **recipes** above is defined <span class="env-green">`latex-workshop.latex.tools`</span>. To include a tool in a recipe, the tool's `name` should be included in the recipe's `tools` list.

Check default tools [HERE](https://github.com/James-Yu/LaTeX-Workshop/wiki/Compile#latex-tools).

Here is taken from my `settings.json` as an example:

```json
// Tools available for building
"latex-workshop.latex.tools": [
  {
    "name": "latexmk",
    "command": "latexmk",
    "args": [
      "-synctex=1",
      "-interaction=nonstopmode",
      "-file-line-error",
      "-pdf",
      "-outdir=%OUTDIR%",
      "%DOC%"
    ],
    "env": {}
  },
  {
    "name": "pdflatex",
    "command": "pdflatex",
    "args": [
      "-synctex=1",
      "-interaction=nonstopmode",
      "-file-line-error",
      "-output-directory=%DIR%/out_dir",
      "%DOC%"
    ],
    "env": {}
  },
  {
    "name": "bibtex",
    "command": "bibtex",
    "args": [
      "out_dir/%DOCFILE%"
    ],
    "env": {
      "BIBINPUTS": "%DIR%:",
      "BSTINPUTS": "%DIR%:"
    }
  },
  {
    "name": "xelatex",
    "command": "xelatex",
    "args": [
      "-synctex=1",
      "-interaction=nonstopmode",
      "-file-line-error",
      "-output-directory=%OUTDIR%",
      "%DOC%"
    ],
    "env": {}
  }
],
```

Each `tool` is an object consisting of a `name`, a `command` to be spawned, its arguments (`args`) and some specific environment variables (`env`). The `env` entry is a dictionary. Imagine you want to use a `texmf` subdirectory local to your home project, just write

```json
"env": {
    "TEXMFHOME": "%DIR%/texmf"
}
```

Q: What does "spawn" mean?  
A: In computing, to "spawn" a process means to *create a new process* that runs concurrently with the parent process. 


You can also override the PATH environment variable. Notice that, in the property, only placeholders, e.g., `%DIR%`, take effect, and other variables, e.g., `$PATH`, are **not** expanded.

See [HERE](https://github.com/James-Yu/LaTeX-Workshop/wiki/Compile#placeholders) for a full list of supported **placeholders**.

Commonly used placeholders:

| Placeholder  | Description                                      |
| -------------| ------------------------------------------------ |
| `%DIR%`      | The root file directory                          |
| `%DOC%`      | The root file full path without the extension    |
| `%DOC_EXT%`  | The root file full path with the extension       |
| `%OUTDIR%`   | The output directory specified by `latex-workshop.latex.outDir` |


--------------------------------------------------------------------------------

Q: LaTeX builds automatically on every save. It can be too frequent and distracting.  
A; Add `"files.autoSave": "onFocusChange"` to your <span class="env-green">workspace `settings.json`</span> so that the pdf only rebuilds when you switch away from the tex file, not on every keystroke.

Generally you still want your files to save automatically, hence in user `settings.json`, I have:

```json
"files.autoSave": "afterDelay"
```



--------------------------------------------------------------------------------

## SyncTeX

[SyncTeX](https://github.com/James-Yu/latex-workshop/wiki/View#synctex) allows you to jump between the source `.tex` file and the compiled PDF file. This helps you to quickly locate the relevant part of the document when editing or reviewing.

First, enable SyncTeX in the `settings.json`:

```json
// enable 
"latex-workshop.synctex.afterBuild.enabled": true
```
This setting syncs PDF with cursor position after compiling, which defaults to `false`.

- **Forward/Direct synctex** (source to pdf) can either be activated by selecting "<i class="codicon codicon-edit" aria-hidden="true" style="vertical-align: middle;"></i> Navigate, select, and edit" > "<i class="codicon codicon-go-to-file" aria-hidden="true" style="vertical-align: middle;"></i> SyncTeX from cursor" in the side bar <i class="fa-brands fa-tex" style="font-size:1.5em; vertical-align: middle;"></i>. 
  
  Alternatively, use the shortcut <span class="env-green">`cmd`+`option`+`j`</span> (on Mac). ✅


- **Backward/Reverse** synctex (pdf to source) is activated by pointing at the relevant element of the pdf preview. 
  
  When using the internal viewer, the default keybinding to point at an element in the pdf preview is `cmd+click`. 
  
  It can be changed to `double-click` using the setting [`latex-workshop.view.pdf.internal.synctex.keybinding`](https://github.com/James-Yu/latex-workshop/wiki/View#latex-workshopviewpdfinternalsynctexkeybinding).
  
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

## Bib Manager

[Zotero Cite](https://marketplace.visualstudio.com/items?itemName=XING.zotero-cite) is a useful extension to insert reference from Zotero library and add them to your bib file automatically.

- Specify in the <span class="env-green">workspace `settings.json`</span> the path to your bib file:

  ```json
  "zotero-cite.defaultBibName": "bibli.bib",
  ```
  Defaults to `ref.bib`.


**Commonly used features**:

- Command Palette: `Zotero Cite: Cite and Create Bibliography for Pandoc/LaTeX` (ctrl+cmd+r)
  
  A graphical interface pops up, you can search and select references from your Zotero library. You can select multiple references to cite at once. 
  
  <img src="https://drive.google.com/thumbnail?id=1XKclCNCfmwUgrF_wuNZWVItw3_nRvppF&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

  When you have selected all references you need, hit <kbd>Enter</kbd>. The selected citations will be inserted at the cursor position in your document, and the corresponding entries will be added to your bib file automatically.

  <span class="env-orange">Issues:</span> 
  
  - Will always add the bib entries to the end of the bib file, and genearte a new cite key. It does not check if the entry already exists in the bib file.
  - After picking a reference, the Zotero app steals focus.



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

--------------------------------------------------------------------------------

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


<span class="env-green">**Synchronizing changes**</span>

Edit your local repository files using your preferred LaTeX editor (e.g., LaTeX Workshop in VS Code). After making changes, you can push them to GitHub and then pull them into Overleaf.

Synchronization between GitHub and Overleaf does <span class="env-orange">NOT</span> happen automatically. Synchronization options are shown by clicking the **GitHub** option within **Integrations**.

<img src="https://drive.google.com/thumbnail?id=1S54nTbx3W-l05m1r62v0AenZLw66H4Mw&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

- GitHub ahead of Overleaf: Pull changes from GitHub to Overleaf.
- Overleaf ahead of GitHub: Push changes from Overleaf to GitHub.

If you are writing together with collaborators, best practice is to frequently pull changes from GitHub to Overleaf to keep your Overleaf project up to date before you start making changes. 
This helps to minimize the chances of merge conflicts when you push your changes back to GitHub.

In case you and your collaborator both made changes to the sentence, following the next section on **Resolving merge conflicts**.

--------------------------------------------------------------------------------

**Resolve merge conflicts**

Merging conflicts happen when your collaborator changed a line in Overleaf and you **changed the same line** in the GitHub repository, Overleaf may not be able to choose which version to keep.

Suggested practice: Always pull changes from GitHub to Overleaf before pushing changes from Overleaf to GitHub. This way, you can resolve any conflicts locally on your computer before pushing the changes to GitHub.


ref: [GitHub synchronization](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization)

## LaTeX Workshop debug log

Problems Pane: Display LaTeX Workshop debug log in output panel. [↩︎](https://github.com/james-yu/latex-workshop/wiki/compile#settings-details)

**Issue:** The LaTeX Workshop output panel often shows an astonishingly large number of amber warnings. Handreds or something. Many of them are NOT essential, e.g., badbox warnings, they do not affect the document compilation, but they clutter the Problems pane and distract from more important messages. 
I also do NOT like the warning icon next to the file name in the File Explorer panel. It just looks ugly.

To disable these warning messages, add the following settings to your `settings.json`:

```json
{   
    /* Filter out LaTeX warnings from Problems panel */
    // disable badbox warnings
    "latex-workshop.message.badbox.show": "none", 
    // disable biber/bibtex log warnings
    "latex-workshop.message.biberlog.exclude": [
        "^no", 
        "page numbers missing",
        "(?i)Unknown word"
    ],
    "latex-workshop.message.bibtexlog.exclude": [
        "^no",
        "page numbers missing",
        "(?i)Unknown word"
    ],
    // disable specific latex log warnings
    "latex-workshop.message.latexlog.exclude": [
        "^Package",
        "^LaTeX"
    ],
    // disable cSpell for bibtex files
    "cSpell.enabledFileTypes": [
      "bibtex": false,
    ]
}
```



--------------------------------------------------------------------------------

## My Config

<div style="height: 400px; overflow-y: auto;" markdown="1">

```json
{
  /* LaTeX Workshop settings */
  // "latex-workshop.view.pdf.color.dark.pageColorsBackground": "#F5F5DC",
  // "latex-workshop.view.pdf.color.dark.backgroundColor": "#F5F5DC",
  "latex-workshop.view.pdf.sidebar.view": "outline",
  "latex-workshop.synctex.afterBuild.enabled": true,
  "latex-workshop.view.pdf.internal.synctex.keybinding": "double-click",
  "latex-workshop.latex.recipe.default": "lastUsed",
  "latex-workshop.latex.outDir": "%DIR%/out_dir",
  "latex-workshop.latex.clean.subfolder.enabled": false,
  "latex-workshop.latex.autoClean.run": "never",
  "latex-workshop.laterx.clean.method": "glob",
  // Disable warning messages
  "latex-workshop.message.warning.show": false,
  "latex-workshop.message.error.show": true,
  // Auxiliary files to clean
  "latex-workshop.latex.clean.fileTypes": [
    "*.aux",
    "*.bbl",
    "*.blg",
    "*.idx",
    "*.ind",
    "*.lof",
    "*.lot",
    "*.out",
    "*.toc",
    "*.acn",
    "*.acr",
    "*.alg",
    "*.glg",
    "*.glo",
    "*.gls",
    "*.fls",
    "*.log",
    "*.fdb_latexmk",
    "*.snm",
    "*.synctex(busy)",
    "*.synctex.gz(busy)",
    "*.nav",
    "*.vrb",
    "*.synctex.gz",
    "out_dir/*.aux",
    "out_dir/*.bbl",
    "out_dir/*.blg",
    "out_dir/*.fls",
    "out_dir/*.log",
    "out_dir/*.fdb_latexmk",
    "out_dir/*.synctex.gz"
  ],
  // LaTeX build recipes and tools
  "latex-workshop.latex.recipes": [
    {
      "name": "pdflatex ➞ bibtex ➞ pdflatex*2",
      "tools": [
        "pdflatex",
        "bibtex",
        "pdflatex",
        "pdflatex"
      ]
    },
    {
      "name": "pdflatex ➞ pdflatex",
      "tools": [
        "pdflatex",
        "pdflatex"
      ]
    },
    {
      "name": "xelatex",
      "tools": [
        "xelatex"
      ]
    },
    {
      "name": "latexmk 🔃",
      "tools": [
        "latexmk"
      ]
    }
  ],
  "latex-workshop.latex.tools": [
    {
      "name": "latexmk",
      "command": "latexmk",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "-pdf",
        "-outdir=%OUTDIR%",
        "%DOC%"
      ],
      "env": {}
    },
    {
      "name": "pdflatex",
      "command": "pdflatex",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "-output-directory=%DIR%/out_dir",
        "%DOC%"
      ],
      "env": {}
    },
    {
      "name": "bibtex",
      "command": "bibtex",
      "args": [
        "out_dir/%DOCFILE%"
      ],
      "env": {
        "BIBINPUTS": "%DIR%:",
        "BSTINPUTS": "%DIR%:"
      }
    },
    {
      "name": "xelatex",
      "command": "xelatex",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "-output-directory=%OUTDIR%",
        "%DOC%"
      ],
      "env": {}
    }
  ],
}
```

</div>


