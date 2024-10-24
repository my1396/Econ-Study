---
layout: post
title: Style Guidelines
tag: study
update: 2024-07-16
---



## **Math Symbols & Equations**

- **<span style='color:#32CD32'>A space</span> should be placed between the numerical value and the unit symbol.** 

  数字和单位之间需要加空格！例外：百分号，摄氏度。

  For example, 1.2 dB is correct, while 1.2dB is not. 

  If you are writing in LaTeX, I recommend you use the siunitx by `\usepackage{siunitx}`. The command `\SI{<value>}{<unit>}` automatically prints the space between the numerical value and the unit symbol. 

  E.g., 3 g, 6 cm, 6 days, 7 years.

  **Exceptions** for percentage and temperatures. 10% and 17ºC. They do <span style='color:#32CD32'>not</span> need a space between numbers and units.

- **Physical units must <span style='color:#32CD32'>not</span> be italicized.** For example, 1.2 dB is correct, while 1.2 *dB* is not.

- Constant *e*, the imaginary unit *i* and the function symbol *f(x)* should be italicized. 

-  There should be a space before and after arithematic operators. E.g., 2.5 ± 0.07. 

- Number range: Use an <span style='color:#32CD32'>en dash</span> and do not include a space either before or after the en dash.

  Read chapters 7–9 before Friday.

  It must have been 1–2 degrees yesterday.

  - Do not mix en dash with ‘between/and’ and ‘from/to'.

- When to spell out numbers?

  - When the number is less than 10, they should be spelled out; 10 以下的数字要拼写。
  - Use Arabic numerals for 10 and above; 10以及10以上的数字用阿拉伯数字表示。
  - when numbers appear in the beginning of a sentence. 以数字开头的句子，数字要拼写出来。

- Decades are written in numerals without an apostrophe: 1970s. 年份都是用numerals.



Some math style conventions

- Variables should always be set in ***italic*** in both text and in equations.
- Vectors should be in **bold** type.
- Functions should be as roman type. E.g., $\exp, \ln, \arg$.
- If you need to break one long expression, the math operator such as `+` should be on the next line.



**Dashes**

- **Hyphen (-)** The shortest of the three, and the one most often used incorrectly with spaces when an en dash without spaces is needed (unless specifically using AP style).
- **En dash (–)** The champion of the hour. This is the little guy – or gal – you need for number ranges. So called because it’s the length of a lower-case ‘n’. How you type an en dash:
  - Option + hyphen key, or equivalently,
  - Make a dash by striking the hyphen key twice. 
  - Use `\textendash`.
- **Em dash (—)** The longest of the three dash types. It has its specific uses, but a number range is not one of them. And, you guessed it, it’s the length of a lower-case ‘m’.
  - Option + Shift + hyphen key



**Decimals**

- Put a zero before the decimal point when a number is less than 1 but the statistic can exceed 1.
- Do not use a zero before a decimal when the statistic cannot be greater than 1 (proportion, correlation, level of statistical significance).



**Statistics**

- Report exact *p*-values (italic lowercase p, 斜体小写) to two or three decimals (e.g., p=.006, p=.03). 
- Peport *p*-values less than .001 as “p < .001.”



**Minus sign**

I am not a fan of typing numbers in the text in mathmode. It's fine if you use a complete font, but what if you decide to change the math font later? I prefer to use the `textminus` from the `textcomp` package. 

```latex
Number \textminus10 (textcomp minus) \\
Number -10 (normal text minus, shown as a hypen, avoid this) \\
Number \num{-10} (siunitx textmode.) \\
Number $\num{-10}$ (siunitx mathmode)
```

Using a hypen is horrible.

<img src="https://drive.google.com/thumbnail?id=1_xGq_-wu8PxIH8sYhXTD2rBj4b2nL7R_&sz=w1000" alt="minus sign" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />



___

### `siunitx` syntax

A manual: <https://texdoc.org/serve/siunitx/0>

use `\sisetup{Option, Option, ...} `to set global appearance

`\num[⟨options⟩]{⟨numbers⟩}` 	Numbers are automatically formatted by the `\num` macro. This takes one optional argument, `⟨options⟩`, and one mandatory one, `⟨number⟩`.  

The formatter removes both ‘soft’ (`␣`) and ‘hard’ spaces (`\,` and `~`), automatically identifies exponents (as standard marked using e, E, d or D) and adds the appropriate spacing of large numbers. If required, a leading zero is added before a decimal marker: both `.` and `,` are recognised as decimal markers.

- `\numlist{10; 30; 50; 70}` print a list of numbers <img src="https://drive.google.com/thumbnail?id=1Q75UXEyC-vcEMwOyl9nxz23lY9EXpc22&sz=w1000" alt="num list" style="zoom:40%;" />

- `\numproduct{10 x 30}` print products <img src="https://drive.google.com/thumbnail?id=1Dab_stboUAZxaldoifgXZ2MzTNEY495v&sz=w1000" alt="num product" style="zoom:40%;" />

- `\numrange{10}{30}` print a range <img src="https://drive.google.com/thumbnail?id=1fnHAAAITCEilCppMtIQYaud4-LwutTbL&sz=w1000" alt="num range" style="zoom:40%;" />



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

- Author or authors. The surname is followed by first initial of their first name, the first initial of therir middle name (if applicable).

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











