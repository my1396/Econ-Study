---
layout: post
title: Style Guidelines
tag: study
update: 2024-07-16
---



## **Math Symbols & Equations**

- **<span style='color:#32CD32'>A space</span> should be placed between the numerical value and the unit symbol.** 

  数字和单位之间需要加空格！例外：百分号，摄氏度，华氏度。

  For example, 1.2 dB is correct, while 1.2dB is not. 

  20ºC, 60ºF. (温度不需要加空格, C 和 F 不需斜体)

  - In LaTex, can use `\degree` from `gensymb` package.
  - Another alternative is the `\textdegree` command, which is provided by the `textcomp` package. 

  If you are writing in LaTeX, I recommend you use the siunitx by `\usepackage{siunitx}`. The command `\SI{<value>}{<unit>}` automatically prints the space between the numerical value and the unit symbol. 

  E.g., 3 g, 6 cm, 6 days, 7 years.

  **Exceptions** for percentage and temperatures. 10% and 17ºC. They do <span style='color:#32CD32'>not</span> need a space between numbers and units.

- **Physical units must <span style='color:#32CD32'>not</span> be italicized.** For example, 1.2 dB is correct, while 1.2 *dB* is not.

- Constant *e*, the imaginary unit *i* and the function symbol *f(x)* should be <span style='color:#32CD32'>*italicized*</span>. 

-  There should be a space before and after arithematic operators. E.g., 2.5 ± 0.07. 

- Number range: Use an <span style='color:#32CD32'>en dash</span> and do not include a space either before or after the en dash.

  Read chapters 7–9 before Friday.

  It must have been 1–2 degrees yesterday.

  - Do not mix en dash with ‘between/and’ and ‘from/to'.

- When to spell out numbers?

  - <span style='color:#32CD32'>When the number is less than 10, they should be spelled out;</span> 10 以下的数字要拼写。
  - Use Arabic numerals for 10 and above; 10 以及 10 以上的数字用阿拉伯数字表示。
  - <span style='color:#32CD32'>When numbers appear in the beginning of a sentence.</span> 以数字开头的句子，数字要拼写出来。

- Decades are written in numerals without an apostrophe: 1970s. 年份都是用numerals.

- Currency format

  - All currency symbols are placed before the number amount <span style='color:#32CD32'>without any spacing</span>. 

    E.g, $500.

  - The abbreviation of a currency (e.g. USD or, EUR) should precede the number amount <span style='color:#32CD32'>with a space</span>.

    E.g., EUR 400.

    The 3-letter come from International Bank Account Number [(IBAN) currency codes](https://www.iban.com/currency-codes).

  - In all numbers greater than three digits, at least one comma will be required. Counting from right to left, place a comma after every third number. E.g., $3,000.

    It is important to note that this is different from many European countries, where the comma and period have reverse roles.

  - Negative currency numbers are indicated in several ways

    - Parentheses. E.g., ($100).

    - A minus sign in front of the currency symbol. E.g., -$100. Do NOT put a space between the minus sign and the value.

      In EU countries, minus sign is also put behind the currency symbol, e.g., $-100.



**Some math style conventions**

- Variables should always be set in ***italic*** in both text and in equations.
  - Identifiers (which can be superscript or subscript words, letters, or numbers) are not italicized. E.g., $M_{\text{girls}}=4.22,$ the symbol for mean is italicized, but the nonvariable identifier `girls` is NOT italicized.

- Vectors should be in **bold** type.
- Functions should be as roman type. E.g., $\exp, \ln, \arg$.
- If you need to break <u>one long expression</u>, the <span style='color:#32CD32'>math operator such as `+` should be on the next line</span>.



**Font for Numbers**

Why put numbers inside `$...$`?

- Sometimes you use <span style='color:#32CD32'>different fonts</span> for math-mode numerals and text-mode numerals. This is when you want to put all your numbers inside dollar signs `$...$`.

  The main takeaway is that numbers should have a consistent font.

  For instance, if you use `\usepackage{charter}` for main text font and `\usepackage[expert]{mathdesign}` for math, if you don't put all your numbers in formulas, they will look differently.

  <img src="https://drive.google.com/thumbnail?id=1HdmojitH48NG9DL70qbomNNvvVCtw012&sz=w1000" alt="charter math font" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

- If the numerals are in a theorem, they will be in *italic* unless you put `$` around them.

  Here is an example showing why mathematical numbers should always be typed as formulas (that is, between `$...$`).

  ```tex
  \begin{lemma}
  If $v\ne0$ is a vector in $\mathbb{R}^{n}$, then $vv^T$ is a rank~$1$ matrix.
  \end{lemma}
  ```

  If we don't type `$1$` but simply `1`, the style in which the statement is typeset would prevail and the number would probably appear in italics, as this is the usual font for mathematical statements. The `1` in italics would be wrong, without any doubt.

- When you have a negative number, you need to type as a formula as `-` outside math mode prints a hypen.

  ```tex
  Without \$'s:
  2, -2; \textit{2, -2}
  With \$'s:
  $2$, $-2$;  \textit{$2$, $-2$}
  The first version is rather unacceptable.
  ```

  <img src="https://drive.google.com/thumbnail?id=1STMfl0cA7HpkmynwxQxiR5DQ0vwi4Db8&sz=w1000" alt="Math mode numerals" style="display: block; margin-right: auto; margin-left: auto; zoom:60%;" />

  Another example:

  <img src="https://drive.google.com/thumbnail?id=1uJj36bHQtGsk-44z7sPVoR1TdG8fkeD0&sz=w1000" alt="Math mode numerals2" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

  Exerpt source: Donald E. Knuth 1989, TUGboat -- ["Typesetting Concrete Mathematics"](http://tug.org/TUGboat/tb10-1/tb23knut.pdf).



**Dashes**

- **Hyphen (-)** The shortest of the three, and the one most often used incorrectly with spaces when an en dash without spaces is needed (unless specifically using AP style).

- **En dash (–)** The champion of the hour. This is the little guy – or gal – you need for **number ranges**. So called because it’s the length of a lower-case ‘n’. How you type an en dash:
  
  - Option + hyphen key, or equivalently,
  - Make a dash by striking the hyphen key twice, i.e., `--`. 
  - Use `\textendash`.
  
- **Em dash (—)** The longest of the three dash types. It has its specific uses, but a number range is not one of them. And, you guessed it, it’s the length of a lower-case ‘m’.
  
  - Option + Shift + hyphen key
  
  - An em dash is usually used to mark abreak in a sentence in place of a semicolon (`;`) or colon (`:`).   
    Can also be used in paris to add additional information that is not essential to understand the sentence. Function similarly to parentheses or a pair of commas.
  
    E.g.,   
    Dark, leafy greens — such as spinach, kale, and chard — are an important part of a healthy diet.
  
    Q: Do I need to add spaces before and after an em dash?
  
    Q: There is no universal rule. Just be consistent throughout your text.



**Decimals**

- Put a zero before the decimal point when a number is less than 1 but the statistic can exceed 1.
- Do not use a zero before a decimal when the statistic cannot be greater than 1 (proportion, correlation, level of statistical significance).



**Statistics**

- Report exact *p*-values (italic lowercase p, 斜体小写) to two or three decimals (e.g., p=.006, p=.03). 
- Peport *p*-values less than .001 as “p < .001”.



### Minus sign

Textmode vs. mathmode numerals

I am not a fan of typing numbers in the text in mathmode. It's fine if you use a complete font, but what if you decide to change the math font later? A complete font include text and math fonts, whereas some fonts only contains text font. In this scenario, math will use the default font, might cause inconsistent appearance.

Two tips:

- use a complete font
- specify a math font

Q: How to type a minus number?

A: `\num{-<number>}` from the `siunitx` package or `textminus` from the `textcomp` package. `textminus` is somewhat thinner than `\num`. I prefer to use `\num`.  Note that a minus sign cannot be used alone, e.g. `\num{-}`, it has to be a valid negative number.

```latex
Number \textminus10 (textcomp minus) \\
Number -10 (normal text minus, shown as a hypen, avoid this) \\
Number \num{-10} (siunitx textmode.) \\
Number $\num{-10}$ (siunitx mathmode)
```

Using a hypen is horrible. No matter what, do NOT use a hypen!

<img src="https://drive.google.com/thumbnail?id=1_xGq_-wu8PxIH8sYhXTD2rBj4b2nL7R_&sz=w1000" alt="minus sign" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

___

Q: How to type a minus sign stand alone?

A: use `\textminus` , `\si{-}` (lowercase), or `\unit{-}`.



___

### `siunitx` syntax

A manual: <https://texdoc.org/serve/siunitx/0>

The `siunitx` package is now in v3, with many changes:

> Instead of `\SI`, `\si`, `\SIlist`, `\SIrange`, `siunitx` now provides more <u>descriptive command names</u>, so you can now write `\qty{3.5}{\meter\per\second}`; `\unit{\kilo\ohm}`; `\qtylist{0.76;0.8;1.54}{\micro\gram}`; `\qtyrange{0.4}{2.5}{\centi\meter}`, etc. 
>
> The <u>old commands will still work</u>, but it is recommended to use the new commands.

V1 manual: <https://www.sys.kth.se/docs/texlive/texmf-dist/doc/latex/siunitx/siunitx.pdf>



Use `\sisetup{Option, Option, ...} `to set global appearance

`\num[⟨options⟩]{⟨numbers⟩}` 	Numbers are automatically formatted by the `\num` macro. This takes one optional argument, `⟨options⟩`, and one mandatory one, `⟨number⟩`.  

The formatter removes both ‘soft’ (`␣`) and ‘hard’ spaces (`\,` and `~`), automatically identifies exponents (as standard marked using e, E, d or D) and adds the appropriate spacing of large numbers. If required, a leading zero is added before a decimal marker: both `.` and `,` are recognised as decimal markers.

- `\numlist{10; 30; 50; 70}` print a list of numbers <img src="https://drive.google.com/thumbnail?id=1Q75UXEyC-vcEMwOyl9nxz23lY9EXpc22&sz=w1000" alt="num list" style="zoom:40%;" />

- `\numproduct{10 x 30}` print products <img src="https://drive.google.com/thumbnail?id=1Dab_stboUAZxaldoifgXZ2MzTNEY495v&sz=w1000" alt="num product" style="zoom:40%;" />

- `\numrange{10}{30}` print a range <img src="https://drive.google.com/thumbnail?id=1fnHAAAITCEilCppMtIQYaud4-LwutTbL&sz=w1000" alt="num range" style="zoom:40%;" />

`\SI[⟨options⟩]{<number>}{<unit>}`  E.g., `\SI{10.5}{\kilo\meter}` for $10.5 \text{ km}$, `\SI{2.6}{\volt\per\meter}` for $2.6 \text{ Vm}^{-1}$.  

- This function now becomes `\qty[⟨options⟩]{⟨number⟩}{⟨unit⟩}`. `\qty{10.5}{\kilo\meter}`, `\qty` for quantity.

Lowercase `\si` typesets units with no values. The new function is `\unit{⟨unit⟩}` in the latest version of the package.

`\si{kg.m/s^2}` is equivalent to `\SI{}{kg.m/s^2}`, which generates $\text{kg m/s}^2$.

___

`siunitx-print` controls font printing for numbers and units.

The following key-value options are available:

| Option                             | Meaning                                                      |
| ---------------------------------- | ------------------------------------------------------------ |
| `mode = match|math|text`           | Selects which mode (math or text) the output is printed in.   <br />`match` matches the mode prevailing at the point `\siunitx_print_...:n` is called. The `math` and `text` options choose the relevant TEX mode for printing. The standard setting is `math`. |
| `propagate-math-font = true|false` | Switch to determine if the currently-active math font is applied within printed output. This is relevant only when `\siunitx_print_...:n` is called from within `math` mode: in `text` mode there is not active math font. When not active, math mode material will be typeset using standard math mode fonts without any changes being made to the supplied argument. The standard setting is `false`. |





___

### Citing equations, tables, and figures

Use `Eq. (1)` when citing one equation, `Eqs. (1) and (2)` for citing more than one equation.  

- It is common that `Eq.` is omitted for all and only `(1)` is used to refer to a equation. 

- If it is the first word of the sentence, use `Equation (1)`.
- Acceptable abbreviations include 
  - `eq` and `eqs`  (no periods)
  - `eq.` and `eqs.` (with periods)
  - `Eq.` and `Eqs.` (capitalization)
  - `eqtn.` and `eqtns.` 
  - `Eqtn.` and `Eqtns.`
- number needs to be put in parentheses.
- labels are right-aligned.



Use `Table 1` (or `Tables 1 and 2` for plural) to refer to tables. No abbreviations for tables. 

- Table labels, titles, and captions are placed on <span style='color:#32CD32'>top</span> of the table.
- Below the table, there can be explanatory footnotes as necessary. Footnotes apply to a specific part of the table; while notes that apply to the whole table should be treated as captions.

Use `Figs. 1` (or `Figs 1a and 1b` for plural) to refer to figures. Use abbreviations for figures.

- Figure titles and captions go <span style='color:#32CD32'>below</span> the figure.
- Subplots are denoted using a lowercase letter within parentheses.



## Bullet points

For a list that contains full sentences:

- Always use a lead-in line, ending with a colon.  开头的介绍要以冒号结尾。
- Ensure that each bullet item is a full sentence.  每个点是句子的时候要<span style='color:#32CD32'>大写首字母</span>，且以<span style='color:#32CD32'>句号结尾</span>。
- Start each bullet item (sentence) with an uppercase letter.
- Use a full stop at the end of each bullet item.

For a list whose bullet points are not full sentences:

- introduce the list with a lead-in line (that ends with a colon)
- ensure that each bullet point makes sense reading on from the lead-in line
- use a consistent form/structure for each bullet point
- start each bullet point with a lowercase letter  每个点不是完整句子的时候，<span style='color:#32CD32'>首字母小写</span>，<span style='color:#32CD32'>结尾不加标点</span>
- omit punctuation at the end of individual bullet points, including the last  即使最后一个点也不加标点！



## Punctuations

**Comma**

Use a comma (often called a “serial comma” or “Oxford comma”) before the final “and” in a list of three or more items.



**Ellipsis**

- Use a space both before and after an ellipsis. 

- Do not add a full stop if the ellipsis ends a sentence.

- Preceding punctuation can be omitted, unless needed for comprehension (e.g. a question mark or exclamation mark). 



**Useful resources**:

1. <https://www.e-education.psu.edu/styleforstudents/c1_p9.html>



The most common sequence of footnote reference marks is: 1. asterisk (*), 2. dagger (†, `\dagger`), 3. double dagger (††), 4. paragraph symbol (¶), 5. section mark (§), 6. parallel rules (\|\|), 7. number sign (#).   
If more are required, they can be doubled up: double asterisks (**), double single daggers (††, `\dagger\dagger`), double double daggers (††††), etc. However, when many footnotes are used, it is more practical to use consecutive numbers to identify each footnote.



## References

Citing sources in APA style 7th ed.

<https://libraryguides.vu.edu.au/apa-referencing/7Books>

<https://www.scribbr.com/apa-examples/book/>

APA style: refer to "Publication Manual of the American Psychological Association".

Citations vs. References

- Traditionally the term "citation" is used to refer to an in-text source, 

- while "reference " is the correct term for a source listed on the reference page of a paper.

**Styling**

- The first line of each citation is left adjusted. Every subsequent line is indented 5-7 spaces.



Book references: general form

Should include the following info:

- Author or authors. The surname is followed by first initial of their first name and the first initial of their middle name (if applicable).

  - 如果只有两个作者，中间用 `,&` 连接。

  - 如果有3个及以上作者，作者中间用 `,␣` (逗号 + 空格)隔开，最后一个作者用 ,`&`。

- Year of publication of the book (in round brackets).

- Book title (in *italics*). If it is a multivolume work, put the specific volumes in parentheses after the book title. E.g.,

  > Harris, K. R., Graham, S., & Urdan T. (Eds.). (2012). *APA educational psychology handbook* (Vols. 1–3). American Psychological Association.

- Edition (in round brackets), if other than first.

- Publisher.

- DOI. Include a DOI for all works that have one, regardless of whether you used the online version or print version.

**Example:** Hasler, E. (2018). *The built environment.* Liverpool University Press.

<img src="https://drive.google.com/thumbnail?id=1HrvZR_Nevrm7WtXAcldZu4pGmE6HCHpz&sz=w1000" alt="book references" style="zoom:80%;" />



| Material Type                   | In-Text Example                                              | Reference List Example                                       |
| ------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Book: 2 Authors, and Edition    | According to Moran and Toner (2017)… <br />**OR**<br /> … this is evident (Moran & Toner, 2017). | Moran, A., & Toner, J. (2017). A critical introduction to sport psychology (3rd ed.). Routledge.<br/><br/>**The edition number is included after the title of the work (not necessary for first editions).** |
| Book: 3 to 20 Authors, with DOI | Interval training involves "performing for a comparatively shorter time period during each exercise session" (Haile et al., 2015, p. 135).<br/>OR<br/>Haile et al. (2015) note that interval training involves "performing for a comparatively shorter time period during each exercise session" (p.135).<br/><br/>**Where there are 3 or more authors cite only the first author's surname followed by et al.** | Haile, L., Gallagher, M., & Robertson, R. J. (2015). Perceived exertion laboratory manual: From standard practice to contemporary application. Springer. https://doi.org/10.1007/978-1-4939-1917-8<br/><br/>**Provide the names of all authors in the reference list, up to and including 20 authors.**<br/><br/>**For a book with 21 or more authors follow the same author format as for a journal article with 21 or more authors.** |
| Book chapter: Case Study        | Scerri & Presbury (2022) use a service language model...     | Scerri, M., & Presbury, M. (2022). The power of words: A case study of service language in an Australian five-star hotel. In S. M. Perry (Ed.), Case based research in tourism, travel, hospitality and events (pp. 117-133). Springer. https://doi. https://doi.org/10.1007/978-981-16-4671-3_7 |
|                                 |                                                              |                                                              |



##### What is an ISBN and a DOI?

- An International Standard Book Number (ISBN) identifies a book by format (print, audio etc.), edition and publisher.
  - It is a 13 (after 1 January 2007) or 10 (before 2007) digits number assigned to all books and book-like publications that are published internationally.
  - The purpose of the ISBN is to establish and identify one title or edition of a title from one specific publisher and is unique to that edition, allowing for more efficient marketing of products by booksellers, libraries, universities, wholesalers and distributors.

- A Digital Object Identifier (DOI) is as persistent and stable as an ISBN. The advantage of using a DOI in the online environment is that it can be expressed in resolvable format, (e.g. http://doi.org/10.4225/35/5715bcdd2df24) so that there is always a link back to the online location of the item.

It is not necessary for an ISBN and DOI to be issued for the same publication unless it will be distributed in both print and electronic formats.











