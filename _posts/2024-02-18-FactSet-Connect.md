---
layout: post
tag: programming
title: Connect to FactSet
---

<a class="top-link hide" href="#" id="js-top">↑</a>

**Steps overview to set up FactSet**:

<ol>
<li> Accept the invitation from FactSet. 
<img src="https://drive.google.com/thumbnail?id=1mIURDf2KsAGCs7OgWDLuciSACUAeCAVA&sz=w1000" alt="invitation" style="display: block; margin-right: auto; margin-left: auto; zoom:50%;" />
</li>

<li>  Whitelist your IP address in the FactSet <a href="https://controlcenter.factset.com/enterprise-data/cloud-credentials">Control Center</a>. 
<img src="https://drive.google.com/thumbnail?id=1sn8lGriU_wuDikhrJDrz_yWjjlNyvzau&sz=w1000" alt="Whitelist IP" style="display: block; margin-right: auto; margin-left: auto; zoom:100%;" />
</li>

<li>  Install Microsoft ODBC SQL driver. </li>
<li>  Install Azure Data Studio to connect to the SQL database.
   <ol type="pa"> 
   <li> Alternatively, could use Python Programmatic Access. Need to install <code>pyodbc</code> to manage the connection. </li>
   </ol>
</li>
</ol>

##  Install Microsoft ODBC

Installation of MS-SQL driver.

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



The connection window looks like this:

<img src="https://drive.google.com/thumbnail?id=1OTqG-rNRKL247_73Ja9_Ttf02g4ebIDC&sz=w1000" alt="Azure Connection" style="display: block; margin-right: auto; margin-left: auto; zoom:100%;" />



`sql` can run one single query.

Notebook can put multiple queries together.




Azure Jupyter Notebook shortcuts

| Command                   | Keybinding       |
| ------------------------- | ---------------- |
| Run Current Cell          | F5               |
| Add Code Cell end of file | ctrl + shift + C |
| Add Text Cell end of file | ctrl + shift + T |



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





