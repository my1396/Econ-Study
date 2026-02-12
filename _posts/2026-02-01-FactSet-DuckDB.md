---
layout: post
tag: programming
title: FactSet DuckDB
date: 2026-02-01
---

<a class="top-link hide" href="#" id="js-top">↑</a>


Run `duckdb -ui` to launch DuckDB UI in your default browser. You can run SQL queries there.

Click "Attached databases" to add a new database connection.

<img src="https://drive.google.com/thumbnail?id=1nWVPfpiOk34dg18NK2MkvglcVZGQFhJj&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

Fill in the connection details:

- **Path:** path to your DuckDB database file (usually ends with `.duckdb`)
- Alias (Optional): a nickname for the database connection, e.g. `FactSet`

Alternatively, you can also launch the UI directly with a specific database connection using the following command:

```bash
duckdb "/Users/menghan/Desktop/FactSet Database/factset_single.duckdb" -ui
```

This will load the specified database in the UI automatically.


Pros: Nice UI for table overview, column browsing, and query execution.

Cons: Cannot save query notebooks to local. → Use Jupyter Notebook / Python for better organization and version control.

You can run SQL queries in the Notebooks. To quit the UI, go to terminal and hit <span class="env-green">`Ctrl + D`</span>.

When you have built a connection in Python, it can be convenient if you open a web UI to view the database schema and run some quick queries. However, if you have an active connection to the database in Python, the web UI will be locked in read-only mode to prevent conflicts. This means you can only open the web UI in read-only mode. 

Use the following command to open the UI in read-only mode:

```bash
duckdb "/Users/menghan/Desktop/FactSet Database/factset_single.duckdb" -readonly -ui
```



ref:

- [DuckDB Local Browser UI](https://duckdb.org/2025/03/12/duckdb-ui)

- [DuckDB SQL](https://duckdb.org/docs/stable/sql/introduction) is a variant of [PostgreSQL](https://www.postgresql.org/docs/current/tutorial-sql-intro.html).



## Keyboard shortcuts

| Action                | Shortcut        |
| --------------------- | --------------- |
| Run Query             | ⌘ Enter         |
| Format Query          | ⌘ ⇧ F           |
| Clear Query Results   | ⌘ ⇧ K           |

Build a Python notebook to connect to DuckDB and run SQL queries. This way, you keep your SQL queries and data analysis in one place.

The notebooks in the web UI persiste btw sessions in the same browser on the same machine. But it's better to use local [Jupyter notebooks](https://duckdb.org/docs/stable/guides/python/jupyter) for better organization and version control.

[Here](https://colab.research.google.com/drive/1bNfU8xRTu8MQJnCbyyDRxvptklLb0ExH?usp=sharing#scrollTo=9Xq5eXmM5bUA) is a Google Colab notebook example connecting to FactSet DuckDB database.





## Jupyter Notebook

Create a new Jupyter notebook. In VS Code, go to Command Palette (⇧⌘P) → "Create: New Jupyter Notebook".

See [HERE](https://my1396.github.io/R-Notes/2.10-vs-code.html#jupyter-notebooks) for basic usage of Jupyter notebooks in VS Code.

> Don't use OneDrive to store you `.ipynb` files, it sync prevents notebooks from saving its kernel state properly.
> 
> OneDrive is rubbish. MS apps should always be avoided if possible...

Set up environment by installing necessary packages:

```python
%conda uninstall --quiet --yes malloy
%conda install --quiet --yes --upgrade duckdb
%conda install --quiet --yes jupysql==0.11.1
%conda install --quiet --yes duckdb-engine
%conda install --quiet --yes pandas
%conda install --quiet --yes matplotlib
```

It will install `duckdb`, `jupysql`, `duckdb-engine`, `pandas`, `matplotlib` packages. It takes a while to install all packages.


[`jupysql`](https://jupysql.readthedocs.io/en/latest/quick-start.html) allows you to run SQL and plot large datasets in Jupyter via a `%sql`, `%%sql`, and `%sqlplot`magics.


**Build the connection**

```python
# Connect to file backed db in read-only mode to avoid lock conflicts
conn = duckdb.connect("~/Desktop/FactSet Database/factset_single.duckdb", read_only=True)

# use the DuckDB connection
%sql conn
```

**Querying DuckDB**


Single line SQL queries can be run using `%sql` at the start of a line. 

```ptyhon
%sql SELECT 'Off and flying!' AS a_duckdb_column;
```

Save result to a variable

```python
%sql res << SELECT 'Off and flying!' AS a_duckdb_column;
```

An entire Jupyter cell can be used as a SQL cell by starting with `%%sql`

```python
%%sql
-- look up price based on tickers
SELECT price.*, sym.ticker_region, cov.proper_name, p.one_day_pct as DailyReturns
FROM fp_v2.fp_total_returns_daily AS p
LEFT JOIN fp_v2.fp_basic_prices AS price
  ON price.fsym_id = p.fsym_id AND p.p_date = price.p_date
LEFT JOIN sym_v1.sym_ticker_region AS sym
  ON p.fsym_id = sym.fsym_id
JOIN sym_v1.sym_coverage AS cov
  ON sym.fsym_id = cov.fsym_id
WHERE sym.ticker_region IN ('AAPL-US','IBM-US','SPY-US','MSFT-US','GOOGL-US') -- change tickers 
  AND p.p_date BETWEEN '2021-08-16' AND '2021-08-20' -- change date scope
ORDER BY p.p_date, sym.ticker_region
```

Query results will be displayed as a Pandas DataFrame.



--------------------------------------------------------------------------------

One liner vs. Cell magic

```python
# Based on ticker-region, find fsym_id
fsym_ids = %sql SELECT cov.*, tr.ticker_region FROM sym_v1.sym_coverage AS cov LEFT JOIN sym_v1.sym_ticker_region AS tr ON tr.fsym_id = cov.fsym_regional_id WHERE tr.ticker_region IN ({{tickers_sql}})
```

```python
# Based on ticker-region, find fsym_id
%%sql fysm_ids << 
SELECT cov.*, tr.ticker_region 
FROM sym_v1.sym_coverage AS cov 
LEFT JOIN sym_v1.sym_ticker_region AS tr 
    ON tr.fsym_id = cov.fsym_regional_id 
WHERE tr.ticker_region IN ({{tickers_sql}})
```

--------------------------------------------------------------------------------

## SQL Syntax

First 10 rows from a table:

```sql
SELECT * 
FROM client.rus3000_prc_data 
LIMIT 10
```
