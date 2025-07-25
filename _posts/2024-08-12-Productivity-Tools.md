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

### Layout

<img src="https://drive.google.com/thumbnail?id=1Ibf8FiPU7Ghc_ckzu1btT44VlRFnVJ4d&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

- **Panel** (<kbd>cmd</kbd> + <kbd>J</kbd>)- An additional space for views below the editor region. By default, it contains output, debug information, errors and warnings, and an integrated terminal. The Panel can also be moved to the left or right for more vertical space.



**Keyboard shortcuts**

| Shortcut                                        | Function                  |
| ----------------------------------------------- | ------------------------- |
| <kbd>dd</kbd>                                   | use vim shortcut          |
| <kbd>cmd</kbd> + <kbd> J</kbd>                  | toggle Panel              |
| <kbd>ctrl</kbd> + <kbd>cmd</kbd> + <kbd>I</kbd> | open GitHub Copilot chat  |
| <kbd>opt</kbd> + <kbd>cmd</kbd> + <kbd>B</kbd>  | close GitHub Copilot chat |

Useful Extensions:

- Markdown: `Markdown Preview Enhanced`, `Markdown+Math`, `Markdown All in One`
- TeX: `LaTeX-Workshop` (this installs `intellisense` automatically)
- Spell check, autocomplete: `Code Spell Checker`, `intellisense`



**Find and Replace in Selection**

1. cmd + F to open Find/Replace
2. Select your line of text
3. Click the "Fine in selection" icon to the right (or using keyboard shortcut opt + cmd + L)
4. Enter your find and replace characters in their inputs
5. Click the Replace all icon



**Language Identifiers**

In Visual Studio Code, each [language mode](https://code.visualstudio.com/docs/languages/overview#_changing-the-language-for-the-selected-file) has a unique specific language identifier. That identifier is rarely seen by the user except in the settings, for example, when associating file extensions to a language:

```json
"files.associations": {
    "*.myphp": "php"
}
```

Note that <span style='color:#008B45'>casing matters</span> for <span style='color:#008B45'>exact identifier</span> matching ('Markdown' != 'markdown')

Every language defines its *id* through the `languages` configuration point in the extension's `package.json` file:

```json
"languages": [{
    "id": "java",
    "extensions": [ ".java", ".jav" ],
    "aliases": [ "Java", "java" ]
}]
```

You can find a list of known identifiers in the [language identifier reference](https://code.visualstudio.com/docs/languages/identifiers#_known-language-identifiers).

___

**Version Control**

Visual Studio Code has integrated source control management (SCM) and includes [Git](https://git-scm.com/) support out-of-the-box.

Use the Source Control icon <img src="https://drive.google.com/thumbnail?id=1WI9raE7rHUOpel0q-qKOD0B5DtVWGrc3&sz=w1000" alt="" style="zoom:10%;" /> in the activity bar to access the Source Control view.

Error: No source control providers registered.  
Cause: Git built-in extension was disabled.  
Fix: Go to Extensions, type: `@builtin git`, then **Enable** Git from the Git extension settings.

The Source Control view shows the details of your current repository changes: CHANGES, STAGED CHANGES and MERGE CHANGES.

When you select a file in the Source Control view, you will see the changes that you have made to that file in a diff editor.

<img src="https://drive.google.com/thumbnail?id=17hy2XUkkIHQ6BytDXQ1raHOYVmq7mcEE&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />



File version control status

- **U** - Untracked file
- **A** - Added file
- **M** - Modified file





___

**Code Actions**

Code Actions can provide both refactorings and **Quick Fixes** for detected issues (highlighted with <span style='color:#EE0000FF'>red squiggles</span>). When the cursor is on a squiggle or on a selected text region, VS Code shows a light bulb icon 💡 in the editor to indicate that a Code Action is available. If you select the Code Action light bulb or use the **Quick Fix** command ⌘., the Quick Fixes and refactorings control is presented.

> If you have enabled GitHub Copilot, you can choose to fix with Copilot. This is a very convenient way to debug your code.

Q: What is refactoring?  
A: Visual Studio Code supports refactoring operations (*refactorings*) such as [Extract Method](https://refactoring.com/catalog/extractMethod.html) and [Extract Variable](https://refactoring.com/catalog/extractVariable.html) to improve your codebase from within the editor. For example, a common refactoring used to avoid duplicating code (a maintenance headache) is the [Extract Method](https://refactoring.com/catalog/extractMethod.html) refactoring, where you select source code and pull it out into its own shared method, so that can reuse the code elsewhere.



___

### **Snippets**

Snippets files are written in JSON, support C-style comments, and can define an *unlimited number* of snippets. Snippets support most TextMate syntax for dynamic behavior, intelligently format whitespace based on the insertion context, and allow easy multiline editing.

- a **language** snippet file

  Single-language user-defined snippets are defined in a specific language's snippet file (for example `javascript.json`), which you can access by language identifier through **Snippets: Configure Snippets**. 

  A snippet is only accessible when editing the language for which it is defined.

- a **global** snippet file

  Multi-language and global user-defined snippets are all defined in "global" snippet files (JSON with the file suffix `.code-snippets`), which is also accessible through **Snippets: Configure Snippets**. 

  File path: <span style='color:#008B45'>`$HOME/Library/Application Support/Code/User/snippets`</span>

Creata your own snippets: `Code` > `Settings` > `Configure Snippets`

**Syntax**

```json
// in file 'Code/User/snippets/javascript.json'
{
  "For Loop": {
    "prefix": ["for", "for-const"],
    "body": ["for (const ${2:element} of ${1:array}) {", "\t$0", "}"],
    "description": "A for loop."
  }
}
```

- "For Loop" is the snippet name. 

  `prefix` defines one or more <span style='color:#008B45'>trigger words</span> that display the snippet in IntelliSense. Substring matching is performed on prefixes, so in this case, "fc" could match "for-const".

  `body` is one or more lines of content, which will be joined as multiple lines upon insertion. Newlines and embedded tabs will be formatted according to the context in which the snippet is inserted.

  `description` is an *optional* description of the snippet displayed by IntelliSense.

  `scope` optional property that takes one or more [language identifiers](https://code.visualstudio.com/docs/languages/identifiers), which makes the snippet available only for those specified languages. If no `scope` property is given, then the global snippet is available in **all** languages.

- Use `$1`, `$2` to specify cursor locations. The number is the order in which tabstops will be visited, whereas `$0` denotes the final cursor position. 

  The `body` of the example above has three placeholders (listed in order of traversal): `${1:array}`, `${2:element}`, and `$0`. You can quickly jump to the next placeholder with <kbd>Tab</kbd>.

  `$0` is an optional special case that always comes last.

- **Placeholders** are tabstops with values, like `${1:foo}`. The placeholder text will be inserted and selected such that it can be easily changed. Placeholders can be nested, like `${1:another ${2:placeholder}}`.

  The string after the colon `:` (if any) is the default text. 

- **Variables**: With `$name` or `${name:default}`, you can insert the value of a variable. 

  - <span style='color:#008B45'>`TM_SELECTED_TEXT`</span> The currently selected text or the empty string.

-  With `\` (backslash), you can escape `$`, `}`, and `\`. 
- Multilined `body`: simply wrap each line with double quotes.

Q: When using `$TM_SELECTED_TEXT`, if you type the prefix, the selected text will be overwritten. What to do with it?  
A: VS code remembers the text. When you finish typing the prefix, the formated text will show up accordingly.

```json
// customer defined snippets
{
	"Colored Span Green": {
		"prefix": "cs-green",
		"body": [
			"<span style=\"color: #008B45;\">$TM_SELECTED_TEXT</span>$0"
		],
		"description": "Insert a green colored span"
	},
	"Math Helper Parentheses": {
		"scope": "markdown, latex",
		"prefix": "\\(",
		"body": [
			"\\left($1\\right)$0"
		],
		"description": "Insert parentheses with LaTeX math formatting"
	},
	"Math Helper Brackets": {
		"scope": "markdown, latex",
		"prefix": "\\[",
		"body": [
			"\\left[$1\\right]$0"
		],
		"description": "Insert brackets with LaTeX math formatting"
	},
}
```

- `"scope": "markdown, latex"` set `scope` to  `"markdown, latex"` such that `\(` works inside dollar signs.

- To [escape double backslashes](https://github.com/microsoft/vscode/issues/33933#issuecomment-328793257), you have to use `\\\\\\\\`.
  - In TextMate you *can* but must not escape a backslash with a backslash, so to insert 1 backslash have either `\` or `\\`
  - In JSON you *must* escape a backslash with another backslash, so to insert 1 backslash have either `\\` or `\\\\`, to insert 2 `\\\\\\\\`

list of user defined snippets

| prefix                           | command           |
| -------------------------------- | ----------------- |
| `cs-green` / `cs-red`/ `cs-blue` | colored html span |
| `\(`                             | `\left(\right)`   |
| `\[`                             | `\left[\right]`   |
| `vec`                            | row vector        |
| `cvec`                           | column vector     |
| `mat`                            | variance matrix   |





___

Q: Is it possible to set max lines of a table printed in notebook?  
A: The simple answer is NO. Seetings → Feasures → Notebook only limits the cell size of a pure text based output. It does NOT apply to outputs such as matrices, dataframes or other spreadsheet-like outputs (e.g. from the `View()` function in R.)

___

[Change settings of VS Code](https://code.visualstudio.com/docs/configure/settings)

- **Menu bar**: Code → Settings (keyboard shortcut: <kbd>cmd</kbd> + <kbd>,</kbd>)
- **Configuration file**: change directly in the user settings file (`settings.json`)

**Setting file locations**: 

- **macOS User Settings:** Global settings that apply to **all VS Code workspaces and projects**

  Located in the user's home directory in the VS Code application data folder: `$HOME/Library/Application\ Support/Code/User/settings.json`

  Examples: Theme, font size, editor preferences, extensions settings, etc.

  Lower priority (can be overridden by workspace settings)

- Workspace Settings: Project-specific settings that apply only to the current workspace/project.

  Located in `.vscode/settings.json` inside the project folder.

  Examples: Project-specific linting rules, build configurations, language settings for this project

  **Priority**: Higher priority (overrides user settings)



Run `Open Config Script` to open `config.js` (a JavaScript configuration file):

- define TeX macros `KatexConfig`, `mathjaxConfig` ...



Q: What is the [difference between `.json` and `.js`](https://www.koombea.com/blog/json-vs-javascript/)?  
A: `.json` is a subset of `.js`, which stands for JavaScript. 

- If you store only data, use `.json`; 

  You can think of `.json` as a YAML frontmatter in markdown.

- if you have some sort of logic (functions, conditions, loops ...), use `.js`.



Q: How to customize language-specific setttings?  
A: Open User Settings → Type `@lang:markdown` into the search widget. This will show configurable settings for that specific language. Alternatively, you can change directly in the settings JSON file.

```json
"[markdown]": {
    "editor.formatOnSave": true,
    "editor.wordWrap": "on",
    "editor.renderWhitespace": "all",
    "editor.acceptSuggestionOnEnter": "off"
  }
```





Q: How to preview a markdown file?  
A: Two options:

- Open Preview (⇧⌘V)
- Open Preview to the Side (⌘K V)

Use either the keyboard shortcuts or click the Preview button. 

- Double clicking an element in the Markdown preview will automatically open the editor for the file and scroll to the line nearest the clicked element.

<img src="https://drive.google.com/thumbnail?id=14rY5JBq2TNjT7Z4Nc5x5_jMa0esNGlN5&sz=w1000" alt="VS code: preview markdown" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />



___

Q: How to open the User settings json file?  
A: Follow the following steps:

1. Open the command palette (either with F1 or <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>)
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



Q: How to show my installed extensions?  
A: By default, the Extensions view will show the extensions you currently have installed, and all extensions that are recommended for you. You can use the **Extensions: Focus on Installed View** command, to show the installed ones.



Q: Disable <kbd>Enter</kbd> to accept suggestions as this confuses inserting a new line.  
A: Set **Editor: Accept Suggestion On Enter** to `off`. 



___

### Markdown

Q: How to get a preview of Rmarkdown?  
A: Open `settings.json`, add the following code inside the braces.

```json
/* this adds additional file extensions to markdown */
"files.associations": {
    "*.Rmd": "markdown",
    "*.qmd": "markdown",
},
```

A drawback of this setting is that you cannot run codes inside the markdown files.



Q: How to get autocomplete, syntax highlighting in Markdown?  
A: Install `Latex Workshop` by James Yu → Switch Language Mode from `Markdown` to `markdown_latex_combined`.

This will disable markdown preview! Therefore, not recommended. ❌

Use `Markdown All in One` extension instead. ✅



Q: How to change the language for the selected file?  
A: In the status bar, click the language indicator. This will bring up the **Select Language Mode** dropdown where you can select another language for the current file.

<img src="https://drive.google.com/thumbnail?id=1d1R_ErtbQeWARja7SbsTsusiP_5Z5hS1&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:120%;" />



Q: How to change [Markdown preview security](https://code.visualstudio.com/docs/languages/markdown#_markdown-preview-security)?  
A: You can change what content is allowed in the Markdown preview by clicking on the popup or running the `Markdown: Change preview security settings` command in any Markdown file.



**Visual Mode and Source Mode**

Visual Mode has inline prview of eqns, and in time preview of your markdown, like in Typora.

Side-to-side preview can be slow and the previewer can crash for a large file. That's where Visual Mode comes in handy.

<img src="https://drive.google.com/thumbnail?id=1j_Btjvfn-PXR6lnNvIafGh4EOo1mK_xW&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />





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

<https://marketplace.visualstudio.com/items?itemName=goessner.mdmath>

Use KaTeX, which is supposedly a fast math renderer.

Function: Simplify the process of authoring and live previewing markdown documents containing math formulas.

Use: Typeset in your markdown source window and see the preview window live updating.

**Define macros for mdmath**

Option 1: use user settings

opt+, open pereferences, add your macros directly there.

```json
"mdmath.macros": {
        "\\indep": "{\\perp \\!\\!\\! \\perp}",
        "\\E": "\\mathbb{E}",
},
```

Option 2: save macros in a file and add the file path. The file take priority. That means the defined macros in option 1 will be ignored if a definition file exists.

Issue: This does not work somehow.

```json
"mdmath.macroFile": "/Users/menghan/Documents/mac_setup/config_files/mdmath_macros.json",
```

After adding the macros in preferences, need to restart VS Code to enable them.



___

### Quarto

You can install the Quarto extension from the [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=quarto.quarto).

But if you have associated `.qmd` with Markdown previewer as follows

```json
"files.associations": {
   "*.Rmd": "markdown",
   "*.qmd": "markdown",
}
```

then it won't be recognized by the Quarto extension and will be processed as a regular markdown file.



___

### LaTeX-Workshop

Snippets: <https://github.com/James-Yu/LaTeX-Workshop/wiki/Snippets#Handy-mathematical-snippets>

The following works in `markdown` inside math environment

| Prefix | Command |
| ------ | ------- |
| `__`   | `_{$1}` |
| `**`   | `^{$1}` |
| `...`  | `\dots` |

Environment snippets works directly in `tex`, you type `B`, a drop-down list will show up for you to choose

- In markdown, these cmds work only inside math environments (`$...$`)

| Prefix | Environment name                           |
| ------ | ------------------------------------------ |
| `BEQ`  | `equation`                                 |
| `BSEQ` | `equation*`                                |
| `BAL`  | `align`                                    |
| `BSAL` | `align*`                                   |
| `BGA`  | `gather`                                   |
| `BSGA` | `gather*`                                  |
| `BMU`  | `multline`                                 |
| `BSMU` | `multline*`                                |
| `BIT`  | `itemize`                                  |
| `BEN`  | `enumerate`                                |
| `BSPL` | <span style='color:#008B45'>`split`</span> |
| `BCAS` | `cases`                                    |
| `BFR`  | `frame`                                    |
| `BFI`  | `figure`                                   |
| `BTA`  | `table`                                    |



[`@` suggestsion](https://github.com/James-Yu/latex-workshop/wiki/Intellisense#-suggestions)

LaTeX-Workshop provides an independent intellisense mechanism triggered by `@`. For example, you can type `@a` for `\alpha`. It works for most Greeks and have some useful mathmatical helpers.

| Prefix | Command               |
| ------ | --------------------- |
| `@(`   | `\left( $1 \right)`   |
| `@{`   | `\left\{ $1 \right\}` |
| `@[`   | `\left[ $1 \right]`   |
| `@^`   | `\Hat{$1}`            |
| `@_`   | `\bar{$1}`            |



___

### Code Spell Checker

Words not in the dictionary files will have a squiggly underline.

Its configuration starts with `cSpell`.

In text-based documents like `.md` and `.qmd` files, the spell checker checks all words. In code-based documents like `.py` and `.R` files, the spell checker only checks strings and comments.



___

### [Intellisense](https://code.visualstudio.com/docs/editing/intellisense)

IntelliSense is a general term for various code editing features including: code completion, parameter info, quick info, and member lists. IntelliSense features are sometimes called by other names such as "code completion", "content assist", and "code hinting."

The inferred symbols are presented first, followed by the global identifiers (indicated by the `abc` word icon).

<img src="https://drive.google.com/thumbnail?id=1gqkzo3mHgWLM140lZFbUdohqffb0rNu3&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:60%;" />

The editor supports *tab completion*, which inserts the best matching completion when pressing <kbd>Tab</kbd>.

**Settings**

```json
// Controls if quick suggestions should show up while typing
"editor.quickSuggestions": {
    "other": true,
    "comments": false,
    "strings": false
},
```



___

### GitHub Copilot

Q: How to delete chat histories?  
A: In the chat window, click the <img src="https://drive.google.com/thumbnail?id=1D0LNpQUiAxzdsyQ2W3anXc3_UREkdBgM&sz=w1000" alt="" style="zoom:5%;" /> icon, it will show history chats in the command palette. You can delete any chats from there. 

Chat histories are stored in `/Users/menghan/Library/Application Support/Code/User/workspaceStorage/[long-serial-number...]/chatSessions`



Q: In chat window, set <kbd>Enter</kbd> to line break and <kbd>Shift</kbd> + <kbd>Enter</kbd> to submit.  
A: Add the following settings to `keybindings.json`

```json
{
    "key": "shift+enter",
    "command": "workbench.action.chat.submit",
    "when": "inChatInput"
},
{
    "key": "enter",
    "command": "-workbench.action.chat.submit",
    "when": "inChatInput"
},
{
    "key": "enter",
    "command": "editor.action.insertLineAfter",
    "when": "inChatInput"
}
```

To summarize the Enter behavior:

- **Enter** now creates a new line in GitHub Copilot Chat
- **Shift+Enter** submits your message



Explain different modes of Github Copilot:

- **Agent Mode** 🤖
  - Complex, multi-step tasks that require planning and coordination
  - Tasks that span multiple files or require understanding project structure
  - When you need systematic problem-solving with multiple tool invocations
  - Research and analysis tasks that require gathering information from various sources
- **Edit Mode** ✏️
  - Direct code modifications and quick fixes
  - When you know exactly what needs to be changed
  - Focused, single-purpose edits
  - Implementing specific functionality or bug fixes
- **Ask Mode** 💬
  - Learning and understanding concepts
  - No code modifications
  - Educational and consultative



___

### SQL Server (MSSQL)

FactSet: Connect to Azure SQL with Microsoft Entra authentication and SqlClient

FactSet uses <span style='color:#00CC66'>**Microsoft Entra ID**</span> as the authentication type. Microsoft Entra ID is previously known as [Azure Active Directory (Azure AD)](https://learn.microsoft.com/en-us/entra/fundamentals/new-name)

Microsoft Entra authentication uses identities in Microsoft Entra ID to access data sources such as Azure SQL Database.

`Active Directory Interactive` authentication supports multifactor authentication technology to connect to Azure SQL data sources. If you provide this authentication mode in the connection string, an Azure authentication screen appears and asks the user to enter valid credentials. You can't specify the password in the connection string.

Issue: cannot run SQL notebook as in Azure Data Studio



___

Q: How to share scripts among multiple projects in one solution? For instance, mathjax config file?   
A: Unresolved yet …



