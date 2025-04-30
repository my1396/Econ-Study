---
layout: post
tag: programming
title: Financial Datasets
---

<a class="top-link hide" href="#" id="js-top">↑</a>



Financial data processing caveats:

1. Match monthly data $\rightarrow$ use year-month combination, in stead of start/end of month;

2. Mind the unit. Many returns are denominated in percentage.
   1. Returns must have matched frequency. E.g., CAPM, monthly equity returns to monthly factors, annual to annual.
   1. Remember to annualize the return if the data is monthly/daily in order to get comparable return results.
   
3. Missing values
   1. choose samples with a threshold length, such that individuals with too few observations are removed.

4. Cross validate data from multiple data sources if not sure whether your data process is correct. Use common sense. 

   For instance, a monthly return is unlikely to be 20%, annual return of 20% makes more sense. 

   If you see a monthly return 1.73, it is likely that it is pct-based, i.e., 1.73%, rather than 1.73 times.



Common return terms

- YTD: year-to-date, measures the return over the period starting from the beginning of the current year up to the present day.



**Security Identifiers**

| ID     | Definition                                                   |
| ------ | ------------------------------------------------------------ |
| ticker | <u>The <strong>combination</strong> of ticker, exchange, and date</u> uniquely identifies a security. <br/>A ticker may be one to three characters for NYSE and AMEX securities or four or five characters for Nasdaq securities. |
| ISIN   | International Security Identification Number<br />ISIN codes contain 12 characters: <br />- the first 2 letters identify the company's nationality; <br />- the following 9 alphanumeric characters identify the security; <br />- the last digit is a “check digit” set by an algorithm to help prevent counterfeiting. |
| SEDOL  | Stock Exchange Daily Official List. <br />Seven-character identification code primarily used in the <u>UK</u>, assigned by the London Stock Exchange. |
| CUSIP  | CUSIP identifiers are supplied to CRSP by the CUSIP Service Bureau, Standard & Poor's, a division of McGraw-Hill, Inc., American Bankers Associate database.<br />Unique 9-digit identification number assigned to financial securities in the <u>United States and Canada</u>. |
| gvkey  | Global Company Key                                           |
| MIC    | Market Identifier Code identifies a unique securities trading exchange, regulated and non-regulated trading market. |

FactSet can be looked up by ticker, ISIN, Sedol, and Cusip.

**Clarification about tickers**: (Ticker is also referred to as "symbol.")

- Shares of the same company can be traded on <u>several exchanges</u>, but they will have different stock ticker symbols for each different exchange the stock is traded on. 

- There are some companies that trade with two different symbols on the <u>same stock market</u> because they offer two classes of shares, one with voting rights and another without voting rights.



One company with multiple ISIN's, e.g., Schibsted A shares and B shares.

<https://schibsted.com/ir/faq/>

The ticker symbol of the A share is “SCHA” and of the B share “SCHB”.

B-shares are created during a share split in May 2015. The B-shares are ordinary, fully- paid shares carrying equal rights with the A-shares in all respects except that the B-shares are **low-voting shares** with only one vote per share while the A-shares have 10 votes per share. [Reference](https://schibsted.com/releases/schibsted-asa-sch-share-split-and-listing-of-b-shares-last-day-inclusive-today/).

- Takeaway point: use `ISIN` to identify equities.

  > - An ISIN is a 12-digit alphanumeric code that uniquely identifies a specific security.
  >
  > - The numbers are allocated by a country's respective national numbering agency (NNA).
  > - An ISIN is not the same as the ticker symbol, which identifies the stock at the exchange level. The ISIN is a unique number assigned to a security that is **universally recognizable**.
  >   - For example, according to ISIN Organization, IBM common stock is traded on close to 25 trading exchanges and platforms, and its stock has a <u>different ticker symbol depending on where it is traded</u>. However, IBM stock has only <u>one ISIN</u> for each security.

- Companies may change ISINs after share split.

  [Example](https://live.euronext.com/en/products/equities/company-news/2024-07-18-xxl-asa-key-information-relating-reverse-share-split-and):

  > <span style="font-size: 30px;">XXL ASA – KEY INFORMATION RELATING TO THE REVERSE SHARE SPLIT AND CHANGE OF ISIN</span>
  >
  > Oslo, 18 July 2024: Reference is made to the stock exchange announcement made by XXL ASA (the "Company") on 4 June 2024, regarding the Company's annual general meeting resolving a reverse share split of the company's shares. Key information related to the reverse share split is set out below: 
  >
  > Date on which the corporate action was made public: 14 May 2024 
  >
  > Reverse split ratio: 100:1, i.e. one hundred (100) old shares give one (1) new share
  >
  > Last day including right: 19 July 2024 
  >
  > Ex-date: 22 July 2024
  >
  > Record date: 23 July 2024
  >
  > Date of approval: 4 June 2024 (AGM)
  >
  > 
  >
  > In connection with the reverse share split, the Company's shares will be transferred to new ISINs. 
  >
  > Please note the following key information for the change of ISIN:
  > • Issuer: XXL ASA
  > • Previous ISIN for the Company's ordinary shares (class A-shares): ISIN NO0010716863
  > • New ISIN for the Company's ordinary shares (class A-shares): ISIN NO0013293142 
  > • Previous ISIN for the Company's non-voting shares (class B-shares): ISIN NO0013014589
  > • New ISIN for the Company's non-voting shares (class B-shares): ISIN NO0013293159 
  > • Date of ISIN change: 23 July 2024



- **Ex-date**: The date of the first trading day on which the shares will be traded without the right to receive shares ccording to the exchange ratio. Shareholders who acquire shares on or after this trading day will not receive shares according to the exchange ratio once the share split/reverse split is carried out.

  In the XXL example, stock closing price on the ex-date will be 1/100 of the previous closing price.

- **Record date**: The date on which the copy of the shareholder register will be taken. This will be used to identify who is entitled to receive shares once the share split/reverse split is carried out. The new number of shares following the split/reverse split accrues to those shareholders who are registered as shareholders on the shareholder register on the record date. With a normal settlement cycle (T+2), the record date will be the day that occurs T+1 after the ex-date.
- **Date of approval**: The date on which the share split/reverse split was approved/is due to be approved by the competent corporate body.



Differentiate ISIN from ISSN

- ISIN for identifying securities
- ISSN (nternational Standard Serial Number)  uniquely identify a periodical publication, such as a journal.



Industry classification systems that are widely used in equity analysis

- the **Global Industry Classification System (GICS)** sponsored by Standard & Poor’s and MSCI Barra

  The GICS structure assigns each company to one of 154 subindustries, an industry (68 in total), an industry group (24 in total), and an economic sector (10 in total: consumer discretionary, consumer staples, energy, financials, health care, industrials, information tech- nology, materials, telecommunication services, and utilities).

- the **Industrial Classification Benchmark (ICB)** developed by Dow Jones and FTSE, which in 2006 replaced the FTSE Global Classification System.

  The ICB, like GICS, has four levels, but the terminology of ICB uses the terms *sector* and *industry* in nearly opposite senses. At the bottom of the four levels are 114 subsectors, each of which belongs to one of 41 sectors; each sector belongs to one of 19 supersectors; and each supersector belongs to one of 10 industries at the highest level of classification. 

  The 10 industries are oil and gas, basic materials, industrials, consumer goods, health care, consumer services, telecommunications, utilities, financials, and technology.

- **Standard Industrial Classification** (SIC): a four-digit code as a method of standardizing industry classification for statistical purposes across agencies. Widely used in the US.





## CRSP

price quotes for US and Canada companies

| Var      | Definition                                                   |
| -------- | ------------------------------------------------------------ |
| comnam   | Company Name                                                 |
| permco   | CRSP Permanent Company Number                                |
| siccd    | SIC Code                                                     |
| tsymbol  | Trading Symbol. A lot like Ticker, but not the same.         |
| primexch | Primary Exchange<br />N: NYSE; A: AMEX; Q: NASDAQ; X: Other Exchange; R: ARCA |
| exchcd   | Exchange code indicating the exchange on which a security is listed. Normal exchange codes are respectively 1,2, and 3 for NYSE, AMEX and the Nasdaq Stock MarketSM. An exchange code of zero indicates that a security is either trading on an unknown exchange, or is temporarily not trading at all. |
| hexcd    | Header Exchange Code (hexcd)<br />Valid hexcd's are 1, 2, or 3, which correspond to the NYSE, AMEX, and Nasdaq respectively. Other exchange codes are not included in hexcd. |
| prc      | Price or Bid/Ask Average (prc). <br>If the closing price is not available on any given trading day, the number in the price field has a negative sign to indicate that it is a bid/ask average and not an actual closing price. Please note that in this field the negative sign is a symbol and that the value of the bid/ask average is not negative.<br />If neither closing price nor bid/ask average is available on a date, prc is set to zero. |
| shrout   | Number of Shares Outstanding, recorded in thousands.         |
| facpr    | Factor to Adjust Price (facpr)                               |
| cfacpr   | Cumulative Factor to Adjust Price (cfacpr)                   |
| facshr   | Factor to Adjust Shares (facshr)                             |
| cfacshr  | Cumulative Factor to Adjust Shares (cfacshr)                 |
| divamt   | Dividend Cash Amount                                         |



Note that CRSP stock prices are **unadjusted** prices.



**Adjusted Price**

`Facpr` is used to adjust stock prices after a distribution so that a comparison can be made on an equivalent basis between prices before and after the distribution. `facpr` equals `facshr` for most distribution events. There are three types of distributions where this is the case: 

1. Cash dividends, facpr is set to zero; 

2. Cases of mergers, total liquidations, or exchanges where the security **disappeared**, `facpr` is set to negative one by convention; 

3. For stock dividends and splits, `facpr` is the number of additional shares per old share issued:
   $$
   \text{facpr} = \frac{S_t-S_{t-1}}{S_{t-1}}
   $$
   $S_t$ is the # shares outstanding on the date after or on the ex-div date for the split. $S_{t-1}$ is the date before the split.



`facshr` is an adjustment for shares outstanding.



Price and dividend data are adjusted with the calculation:
$$
AP_t = \frac{P_t}{\text{cfacpr}_t}
$$
Share and volume data are adjusted with the calculation:
$$
\text{Ashrout}_t = \text{shrout}_t \times \text{cfacshr}_t
$$



## Compustat

Provides data for **global** companies, also index constituents.

Document: <https://tevgeniou.github.io/EquityRiskFactors/CompustatManualChpt5.pdf>

- Adjusted close price = $\frac{\text{PRCCD}}{\text{AJEXDI}}$

  - PRCCD: close price daily.

  - AJEXDI: adjustment factor, (Issue)-Cumulative by Ex-Date (ajexdi)

- To compute returns, you will need to apply a DAILY RETURN FACTOR (variable `TRFD`) to the close price. That is, multiplying the current adjusted close price (PRCCD/AJEXDI) by the current total return factor (TRFD) and dividing the result by the product of the adjusted close price of the prior period multiplied by the Total Return Factor of the prior period. 

   $$
   \frac{\frac{\text{PRCCD}_t}{\text{AJEXDI}_t}\times \text{TRFD}_t}{\frac{\text{PRCCD}_{t-1}}{\text{AJEXDI}_{t-1}}\times \text{TRFD}_{t-1}} -1
   $$

   `TRFD` includes Cash Equivalent Distributions + reinvestment of dividends and the compounding effect of dividends paid on reinvested dividends. 

   If you are looking for a price only return, do NOT use the total return factor.



___

## Fama-French data library

<http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html>

The Fama/French factors are constructed using the 6 **value-weight** portfolios formed on size (small-big) and book-to-market (value-neutral-growth).



K. French's data library gets **updated with a delay**. As of April 2025, the data is up to the end of 2024.

Alternatives of the FF data library are:

- Mkt-RF: [Dow Jones U.S. Total Stock Market Index](https://www.spglobal.com/spdji/en/indices/equity/dow-jones-us-total-stock-market-index/#overview) minus [S&P U.S. Treasury Bill 0-3 Month Index](https://www.spglobal.com/spdji/en/indices/fixed-income/sp-us-treasury-bill-0-3-month-index/#overview)
- SMB: [Dow Jones U.S. Thematic Market Neutral Size Index](https://www.spglobal.com/spdji/en/indices/dividends-factors/dow-jones-us-thematic-market-neutral-size-index/#overview)
- HML: [Dow Jones U.S. Thematic Market Neutral Value Index](https://www.spglobal.com/spdji/en/indices/dividends-factors/dow-jones-us-thematic-market-neutral-value-index/#overview)

Dow Jones US Thematic Indices are equal-weighted. See Methodology [HERE](https://www.spglobal.com/spdji/en/documents/methodologies/methodology-dj-us-thematic-neutral.pdf).

It's important that we use market-neutral indices to replace the factors. A value or large-cap index or ETF would not do the trick, as these only cover the long side.



___

## Norway

Oslo operates two EU regulated markets, Oslo Børs (`XOSL`) and Euronext Expand (`XOAS`).

- more than 200 constituents in XOSL: <https://live.euronext.com/en/markets/oslo/equities/list>
- ~20 constituents in XOAS.

___

### Index

OSEAX index: All-share index, consists of all shares listed on Oslo Børs; about 270 companies as of 2025;

OSEBX index: Benchmark index, about 60-70 companies; the index is revised twice a year: June 1 and December 1.

OBX: 25 most traded (liquidity) shares listed on Oslo Børs.



*Euronext* and *Euronext Growth*

- Euronext  lists larger, established companies with substantial financing depth.
- Euronext Growth is suited to small- and mid-sized companies (SMEs) that want to raise funds to finance their growth.
  - Euronext Growth Oslo listing MIC: `MERK`
  - Not a regulated market.



___

### Titlon

Homepage: <https://uit.no/forskning/forskningsgrupper/sub?sub_id=417205&p_document_id=352767>

TITLON is a database with financial data on stocks, indicies, bonds, funds and derivatives from all exhanges at EURONEXT and with data from Oslo Stock Exchange back to 1980. 

Field Description: <https://titlon.uit.no/tabledefs.php>

- Table `equity`

  Oslo Stock Exchange $\rightarrow$ Equity $\rightarrow$ Advanced

  Highlight:

  - Fully adjusted closing prices for dividends, splits, etc.
  - Fama-French and Pástor-Stambaug (liquidity) factors matching the OSEBX portfolio.
  - Index change (OSEBX and OBX) and risk free interest rate (NOWA and 3-mon bill)

  <img src="https://drive.google.com/thumbnail?id=1bJsosmCmjWB9sSOu25Ujy_D2tPwaUyuU&sz=w1000" alt="Titlon preview" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

| Field name                                             | Type        | Description                                                  |
| ------------------------------------------------------ | ----------- | ------------------------------------------------------------ |
| Date                                                   | date(3)     | Date                                                         |
| SecurityId                                             | bigint(8)   | Security id                                                  |
| CompanyId                                              | bigint(8)   | Company id                                                   |
| Symbol                                                 | varchar(16) | Symbol                                                       |
| ISIN                                                   | varchar(24) | ISIN                                                         |
| Name                                                   | varchar(50) | of associated equity                                         |
| BestBidPrice                                           | float(8)    | Best bid price                                               |
| BestAskPrice                                           | float(8)    | Best ask price                                               |
| Open                                                   | float(8)    | Open price                                                   |
| High                                                   | float(8)    | Higest observed price during trading day                     |
| Low                                                    | float(8)    | Lowest observed price during trading day                     |
| Close                                                  | float(8)    | Closing price                                                |
| OfficialNumberOfTrades                                 | float(8)    | Official number of trades                                    |
| OfficialVolume                                         | float(8)    | Official volume                                              |
| UnofficialNumberOfTrades                               | float(8)    | Unofficial number of trades                                  |
| UnofficialVolume                                       | float(8)    | Unofficial volume                                            |
| VolumeWeightedAveragePrice                             | float(8)    | Volume weighted average price                                |
| Price                                                  | float(8)    | Same as closing price                                        |
| <span style='color:#00CC66'>AdjustedPrice</span>       | float(8)    | Adjusted price for dividend, split, etc.                     |
| Dividends                                              | float(8)    | Last payed dividend                                          |
| LDividends                                             | float(8)    | Lagged dividend                                              |
| CorpAdj                                                | float(8)    | Corp adjustments (splits etc.)                               |
| DividendAdj                                            | float(8)    | Dividend adjustment factor                                   |
| Currency                                               | varchar(3)  | Currency. Currently allways NOK                              |
| Description                                            | varchar(40) | Description                                                  |
| CountryCode                                            | varchar(10) | Country code                                                 |
| SumAnnualDividends                                     | float(8)    | Sum annual dividends                                         |
| NumberOfShares                                         | float(8)    | Number of shares issued (not free float adjusted)            |
| CompanyOwnedShares                                     | float(8)    | Company owned shares                                         |
| OutstandingShares                                      | float(8)    | Outstanding shares                                           |
| Exchange                                               | varchar(3)  | Exchange                                                     |
| NOKPerForex                                            | float(8)    | Exchange rate. Currently allways 1.                          |
| mktcap                                                 | float(8)    | Market capitalization                                        |
| OSEBXmktshare_prevmnth                                 | float(8)    | Prevoius month market share in OSEBX index                   |
| OSEBXAlpha_prevmnth                                    | float(8)    | Prevoius month alpha relative to OSEBX index                 |
| OSEBXBeta_prevmnth                                     | float(8)    | Prevoius month beta relative to OSEBX index                  |
| <span style='color:#00CC66'>SMB</span>                 | float(8)    | SMB Fama-French factor                                       |
| <span style='color:#00CC66'>HML</span>                 | float(8)    | HML Fama french factor                                       |
| <span style='color:#00CC66'>MOM</span>                 | float(8)    | MOM Fama-French factor                                       |
| LIQ                                                    | float(8)    | LIQ Pastor-Stambaugh factor                                  |
| DividendPriceRatio                                     | float(8)    | Dividend price ratio                                         |
| lnDeltaP                                               | float(8)    | log return of the adjusted price (CorpAdj and DividendAdj)<br/><span style='color:#00CC66'>MY Note: seems to be <strong>the closing price</strong>, in stead of adjusted closing price.</span> |
| <span style='color:#00CC66'>lnDeltaOSEBX</span>        | float(8)    | log return of the OSEBX index, market benchmark return       |
| lnDeltaOBX                                             | float(8)    | log return of the OBX index                                  |
| <span style='color:#00CC66'>NOWA_DayLnrate</span>      | float(8)    | Log difference of Norwegian Overnight Weighted Average rate from the norwegian central bank after 2013. NIBOR before that. Risk-free rate. |
| <span style='color:#00CC66'>bills_3month_Lnrate</span> | float(8)    | 3 months Norwegian Goverment Bills, from the bondindex table, CloseYield field. |
| Sector                                                 | varchar(50) | Sector                                                       |
| IN_OSEBX                                               | int(4)      | True if the stock is in the OSEBX index at the moment        |
| Equity                                                 | float(8)    | Amount of Equity                                             |
| Debt                                                   | float(8)    | Amount of Debt                                               |
| Earnings                                               | float(8)    | Total earnings                                               |
| debt_ratio                                             | float(8)    | Debt ratio                                                   |
| PE                                                     | float(8)    | Price/Earnings                                               |





### Risk free rate (RFR)

- Before 2013 NIBOR: [Norges Bank](https://www.norges-bank.no/en/topics/Statistics/Historical-monetary-statistics/)

- After 2013 Norwegian Overnight Weighted Average rate: [Norske Finansielle Referenser AS (NoRe)](https://nore-benchmarks.com)
- [Titlon](https://titlon.uit.no/tabledefs.php): 3 months Norwegian Government Bills, from the `bondindex` table, `CloseYield field`.



Financial service companies publish surveys about financial data. For instance, PwC Norge.

- Here is their annual report about RFF: <https://www.pwc.no/no/publikasjoner/risikopremien.html>







**Asset Pricing data at OSE**

<https://ba-odegaard.no/financial_data/ose_asset_pricing_data/index.html>

