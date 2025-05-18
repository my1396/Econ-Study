---
layout: post
title: Research and Teaching Tools
tag: life
update: 2024-08-12
---



## Notion

Pressing `/` in Notion brings up a full menu of content blocks you can choose to insert. You can shortcut this further by pressing `/` and then typing what you want. 



How to center text: insert a block equation then use `\text{}`.



| Shortcut | Function                   |
| -------- | -------------------------- |
| cmd + E  | turn text into inline code |



Add inline equations

- method 1: type 2 dollar signs, i.e., `$$`, followed by your eqn., then close with another 2 dollar signs.
- method 2: type `/inline` equation





Add block eqn: type `/math`

Add quote blocks: type `"` followed by `space` to create a quote block.



## DataCamp

DataCamp Classrooms grant full Teams access for six months for all members of the Classroom. Students and teachers have full access to every piece of content on DataCamp except courses on Tableau and Power BI. Additionally, teachers will have access to Teams admin features in the group dashboard like Assignments, Teams, Leaderboards, Reporting, and more.

Furthermore, DataCamp Classrooms accounts and their members gain access to an upgraded version of DataLab with more 2xCPU and 4 GB RAM and full access to DataCamp Certification and DataCamp Jobs.



___

## VS Code

Markdown Preview: <https://code.visualstudio.com/docs/languages/markdown#_markdown-preview>

**Keyboard shortcuts**

| Shortcut | Function            |
| -------- | ------------------- |
| ⇧⌘K      | Delete current line |

Useful Extensions:

- `Markdown Preview Enhanced`, `Markdown+Math`



___

Q: Is it possible to set max lines of a table printed in notebook?  
A: The simple answer is NO. Seetings → Feasures → Notebook only limits the cell size of a pure text based output. It does NOT apply to outputs such as matrices, dataframes or other spreadsheet-like outputs (e.g. from the `View()` function in R.)

___

[Change settings of VS Code](https://code.visualstudio.com/docs/configure/settings)

- change directly in the user settings file (`settings.json`), or
- open Code → Settings (cmd + ,)

Setting file locations: 

- **macOS** `$HOME/Library/Application\ Support/Code/User/settings.json`



Run `Open Config Script` to open `config.js` (a JavaScript configuration file):

- define TeX macros `KatexConfig`, `mathjaxConfig` ...



Q: What is the [difference between `.json` and `.js`](https://www.koombea.com/blog/json-vs-javascript/)?  
A: `.json` is a subset of `.js`, which stands for JavaScript. 

- If you store only data, use `.json`; 

  You can think of `.json` as a YAML frontmatter in markdown.

- if you have some sort of logic (functions, conditions, loops ...), use `.js`.



Q: How to preview a markdown file?  
A: Two options:

- Open Preview (⇧⌘V)
- Open Preview to the Side (⌘K V)

Use either the keyboard shortcuts or click the Preview button. 

- Double clicking an element in the Markdown preview will automatically open the editor for the file and scroll to the line nearest the clicked element.

<img src="https://drive.google.com/thumbnail?id=14rY5JBq2TNjT7Z4Nc5x5_jMa0esNGlN5&sz=w1000" alt="VS code: preview markdown" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />



___

Q: How to open the User settings?  
A: Follow the following steps:

1. Open the command palette (either with F1 or Ctrl+Shift+P)
2. Type *"open settings"*
3. You are presented with a few options, choose **Open User Settings (JSON)**

You can change setting using the UI or there is a `settings.json` file which saves all configurations.

VS Code includes a button in the Settings UI gutter which can be used to switch between JSON and graphical view.

<img src="https://drive.google.com/thumbnail?id=1-l2nIxBZuTRE5_zHkirjS4HzZ_5c-be5&sz=w1000" alt="VS Settings" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />



Q: How to spell check code and document?  
A: Use the extension [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker). Put your cursor in the word, use `Cmd`+`.` to show suggestions and select.



Q: How to ignore unknown words?  
A: Go to Settings (⌘,) → `cSpell.diagnosticLevel` → Choose `Hint`  from the drop down menu. 

<img src="https://drive.google.com/thumbnail?id=1ZxDhrGmvNKGtokZ88epXUw7zw7hEG3Dl&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:60%;" />





Q: How to get a preview of Rmarkdown?  
A: Open `settings.json`, add the following code inside the braces.

```css
"files.associations": {
     "*.Rmd": "markdown"
}
```



Q: How to change [Markdown preview security](https://code.visualstudio.com/docs/languages/markdown#_markdown-preview-security)?  
A: You can change what content is allowed in the Markdown preview by clicking on the popup or running the `Markdown: Change preview security settings` command in any Markdown file.



Q: How to show my installed extensions?  
A: By default, the Extensions view will show the extensions you currently have installed, and all extensions that are recommended for you. You can use the **Extensions: Focus on Installed View** command, to show the installed ones.



___

### Markdown Preview Enhanced

Q: How to define MathJax macros?  
A: You can configure MathJax by running command `Markdown Preview Enhanced: Open MathJax Config`.



Q: How to set Math Rendering Engine?  
A: Run command `Markdown Preview Enhanced: Math Rendering Option`.

<img src="https://drive.google.com/thumbnail?id=1rH7Yf7_8nzpEoHKeqnKBfRPSRzj4JE41&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

References:

- <https://github.com/shd101wyy/vscode-markdown-preview-enhanced/issues/67>



Q: How to enable automatic numbering for MathJax?  
A: Run `Open Config Script` (will open `config.js`, a JavaScript configuration file), and add 

```css
mathjaxConfig: {
  tex: {
    tags: 'ams',
    "macros": {
        bold: ["{\\boldsymbol #1}", 1], // use \bold as a shorthand
        indep: "{\\perp \\!\\!\\! \\perp}",
        // bold face capital letter
        bA: "\\boldsymbol{A}",
    }
  }
};
```

to tell the TeX input processor to use the AMS **numbering** rules (where only certain environments produce numbered equations, as they would be in LaTeX, e.g., `\begin{equation}`).

You can use `\notag` or `\nonumber` to prevent individual equations from being numbered, and `\tag{}` can be used to override the usual equation number with your own symbol instead (or to add an equation tag even when automatic **numbering** is off).

You can also define your TeX macros in `config.js`.

File path: `/Users/menghan/.local/state/crossnote/config.js`



Q: How to use dark theme for Markdown Preview Enhanced (MPE)?  
A:  Run command `Markdown Preview Enhanced: Preview Theme`, choose `github-dark.css`.

<img src="https://drive.google.com/thumbnail?id=1cyw-XBsexYGX08gR79k0WqjvRC9gH1f4&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />



Q: How to get separate preview for individual files?  
A:  MPE has one preview tab for all files by default. You can change this by going to preferences > Markdown Preview Enhanced > Preview Mode > Set to Multiple Previews. Restart VS Code to activate the setting.

<img src="https://drive.google.com/thumbnail?id=1eCCWZT7c8UZA3o_WpTRGP8xsfN6tfvrX&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />



___

### Markdown+Math

https://marketplace.visualstudio.com/items?itemName=goessner.mdmath

Use KaTeX, which is supposedly a fast math renderer.

Function: Simplify the process of authoring and live previewing markdown documents containing math formulas.

Use: Typeset in your markdown source window and see the preview window live updating.

**Define macros for mdmath**

Option 1: use user settings

opt+, open pereferences, add your macros directly there.

```css
"mdmath.macros": {
        "\\indep": "{\\perp \\!\\!\\! \\perp}",
        "\\E": "\\mathbb{E}",
    },
```

Option 2: save macros in a file and add the file path. The file take priority. That means the defined macros in option 1 will be ignored if a definition file exists.

Issue: This does not work somehow.

```css
"mdmath.macroFile": "/Users/menghan/Documents/mac_setup/config_files/mdmath_macros.json",
```

After adding the macros in preferences, need to restart VS Code to enable them.



___

### Quarto

You can install the Quarto extension from the [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=quarto.quarto).

But if you have associated `.qmd` with Markdown previewer as follows

```css
"files.associations": {
   "*.Rmd": "markdown",
	 "*.qmd": "markdown",
}
```

then it won't be recognized by the Quarto extension and will be processed as a regular markdown file.



___

### SQL Server (MSSQL)

FactSet: Connect to Azure SQL with Microsoft Entra authentication and SqlClient

FactSet uses <span style='color:#00CC66'>**Microsoft Entra ID**</span> as the authentication type. Microsoft Entra ID is previously known as [Azure Active Directory (Azure AD)](https://learn.microsoft.com/en-us/entra/fundamentals/new-name)

Microsoft Entra authentication uses identities in Microsoft Entra ID to access data sources such as Azure SQL Database.

`Active Directory Interactive` authentication supports multifactor authentication technology to connect to Azure SQL data sources. If you provide this authentication mode in the connection string, an Azure authentication screen appears and asks the user to enter valid credentials. You can't specify the password in the connection string.

Issue: cannot run SQL notebook as in Azure Data Studio
