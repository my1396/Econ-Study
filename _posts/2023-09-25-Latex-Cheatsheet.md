---
layout: post
title: LaTex Cheatsheet
tag: study
---


<a class="top-link hide" href="#" id="js-top">↑</a>

### Special characters / Symbols

#### No dot
`\imath` $\rightarrow$ $\imath$,
`\jmath` $\rightarrow$ $\jmath$

#### Hat  
`\hat{\imath}`  $\rightarrow$ $\hat{\imath}$,
`\hat{\jmath}`  $\rightarrow$ $\hat{\jmath}$

### Vectors

`\vec`: $\vec{A}$

`\overrightarrow`: $\overrightarrow{AB}$

Sample average: $\overline{X}$ (`\overline{X}`, line is longer), $\bar{X}$ (`\bar{X}`, bar is shorter)

`\tilde{X}`: $\tilde{X}$

`\hat{\beta}`: $\hat{\beta}$



Sometimes, hat or bar symbols look too light. You might want a bolder version of them.

```latex
\newcommand{\thickhat}[1]{\mathbf{\hat{\text{$#1$}}}}
\newcommand{\thickbar}[1]{\mathbf{\bar{\text{$#1$}}}}
\newcommand{\thicktilde}[1]{\mathbf{\tilde{\text{$#1$}}}}
```

<img src="https://drive.google.com/thumbnail?id=1vB4OiKSNhAngU57BkMlfxzH54NF-7g9x&sz=w1000" alt="thick_symbol" style="display: block; margin-right: auto; margin-left: auto; zoom:50%;" />



### Matrices

| Type                        | LATEX markup                                       | Renders as                                         |
| :-------------------------- | :------------------------------------------------- | :------------------------------------------------- |
| Plain                       | `\begin{matrix}1 & 2 & 3\\ a & b & c\end{matrix}`   | $$\begin{matrix}1 & 2 & 3\\ a & b & c\end{matrix}$$   |
| Parentheses; round brackets | `\begin{pmatrix}1 & 2 & 3\\ a & b & c\end{pmatrix}` | $$\begin{pmatrix}1 & 2 & 3\\ a & b & c\end{pmatrix}$$ |
| Brackets; square brackets   | `\begin{bmatrix}1 & 2 & 3\\ a & b & c\end{bmatrix}` | $$\begin{bmatrix}1 & 2 & 3\\ a & b & c\end{bmatrix}$$ |
| Braces; curly brackets      | `\begin{Bmatrix}1 & 2 & 3\\ a & b & c\end{Bmatrix}` | $$\begin{Bmatrix}1 & 2 & 3\\ a & b & c\end{Bmatrix}$$ |
| Pipes                       | `\begin{vmatrix}1 & 2 & 3\\ a & b & c\end{vmatrix}` | $$\begin{vmatrix}1 & 2 & 3\\ a & b & c\end{vmatrix}$$ |
| Double pipes                | `\begin{Vmatrix}1 & 2 & 3\\ a & b & c\end{Vmatrix}` | $$\begin{Vmatrix}1 & 2 & 3\\ a & b & c\end{Vmatrix}$$ |

Note: 

- `\\` for row break, `&` for column separation.
  - sometimes `\\` doesn't work in cloumn vectors, use `\cr` instead.





### Greek Letters

#### Capital

|      LaTex |      |    LaTex |      |
| ---------: | ---: | -------: | ---: |
|   `\Gamma` |    Γ | `\Delta` |    ∆ |
|  `\Lambda` |    Λ |   `\Phi` |    Φ |
|      `\Pi` |    Π |   `\Psi` |    Ψ |
|   `\Sigma` |    Σ | `\Theta` |    Θ |
| `\Upsilon` |    Υ |    `\Xi` |    Ξ |
|   `\Omega` |    Ω |          |      |

#### Lowercase

|      LaTex |      |     LaTex |      |
| ---------: | ---: | --------: | ---: |
|   `\alpha` |    α |     `\nu` |    ν |
|    `\beta` |    β |  `\kappa` |    κ |
|   `\gamma` |    γ | `\lambda` |    λ |
|   `\delta` |    δ |     `\mu` |    µ |
| `\epsilon` |    ϵ |   `\zeta` |    ζ |
|     `\eta` |    η |  `\theta` |    θ |
|    `\iota` |    ι |     `\xi` |    ξ |
|      `\pi` |    π |    `\rho` |    ρ |
|   `\sigma` |    σ |    `\tau` |    τ |
| `\upsilon` |    υ |    `\phi` |    φ |
|     `\chi` |    χ |    `\psi` |    ψ |
|   `\omega` |    ω |           |      |

#### Other

|       LaTex |             |        LaTex |         |
| ----------: | ----------- | -----------: | ------: |
|  `\digamma` | ϝ           | `varepsilon` |       ε |
| `\varkappa` | ϰ           |    `\varphi` |       ϕ |
|    `\varpi` | $\varpi$    |    `\varrho` |       ϱ |
| `\varsigma` | $\varsigma$ |  `\vartheta` |       ϑ |
|      `\eth` | ð           |      `\hbar` | $\hbar$ |

### Other

#### Other Symbols

|         LaTex |      |            LaTex |      |
| ------------: | ---- | ---------------: | ---: |
|    `\partial` | ∂    |         `\infty` |    ∞ |
|      `\wedge` | ∧    |           `\vee` |    ∨ |
| `\neg` `\not` | ¬    |                  |      |
|        `\bot` | ⊥    |           `\top` |    ⊤ |
|      `\nabla` | ∇    |    `\varnothing` |    ∅ |
|      `\angle` | ∠    | `\measuredangle` |    ∡ |
|       `\surd` | √    |        `\forall` |    ∀ |

**QED**

When creating TeX, Knuth provided the symbol $\blacksquare$ (black square, `\blacksquare`), also called by mathematicians tombstone or Halmos symbol (after Paul Halmos, who pioneered its use). 

The tombstone is sometimes open: $\square$ (white square, `\square`) or $\Box$ (`\Box`).

HTML and XML provide ways to reference Unicode characters when the characters themselves either cannot or should not be used.

Unicode characters for geometric shapes: <http://www.unicode.org/charts/nameslist/n_25A0.html>

A numeric character reference uses the format`&#nnnn;` or `&#xhhhh;`. `nnnn` is in decimal form, `hhhh` is in hexadecimal form. The `&#` and `;` are required.



#### Sets

|     LaTex |           |         LaTex |               |
| --------: | --------- | ------------: | ------------: |
|    `\cap` | $\cap$    |        `\cup` |        $\cup$ |
| `\subset` | ⊂         |   `\subseteq` |             ⊆ |
|     `\in` | ∈         |      `\notin` |             ∉ |
| `\exists` | $\exists$ | `\not\exists` | $\not\exists$ |
| `\forall` | $\forall$ |               |               |

- use `\not` before an operator to negate it. 





#### Binary operators

|    LaTex |              |    LaTex |          |
| -------: | ------------ | -------: | -------: |
| `\wedge` | ∧ (and)      |   `\vee` |   ∨ (or) |
|   `\neg` | $\neg$ (not) |   `\div` |   $\div$ |
|   `\ast` | $\ast$       | `\times` | $\times$ |





#### Relational Symbols

|          LaTex |                |       LaTex |             |
| -------------: | -------------- | ----------: | ----------: |
|         `\geq` | ≥              |      `\leq` |           ≤ |
|       `\equiv` | ≡              |      `\sim` |      $\sim$ |
|          `\gg` | ≫              |       `\ll` |       $\ll$ |
|         `\mid` | $\mid$         |   `\propto` |   $\propto$ |
|        `\perp` | ⊥              | `\parallel` | $\parallel$ |
| `\vartriangle` | $\vartriangle$ |  `\leadsto` |  $\leadsto$ |
|   `\triangleq` | $\triangleq$   |   `\approx` |   $\approx$ |

**Note:** 

- use `\vert` or `\mid` ($\vert$) to show a pipe operator, otherwise markdown recognizes it as a table column.

  - `\lVert` and `\rVert` ($\rVert$) used to take the norm of a vector;

  - `\lvert` and `\vert` ($\lvert$) used to take absolute value of real numbers and modulus of complex numbers;

  - `\mid` is often used as delimitor, $\{a\in S \mid \text{\(a=0\) or \(a\) is odd}\}$; $\mid$ in set theory means "such that", to introduce properties of the set; in probability, meaning conditional on;

  - `\mid` is also used to divide numbers. $4 \mid 12=3$, meaning $\text{\(4\) divides \(12\)}$. $a \mid b$ meaning $b$ is completely divisible by $a$. E.g., 

    $$
    \{𝑥\in \mathbb{Z}\mid 4\mid𝑥\}
    $$

    which describes the set of integers which 4 divides, namely $\{0,\pm4,\pm8,\pm12,…\}$. Some people prefer to use a colon there

    $$
    \{𝑥\in \mathbb{Z}: 4\mid 𝑥 \}.
    $$

- `\perp` ($\perp$) indicates zero correlation; `\indep` ($\indep$) indicates independece.

- $\triangleq$  and `:=` used to define a variable using the RHS.

  $\equiv$ (`\equiv`) is used to denote shorthand. There is no logical or physical content here; two expressions which are separated by $\equiv$ have exactly the same meaning, but are written a different way.

- $\sim$      means 

  - "sampled from" or "has the distribution of",

  - "of the order of", "approximately equal to",

  - "proportional to".  

- $\propto$ (`\propto`)  means proportional to.

- $\overset{\text{aprrox}}{\sim}$ (`\overset{\text{aprrox}}{\sim}`) for approximately distributed with.

  $\;\;\overset{\text{a}}{\sim}\;\;$ (`\overset{\text{a}}{\sim}`) indicates that the distributional relation is asymptotic.

  $\;\;\overset{\text{a}}{=}\;\;$ (`\overset{\text{a}}{=}`) indicates that the equality holds asymptotically.

  



#### Arrows

|             LaTex |            |             LaTex |              |
| ----------------: | ---------- | ----------------: | -----------: |
| `\hookrightarrow` | ↪          |     `\Rightarrow` |            ⇒ |
|     `\rightarrow` | →          | `\Leftrightarrow` |            ⇔ |
|    `\nrightarrow` | ↛          |         `\mapsto` |    $\mapsto$ |
|        `\nearrow` | $\nearrow$ |        `\searrow` |   $\searrow$ |
|        `\uparrow` | $\uparrow$ |      `\downarrow` | $\downarrow$ |

- $\rightarrow$ denotes a mapping between two sets. 两边都是集合。

  $\mapsto$ called *mapsto*,  tells you what it does to each element of the set. 两边是数值的一个transform。

  For example, I can define a function $𝑓:\mathbb{R}\rightarrow\mathbb{R}$ by $𝑓(𝑥):=2𝑥$. Notice that the $\rightarrow$ is between the two real number sets. But, I can also express that $𝑓(3)=6$ by $3\mapsto 6$. More generally, $𝑓(𝑥):=2𝑥$ can be written as $𝑥 \mapsto 2𝑥$.

- Text above or under symbols or other text, e.g., $\sim$ 

  - `\overset{#1}{#2}` put argument #1 (in script style) over argument #2. E.g., $\overset{\text{a}}{\sim}$ `\overset{\text{a}}{\sim}` or `\overset{\rm a}{\sim}`. `\rm` for Roman font (upright). A side note: Words in subscripts or superscripts should be upright.

  - `\underset{#1}{#2}` put argument #1 (in script style) under argument #2. $\widetilde{\beta}_{k}^{\rm ridge}=\underset{b\in \mathbb{R}^{p+1}}{\rm argmin}  \lVert y-X b  \rVert ^{2}$. 

- Text above arrows. $\xrightarrow{d}$ `\xrightarrow{d}` convergence in distribution.



#### Cumulative operators

|     LaTex |           |       LaTex |             |
| --------: | --------- | ----------: | ----------: |
|    `\int` | ∫         |     `\iint` |     $\iint$ |
|  `\iiint` | $\iiint$  | `\idotsint` | $\idotsint$ |
|   `\prod` | $\prod$   |      `\sum` |      $\sum$ |
| `\bigcup` | $\bigcup$ |   `\bigcap` |   $\bigcap$ |

Summation operators: $\displaystyle\sum_{i=1}^n$ (`\displaystyle\sum_{i=1}^n`) vs $\textstyle\sum_{i=1}^n$ (`\textstyle\sum_{i=1}^n`).

- `\displaystyle` apply the style used for mathematics typeset on lines by themselves.
- `\textstyle` apply the style used for mathematics typeset in paragraphs.

 `\lim_{n\to\infty}` for inline limits: $\lim_{n\to\infty}$

 `\displaystyle\lim_{n\to\infty}` for display limits: $\displaystyle\lim_{n\to\infty}$

`$X_n \xrightarrow{p} c$` convergence in probability: $X_n \xrightarrow{p} c$



Display shows eqns in block, text style shows inline.

- `\dfrac` used to show display style. $\dfrac{\partial f}{\partial x}$

- `\tfrac` used to show text style. $\tfrac{\partial f}{\partial x}$





**Ellipsis**

- `\ldots` are used between commas, e.g., $a_1, \ldots, a_n$ ;

  `\cdots` used between plus/minus signs, e.g., $a_1+ \cdots + a_n$ ;

**Interpunct** 

An interpunct `⟨·⟩`, also known as an interpoint, middle dot, middot, centered dot or centred dot, is a punctuation mark consisting of a vertically centered dot used for interword separation in Classical Latin. 

On mac, use `Shift+Opt+9` to type `·`





#### Named operators

$\arccos$, $\arcsin$, $\arctan$, $\cos$, $\cosh$, $\cot$, $\coth$, $\sec$, $\sin$, $\sinh$, 

$\deg$, $\det$, $\dim$, ${\color{#32CD32}\exp}$, $\gcd$, $\hom$, $\injlim$, $\projlim$, 

$\lim$, $\liminf$, $\limsup$, 

$\ln$ (natural logarithm), $\log$, $\lg$ (the logarithm to base 10), 

$\max$, $\min$, $\arg$,  $\Pr$, 

$\sup$, $\inf$



**Note**:

- `\right .` creates an "invisible" delimiter that is used to match a corresponding `\left`, e.g., in multi-case function definition, you only need one left brace, then you use `\right .` to indicate the end of the function.

- In `markdown`, you can define your own commands by putting the following codes at the beginning of the file.

  ```markdown
  $$
  \newcommand{\indep}{\perp \!\!\! \perp}
  $$
  ```

- Curly braces in eqns need to be escaped. `\{ ... \}` or `\\{ ... \\}` (the slash needs to be escaped itself).  E.g., 

  - $\exp \\{ \ldots \\}$ (`\exp \\{ \ldots \\}`)
  - $\exp \\{-\frac{1}{2}\left(\frac{x-\mu}{\sigma^2}\right)^2 \\}$ (`\exp \\{-\frac{1}{2}\left(\frac{x-\mu}{\sigma^2}\right)^2 \\}`)
  - If still encounter problems, use `\lbrace` and `\rbrace`: $\exp \lbrace \ldots \rbrace$ (`\exp \lbrace \ldots \rbrace`) and $\lbrace Z_t \rbrace_{t=0}^T$ (`\lbrace Z_t \rbrace_{t=0}^T`). This is the **safest** way.

- Add whitespace between equations, use `\quad`, `\qquad`, and `\hspace{20pt}` for long space; and  `\;` for short space.

- $\min_{\forall s \in S_j} q_k(s)$ (`\min_{\forall s \in S_j} q_k(s)`) text under min/max.







**Colored math symbols**

`${\color{#32CD32}\exp}$` ${\color{#32CD32}\exp}$ Need to quote the part you want to color in curly braces; otherwise, everything behind will change color too.



#### Escaped/Reserved Characters

The reserved characters have, in addition to the pure representation of the character, an additional function. Therefore, they cannot be used simply because it is generally assumed first that the function and not the character is meant. 

<https://www.sascha-frank.com/reserved_characters.html>

| \    | masks special characters and initiates commands.    |
| ---- | --------------------------------------------------- |
| { }  | Contains arguments, creates text blocks             |
| %    | Comment character: The rest of the line is ignored. |
| ^    | Exponent in math mode                               |
| _    | Index in math mode                                  |
| &    | depending on context - Tabulator                    |
| #    | Parameters                                          |
| ~    | Protected space.                                    |
| [,]  | Square brackets                                     |
| <,>  | Lace braces                                         |
| "    | Quotation marks                                     |



### Reference

@LKS90, Github Repository, <https://gist.github.com/LKS90/252ac41bd4a173be35b0>.
