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
| Plain                       | `\begin{matrix}1 & 2 & 3\\a & b & c\end{matrix}`   | $\begin{matrix}1 & 2 & 3\\a & b & c\end{matrix}$   |
| Parentheses; round brackets | `\begin{pmatrix}1 & 2 & 3\\a & b & c\end{pmatrix}` | $\begin{pmatrix}1 & 2 & 3\\a & b & c\end{pmatrix}$ |
| Brackets; square brackets   | `\begin{bmatrix}1 & 2 & 3\\a & b & c\end{bmatrix}` | $\begin{bmatrix}1 & 2 & 3\\a & b & c\end{bmatrix}$ |
| Braces; curly brackets      | `\begin{Bmatrix}1 & 2 & 3\\a & b & c\end{Bmatrix}` | $\begin{Bmatrix}1 & 2 & 3\\a & b & c\end{Bmatrix}$ |
| Pipes                       | `\begin{vmatrix}1 & 2 & 3\\a & b & c\end{vmatrix}` | $\begin{vmatrix}1 & 2 & 3\\a & b & c\end{vmatrix}$ |
| Double pipes                | `\begin{Vmatrix}1 & 2 & 3\\a & b & c\end{Vmatrix}` | $\begin{Vmatrix}1 & 2 & 3\\a & b & c\end{Vmatrix}$ |

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
|     `\exists` | ∃    |       `\nexists` |    ∄ |

#### Sets

|     LaTex |        |       LaTex |        |
| --------: | ------ | ----------: | -----: |
|    `\cap` | $\cap$ |      `\cup` | $\cup$ |
| `\subset` | ⊂      | `\subseteq` |      ⊆ |
|     `\in` | ∈      |    `\notin` |      ∉ |

#### Relational Symbols

|          LaTex |                |       LaTex |             |
| -------------: | -------------- | ----------: | ----------: |
|         `\geq` | ≥              |      `\leq` |           ≤ |
|       `\equiv` | ≡              |      `\sim` |           ∼ |
|          `\gg` | ≫              |       `\ll` |           ≪ |
|          `\in` | ∈              |    `\notin` |           ∉ |
|         `\mid` | $\mid$         |   `\propto` |           ∝ |
|        `\perp` | ⊥              | `\parallel` | $\parallel$ |
| `\vartriangle` | $\vartriangle$ |  `\leadsto` |  $\leadsto$ |
|   `\triangleq` | $\triangleq$   |             |             |

**Note:** 

- use `\vert` or `\mid` ($\vert$) to show a pipe operator, otherwise markdown recognizes it as a table column.
- `\perp` ($\perp$) indicates zero correlation; `\indep` ($\indep$) indicates independece.
- $\triangleq$  and `:=` used to define a variable using the RHS.



#### Arrows

|             LaTex |            |             LaTex |              |
| ----------------: | ---------- | ----------------: | -----------: |
| `\hookrightarrow` | ↪          |     `\Rightarrow` |            ⇒ |
|     `\rightarrow` | →          | `\Leftrightarrow` |            ⇔ |
|    `\nrightarrow` | ↛          |         `\mapsto` |    $\mapsto$ |
|        `\nearrow` | $\nearrow$ |        `\searrow` |   $\searrow$ |
|        `\uparrow` | $\uparrow$ |      `\downarrow` | $\downarrow$ |

$\rightarrow$ denotes a mapping between two sets. 两边都是集合。

$\mapsto$ called mapsto,  tells you what it does to each element of the set. 

For example, I can define a function $𝑓:\mathbb{R}\rightarrow\mathbb{R}$ by $𝑓(𝑥):=2𝑥$. Notice that the $\rightarrow$ is between the two real number sets. But, I can also express that $𝑓(3)=6$ by $3\mapsto 6$. More generally, $𝑓(𝑥):=2𝑥$ can be written as $𝑥 \mapsto 2𝑥$.



#### Binary operators

|        LaTex |         |  LaTex |        |
| -----------: | ------- | -----: | -----: |
|     `\wedge` | ∧ (and) | `\vee` | ∨ (or) |
| `\neg``\not` | ¬       |        |        |

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



#### 



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

























