---
layout: post
tag: programming
title: Connect to FactSet
---

<a class="top-link hide" href="#" id="js-top">↑</a>

## Overview

**Steps overview to set up FactSet**:

<ol>
<li> <strong>Accept the invitation from FactSet.</strong><div style="height:7px;"><br></div>
<img src="https://drive.google.com/thumbnail?id=1mIURDf2KsAGCs7OgWDLuciSACUAeCAVA&sz=w1000" alt="invitation" style="display: block; margin-right: auto; margin-left: auto; zoom:50%;" />
</li>
<li> <strong>Whitelist your IP address in the FactSet <a href="https://controlcenter.factset.com/enterprise-data/cloud-credentials">Control Center</a>.</strong> <div style="height:7px;"><br></div>
<img src="https://drive.google.com/thumbnail?id=1sn8lGriU_wuDikhrJDrz_yWjjlNyvzau&sz=w1000" alt="Whitelist IP" style="display: block; margin-right: auto; margin-left: auto; zoom:100%;" />
</li>
  Remember to click "Save All Changes"!

<li> <strong>Install Microsoft ODBC SQL driver. </strong></li>
<li> <strong>Install Azure Data Studio to connect to the SQL database.</strong>

   <ol type="pa"> 
   <li> Alternatively, could use Python Programmatic Access. Need to install <code>pyodbc</code> to manage the connection. </li>
   </ol>
</li>
</ol>

##  Install Microsoft ODBC

Installation of <span style='color:#00CC66'>**MS-SQL** (**SQL Server**) </span>driver.

1. To install Microsoft ODBC driver 17 for **SQL Server** on macOS, run the following commands:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" 
   brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release 
   brew update 
   HOMEBREW_NO_ENV_FILTERING=1 ACCEPT_EULA=Y 
   brew install msodbcsql17 mssql-tools
   ```
   You may encounter "Error: Your Command Line Tools are too outdated.", just follow the instruction showed on the screen and update your command line tools.

2. Resource file loading \
   The driver needs to load the resource file in order to function. 
   This file is called `msodbcsqlr17.rll`. The default resource file path on macOS is `/usr/local/share/msodbcsql17/resources/en_US/`.

3. **Troubleshooting** \
   Some users encounter an issue when trying to connect after installing the ODBC driver and receive an error like: `"[01000] [unixODBC][Driver Manager]Can't open lib 'ODBC Driver 17 for SQL Server' : file not found (0) (SQLDriverConnect)"`. It may be the case that unixODBC is not configured correctly to find registered drivers. In these cases, creating a couple symbolic links can resolve the issue.

   ```bash
   sudo ln -s /usr/local/etc/odbcinst.ini /etc/odbcinst.ini
   sudo ln -s /usr/local/etc/odbc.ini /etc/odbc.ini
   ```



For ODBC 18 (latest version in 2024): <https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos?view=sql-server-ver16>



| Components                                         | Description                                                  |
| -------------------------------------------------- | ------------------------------------------------------------ |
| `libmsodbcsql.18.dylib` or `libmsodbcsql.17.dylib` | The dynamic library (`dylib`) file that contains all of the driver's functionality. This file is installed in `/usr/local/lib/`. |
| `msodbcsqlr18.rll`or `msodbcsqlr17.rll`            | The accompanying resource file for the driver library. This file is installed in `[driver .dylib directory]../share/msodbcsql18/resources/en_US/` for Driver 18, `[driver .dylib directory]../share/msodbcsql17/resources/en_US/` for Driver 17. |





___

## Connect Using **Azure Data Studio**

Azure Data Studio homepage: <https://learn.microsoft.com/en-us/azure-data-studio/>

Server info

- <span style='color:#32CD32'>**Server name**</span>: ofprod-norduni-1214693-sql.database.windows.net
- Authentication type: Microsoft Extra ID - Universal with MFA support
- Account: menghan.yuan@nord.no
- **Database name**: fds

<img src="https://drive.google.com/thumbnail?id=1nO_hwdBpDAwzijkNPOskhSnrufEPA123&sz=w1000" alt="image-20210914084652582" style="zoom:67%;" />



<span style='color:#32CD32'>**SQL Credentials**</span>

- `Username`: menghan.yuan@factset.net
- `Application Id`: 175bb48c-3918-4882-864d-e0005a3fb1b9
- `Application Secret`: s*adq9nuPyIlO6?6
- `Tenant Id`: 19c2ed02-03ce-49b9-ab35-7e07b729dc04



Azure Data Studio connection window looks like this:

<img src="https://drive.google.com/thumbnail?id=1OTqG-rNRKL247_73Ja9_Ttf02g4ebIDC&sz=w1000" alt="Azure Connection" style="display: block; margin-right: auto; margin-left: auto; zoom:100%;" />



Important tips:

- Azure Data Studio exits unexpectedly frequently, need to save your files mannually every a few minutes.



___

## Migrate to VS Code

Azure Data Studio is [retiring on February 28, 2026](https://learn.microsoft.com/en-us/lifecycle/definitions#retirement). We recommend that you use [Visual Studio Code](https://code.visualstudio.com/). For more information about migrating to Visual Studio Code, visit [What's happening to Azure Data Studio?](https://learn.microsoft.com/en-us/azure-data-studio/whats-happening-azure-data-studio)

VS Code MSSQL connection:

<https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver16>

<img src="https://drive.google.com/thumbnail?id=136PQMkqsMJ6xuYYhv2fdjKs34MGGr2vE&sz=w1000" alt="VS Code SQL Connect" style="display: block; margin-right: auto; margin-left: auto; zoom:60%;" />



Q: What is the difference between `.sql` and `.ipynb`?  
A: `.sql` can run one single query. Notebooks (`.ipynb`) can put multiple queries together. Need to set kernel as `SQL`.



#### Azure Jupyter Notebook shortcuts

Create and run a SQL Server notebook:

<https://learn.microsoft.com/en-us/azure-data-studio/notebooks/notebooks-sql-kernel>



| Command                                                      | Keybinding       |
| ------------------------------------------------------------ | ---------------- |
| Show all commands<br />If you want to do sth and you don't see a button, press *F1*. | F1               |
| Run Current Cell                                             | F5               |
| Add Code Cell end of file                                    | ctrl + shift + C |
| Add Text Cell end of file                                    | ctrl + shift + T |

___

Q: How to export more than 5000 rows in Azure Data Studio?

A: Change Notebook settings (cmd+, to open settings), `Max Table Rows` (defaults to 5,000) to a large number. ([Source](https://github.com/microsoft/azuredatastudio/issues/10389#issuecomment-629429453))

Azure Data Studio set 5,000 initially because performance on a notebook with many cells and many outputs (such as tables) can cause performance degradation when a notebook gets fairly large (say, 50MB+).

After setting a large max rows, the whole table can be displayed. Then click `Save As CSV` to save to local, which might take a long time to write, even taking a longer time than executing the query.

<img src="https://drive.google.com/thumbnail?id=1Oa-vOxuSKl_rqwP6N7i0vmcHwPebxh2L&sz=w1000" alt="ADS max rows" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

___

Q: Long lines cannot be printed. Warning message like the following:

> Rendering paused for long line for performance reasons. This can be configured via `editor.stopRenderingLineAfter`.

<img src="https://drive.google.com/thumbnail?id=1QNs6_fluDRtPlbpC339KU7F2BIgHh4wj&sz=w1000" alt="Azure long lines" style="display: block; margin-right: auto; margin-left: auto; zoom:120%;" />

A: This does NOT affect running the query. Don't need to deal with it.



___

## **Python** Connection

SQL Query Examples
```sql
SELECT TOP 100 * from fp_v2.fp_basic_dividends;
SELECT TOP 100 * FROM fp_v2.fp_basic_shares_current;
SELECT TOP 100 * FROM fp_v2.fp_basic_splits;
SELECT TOP 100 * from fp_v2.fp_sec_coverage;
SELECT top 10 * from fp_v2.fp_sec_entity;
SELECT top 10 * from tv_v2.tv_esg_ranks;
SELECT top 10 * from fp_v2.fp_basic_prices;
```

<a href="{{ site.baseurl}}/source/FaceSet_Sample_Codes.ipynb">Download Sample Python Codes Here</a>



___

## Troubleshooting

**Connection error - multiple matching tokens detected**

Error message

> Failed to authenticate the user in Active Directory (Authentication=ActiveDirectoryInteractive).
> Error code 0xmultiple_matching_tokens_detected
> The cache contains multiple tokens satisfying the requirements. Try to clear token cache.

Fix: Clear the Azure Token Cache using the command in the Command Palette. Specifically.

1. Click F1
2. type something like `clear`
3. Run the `Clear Azure Token Cache` entry.

<img src="https://drive.google.com/thumbnail?id=15nkQUk6TAWVJgXa5Z8YxwWMX_Ynv4p6t&sz=w1000" alt="Azure clear cache" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />






___




FactSet **Support** Contact at Nord:
- Official support: [support@factset.com](mailto:support@factset.com)
- Felix Goosmann: [hf.goosmann@factset.com](mailto:hf.goosmann@factset.com); 
- Vivek Patel: [vivek.patel@factset.com](mailto:vivek.patel@factset.com)





