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

- There should be a space before and after arithematic operators. E.g., 2.5 ± 0.07. 

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



### `siunitx` syntax

A manual: <https://texdoc.org/serve/siunitx/0>

use `\sisetup{Option, Option, ...} `to set global appearance

`\num[⟨options⟩]{⟨numbers⟩}` 	Numbers are automatically formatted by the `\num` macro. This takes one optional argument, `⟨options⟩`, and one mandatory one, `⟨number⟩`.  

The formatter removes both ‘soft’ (`␣`) and ‘hard’ spaces (`\,` and `~`), automatically identifies exponents (as standard marked using e, E, d or D) and adds the appropriate spacing of large numbers. If required, a leading zero is added before a decimal marker: both `.` and `,` are recognised as decimal markers.

- `\numlist{10; 30; 50; 70}` print a list of numbers <img src="https://drive.google.com/thumbnail?id=1Q75UXEyC-vcEMwOyl9nxz23lY9EXpc22&sz=w1000" alt="num list" style="zoom:40%;" />

- `\numproduct{10 x 30}` print products <img src="https://drive.google.com/thumbnail?id=1Dab_stboUAZxaldoifgXZ2MzTNEY495v&sz=w1000" alt="num product" style="zoom:40%;" />

- `\numrange{10}{30}` print a range <img src="https://drive.google.com/thumbnail?id=1fnHAAAITCEilCppMtIQYaud4-LwutTbL&sz=w1000" alt="num range" style="zoom:40%;" />







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





**Comma**

Use a comma (often called a “serial comma” or “Oxford comma”) before the final “and” in a list of three or more items.



**Ellipsis**

- Use a space both before and after an ellipsis. 

- Do not add a full stop if the ellipsis ends a sentence.

- Preceding punctuation can be omitted, unless needed for comprehension (e.g. a question mark or exclamation mark). 





