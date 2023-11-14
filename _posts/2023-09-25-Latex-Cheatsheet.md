---
layout: post
title: LaTex Cheatsheet
tag: study
---

Special characters / Symbols
============================
### Latin:
##### No dot:  
`\imath` $\rightarrow$ $\imath$,
`\jmath` $\rightarrow$ $\jmath$

##### Hat:  
`\hat{\imath}`  $\rightarrow$ $\hat{\imath}$,
`\hat{\jmath}`  $\rightarrow$ $\hat{\jmath}$

### Vectors:

`\vec`: $\vec{A}$

`\overrightarrow`: $\overrightarrow{AB}$



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





### Greek Letters:

##### Capital:

|      LaTex |      |    LaTex |      |
| ---------: | ---: | -------: | ---: |
|   `\Gamma` |    Γ | `\Delta` |    ∆ |
|  `\Lambda` |    Λ |   `\Phi` |    Φ |
|      `\Pi` |    Π |   `\Psi` |    Ψ |
|   `\Sigma` |    Σ | `\Theta` |    Θ |
| `\Upsilon` |    Υ |    `\Xi` |    Ξ |
|   `\Omega` |    Ω |          |      |

##### Lowercase:

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

##### Other:

|       LaTex |             |        LaTex |         |
| ----------: | ----------- | -----------: | ------: |
|  `\digamma` | ϝ           | `varepsilon` |       ε |
| `\varkappa` | ϰ           |    `\varphi` |       ϕ |
|    `\varpi` | $\varpi$    |    `\varrho` |       ϱ |
| `\varsigma` | $\varsigma$ |  `\vartheta` |       ϑ |
|      `\eth` | ð           |      `\hbar` | $\hbar$ |

### Other:
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



When creating TeX, Knuth provided the symbol $\blacksquare$ (black square, `\blacksquare`), also called by mathematicians tombstone or Halmos symbol (after Paul Halmos, who pioneered its use). 

The tombstone is sometimes open: $\square$ (white square, `\square`).

HTML and XML provide ways to reference Unicode characters when the characters themselves either cannot or should not be used.

Unicode characters for geometric shapes: <http://www.unicode.org/charts/nameslist/n_25A0.html>

A numeric character reference uses the format`&#nnnn;` or `&#xhhhh;`. `nnnn` is in decimal form, `hhhh` is in hexadecimal form. The `&` and `;` are required.



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

|    LaTex |              |  LaTex |        |
| -------: | ------------ | -----: | -----: |
| `\wedge` | ∧ (and)      | `\vee` | ∨ (or) |
|   `\neg` | $\neg$ (not) |        |        |
|   `\ast` | $\ast$       |        |        |





#### Relational Symbols

|          LaTex |                |       LaTex |             |
| -------------: | -------------- | ----------: | ----------: |
|         `\geq` | ≥              |      `\leq` |           ≤ |
|       `\equiv` | ≡              |      `\sim` |           ∼ |
|          `\gg` | ≫              |       `\ll` |           ≪ |
|         `\mid` | $\mid$         |   `\propto` |           ∝ |
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

- $\overset{\text{aprrox}}{\sim}$ (`\overset{\text{aprrox}}{\sim}`) for approximately distributed with.



#### Arrows

|             LaTex |            |             LaTex |              |
| ----------------: | ---------- | ----------------: | -----------: |
| `\hookrightarrow` | ↪          |     `\Rightarrow` |            ⇒ |
|     `\rightarrow` | →          | `\Leftrightarrow` |            ⇔ |
|    `\nrightarrow` | ↛          |         `\mapsto` |    $\mapsto$ |
|        `\nearrow` | $\nearrow$ |        `\searrow` |   $\searrow$ |
|        `\uparrow` | $\uparrow$ |      `\downarrow` | $\downarrow$ |

- $\rightarrow$ denotes a mapping between two sets. 两边都是集合。

  $\mapsto$ called mapsto,  tells you what it does to each element of the set. 两边是数值的一个transform。

  For example, I can define a function $𝑓:\mathbb{R}\rightarrow\mathbb{R}$ by $𝑓(𝑥):=2𝑥$. Notice that the $\rightarrow$ is between the two real number sets. But, I can also express that $𝑓(3)=6$ by $3\mapsto 6$. More generally, $𝑓(𝑥):=2𝑥$ can be written as $𝑥 \mapsto 2𝑥$.

- Text above or under symbols or other text, e.g., $\sim$ 

  - `\overset{#1}{#2}` put argument #1 (in scriptstyle) over argument #2. E.g., $\overset{\text{a}}{\sim}$ `\overset{\text{a}}{\sim}` or `\overset{\rm a}{\sim}`. `\rm` for Roman font. A side note: Words in subscripts or superscripts should be upright.

  - `\underset{#1}{#2}` put argument #1 (in scriptstyle) under argument #2. $\widetilde{\beta}_{k}^{\rm ridge}=\underset{b\in \mathbb{R}^{p+1}}{\rm argmin}  \lVert y-X b  \rVert ^{2}$. 

- Text above arrows. $\xrightarrow{D}$ `\xrightarrow{D}` convergence in distribution.



#### Cumulative operators

|     LaTex |           |       LaTex |             |
| --------: | --------- | ----------: | ----------: |
|    `\int` | ∫         |     `\iint` |     $\iint$ |
|  `\iiint` | $\iiint$  | `\idotsint` | $\idotsint$ |
|   `\prod` | $\prod$   |      `\sum` |      $\sum$ |
| `\bigcup` | $\bigcup$ |   `\bigcap` |   $\bigcap$ |

Summation operators: $\displaystyle\sum_{i=1}^n$ (`\displaystyle\sum_{i=1}^n`) vs $\textstyle\sum_{i=1}^n$ (`\textstyle\sum_{i=1}^n`).

 `\lim_{n\to\infty}` for inline limits: $\lim_{n\to\infty}$

 `\displaystyle\lim_{n\to\infty}` for display limits: $\displaystyle\lim_{n\to\infty}$

`$X_n \xrightarrow{p} c$` convergence in probability: $X_n \xrightarrow{p} c$



**Ellipsis**

- `\ldots` are used between commas, e.g., $a_1, \ldots, a_n$ ;

  `\cdots` used between plus/minus signs, e.g., $a_1+ \cdots + a_n$ ;



#### Named operators

$\arccos$,
$\arcsin$,
$\arctan$,
$\arg$,
$\cos$,
$\cosh$,
$\cot$,
$\coth$,
$\deg$,
$\det$,
$\dim$,
$\exp$,
$\gcd$,
$\hom$,
$\inf$,
$\injlim$,
$\lg$,
$\lim$,
$\liminf$,
$\limsup$,
$\ln$,
$\log$,
$\max$,
$\min$,
$\Pr$,
$\projlim$,
$\sec$,
$\sin$,
$\sinh$,
$\sup$



**Note**:

- `\right .` creates an "invisible" delimiter that is used to match a corresponding `\left`, e.g., in multi-case function definition, you only need one left brace, then you use `\right .` to indicate the end of the function.

- In `markdown`, you can define your own commands by putting the following codes at the beginning of the file.

  ```markdown
  $$
  \newcommand{\indep}{\perp \!\!\! \perp}
  $$
  ```

  







# Reference

@LKS90, Github Repository, <https://gist.github.com/LKS90/252ac41bd4a173be35b0>.

























