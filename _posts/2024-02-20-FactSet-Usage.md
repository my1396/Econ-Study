---
layout: post
tag: study
title: FactSet Tutorial
---

<a class="top-link hide" href="#" id="js-top">↑</a>

## Get help

Need to have one FactSet account in order to use data dictionaries and user guides.

FactSet Table and Data Dictionary Overview: \
<https://open.factset.com/navigator/>

How to look up documentations, help files for one theme database, eg *Fundamentals*? Get an overview for one theme.

1. In the *Marketplace*, search for "Fundamentals". Open the one tagged "Data Feed".
2. Click "RESOURCES". You will have several options:
   - Data Methodology: general overview.
   - Data Dictionary: summary of table and included fields in pdf. 每张表包含的字段。
   - Data Items Definitions: detailed definitions for fields in pdf. 字段具体计算方式。
   - View in Data Navigator: nice portal for an overview of both tables and feild descriptions. UI做的比较好，用户友好。



Check detailed data dictionary, field definition, mappings for values and their meanings.

Online Assistant: <https://my.apps.factset.com/oa/pages/8>



**Main takeaway**: FactSet and SQL are tools to download data. Just download the full dataset containing what you are interested. Use other programming language to process the data. 

- It's more flexible that way. SQL is not designed to do data manipulation.
- Only do the most necessary data cleaning job in SQL. More refined data cleaning, do in R or Python.



## Reference Data

Look up FactSet ID $\rightarrow$ **Symbology Schema** contains mappings between FactSet Permanent Identifiers and CUSIPs,
SEDOLs, ISINs, and tickers.

- It allows users to translate from a wide variety of symbols (CUSIPs, SEDOLS, ISINs, Bloomberg FIGI, etc) to FactSet's native symbology. 

`sym_v1.sym_isin` This table contains ISIN to FactSet Permanent Identifier (FSYM_ID) mappings.

| Field Name | Description                               |
| ---------- | ----------------------------------------- |
| `fsym_id`  | FactSet identifier assgined to a security |
| `isin`     | ISIN assgined to a security               |



### `sym_v1.sym_coverage` 

This table contains reference data on the securities and listings.

- `fref_security_type` check security type, see complete list [here](https://my.apps.factset.com/oa/pages/15776).

  - `SHARE`: 	Share/Common/Ordinary

  - `PREFEQ`        Preferred Equity
  - `MF_O`            Open-ended Fund.
  - `MF_C`            Closed-ended Fund.

- `fref_listing_exchange` exchange where the security trades
- `universe_type` denotes whether the security is equity (`EQ`) or fixed income (`FI`).



### `sym_v1.sym_ticker_region` 

This table contains FactSet Permanent Identifier (`FSYM_ID`) mappings to *Exchange Specific Ticker*.

- `ticker_region`	Current or most recent regional ticker assigned to the listing. 

  - Ticker is the current or most recent global ticker assgined to the listing.

  - The ticker is appended with the **two digit code** that corresponds to the county or region in which the  listing trades. Ticker and region are separated by a hypen `-`.

    For instance, `AAPL-US`.





## Return Data

### `fp_v2.fp_total_returns_daily` 

| Field Name    | Description                                      |
| ------------- | ------------------------------------------------ |
| `fsym_id`     | FactSet identifier assgined to a security        |
| `p_date`      | Date on which the security priced                |
| `currency`    | Currency in which the security or listing trades |
| `one_day_pct` | Returns since the previous trade date            |

- `currency` doesn't tell about the exchange on which the security trades as one exchange is capable of listing equitie denominated in different currencies. 
- If want to get exchange info, better to use  `fref_listing_exchange` (exchange code) or `ticker_region` (country code).











