---
layout: post
title: Style Guidelines
tag: study
update: 2024-07-16
---



## Math Symbols & Equations

- **<span style='color:#00CC66'>A space</span> should be placed between the numerical value and the unit symbol.** 

  数字和单位之间需要加空格！例外：百分号，摄氏度，华氏度。

  For example, 1.2 dB is correct, while 1.2dB is not. 

  20ºC, 60ºF. (温度不需要加空格, C 和 F 不需斜体)

  - In LaTex, can use `\degree` from `gensymb` package.
  - Another alternative is the `\textdegree` command, which is provided by the `textcomp` package. 

  If you are writing in LaTeX, I recommend you use the siunitx by `\usepackage{siunitx}`. The command `\SI{<value>}{<unit>}` automatically prints the space between the numerical value and the unit symbol. 

  E.g., 3 g, 6 cm, 6 days, 7 years.

  **Exceptions** for percentage and temperatures. 10% and 17ºC. They do <span style='color:#00CC66'>not</span> need a space between numbers and units.

- Put a space before and after a mathematical operator (e.g., minus, plus, greater than, less than).

  For a negative value, put a space only before the minus sign, not after it (e.g., –8.25).

- **Physical units must <span style='color:#00CC66'>not</span> be italicized.** For example, 1.2 dB is correct, while 1.2 *dB* is not.

- Constant *e*, the imaginary unit *i* and the function symbol *f(x)* should be <span style='color:#00CC66'>*italicized*</span>. 

- There should be a space before and after arithematic operators. E.g., 2.5 ± 0.07. 

- Number range: Use <span style='color:#00CC66'>two hypens</span> or opt + hypen ( <span style='color:#00CC66'>an en dash</span>) and do not include a space either before or after the dash.

  Read chapters 7–9 before Friday.

  It must have been 1–2 degrees yesterday.

  - Do <span style='color:red'>NOT</span> mix en dash with ‘between/and’ and ‘from/to'. ❌

    Michaelmas term runs from October to December. ✅

    Michaelmas term runs October–December. ✅

    Michaelmas term runs from October–December. ❌

  - If using dash symbols cause confusion, such as when negative values are involved, use words. For example, "from –0.2 to –0.14" and from "–3 to 3."

- When to spell out numbers?

  - <span style='color:#00CC66'>When the number is less than 10, they should be spelled out;</span> 10 以下的数字要拼写。
  - Use Arabic numerals for 10 and above; 10 以及 10 以上的数字用阿拉伯数字表示。
  - <span style='color:#00CC66'>When numbers appear in the beginning of a sentence.</span> 以数字开头的句子，数字要拼写出来。

- Decades are written in numerals without an apostrophe: 1970s. 年份都是用numerals.

- Currency format

  - All currency symbols are placed before the number amount <span style='color:#00CC66'>without any spacing</span>. 

    E.g, $500.

  - The abbreviation of a currency (e.g. USD or, EUR) should precede the number amount <span style='color:#00CC66'>with a space</span>.

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
- If you need to break <u>one long expression</u>, the <span style='color:#00CC66'>math operator such as `+` should be on the next line</span>.



**Font for Numbers**

Why put numbers inside `$...$`?

- Sometimes you use <span style='color:#00CC66'>different fonts</span> for math-mode numerals and text-mode numerals. This is when you want to put all your numbers inside dollar signs `$...$`.

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



___

### Dashes

- **Hyphen (-)** The shortest of the three, and the one most often used incorrectly with spaces when an en dash without spaces is needed (unless specifically using AP style).

  - Function:  used to link parts of a compound word, such as eye-opener, fifty-xis, two-thirds, three-year-old, three-quarter-mile, half-hour, six-pack, president-elect, Mexican-American.

- **En dash (–)** The champion of the hour. This is the little guy – or gal – you need for **number ranges**. So called because it’s the length of a lower-case ‘n’. 
  
  - Function: The en dash is used to represent a span or range of numbers, dates, or time. There should be N**O space** between the en dash and the adjacent material. E.g.,
  
    > The 2010⁠–⁠2011 season was our best yet.
    >
    > You will find this material in chapters 8⁠–⁠12.
    >
    > The professor holds office hours every Wednesday, 11:00 a.m.⁠–⁠1:00 p.m.
  
    Note that if you introduce a span or range with words such as *from* or *between*, do NOT use the en dash.
  
    > She served as secretary of state *from* 1996 to 1999.  ✅  
    > She served as secretary of state *from* 1996⁠–⁠1999. ❌
    >
    > The regime’s most oppressive treatment occurred *between* 1965 and 1970. ✅  
    > The regime’s most oppressive treatment occurred *between* 1965⁠–⁠1970. ❌
  
  - How you type an en dash:
  
    - Use <span style='color:#00CC66'>`\textendash`</span> safe to encoding changes, ✅
  - Option + hyphen key, or equivalently, strike the hyphen key twice, i.e., `--`.  (<span style='color:#FF9900'>Required unicode support! **Not safe**.</span>)
  
- **Em dash (—)** The longest of the three dash types. It has its specific uses, but a number range is not one of them. And it’s the length of a lower-case ‘m’.
  
  - How you type em dash: 
  
    - Use <span style='color:#00CC66'>`\textemdash`</span> safe to encoding changes, ✅
    - Option + Shift + hyphen key (<span style='color:#FF9900'>Required unicode support! **Not safe**.</span>)
  
  - Function: An em dash is usually used to mark abreak in a sentence in place of a semicolon (`;`) or colon (`:`).   
    Can also be used in paris to add additional information that is not essential to understand the sentence. Function similarly to parentheses or a pair of commas.
  
    E.g.,   
    Dark, leafy greens — such as spinach, kale, and chard — are an important part of a healthy diet.
  
    Q: Do I need to add spaces before and after an em dash?  
    A: There is <u>no universal rule</u>. Just be consistent throughout your text.



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

More about minus sign

- No space between the minus sign and the number

- Format negative values in tables

  See the following two examples with correctly formatted negative values. This can be achieved by 

  - `D` column type in the  `dcolumn` package

    `\newcolumntype{d}[1]{D{.}{.}{#1}}`, or

  - `S` column type in the `siunitx` package.

    `S[table-format=3.2]` is equivalent to `D{.}{.}{3.2}`. 

  <img src="https://drive.google.com/thumbnail?id=1oqJLONxbOIZSQKS8oy1NEzC0oTSuGV70&sz=w1000" alt="Table with negative value" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

  <img src="https://drive.google.com/thumbnail?id=1QPQldSvgt-x__eZ_COzAVnH6ghmZ6qBw&sz=w1000" alt="Table with negative value" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />



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

- Table labels, titles, and captions are placed on <span style='color:#00CC66'>top</span> of the table.
- Below the table, there can be explanatory footnotes as necessary. Footnotes apply to a specific part of the table; while notes that apply to the whole table should be treated as captions.

Use `Figs. 1` (or `Figs 1a and 1b` for plural) to refer to figures. Use abbreviations for figures.

- Figure titles and captions go <span style='color:#00CC66'>below</span> the figure.
- Subplots are denoted using a lowercase letter within parentheses.



## Bullet points

For a list that contains full sentences:

- Always use a lead-in line, ending with a colon.  开头的介绍要以冒号结尾。
- Ensure that each bullet item is a full sentence.  每个点是句子的时候要<span style='color:#00CC66'>大写首字母</span>，且以<span style='color:#00CC66'>句号结尾</span>。
- Start each bullet item (sentence) with an uppercase letter.
- Use a full stop at the end of each bullet item.

For a list whose bullet points are not full sentences:

- introduce the list with a lead-in line (that ends with a colon)
- ensure that each bullet point makes sense reading on from the lead-in line
- use a consistent form/structure for each bullet point
- start each bullet point with a lowercase letter  每个点不是完整句子的时候，<span style='color:#00CC66'>首字母小写</span>，<span style='color:#00CC66'>结尾不加标点</span>
- omit punctuation at the end of individual bullet points, including the last  即使最后一个点也不加标点！



___

### Lists of items

- Sentences often contain lists of items. When a list within a sentence contains three or more items, [use a serial comma before the final item](https://apastyle.apa.org/style-grammar-guidelines/punctuation/serial-comma).

  > We gathered information about participants’ age, gender, and socioeconomic status.

- However, if any item in a list of three or more items already contains commas, use semicolons instead of commas between the items.

  > We divided participants by age into categories of young adults, which included people between the ages of 18 and 40 years; middle-aged adults, which included people between the ages of 40 and 60 years; and older adults, which included people ages 60 years and older.

- To draw more attention to the items and help readers understand the separate, parallel items in a complex list, use lowercase letters in parentheses before each item. Do not use numbers in parentheses.

  > Participants provided information about their (a) level of education; (b) income, specified at the family level; (c) occupation, including both specific role and industry; and (d) family size.

- [Use a numbered list](https://apastyle.apa.org/style-grammar-guidelines/lists/numbered) if you want to display items in a numbered series. [Use a bulleted list](https://apastyle.apa.org/style-grammar-guidelines/lists/bulleted) if you want to draw visual attention to items without implying that they go in a certain order.



___

### Introducing Examples

There are several phrases that are commonly used to introduce examples.

<table style="width: 25%; margin-left: auto; margin-right: auto;"><tbody>
  <tr>
    <td>for example</td>
  </tr>
  <tr>
    <td>for instance</td>
  </tr>
  <tr>
    <td>such as</td>
  </tr>
  <tr>
    <td>e.g.</td>
  </tr>
</tbody>
</table>

For our purposes, let's break them up into 2 groups: phrases used within a sentence and phrases used to begin a new sentence. 

1. **Phrases used within a sentence** 

   Each phrase can be used within a sentence when it is followed by a list of items which elaborate on or show examples for the main idea of the sentence. 

   <table><tbody>
     <tr>
       <td>I can play quite a few musical instruments, <span style='color:red'>for example</span>, the flute, the guitar, and the piano. </td>
     </tr>
     <tr>
       <td>I can play quite a few musical instruments, <span style='color:red'>for instance,</span> the flute, the guitar, and the piano.</td>
     </tr>
     <tr>
       <td>I can play quite a few musical instruments, <span style='color:red'>e.g.,</span> the flute, the guitar, and the piano.</td>
     </tr>
     <tr>
       <td>I can play quite a few musical instruments, <span style='color:red'>such as</span> the flute, the guitar, and the piano.</td>
     </tr>
   </tbody>
   </table>

   **Such as** does NOT have a comma after it; the first three phrases have commas before and after them.

   The phrase such as can be used in the middle of a sentence without any commas.

   <table><tbody>
     <tr>
       <td>Car companies <span style='color:red'>such as</span> Toyota and Ford manufacture their automobiles in many different countries around the world. </td>
     </tr>
   </tbody>
   </table>

   - If the words after `such as` are necessary and essential to the meaning of the sentence, you do NOT use the commas. This is the case in the example above.

     If you take out `such as` from the sentence, it would be "Car companies manufacture their automobiles in many different countries around the world." 

     It could mean ALL car companies manufacture their automobiles in many different countries around the world. This is not true because some companies produce their cars in just one or two countries. Therefore, the phrase **such as Toyota and Ford** is necessary. $\rightarrow$  Do NOT use commas.

   - If the examples can be taken out without losing the meaning of the sentence, you put the comma before `such as`.

   

2. **Phrases used to begin a new sentence**

   Usually only for example and for instance can begin new sentences.  Each can begin a new sentence when the phrase is followed by <u>a complete idea or sentence</u> (NOT a list of items). 

   <table><tbody>
     <tr>
       <td> My father loves going to restaurants which serve exotic foods.  <span style='color:red'>For example,</span> last week he went to a restaurant which serves deep-fried rattlesnake.  </td>
     </tr>
       <tr><td>My father loves going to restaurants which serve exotic foods. <span style='color:red'>For instance,</span> last week he went to a restaurant which serves deep-fried rattlesnake. </td>
     </tr>
   </tbody>
   </table>



Use *"alternatively"* when there is a **choice**, or you intend to **suggest an action** different from that mentioned in a previous sentence. This sentence connector occurs most frequently with *"can"* or *"could"*, and can also follow *"or"* (often without a comma). 





## Punctuations

Chicago Mannual of Style – Punctuation: <https://www.chicagomanualofstyle.org/book/ed18/part2/ch06/toc.html>

**Comma**

Use a comma (often called a “serial comma” or “Oxford comma”) before the final “and” in a list of three or more items.



**Forward Slashes** (/)

- If the slash divides <u>two words</u>, there is NO need to include a space on either side of a forward slash.

  E.g., apples/bananas 

- If it divides <u>two phrases or sentences</u> (or a single word from a phrase), it requires a space before and after. 

  E.g., truwana / Cape Barren Island 



___

**Ellipsis**

- Use a space both before and after an ellipsis. 

- Do not add a full stop if the ellipsis ends a sentence.

- Preceding punctuation can be omitted, unless needed for comprehension (e.g. a question mark or exclamation mark). 



___

### Quotation Marks

- When to use double quotation marks:

  - Providing direct quotations of less than forty words (for quotes with >40 words, use <u>block quotations</u>). Used to copy contents from any other source (including published texts, internet resources, marketing or business materials, test or interview questions, and more) into your paper.

    - If there are quotation marks within a quote of less than forty words, change those to <u>single quotation marks</u>.

  - Referring to a letter, word, phrase, or sentence as a <u>linguistic example of itself</u>: the letter "p"; the singular "they"; he wrote over and over "all work and no play makes Jack a dull boy."

    Ex:

    > The student struggled with the use of "their" "they're," and "there."

  - <u>First introducing a word or phrase <span style='color:#00CC66'>ironically</span></u>, as slang, or newly coined: I was not what you would call a "normal" teenager. The study produced what I will refer to as "alpha-particles."

    Ex:

    > There were many instances of "friendly joking" that created a hostile workplace environment.

    Note: Use quotation marks only the first time the words or phrases are used, not for later uses.

  - Mentioning the title of a periodical or book chapter**:** In chapter one, "The Boy Who Lived"...; Maniotes and Kuhlthau's (2014) article, "Making the Shift: From Traditional Research Assignments to Guiding Inquiry Learning," describes...

    Ex:

    > The fourth chapter of the APA 7 manual, "Writing Style and Grammar," contains a lot of useful information.

- <span style='color:#00CC66'>Typesetting of double quotation marks</span>:

  - One set of quotation marks will show the beginning of the quote and the other will show when it ends. <u>Leave no space</u> between the quotation marks and the text they surround.

  - <u>Capitalize the first word</u> of the quotation when it is introduced as dialogue.

    Ex:

    > Samson (2010) stated, “<u>M</u>irror neurons allow for imitation and empathy” (p. 214).
    >
    > Johnson (2017) reported, "<u>W</u>alden students should use APA" (p. 45).

  - Place commas (`,`), periods (`.`), exclamation marks (`!`), and question marks (`?`) <u>inside quotation marks</u>; all other punctuation marks are placed <u>outside quotation marks.</u>

    | **Punctuation mark**                                         | **In relation to closing quotation mark, place it…** | **Example**                                                  | **Notes**                                                    |
    | ------------------------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | Comma                                                        | Inside                                               | Many dream images were characterized as <span style='color:#00CC66'>“</span>raw<span style='color:#00CC66'>,” “</span>powerful<span style='color:#00CC66'>,”</span> and <span style='color:#00CC66'>“</span>evocative<span style='color:#00CC66'>.”</span> |                                                              |
    | Period                                                       | Inside                                               | Participants who kept dream diaries described themselves as <span style='color:#00CC66'>“</span>introspective<span style='color:#00CC66'>”</span> and <span style='color:#00CC66'>“</span>thoughtful<span style='color:#00CC66'>.”</span> |                                                              |
    | Question mark or exclamation point (<span style='color:#00CC66'>part of quoted material</span>) | Inside                                               | The Dream Questionnaire items included <span style='color:#00CC66'>“</span>How often do you remember your dreams<span style='color:#00CC66'>?”</span> and <span style='color:#00CC66'>“</span>What do you most often dream about<span style='color:#00CC66'>?”</span> We found intriguing results. | When a quotation ending in a question mark or exclamation point ends a sentence, no extra period is needed. |
    | Quotation within a quotation + period or comma               | Inside                                               | Some participants were skeptical about the process<span style='color:#00CC66'>: “</span>I don’t put any stock in these <span style='color:#00CC66'>‘</span>dream diaries<span style='color:#00CC66'>.’”</span> | When multiple quotation marks are used for quotations within quotations, keep the quotation marks together (put periods and commas inside both; put semi-colons, colons, etc., outside both). |
    |                                                              |                                                      |                                                              |                                                              |
    | Parentheses                                                  | Outside                                              | Barris (2010) argued that <span style='color:#00CC66'>“</span>dreams express and work with the logic of gaining a sense of and a relation to ourselves, our lives, or our sense of reality as a whole<span style='color:#00CC66'>” (p. 4).</span> | See more examples of how to cite direct quotations [here](https://blog.apastyle.org/apastyle/2010/03/how-to-cite-direct-quotations.html). |
    | Semi-colon                                                   | Outside                                              | At the beginning of the study, participants described their dream recall rate as <span style='color:#00CC66'>“</span>low to moderate<span style='color:#00CC66'>”;</span> at the end, they described it as “moderate to high<span style='color:#00CC66'>.”</span> |                                                              |
    | Colon                                                        | Outside                                              | Participants stated they were <span style='color:#00CC66'>“</span>excited to begin<span style='color:#00CC66'>”:</span> We controlled for participants' expectations in our study. |                                                              |
    | Question mark or exclamation point (<span style='color:#00CC66'>**NOT** part of quoted material</span>) | Outside                                              | How will this study impact participants who stated at the outset<span style='color:#00CC66'>, “</span>I never remember my dreams<span style='color:#00CC66'>”?</span> We hypothesized their dream recall would increase. |                                                              |

     Table source: <https://blog.apastyle.org/apastyle/2011/08/punctuating-around-quotation-marks.html>

- Within double quotation marks, convert double quotation marks to single quotation marks: She told me, "It seems like everyone is always looking down at their phones, but, as Plato said, 'It is clear to everyone that astronomy at all events compels the soul to look upwards, and draws it from the things of this world to the other' (ca. 375 B.C.E./1908)." 
- Do not use quotation marks when:
  - Highlighting a key term or phrase for which a definition will be provided; instead, use italics: the principle of *reciprocity* can be defined as...
  - The meaning of a number is clear: Alex wears the number 13 jersey.
  - Note that <u>after the first time</u> you define a key term, you will format it normally.



**Useful resources**:

1. <https://www.e-education.psu.edu/styleforstudents/c1_p9.html>



### Footnotes

The most common sequence of footnote reference marks is: 1. asterisk (*), 2. dagger (†, `\dagger`), 3. double dagger (††), 4. paragraph symbol (¶), 5. section mark (§), 6. parallel rules (\|\|), 7. number sign (#).   
If more are required, they can be doubled up: double asterisks (**), double single daggers (††, `\dagger\dagger`), double double daggers (††††), etc. However, when many footnotes are used, it is more practical to use consecutive numbers to identify each footnote.



This is a sentence with a footnote.<sup>[1]</sup>

<sup>[1]</sup>Supplementary information about the sentence.



Note that

- the superscript number <sup>[1]</sup> follows the sentence in the text directly, with <u>no space</u> before a footnote callout. 
- should be placed after any punctuation, except an end parenthesis if the footnote pertains specifically to the text inside the parentheses  
- Depending on the referencing methods – APA, MLA, Oxford, Chicago, etc, there are different styles for the footnotes:
  - Turabian Style (or Chicago Style): Leave <u>no space</u> between the superscript (footnote number) and the first word in the footnote.
  - APA 7: put a space between the footnote number and the footnote itself.




___

## Styles

The following chart shows some of the major differences in punctuation style between The Associated Press Stylebook (2018 edition) and The Chicago Manual of Style (17th edition).

|                                                    | [The Chicago Manual of Style](https://www.chicagomanualofstyle.org/home.html) | The Associated Press Stylebook                               |
| -------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Serial comma**                                   | Include a comma before the conjunction.   <br />My favorite composers are Beethoven, Brahms, Mahler<span style='color:#00CC66'>, and</span> Mozart. | Do not include a comma before the conjunction.   <br />My favorite composers are Beethoven, Brahms, Mahler <span style='color:#00CC66'>and</span> Mozart. |
| **Spacing between initials in name**               | Include a space between initials.   <br />E. L. Doctorow     | Do not include a space between initials.   <br />E.L. Doctorow |
| **Abbreviations**                                  | Preference against periods.   <br />JD, BA, PhD, BCE (referring to the era), PO Box, US, UN | Preference for periods.   <br />J.D., B.A., Ph.D., B.C.E., P.O. Box, U.S., U.N. |
| Possessives of singular proper nouns ending in *s* | Add an apostrophe and *s*.   <br />Texas’s, James’s, Xerxes’s | Add only an apostrophe.   <br />Texas’, James’, Xerxes’      |



___

#### Abbreviations

If an organisation's name is long and you will use it multiple times (more than 3 times), you can use an abbreviation in your citations.

The general tips for abbreviation are: 

- **If the term will be used three times or fewer, do not abbreviate**. However, you may use a recognisable abbreviation if it appears fewer than three times and helps avoid cumbersome language.
- **Do not define abbreviations in headings**. Use abbreviations in headings **only** if they have been previously defined.
- **Use the abbreviation consistently**. Do not alternate between the abbreviation and the full term.
- **Make abbreviations plural by adding "s"** (e.g., hours = hrs); do not use an apostrophe.
- **Do not use periods** with abbreviations (e.g., NASA, not N.A.S.A).



**Latin Abbreviations**

Many Latin abbreviations are used in APA Style papers to save space. Use the following standard Latin abbreviations <u>only in parenthetical material</u>; in the narrative, use the translation of the Latin term. In both cases, punctuate as if the abbreviation were spelled out in the language in which you are writing.

| Latin abbreviation | Meaning                                                      |
| :----------------- | :----------------------------------------------------------- |
| cf.                | *compare*, used to indicate that the cited source supports a different claim (propoition) than the one just made |
| e.g.,              | for example,                                                 |
| , etc.             | , and so forth                                               |
| i.e.,              | that is,                                                     |
| viz.,              | namely,                                                      |
| vs.                | versus or against                                            |

-  if you want to give a [list of examples within parentheses](https://apastyle.apa.org/style-grammar-guidelines/lists), use the abbreviation “e.g.,” (including the comma) before the examples. If the words “for example” appear outside of parentheses, do not use the abbreviation “e.g.”

  > Participants watched different kinds of funny movies (e.g., featuring either slapstick, self-deprecating, or dark humor).

- Use the Latin abbreviation “et al.” (which means “and others”) in both [narrative and parenthetical citations](https://apastyle.apa.org/style-grammar-guidelines/citations).





## References

Citing sources in [APA style](https://apastyle.apa.org) 7th ed.

<https://libraryguides.vu.edu.au/apa-referencing/7Books>

<https://www.scribbr.com/apa-examples/book/>

All types of reference materials: <https://libguides.murdoch.edu.au/APA/all>

APA style: refer to "Publication Manual of the American Psychological Association".

Citations vs. References

- Traditionally the term "citation" is used to refer to an in-text source, 

- while "reference" is the correct term for a source listed on the reference page of a paper.

**Styling**

- The first line of each citation is left adjusted. Every subsequent line is indented 5-7 spaces.



**Parenthetical vs Narrative citations**

|                   | Parenthetical citation       | Narrative citation          |
| :---------------- | :--------------------------- | :-------------------------- |
| 1 author          | (Smith, 2007)                | Smith (2007)                |
| 2 authors         | (Mihrshahi & Baur, 2018)     | Mihrshahi and Baur (2018)   |
| 3 or more authors | (Hewit et al., 2016)         | Hewit et al. (2016)         |
| Group author      | (Department of Health, 2020) | Department of Health (2020) |

Table source: <https://ecu.au.libguides.com/referencing/in-text-citations>

- If the work you are citing has **one or two authors**, include them in your citation every time. Separate two authors with an ampersand (&) in parenthetical citations, but write out the word 'and' if discussing the work in-text.
- If the work has **3 or more authors**, your in-text citation will give only the family name of the first author, followed by "et al." (which means "and others").



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



###  ISBN and DOI

What is an ISBN and a DOI?

- An International Standard Book Number (ISBN) identifies a book by format (print, audio etc.), edition and publisher.
  - It is a 13 (after 1 January 2007) or 10 (before 2007) digits number assigned to all books and book-like publications that are published internationally.
  - The purpose of the ISBN is to establish and identify one title or edition of a title from one specific publisher and is unique to that edition, allowing for more efficient marketing of products by booksellers, libraries, universities, wholesalers and distributors.

- A Digital Object Identifier (DOI) is as persistent and stable as an ISBN. The advantage of using a DOI in the online environment is that it can be expressed in resolvable format, (e.g. http://doi.org/10.4225/35/5715bcdd2df24) so that there is always a link back to the online location of the item.

It is not necessary for an ISBN and DOI to be issued for the same publication unless it will be distributed in both print and electronic formats.



## Prepare for submission 

- Include page numbers and continuous line numbers in the manuscript file.

  Line numbers DO NOT begin with "1" on each page. 

  Reviewers might refer to line numbers.

- Font size: 12 pt



___

**Useful Resources**:

Phrasebank: <https://www.phrasebank.manchester.ac.uk/giving-examples/>





