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



___

Q: Is it possible to set max lines of a table printed in notebook?  
A: The simple answer is NO. Seetings → Feasures → Notebook only limits the cell size of a pure text based output. It does NOT apply to outputs such as matrices, dataframes or other spreadsheet-like outputs (e.g. from the `View()` function in R.)

___

Change settings of VS

- change directly in the user settings file (`settings.json`), or
- open Code → Settings (cmd + ,)



Q: How to preview a markdown file?  
A: Two options:

- Open Preview (⇧⌘V)
- Open Preview to the Side (⌘K V)

Use either the keyboard shortcuts or click the Preview button. 

- Double clicking an element in the Markdown preview will automatically open the editor for the file and scroll to the line nearest the clicked element.

<img src="https://drive.google.com/thumbnail?id=14rY5JBq2TNjT7Z4Nc5x5_jMa0esNGlN5&sz=w1000" alt="VS code: preview markdown" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />



___

Q: How to open the User settings?  
A: follow the following steps:

- Open the command palette (either with F1 or Ctrl+Shift+P)
- Type *"open settings"*
- You are presented with a few options, choose **Open User Settings (JSON)**

Or VS Code includes a button in the Settings UI gutter which can be used to switch between JSON and graphical view.

<img src="https://drive.google.com/thumbnail?id=1-l2nIxBZuTRE5_zHkirjS4HzZ_5c-be5&sz=w1000" alt="VS Settings" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />



Q: How to spell check code and document?  
A: Use the extension [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker). Put your cursor in the word, use `Cmd`+`.` to show suggestions and select.



___

### SQL Server (MSSQL)

FactSet: Connect to Azure SQL with Microsoft Entra authentication and SqlClient

FactSet uses <span style='color:#00CC66'>**Microsoft Entra ID**</span> as the authentication type. Microsoft Entra ID is previously known as [Azure Active Directory (Azure AD)](https://learn.microsoft.com/en-us/entra/fundamentals/new-name)

Microsoft Entra authentication uses identities in Microsoft Entra ID to access data sources such as Azure SQL Database.

`Active Directory Interactive` authentication supports multifactor authentication technology to connect to Azure SQL data sources. If you provide this authentication mode in the connection string, an Azure authentication screen appears and asks the user to enter valid credentials. You can't specify the password in the connection string.

Issue: cannot run SQL notebook as in Azure Data Studio
