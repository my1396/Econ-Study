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
   1. Remember to annualize the return if the data is monthly in order to get comparable return results.
   
3. Missing values
   1. choose samples with a threshold length, such that individuals with too few observations are removed.

4. Cross validate data from multiple data sources if not sure whether your data process is correct. Use common sense. 

   For instance, a monthly return is unlikely to be 20%, annual return of 20% makes more sense. 

   If you see a monthly return 1.73, it is likely that it is pct-based, i.e., 1.73%, rather than 1.73 times.



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



**Fama-French data library** 

<http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html>





## Norway

Oslo operates two EU regulated markets, Oslo Børs (`XOSL`) and Euronext Expand (`XOAS`).

- more than 200 constituents in XOSL: <https://live.euronext.com/en/markets/oslo/equities/list>
- ~20 constituents in XOAS.



OSEAX index: All-share index, consists of all shares listed on Oslo Børs; about 270 companies as of 2025;

OSEBX index: Benchmark index, about 60-70 companies; the index is revised twice a year: June 1 and December 1.

OBX: 25 most traded (liquidity) shares listed on Oslo Børs.



*Euronext* and *Euronext Growth*

- Euronext  lists larger, established companies with substantial financing depth.
- Euronext Growth is suited to small- and mid-sized companies (SMEs) that want to raise funds to finance their growth.
  - Euronext Growth Oslo listing MIC: `MERK`
  - Not a regulated market.



### **Titlon**

<https://uit.no/forskning/forskningsgrupper/sub?sub_id=417205&p_document_id=352767>

<https://titlon.uit.no/tabledefs.php>

- Table `equity`

| Field name                 | Type        | Description                                                  |
| -------------------------- | ----------- | ------------------------------------------------------------ |
| Date                       | date(3)     | Date                                                         |
| SecurityId                 | bigint(8)   | Security id                                                  |
| CompanyId                  | bigint(8)   | Company id                                                   |
| Symbol                     | varchar(16) | Symbol                                                       |
| ISIN                       | varchar(24) | ISIN                                                         |
| Name                       | varchar(50) | of associated equity                                         |
| BestBidPrice               | float(8)    | Best bid price                                               |
| BestAskPrice               | float(8)    | Best ask price                                               |
| Open                       | float(8)    | Open price                                                   |
| High                       | float(8)    | Higest observed price during trading day                     |
| Low                        | float(8)    | Lowest observed price during trading day                     |
| Close                      | float(8)    | Closing price                                                |
| OfficialNumberOfTrades     | float(8)    | Official number of trades                                    |
| OfficialVolume             | float(8)    | Official volume                                              |
| UnofficialNumberOfTrades   | float(8)    | Unofficial number of trades                                  |
| UnofficialVolume           | float(8)    | Unofficial volume                                            |
| VolumeWeightedAveragePrice | float(8)    | Volume weighted average price                                |
| Price                      | float(8)    | Same as closing price                                        |
| AdjustedPrice              | float(8)    | Adjusted price for dividend, split, etc.                     |
| Dividends                  | float(8)    | Last payed dividend                                          |
| LDividends                 | float(8)    | Lagged dividend                                              |
| CorpAdj                    | float(8)    | Corp adjustments (splits etc.)                               |
| DividendAdj                | float(8)    | Dividend adjustment factor                                   |
| Currency                   | varchar(3)  | Currency. Currently allways NOK                              |
| Description                | varchar(40) | Description                                                  |
| CountryCode                | varchar(10) | Country code                                                 |
| SumAnnualDividends         | float(8)    | Sum annual dividends                                         |
| NumberOfShares             | float(8)    | Number of shares issued (not free float adjusted)            |
| CompanyOwnedShares         | float(8)    | Company owned shares                                         |
| OutstandingShares          | float(8)    | Outstanding shares                                           |
| Exchange                   | varchar(3)  | Exchange                                                     |
| NOKPerForex                | float(8)    | Exchange rate. Currently allways 1.                          |
| mktcap                     | float(8)    | Market capitalization                                        |
| OSEBXmktshare_prevmnth     | float(8)    | Prevoius month market share in OSEBX index                   |
| OSEBXAlpha_prevmnth        | float(8)    | Prevoius month alpha relative to OSEBX index                 |
| OSEBXBeta_prevmnth         | float(8)    | Prevoius month beta relative to OSEBX index                  |
| SMB                        | float(8)    | SMB Fama-French factor                                       |
| HML                        | float(8)    | HML Fama french factor                                       |
| MOM                        | float(8)    | MOM Fama-French factor                                       |
| LIQ                        | float(8)    | LIQ Pastor-Stambaugh factor                                  |
| DividendPriceRatio         | float(8)    | Dividend price ratio                                         |
| lnDeltaP                   | float(8)    | log return of the adjusted price (CorpAdj and DividendAdj)<br/><span style='color:#32CD32'>MY Note: seems to be <strong>the closing price</strong>, in stead of adjusted price.</span> |
| lnDeltaOSEBX               | float(8)    | log return of the OSEBX index                                |
| lnDeltaOBX                 | float(8)    | log return of the OBX index                                  |
| NOWA_DayLnrate             | float(8)    | Log difference of Norwegian Overnight Weighted Average rate from the norwegian central bank after 2013. NIBOR before that. |
| bills_3month_Lnrate        | float(8)    | 3 months Norwegian Goverment Bills, from the bondindex table, CloseYield field. |
| Sector                     | varchar(50) | Sector                                                       |
| IN_OSEBX                   | int(4)      | True if the stock is in the OSEBX index at the moment        |
| Equity                     | float(8)    | Amount of Equity                                             |
| Debt                       | float(8)    | Amount of Debt                                               |
| Earnings                   | float(8)    | Total earnings                                               |
| debt_ratio                 | float(8)    | Debt ratio                                                   |
| PE                         | float(8)    | Price/Earnings                                               |





### **Risk free rate** (RFR)

- Before 2013 NIBOR: [Norges Bank](https://www.norges-bank.no/en/topics/Statistics/Historical-monetary-statistics/)

- After 2013 Norwegian Overnight Weighted Average rate: [Norske Finansielle Referenser AS (NoRe)](https://nore-benchmarks.com)
- [Titlon](https://titlon.uit.no/tabledefs.php): 3 months Norwegian Government Bills, from the `bondindex` table, `CloseYield field`.



Financial service companies publish surveys about financial data. For instance, PwC Norge.

- Here is their annual report about RFF: <https://www.pwc.no/no/publikasjoner/risikopremien.html>







**Asset Pricing data at OSE**

<https://ba-odegaard.no/financial_data/ose_asset_pricing_data/index.html>

