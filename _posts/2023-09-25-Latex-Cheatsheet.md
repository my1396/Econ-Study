---
layout: post
title: LaTex Cheatsheet
tag: study
---


<a class="top-link hide" href="#" id="js-top">↑</a>

## Special Characters / Symbols

#### No dot
`\imath` $\rightarrow$ $\imath$,
`\jmath` $\rightarrow$ $\jmath$

#### Hat  
`\hat{\imath}`  $\rightarrow$ $\hat{\imath}$,
`\hat{\jmath}`  $\rightarrow$ $\hat{\jmath}$

Widehat `\widehat{\beta}` gives $\widehat{\beta}$ 

Ordinary hat `\hat{\beta}` gives $\hat{\beta}$.

`\textvisiblespace` gives `␣`. 空格占位符

`\S` (from basic LaTex) or `\textsection` (from `textcomp` package) gives  the section symbol §1 (`\S1`)



## Brackets and Braces

| LaTeX markup                                                | Renders as                                                  |
| ----------------------------------------------------------- | ----------------------------------------------------------- |
| `\bigl( \Bigl( \biggl( \Biggl(`                             | $\bigl( \Bigl( \biggl( \Biggl($                             |
| `\bigr] \Bigr] \biggr] \Biggr]`                             | $\bigr] \Bigr] \biggr] \Biggr]$                             |
| `\bigl\{ \Bigl\{ \biggl\{ \Biggl\{`                         | $$\bigl\{ \Bigl\{ \biggl\{ \Biggl\{$$                       |
| `\bigl \langle \Bigl \langle \biggl \langle \Biggl \langle` | $\bigl \langle \Bigl \langle \biggl \langle \Biggl \langle$ |
| `\bigr \rangle \Bigr \rangle \biggr \rangle \Biggr \rangle` | $\bigr \rangle \Bigr \rangle \biggr \rangle \Biggr \rangle$ |

- Parentheses (`(`) and brackets (`[`) don't need to be espcaped; need to escape curly braces (`{`).



## Vectors

`\vec{A}`: $\vec{A}$

`\overrightarrow{AB}`: $\overrightarrow{AB}$

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



## Matrices

| Type                                                         | LATEX markup                                        | Renders as                                            |
| :----------------------------------------------------------- | :-------------------------------------------------- | :---------------------------------------------------- |
| Plain                                                        | `\begin{matrix}1 & 2 & 3\\ a & b & c\end{matrix}`   | $$\begin{matrix}1 & 2 & 3\\ a & b & c\end{matrix}$$   |
| Parentheses; round brackets                                  | `\begin{pmatrix}1 & 2 & 3\\ a & b & c\end{pmatrix}` | $$\begin{pmatrix}1 & 2 & 3\\ a & b & c\end{pmatrix}$$ |
| <span style='color:#008B45'>Brackets</span>; square brackets | `\begin{bmatrix}1 & 2 & 3\\ a & b & c\end{bmatrix}` | $$\begin{bmatrix}1 & 2 & 3\\ a & b & c\end{bmatrix}$$ |
| Braces; curly brackets                                       | `\begin{Bmatrix}1 & 2 & 3\\ a & b & c\end{Bmatrix}` | $$\begin{Bmatrix}1 & 2 & 3\\ a & b & c\end{Bmatrix}$$ |
| Pipes                                                        | `\begin{vmatrix}1 & 2 & 3\\ a & b & c\end{vmatrix}` | $$\begin{vmatrix}1 & 2 & 3\\ a & b & c\end{vmatrix}$$ |
| Double pipes                                                 | `\begin{Vmatrix}1 & 2 & 3\\ a & b & c\end{Vmatrix}` | $$\begin{Vmatrix}1 & 2 & 3\\ a & b & c\end{Vmatrix}$$ |

Note: 

- <span style='color:#008B45'>`\\`</span> for <span style='color:#008B45'>row</span> break, <span style='color:#008B45'>`&`</span> for <span style='color:#008B45'>column</span> separation.
  - sometimes `\\` doesn't work in cloumn vectors, use `\cr` instead.





| Common symbols                                               | Matrices                                             |
| ------------------------------------------------------------ | ---------------------------------------------------- |
| $\boldsymbol{I}_n$ (`\boldsymbol{I}_n`)                      | $n\times n$ identity matrix                          |
| $\mathbb{1}_n$ (`\mathbb{1}` from `\usepackage{bbold}`)      | $n\times n$ identity matrix, double 1 representation |
| $\boldsymbol{1}_n$ or $\boldsymbol{i}_n$ (`\boldsymbol{1}_n` or `\boldsymbol{i}_n`) | $n\times 1$ vector of ones                           |
| $\mathbb{1}(a)$ (`\mathbb{1}(a)`) or $\boldsymbol{I}(a)$ (`\boldsymbol{I}(a)`) | Indicator function (1 if $a$ is true, else 0)        |



### Delimiters

| Term                |   LaTeX   | Symbol    |
| :------------------ | :-------: | --------- |
| Left angle          | `\langle` | $\langle$ |
| Right angle         | `\rangle` | $\rangle$ |
| Left bracket        | `\lbrack` | $\lbrack$ |
| Right bracket       | `\rbrack` | $\rbrack$ |
| Left brace          | `\lbrace` | $\lbrace$ |
| Right brace         | `\rbrace` | $\rbrace$ |
| Double vertical bar |   `\|`    | $\|$      |





## Greek Letters

#### Capital

|      LaTex |      |    LaTex |      |
| ---------: | --- | -------: | --- |
|   `\Gamma` | $\Gamma$ | `\Delta` | $\Delta$ |
|  `\Lambda` | $\Lambda$ |   `\Phi` | $\Phi$ |
|      `\Pi` | $\Pi$ |   `\Psi` | $\Psi$ |
|   `\Sigma` | $\Sigma$ | `\Theta` | $\Theta$ |
| `\Upsilon` | $\Upsilon$ |    `\Xi` | $\Xi$ |
|   `\Omega` | $\Omega$ |          |      |

#### Lowercase

|      LaTex |      |             LaTex |              |
| ---------: | --- | ----------------: | ----------- |
|   `\alpha` |    α |             `\nu` |            ν |
|    `\beta` |    β | `\kappa`, `\varkappa` | κ, $\varkappa$ |
|   `\gamma` |    γ |         `\lambda` |            λ |
|   `\delta` |    δ |             `\mu` |            µ |
| `\epsilon`, `\varepsilon` | ϵ, $\varepsilon$ |           `\zeta` |            ζ |
|     `\eta` |    η | `\theta`, `\vartheta` | θ, $\vartheta$ |
|    `\iota` |    ι |             `\xi` |            ξ |
| `\pi`, `\varpi` | π, $\varpi$ | `\rho`, `\varrho` | ρ, $\varrho$ |
| `\sigma`, `\varsigma` | σ, $\varsigma$ |            `\tau` |            τ |
| `\upsilon` |    υ | `\phi`, `\varphi` | φ, $\varphi$ |
|     `\chi` |    χ |            `\psi` |            ψ |
|   `\omega` |    ω |                   |              |

#### Other

|       LaTex |             |         LaTex |               |
| ----------: | ----------- | ------------: | ------------: |
|  `\digamma` | $\digamma$  | `\varepsilon` | $\varepsilon$ |
| `\varkappa` | $\varkappa$ |     `\varphi` |     $\varphi$ |
|    `\varpi` | $\varpi$    |     `\varrho` |     $\varrho$ |
| `\varsigma` | $\varsigma$ |   `\vartheta` |   $\vartheta$ |
|      `\eth` | $\eth$      |       `\hbar` |       $\hbar$ |



## Other Symbols

|                       LaTex |                                 |               LaTex |                     |
| --------------------------: | ------------------------------- | ------------------: | ------------------: |
|                  `\partial` | ∂                               | `\infty` (infinity) |                   ∞ |
| `\propto` (proportional to) | $\propto$                       |                     |                     |
|                    `\wedge` | ∧                               |              `\vee` |                   ∨ |
|               `\neg` `\not` | ¬                               |                     |                     |
|                      `\bot` | ⊥                               |              `\top` |                   ⊤ |
|                    `\nabla` | ∇                               |       `\varnothing` |                   ∅ |
|                    `\angle` | ∠                               |    `\measuredangle` |                   ∡ |
|                     `\surd` | √                               |           `\forall` |                   ∀ |
|           `\lceil{x}\rceil` | $\left \lceil{x}\right \rceil $ | `\lfloor x \rfloor` | $\lfloor x \rfloor$ |

- `'` prime symbol is a shorthand for `^\prime` .



**QED**

When creating TeX, Knuth provided the symbol $\blacksquare$ (black square, `\blacksquare`), also called by mathematicians tombstone or Halmos symbol (after Paul Halmos, who pioneered its use). 

The tombstone is sometimes open: $\square$ (white square, `\square`) or $\Box$ (`\Box`).

HTML and XML provide ways to reference Unicode characters when the characters themselves either cannot or should not be used.

Unicode characters for geometric shapes: <http://www.unicode.org/charts/nameslist/n_25A0.html>

A numeric character reference uses the format`&#nnnn;` or `&#xhhhh;`. `nnnn` is in decimal form, `hhhh` is in hexadecimal form. The `&#` and `;` are required.

Use `\tag*{\(\square\)}` to avoid QED showing on top of the equation.

```latex
$$
  \begin{align*}
    E\left[g(X)h(Y)\vert Y\right] &= \sum_x g(x) h(y) P(x|y) \\
    &= h(y) \sum_x g(x) P(x|y) \\
    &= h(y)\, \mathbb E[g(X)|Y=y] \tag*{\(\square\)}
  \end{align*} 
$$
```


$$
\begin{align*}
    E\left[g(X)h(Y)\vert Y\right] &= \sum_x g(x) h(y) P(x|y) \\
    &= h(y) \sum_x g(x) P(x|y) \\
    &= h(y)\, \mathbb E[g(X)|Y=y] \tag*{\(\square\)}
  \end{align*}
$$



### Sets

|        LaTex |              |                        LaTex |                            |
| -----------: | ------------ | ---------------------------: | -------------------------: |
|       `\cap` | $\cap$       |                       `\cup` |                     $\cup$ |
|    `\subset` | $\subset$    |                  `\subseteq` |                $\subseteq$ |
|    `\supset` | $\supset$    |                  `\supseteq` |                $\supseteq$ |
| `\subsetneq` | $\subsetneq$ |                 `\supsetneq` |               $\supsetneq$ |
|        `\in` | $\in$        |                     `\notin` |                   $\notin$ |
|    `\exists` | $\exists$    |                `\not\exists` |              $\not\exists$ |
|    `\forall` | $\forall$    | `\emptyset` or `\varnothing` | $\emptyset$, $\varnothing$ |
|  `\setminus` | $\setminus$  |                              |                            |

- use `\not` before an operator to negate it. 
- Union
  - $A \cup B$ (`A \cup B`)
  - $\bigcup_{i \in I} A_i$ (`\bigcup_{i \in I} A_i`)


- Set difference 
  - $A\setminus B$  (`\setminus`, good margins)
  - $A\backslash B$  (`\backslash`, narrow margins)
  - $A\mathbin{\backslash} B$  (`\mathbin{\backslash}`, good margins)



### Binary operators

|             LaTex |                                               |           LaTex |                     |
| ----------------: | --------------------------------------------- | --------------: | ------------------ |
| `\and` or `\land` | $\land$ (logical and)                         | `\or` or `\lor` | $\lor$ (logical or) |
| `\neg` or `\lnot` | $\neg$ (not)                                  |          `\div` |              $\div$ |
|            `\ast` | $\ast$                                        |        `\times` |            $\times$ |
|         `\otimes` | $\otimes$ (Kronecker product, tensor product) |                 |                     |





### Relational Symbols

|           LaTex |                 |             LaTex |                   |
| --------------: | --------------- | ----------------: | ---------------- |
|          `\geq` | ≥               |            `\leq` |                 ≤ |
|        `\equiv` | ≡               |            `\sim` |            $\sim$ |
|       `\approx` | $\approx$       | `\simeq` | $\simeq$ |
|           `\gg` | ≫               |             `\ll` |             $\ll$ |
|          `\mid` | $\mid$          |         `\propto` |         $\propto$ |
|         `\perp` | ⊥               |       `\parallel` |       $\parallel$ |
| `\Vert X \Vert` | $\Vert X \Vert$ | `\lVert X \rVert` | $\lVert X \rVert$ |
| `\leadsto` | $\leadsto$ |  |                   |
|    `\triangleq` | $\triangleq$    | `\vartriangle` | $\vartriangle$ |
| `\triangledown` | $\triangledown$ |          `\nabla` |          $\nabla$ |

**Note:** 

- use `\vert` or `\mid` ($\vert$) to show a pipe operator, otherwise <span style='color:#008B45'>Markdown recognizes it as a table column separator</span> in inline equations (block equations enclosed in `$$...$$` works fine though). 

  - `\lVert` and `\rVert` ($\rVert$) used to take the <span style='color:#008B45'>norm</span> of a vector;

  - `\lvert` and `\rvert` ($\lvert$) used to take <span style='color:#008B45'>absolute value</span> of real numbers and modulus of complex numbers;

    The issue with `\vert` is that it does not deal with the space around *binary operators* such as `+` and `-`. See examples as follows.

    | Poor                                | Good                                                   |
    | ----------------------------------- | ------------------------------------------------------ |
    | $\vert-x\vert$ (`$\vert-x\vert$`)   | $\lvert-x\rvert$ (`$\lvert-x\rvert $`, absolute value) |
    | $\vert a+\vert$ (`$\vert a+\vert$`) | $\lvert a+\rvert$  (`$\lvert a+\rvert$ `)              |
    | $\Vert+z\Vert$ (`$\Vert+z\Vert$`)   | $\lVert +z\rVert$ (`$\lVert +z\rVert$`, norm)          |
  
    
  
  - `\mid` is often used as delimitor, $\{a\in S \mid \text{\(a=0\) or \(a\) is odd}\}$; $\mid$ in set theory means "such that", to introduce properties of the set; in probability, meaning <span style='color:#008B45'>conditional on</span>;
  
  - `\mid` is also used to divide numbers. $4 \mid 12=3$, meaning $\text{\(4\) divides \(12\)}$. $a \mid b$ meaning $b$ is completely divisible by $a$. E.g., 
    $$
    \{𝑥\in \mathbb{Z}\mid 4\mid𝑥\}
    $$
    
    which describes the set of integers which 4 divides, namely $\{0,\pm4,\pm8,\pm12,…\}$. Some people prefer to use a colon there
    
    $$
    \{𝑥\in \mathbb{Z}: 4\mid 𝑥 \}.
    $$
  
  - `\mid` can be used in conditional probabilities. 
    $$
    p\text{-value} = P(Z\le z \mid H_0 \text{ is true}) = F(z)
    $$
    `\mid` creates **nicer margins** to the left and right compared to `\vert`.
    
    $\E[Y \mid X]$ (`$\E[Y \mid X]$`, whitespace around vertical bar) ✅
    
    vs. $\E[Y \vert X]$ ($\E[Y \vert X]$, more compact)
  
- `\perp` ($\perp$) indicates zero correlation; `\indep` ($\indep$) indicates independece.

- $\triangleq$  and `:=` used to define a variable using the RHS.

  $\equiv$ (`\equiv`) is used to denote shorthand. There is no logical or physical content here; two expressions which are separated by $\equiv$ have exactly the same meaning, but are written a different way.

- $\vartriangle$ is a math operator, standing for increment, should be up right;

  - $\Delta$ is a Greek letter, should be italic

- $\nabla$ commonly used to denote increments. 

  $$
  \nabla_1 h(x_1, \boldsymbol{x_2}, \boldsymbol{u}) = h(1,\boldsymbol{x_2}, \boldsymbol{u})-h(0,\boldsymbol{x_2}, \boldsymbol{u}) . 
  $$

- $\sim$      means 

  - "sampled from" or "has the distribution of",

  - "of the order of", "approximately equal to",

  - "proportional to".  

- $\propto$ (`\propto`)  means proportional to.

- $\overset{\text{aprrox}}{\sim}$ (`\overset{\text{aprrox}}{\sim}`) for approximately distributed with.

  $\;\;\overset{\text{a}}{\sim}\;\;$ (`\overset{\text{a}}{\sim}`) indicates that the distributional relation is asymptotic.

  $\;\;\overset{\text{a}}{=}\;\;$ (`\overset{\text{a}}{=}`) indicates that the equality holds asymptotically.

  



### Arrows

|             LaTex | Symbol        |             LaTex | Symbol            |
| ----------------: | ------------- | ----------------: | :---------------- |
| `\hookrightarrow` | ↪             |     `\rightarrow` | $\rightarrow$     |
|     `\Rightarrow` | $\Rightarrow$ | `\Leftrightarrow` | $\Leftrightarrow$ |
|        `\implies` | $\implies$    |            `\iff` | $\iff$            |
|    `\nrightarrow` | ↛             |         `\mapsto` | $\mapsto$         |
|        `\nearrow` | $\nearrow$    |        `\searrow` | $\searrow$        |
|        `\uparrow` | $\uparrow$    |      `\downarrow` | $\downarrow$      |

- $\rightarrow$ denotes a mapping between two sets. 两边都是集合。

  $\mapsto$ called *mapsto*,  tells you what it does to each element of the set. 两边是数值的一个transform。

  For example, I can define a function $𝑓:\mathbb{R}\rightarrow\mathbb{R}$ by $𝑓(𝑥):=2𝑥$. Notice that the $\rightarrow$ is between the two real number sets. But, I can also express that $𝑓(3)=6$ by $3\mapsto 6$. More generally, $𝑓(𝑥):=2𝑥$ can be written as $𝑥 \mapsto 2𝑥$.



- Text above arrows. $\xrightarrow{d}$ <span style='color:#008B45'>`\xrightarrow{d}`</span> convergence in distribution.

  If you want to use a longer arrow, you can use <span style='color:#008B45'>`\overset`</span>: $\overset{d}{\longrightarrow}$ (`\overset{d}{\longrightarrow}`).

- $n\to\infty$  (`n\to\infty`): as $n$ approximates to infinity.





### Cumulative operators

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





### Differtials

Display shows eqns in block, text style shows inline.

- `\dfrac` used to show *display* style. $\dfrac{\partial f}{\partial x}$

- `\tfrac` used to show *text* style. $\tfrac{\partial f}{\partial x}$



In terms of ordinary derivative, `d` should be upright as it is not a variable.

Use [`derivative` package](https://ftp.fagskolen.gjovik.no/pub/tex-archive/macros/latex/contrib/derivative/derivative.pdf) to format differtials.

```latex
\usepackage{derivative}


\begin{align*}
& \quad &\text{partial derivative: }  & \pdv{f}{x} \\
&  &\text{partial derivative: }  & \pdv{f}{x,y} \\
&  &\text{partial derivative with star (*): }  & \pdv*{f}{x,y} \\
& & \text{higher order derivative: } & \odv*{\odv[delims-frac=(), frac
]{y}{x}}{x} \\
& & \text{ordinary derivative: } & \odv{s}{t} \\
& & \text{higher order derivative: } & \odv[switch-*=false, order=n]{y}{x} \\
\end{align*}
```

<img src="https://drive.google.com/thumbnail?id=1RfGEewnk04yXfSkaUoB6ULN6vt0nQfrs&sz=w1000" alt="pdv and odv" style="zoom:40%;" />





**Ellipsis**

- `\ldots` are used between commas, e.g., $a_1, \ldots, a_n$ ;

  `\cdots` used between plus/minus signs, e.g., $a_1+ \cdots + a_n$ ;
  
  `\ddots` often used in matrices, e.g., 
  $$
  \boldsymbol{X} = \begin{pmatrix}
  x_1'\\
  x_2'\\
  \vdots \\
  x_n'\\ 
  \end{pmatrix}
  = \begin{pmatrix}
  x_{11} & x_{21} &  \cdots & x_{K1} \\
  x_{12} & x_{22} & \cdots & x_{K2} \\
  \vdots & \vdots & \ddots & \vdots \\
  x_{1n} & x_{2n} & \cdots & x_{Kn} 
  \end{pmatrix}_{n\times K}
  $$
  



**Interpunct** 

An interpunct `⟨·⟩`, also known as an interpoint, middle dot, middot, centered dot or centred dot, is a punctuation mark consisting of a vertically centered dot used for interword separation in Classical Latin. 

On mac, use `Shift+Opt+9` to type `·`





### Named operators

$\arccos$, $\arcsin$, $\arctan$, $\cos$, $\cosh$, $\cot$, $\coth$, $\sec$, $\sin$, $\sinh$, 

$\deg$, $\det$, $\dim$, ${\color{#008B45}\exp}$, $\gcd$, $\hom$, $\injlim$, $\projlim$, 

$\lim$, $\liminf$, $\limsup$, 

$\ln$ (natural logarithm), $\log$, $\lg$ (the logarithm to base 10), 

$\max$, $\min$, $\arg$,  $\Pr$, 

$\sup$, $\inf$



**Note**:

- `\right .` creates an "invisible" delimiter that is used to match a corresponding `\left`, e.g., in multi-case function definition, you only need one left brace, then you use `\right .` to indicate the end of the function.

  ```latex
  \left. \frac{\partial \by}{\partial \bx'} \right\vert_{\bx=\bmu}
  ```

  $$
  \left. \frac{\partial \by}{\partial \bx'} \right\vert_{\bx=\bmu}
  $$

- In `markdown`, you can define your own commands by putting the following codes at the beginning of the file.

  ```markdown
  $$
  \newcommand{\indep}{\perp \!\!\! \perp}
  $$
  ```

- Curly braces in eqns need to be escaped. `\{ ... \}` or `\\{ ... \\}` (the slash needs to be escaped itself).  E.g., 

  - $\exp \\{ \ldots \\}$ (`\exp \\{ \ldots \\}`)

  - $\exp \\{-\frac{1}{2}\left(\frac{x-\mu}{\sigma^2}\right)^2 \\}$ (`\exp \\{-\frac{1}{2}\left(\frac{x-\mu}{\sigma^2}\right)^2 \\}`)

  - If still encounter problems, use `\lbrace` and `\rbrace`: $\exp \lbrace \ldots \rbrace$ (`\exp \lbrace \ldots \rbrace`) and $\lbrace Z_t \rbrace_{t=0}^T$ (`\lbrace Z_t \rbrace_{t=0}^T`). This is the <span style='color:#008B45'>**safest**</span> way.

  - Use `\left\lbrace` and `\right\rbrace` if you want to scale the braces with the expression inside. This is called "dynamic delimiter sizing."

    You could also use `\left\{` and `\right\}`. 

    Here is a nice [guide](https://www.overleaf.com/learn/latex/Brackets_and_Parentheses).

- Text above or under symbols or other text, e.g., $\sim$ 

  - `\overset{#1}{#2}` put argument #1 (in script style) over argument #2. E.g., $\overset{\text{a}}{\sim}$ `\overset{\text{a}}{\sim}` or `\overset{\rm a}{\sim}`. `\rm` for Roman font (upright). A side note: Words in subscripts or superscripts should be upright.

  - `\underset{#1}{#2}` put argument #1 (in script style) under argument #2. E.g.,

    $$
    \begin{align*}
    \widetilde{\beta}_{k}^{\rm ridge} &= \underset{b\in \mathbb{R}^{p+1}}{\rm arg\, min}  \lVert y-X b  \rVert ^{2} \\
    \hat{\boldsymbol{\beta}} &= \underset{\boldsymbol{\beta}}{\arg\min} \sum_{i=1}^n \varepsilon_i^2
    \end{align*}
    $$
    
     `\underset{\boldsymbol{\beta}}{\arg\min}` gives you $\underset{\boldsymbol{\beta}}{\arg\min}$.

- Braces under/above eqs. Use `_` for under, and `^` for above.

  Text under eqs: `\underbrace{eqn}_\text{...under...}`

  $\underbrace{x+1}_\text{addition}$ (`\underbrace{x+1}_\text{addition}`)

  Text over eqs: `\overbrace{eqn}^\text{...over...}`

  $\overbrace{x+1}^\text{addition}$ (`\overbrace{x+1}^\text{addition}`)

- Square brakets: $E\lbrack x \rbrack$ (`E\lbrack x \rbrack`)

- Add whitespace between equations, use `\quad`, `\qquad`, and `\hspace{20pt}` for long space; and  `\;` for short space.

- $\min_{\forall s \in S_j} q_k(s)$ (`\min_{\forall s \in S_j} q_k(s)`) text under min/max.







**Colored math symbols**

`${\color{#008B45}\exp}$` ${\color{#008B45}\exp}$ Need to quote the part you want to color in curly braces; otherwise, everything behind will change color too.



### Escaped/Reserved Characters

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
