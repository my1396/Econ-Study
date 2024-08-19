---
layout: post
title: Style Guidelines
tag: study
update: 2024-07-16
---



**Math Symbols & Equations**

- **<span style='color:#32CD32'>A space</span> should be placed between the numerical value and the unit symbol.** 

  数字和单位之间需要加空格！例外：百分号，摄氏度。

  For example, 1.2 dB is correct, while 1.2dB is not. If you are writing in LaTeX, I recommend you use the siunitx by `\usepackage{siunitx}`. Then the command` \SI{<value>}{<unit>}` automatically print the space between the numerical value and the unit symbol. 

  E.g., 3 g, 6 cm, 6 days, 7 years.

  Exceptions for percentage and temperatures. 10% and 17ºC.

- **Physical units must not be italicized.** For example, 1.2 dB is correct, while 1.2 *dB* is not.

- There should be a space before and after arithematic operators. E.g., 2.5 ± 0.07. 

- When to spell out numbers?

  - when the number is less than 10, then it should be spelled out; 10 以上的数字要拼写
  - when numbers appear in the beginning of a sentence. 以数字开头的句子，数字要拼写出来。

- Decades are written in numerals without an apostrophe: 1970s. 



Some math style conventions

- Variables should always be set in ***italic*** in both text and in equations.
- Vectors should be in **bold** type.
- Functions should be as roman type. E.g., $\exp, \ln, \arg$.
- If you need to break one long expression, the math operator such as `+` should be on the next line.
