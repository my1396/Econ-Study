---
layout: post
title: Econometric Notes
tag: study
update: 2023-10-05
---

$$
\newcommand{\indep}{\perp \!\!\! \perp}
$$

<head>
    <style>
      /* Whatever that is inside this <style> tag is all styling for your markup / content structure.
      /* The . with the boxed represents that it is a class */
      /* this is only for proper styling in VS Code Preview */
      .boxed {
        background: #FFFAEE;
        color: black;
        border: 1px solid #535353;
        margin: 0px auto;
        width: 526px;
        padding: 10px;
        border-radius: 10px;
      }
    </style>
</head>


<a class="top-link hide" href="#" id="js-top">↑</a>


## Notation

$\mathbb{E}_Y$ and $\mathrm{Var}_Y$ denote expectation over $Y$ and variance over $Y$.

$\text{Pr}(.)$ and $\mathbb{P}(.)$ denote the probability of an event.

Blackboard bold 黑板粗体 (`\mathbb`) is often used to denote **sets of numbers**, e.g. $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{O}$, or a general field $\mathbb{F}$ or $\mathbb{K}$, and in probability to denote expectation of a random variable $\mathbb{E}(X)$ , written as `\mathbb{E}(X)`, or probability of an event $\mathbb{P}(E)$, written as `\mathbb{P}(E)`. 

Sometimes you see a sphere denoted $\mathbb{S}$ or a torus denoted $\mathbb{T}$. 

Mathematical calligraphic font or script letters 花体 (`\mathcal`), uppercase only, font for categories and sheaves.

-   $\mathcal L$（`\mathcal L`）常用来表示损失函数; log likelihood function;
-   $\mathcal D$（`\mathcal D`）表示样本集;
-   $\mathcal N$（`\mathcal N`）常用来表示高斯分布; normal distribution;
-   $\ell$（`\ell`）：用于和 $l$ 和 数字 1 相区分。

`:=` and $\triangleq$ are used to define a variable.

$\nabla:=\begin{pmatrix}\frac{\partial}{\partial x_1} \cr
\vdots \cr
\frac{\partial}{\partial x_n} \end{pmatrix}$, called "nabla symbol" or "nabla operator" (`\nabla`), commonly used in vector analysis and multivariate calculus.
E.g., Let $f(x_1, x_2)=x_1^3$, $\mathbb{R}^2 \rightarrow \mathbb{R}$, then the *gradient* of $f$ is $\nabla f(x_1, x_2) = 
\begin{pmatrix}\frac{\partial f}{\partial x_1} \cr
\frac{\partial f}{\partial x_2} 
\end{pmatrix} = 
\begin{pmatrix} 3x_1^2 \cr
0
\end{pmatrix}
$.

**Upper- and lower-case letters**

Vectors are lowercase and matrices are uppercase symbols. Both vectors and matrices are written in bold-italic. 

- Vectos $\boldsymbol a$, $\boldsymbol b, \boldsymbol c$  are produced by `\mathbfit a` or `\boldsymbol a`... ; vectors can also be denoted by Greek lowercase letters: $\boldsymbol{\alpha, \ldots \omega}$
- Matrices $\boldsymbol A, \boldsymbol B, \boldsymbol C$ by `\mathbfit A` or `\boldsymbol a` ... ; matrices can also be deonoted by Greek uppercase letters: $\boldsymbol{\Gamma, \ldots, \Theta}$
  - $A=[a_{i,j}]$ to show the components of matrix $\boldsymbol A$.
- Random variables are uppercase italic Latin letters $X, Y, X$. Lower case letters $x, y,z$ mean values of random variables. Sometimes, $X_i$ also denotes a value. If $X$ is a RV, then $X$ is written in words, and $x$ is given as a number.

  - Sample data use lowercase.
  - Population data use uppercase.

- Use Greek letters $\boldsymbol\theta, \boldsymbol\phi$ for parameters or $\alpha, \beta, \gamma$ for hyperparameters.
- Error terms are denoted by $\epsilon, \varepsilon, \eta, \xi, \zeta$.
- Variance-covariance matrices: $\boldsymbol{\Omega}, \boldsymbol{\Sigma}, \boldsymbol{V}, \boldsymbol{G}$.
- $\text{aVar}[.]$ denotes the asymptotic variance operator.

- $f(x) \approx g(x)$ (`\approx`) if the two functions are approximately equal in some sense depending on the context. 
- $f(x) \propto g(x)$ (`\propto`) If $f(x)$ is proportional to $g(x)$ we write. 
- $f(x) = O(g(x))$  We say that  “$f(x)$ is at most of order $g(x)$," if $\vert f(x)/g(x)\vert$ is bounded from above in some neighborhood of *x* = *c* (possibly *c* = ±∞). 
- $f(x) = o(g(x))$  we say that "$f(x)$ is of order less than $g(x)$," if $f(x)/g(x)$→ 0 when $x \rightarrow c$. 
- $f(x)\sim g(x)$ (`\sim`) if $f(x)/g(x) \rightarrow 1$ when $x \rightarrow c$. The two functions are then said to be "asymptotically equal". Notice that when $f(x)$ and $g(x)$ are asymptotically equal, then  $f(x)\approx g(x)$ and also $f(x) = O(g(x))$, but not vice versa.

Reference: <https://www.principlesofeconometrics.com/poe5/writing/abadir_magnus.pdf>



`crit pt`: critical point.

`cts`: continuous.

`def'n`: definition.

`cont'd`: continued.

`iff`: if and only if.

`Thm`: theorem.

`viz.`: namely, that is to say.

`Q.E.D`: Latin words to indicate this is the *end* of a mathematical proof. At the begining, you simply write `Proof:`.

Ceteris paribus:  Latin phrase that generally means "all other things being equal."

axiom or postulate: a fundamental assumption that is accepted without proof.

theorem: a statement that has been proven to be true based on axioms and other theorems.

preposition: a theorem of less importance, or one that is considered so elementary or immediately obvious, that it may be stated without proof.

lemma: an "accessory preposition" - a preposition with little applicability outside its use in a particular proof. Over time a lemma may gain in importance and be considered a *theorem*, though the term "lemma" is usually kept as part of its name.

corollary: is a theorem of less importance which can be readily deduced from a previous, more notable statement.  A corollary may also be a restatement of a theorem in a simpler form, or for a special case. 

罗马数字共有7个，即 Ⅰ (1)、Ⅴ(5)、Ⅹ(10)、Ⅼ(50)、Ⅽ(100)、Ⅾ(500)  和Ⅿ(1000)。

-   重复数次：一个罗马数字重复几次，就表示这个数的几倍。
-   从小到大，表示大数字减小数字。E.g. IV(4).
-   从大到小，表示大数字加小数字。E.g. VI(6).
-   常见罗马数字 **IV(4)**, V (5), Ⅵ (6), Ⅶ (7), ⅦI (8), **IX(9)**.

domain 定义域

range 值域

summand 被加数

reciprocal (multiplicative inverse) 倒数

normal vector 法向量

direction vector 方向向量

recursive substitution 迭代

counterexample 反例

$>$ **g**reater than, larger than 大于

$<$ **l**ess than, smaller than 小于

$\geq$ is greater than or equal to 大于等于

$\leq$ is greater than or equal to 小于等于

$\approx$ approximately equal to  约等于

inequality 不等式 (大于/小于)

Multiplying or dividing both sides by a positive number leaves the inequality symbol unchanged.

Multiplying or dividing both sides by a negative number **reverses**/ **flips** the inequality. This means $<$ changes to $>$, and vice versa.

**Sample and population**

- DGP (data generating process) generates the data that we observe.
- Any quantity, the calculation of which requires one to know the DGP, is a population quantity


*Degenerate* distribution: sometimes called a constant distribution, is a distribution of a degenerate random variable — a constant with probability of 1. \
In other words, a random variable $X$ has a single possible value. E.g., a weighted die (or one that has a number 6 on all faces) always lands on the number six, so the probability of a six is 1, i.e., $P_X(X=6)=1$.


*Average* ($\overline{X}$) usually denotes sample, *expected value* ($E[X]$) and *mean* ($\mu$) denote population.

## Geometry

**Quadrant** (plane geometry)

The axes of a two-dimensional Cartesian system divide the plane into four infinite regions, called quadrants, each bounded by two half-axes.

-   the numbering goes counter-clockwise starting from the upper right ("northeast") quadrant.

<img src="https://drive.google.com/thumbnail?id=1FlWhw7t0EIuk4PAV5-CTsLJGR0WZWGsl&sz=w1000" alt="quadrant geometry" style="display: block; margin-right: auto; margin-left: auto; zoom:50%;" />

orthographic projection (正射投影): top view, front view, (right) side view.

锐角 acute angel \
钝角 obtuse angel \
直角 right angel

complementary angel 互余角 $\alpha+\beta=\frac{\pi}{2}$.

supplementary angel 互补角 $\alpha+\beta=\pi$.

<img src="https://drive.google.com/thumbnail?id=1FlFGD-wVxC1UacQiLtg4W3NKAOcie-z7&sz=w1000" alt="triangel" style="display: block; margin-right: auto; margin-left: auto; zoom:60%;" />

斜边 hypotenuse  /haɪˈpɑːtənuːs/ \
邻边 adjacent side \
对边 opposite side

<span style='color:#32CD32'>Pythagoras’ /pəˈθægərəs/ or Pythagorean /pəˌθæɡəˈriən/ theorem</span> 勾股定理

**Law of Cosine**: tells the length of the 3rd side of a triangle if we know 2 sides and the angle between them.

$$
\begin{align*}c^2=a^2+b^2-2ab\cos\theta\end{align*}
$$


circumference /sərˈkʌmfərəns/ 周长

trapezoid 梯形 $A=\frac{(a+b)}{2}\cdot h$. (上底 + 下底) $\times$ 高/2.

parallelogram /ˌpærəˈleləɡræm / 平行四边形

parallelepiped /ˌpærəˌleləˈpaɪˌpɪd / 平行六面体 (倾斜长方体)

tetrahedron / ˌtetrəˈhiːdrən/ 四面体, also called "tiangular pyramid", 三角锥, is a polyhedron composed of four triangular faces.

polyhedron 多面体 \
cube 正方体 \
cuboid 长方体 

sector 扇形  \
已知弧长 $A=\frac{1}{2}l\cdot r$。 $l$ 为扇形弧长，$r$ 为半径。与三角形面积类比，$\frac{1}{2}$底$\times$高，半径可看作底，弧长看作高。

已知圆心角 $A=\frac{n}{360}\pi r^2=\frac{1}{2}\theta\cdot r^2$。$n$单位为度数degree， $\theta$ 为圆心角，单位为弧度radian。

-   度数弧度转换公式：$\frac{n}{180}\pi=\theta$。

-   弧长公式：$l=\theta \cdot r$ (圆心角弧度 $\times$ 半径)。

    圆周长 $C=2\pi r$，弧长 $l=\frac{\theta}{2\pi}\cdot C=\frac{\theta}{2\pi}\cdot 2\pi r=\theta r$。

Volume of a sphere (ball) $V=\frac{4}{3}\pi r^3$, $r$ is radius. Surface $S=4\pi r^2$.

secant line 割线 \
tagent line 切线

**直线方程的各种形式**

<ol>
<li>一般式: $Ax+By+C=0$ <br/>

斜率: $k=-\frac{A}{B}$ <br/>
法向量: $\overrightarrow{\textbf{n}}=(A,B)$ <br/>
方向向量: $\overrightarrow{\textbf{a}}=(B,-A)$ 

</li>


<li>点斜式: $y-y_0=k(x-x_0)$ <br/>

点斜式是由一个定点 $P(x_0,y_0)$ 和斜率 $k$ 确定的直线方程。<br/>

斜率: $k$ <br/>
法向量: $\overrightarrow{\textbf{n}}=(k,-1)$ <br/>
方向向量: $\overrightarrow{\textbf{a}}=(1,k)$ 

</li>

<li> 斜截式: $y=kx+b$ <br/>

斜截式是由斜率 $k$ 和 $y$ 轴上的截距 $b$ 确定的直线方程。<br/>

斜率: $k$ <br/>
法向量: $\overrightarrow{\textbf{n}}=(k,-1)$ <br/>
方向向量: $\overrightarrow{\textbf{a}}=(1,k)$ 

</li>

<li> 两点式: $\displaystyle \frac{y-y_1}{y_2-y_1} = \frac{x-x_1}{x_2-x_1}$ <br/>

两点式是由已知的两个点 $(x_1,y_1)$, $(x_2,y_2)$ 确定的直线方程。<br/>

斜率: $k = \frac{y_2-y_1}{x_2-x_1}$ <br/>
法向量: $\overrightarrow{\textbf{n}}=(y_2-y_1,x_1-x_2)$ <br/>
方向向量: $\overrightarrow{\textbf{a}}=(x_2-x_1,y_2-y_1)$ 

</li>

<li> 点向式: $\displaystyle \frac{y-y_0}{b} = \frac{x-x_0}{a}$ <br/>

点向式是由已知的定点 $P(x_0,y_0)$ 和方向向量 $\overrightarrow{\textbf{a}}=(a,b)$ 所确定的直线方程。<br/>

斜率: $k = \frac{b}{a}$ <br/>
法向量: $\overrightarrow{\textbf{n}}=(b,-a)$ <br/>
方向向量: $\overrightarrow{\textbf{a}}=(a,b)$ 

</li>

<li> 参数式: $\left\{\begin{aligned}&x=x_0+at & \\ &y = y_0+bt & \end{aligned}\right.$ <br/>

这里的参数是$t$，是点向式的变式，也是由定点 $P(x_0,y_0)$ 和方向向量 $\overrightarrow{\textbf{a}}=(a,b)$ 所确定的直线方程。<br/>

斜率: $k = \frac{b}{a}$ <br/>
法向量: $\overrightarrow{\textbf{n}}=(b,-a)$ <br/>
方向向量: $\overrightarrow{\textbf{a}}=(a,b)$ 

</li>

<li> 特别参数式: $\left\{\begin{aligned}&x=x_0+t\cos \alpha & \\ &y = y_0+t\sin \alpha & \end{aligned}\right.$ <br/>

这里的参数是 $t$，是参数式的特例，即以直线的倾角。<br/>

斜率: $k = \tan \alpha$ <br/>
法向量: $\overrightarrow{\textbf{n}}=(\sin \alpha, -\cos \alpha)$ <br/>
方向向量: $\overrightarrow{\textbf{a}}=(\cos \alpha, \sin \alpha)$ 

</li>

<li> 点法式: $A(x-x_0)+B(y-y_0)=0$ <br/>

点向式是由已知的定点 $P(x_0,y_0)$ 和法向量 $\overrightarrow{\textbf{a}}=(a,b)$ 所确定的直线方程。<br/>

斜率: $k = -\frac{A}{B}$ <br/>
法向量: $\overrightarrow{\textbf{n}}=(A,B)$ <br/>
方向向量: $\overrightarrow{\textbf{a}}=(B,-A)$ 

</li>

</ol>
Reference: <https://zhuanlan.zhihu.com/p/26263309>

**dot product** vs. **cross product**

- dot product is a scalar, used to calculate projection along a direction ($\vec{A}\cdot \hat{u}$ is the component of $\vec{A}$ along $\hat{u}$, ^ indicates a unit vector); determine if two vectors are <span style='color:#32CD32'>orthogonal</span> (if $\vec{A}\cdot\vec{B}=0$, then $\vec{A}\perp\vec{B}$);

  - The magnitude of the dot product is the same as the magnitude of one of them, multiplied by the component of one vector that is parallel to the other. 

  $$
  \begin{align*}
  \vec{A}\cdot\vec{B} &= \sum_i a_ib_i \\
  \vec{A}\cdot\vec{B} &= \vert\vec{A}\vert\vert\vec{B}\vert \cos\theta \\
  \vec{A}\cdot\vec{A} &= \vert A\vert^2 \quad (\cos0=1)
  \end{align*}
  $$

  

- cross product is a vector, used to 1) calculate area of parallelogram formed by two vectors; 2) get the normal vector; if $\vec{A}\times\vec{B}=0$, then $\vec{A}\parallel\vec{B}$ (<span style='color:#32CD32'>parallel</span>);

  - The magnitude of the cross product is the same as the magnitude of one of them, multiplied by the component of one vector that is perpendicular to the other. 
  - If $\vec{A}\parallel\vec{B}$, no component is perpendicular to the other vector. Hence, the cross product is 0 although you can still find a perpendicular vector to both of these. 

  $$
  \begin{align*}
  \vec{A}\times\vec{B} &=\vert\vec{A}\vert\vert\vec{B}\vert \sin\theta\cdot\vec{n},\; \vec{n} \textrm{ decided by right-hand rule.} \\
  \vec{A}\times\vec{A}&=0 \quad (\sin0=0\textrm{, area of a line is 0})
  \end{align*}
  $$

Geometric illustraion: \
<https://math.stackexchange.com/a/1730547>


## Inner and Outer Product

If $\boldsymbol{u}$ and $\boldsymbol{v}$ are column vectors with the same size, then $\boldsymbol{u}^T \boldsymbol{v}$ is the inner product; if $\boldsymbol{u}$ and $\boldsymbol{v}$ are column vectors of any size, then $\boldsymbol{u} \boldsymbol{v}^T$ is the outer product.

- Inner product is a *number*;
- Outer product is a *matrix*. Let $\boldsymbol{u}$ be $n\times 1$ and $\boldsymbol{v}$ be $m\times 1$, then $\boldsymbol{u} \boldsymbol{v}^T$ is $n\times m$.

**Elementary arithmetic**

四则运算

$a+b=c$: a plus b equals c (plus是介词).

$a-b=c$: a minus b equals c (minus是介词); b substracted from a leaves c.

$a\times b=c$: a times b equals c (times是介词); a multiplied by b is c.

$a\div b=c$: a divided by b equals c.

$1/x$: the reciprocal of x.

$3:5$: three to five.

## Polynomial and Exponential 

多项式与指数

$A^B$: $A$ is called the base (底数), $B$ is exponent (指数).

Polynomials, $x$ in the base. constant ($x^0$), linear ($x$), quadratic ($x^2$), cubic ($x^3$), quartic terms ($x^4$).

$x^4$ read as $x$ to the 4th or the quartic term.

 $2^{16}$ is read as "2 to the 16th power" or "2 to the power of 16" in formal speech. Commonly, a ellipsis of the first expression is used "2 to the 16th" (ordinal) or "2 to the 16" (w/o ordinal).

For example, a polynomial $x^{109} + 9x^5 − 2x^2$ is most likely pronounced:

>   x to the hundred and nine plus nine x to the fifth minus two x squared.

**Exponential** $x$ in the exponent.

If there is a *variable* in the exponent, the ordinal is not used. $x^y$ is read as "x to <span style='color:#32CD32'>*the*</span> y". The -th is dropped.

开方 ($n$th root)

$\sqrt{9}$: the square root of $9$.

$\sqrt[3]{9}$: the cube root of $8$.

$\sqrt[b]{b}$: the $n$-th root of $b$.

$e^x$: take the exponential of $x$ or apply the exponential function to $x$.

对数 (logarithm)

$\log_b x$: the logarithm of $x$ to base $b$.

$\log x, \ln x, \log_ex$: the natural logarithm of $x$.

$\lg x, \log_{10}x$: the common logarithm of $x$.

$\text{lb} x, \log_2x$: the binary logarithm of $x$.


1 micrometer = $10^{-6}$ meter

1 nanometer = $10^{-9}$ meter

$a_1$: a (sub) one.

$\epsilon_{ijk}$: epsilon (sub) ijk.

$a^i$: a super $i$.

Distributive law for multiplication (from product of sums to double sums)

$$
\sum_{i=1}^k a_i \cdot \sum_{j=1}^m b_j = \sum_{i=1}^k \left(\sum_{j=1}^m a_ib_j\right)
$$

**Arithmetic Sequence/Progression** 等差数列

$a_1, a_2, ..., a_n$ has common difference $d$, $n$ is the number of terms. Some useful formulas:

-   the $n$-th term $a_n=a_1+(n-1)d$ 
-   sum of $n$ terms $S_n=\frac{(a_1+a_n)n}{2}=na_1+\frac{n(n-1)}{2}d$
-   number of terms $n=\frac{a_n-a_1}{d}+1$
-   common difference $d=\frac{a_n-a_1}{n-1}$

**Geometric Sequence/Progression** 等比数列

$a_1, a_2, ..., a_n$ has common ratio $q$.

-   $a_n=a_1\cdot q^{n-1}$
-   $\displaystyle S_n= \frac{a_1(1-q^n)}{1-q}$



**Distribution Functions**

Visualization tool: <https://seeing-theory.brown.edu/probability-distributions/>

Plot a function: <https://www.desmos.com/calculator>

___

## Matrices

**Inverse** 

$A^{-1} = \frac{1}{\vert A \vert} \text{Adj}(A)$ where $\text{Adj}(A)$ is the adjoint matrix. Steps to find the inverse of $A$:
<ol>
<li> Calculate the matrix of minors $M$. <br/>
  The minor is defined for every element of a matrix. The minor of a particular element is the determinant, denoted as $M_{ij}$, obtained after eliminating the $i$-th row and $j$-th column. For instance
  $$
  A = \begin{bmatrix} 
  a_{11}  & a_{12}  & a_{13} \\
  a_{21}  & a_{22}  & a_{23} \\
  a_{31}  & a_{32}  & a_{33} \\
  \end{bmatrix}
  $$
  The minor of the element $a_{11}$, i.e., $M_{11}$, is:

  $$
  \text{Minor of }a_{11} = 
  \begin{vmatrix} 
  a_{22}  & a_{23} \\
  a_{32}  & a_{33} \\
  \end{vmatrix}
  $$
</li>
<li> Add the sign $(-1)^{i+j}$ to minors, then you get a cofactor matrix $C_{ij} = (-1)^{i+j}M_{ij}$. </li>
<li> Take the transpose of the cofactor matrix, then you get the adjoint matrix. $\text{Adj}(A)=C^T$ </li>
<li> Divide the $\text{Adj}(A)$ by the determinant.</li>
</ol>

**Properties of inverse**: 

- $(A^T)^{-1} = (A^{-1})^T$ Transpose of inverse equal to inverse of transpose.

- $(ABC)^{-1}=C^{-1}B^{-1}A^{-1}$ The inverse of a product is the product of the inverse in the *opposite* order. This holds only on the condition that all matrices are invertible.

- If $A$ is symmetric, then $A^{-1}$ is symmetric. The inverse of a symmetric matrix is still symmetric.


**Variance matrix of random vector**

A random vector $\vec{X}$ is a vector 
$$
\vec{X}=\begin{bmatrix}
X_1 \\
X_2 \\
\vdots \\
X_p
\end{bmatrix}
$$
of $p$ jointly distributed random variables.

- Expectation $\mathbb{E}[\vec{X}]$ is given by

$$
\mathbb{E}[\vec{X}]=\begin{bmatrix}
\mathbb{E}X_1 \\
\mathbb{E}X_2 \\
\vdots \\
\mathbb{E}X_p
\end{bmatrix}
$$

- Variance-Covariance Matrix of a random vector $\vec{X}$ is given by:

$$
\begin{align*}
\text{Cov}(\vec{X}) &= \mathbb{E}\left[ (\vec{X}-\mathbb{E}[\vec{X}])(\vec{X}-\mathbb{E}[\vec{X}])^T \right] \\
&= \mathbb{E}[\vec{X}\vec{X}^T] - \mathbb{E}[\vec{X}] (\mathbb{E}[\vec{X}])^T
\end{align*}
$$

$$
\text{Cov}(\vec{X}) = 
\begin{bmatrix}
\text{Var}(X_1) &  \text{Cov}(X_1, X_2) &  \cdots &  \text{Cov}(X_1, X_p) \\
\text{Cov}(X_2, X_1) &  \text{Var}(X_2) &  \cdots &  \text{Cov}(X_2, X_p) \\
\vdots & \vdots & \ddots & \vdots \\
\text{Cov}(X_p, X_1) &  \text{Cov}(X_2, X_p) &  \cdots &   \text{Var}(X_p)
\end{bmatrix}_{p\times p}
$$

**Trace Properties** 

The trace of a square matrix A, denoted $\text{tr}(A)$, is defined to be the sum of elements on the main diagonal. The trace is only defined for a square matrix ($n \times n$).

$$\text{tr}(A) = \sum_{i=1}^n a_{ii}$$ 

Basic properties: \
$\text{tr}(\boldsymbol{I}_K) = K$ \
$\text{tr}(cA) = c \cdot \text{tr}(A)$ \
$\text{tr}(XA) = \text{tr}(AX)$ \
$\text{tr}(A+B) = \text{tr}(A) + \text{tr}(B)$


For a random vector $z$ with $\mathbb{E}(z)=\mu$ and $\text{Var}(z)=\Sigma$, then 

$$
\mathbb{E}(z'z) = \text{tr} (\Sigma) + \mu'\mu .
$$

Multiplication by a full-rank square matrix preserves rank.
<ul>
<li> Let $A$ be a $K\times L$ matrix and $B$ a square $L\times L$ matrix. If $B$ is full-rank, then

$$
\text{rank}(AB) = \text{rank}(A).
$$
</li>

<li> Let $A$ be a $K\times L$ matrix and $B$ a square $K\times K$ matrix. If $B$ is full-rank, then

$$
\text{rank}(BA) = \text{rank}(A).
$$
</li>
</ul>

**Diagonal Matrix Properties**

If $D$ is a $n\times n$ diagonal matrix, then 

$D=D^{T}$

$D_1 \times D_2 = D_2 \times D_1 = C$  Diagonal Matrices multiplication are commutative. 
$$
c_{ii} = d1_{ii} d2_{ii}
$$

$$
D^{-1}_{ii} = \frac{1}{d_{ii}}
$$ 
Inverse is taking the inverse of each entry. 

$\vert D \vert = \prod_{i=1}^n d_{ii}$ Determinant is the product of the elements of $D$. 

左乘 (pre-multiply) 一个对角矩阵: $D$ is $K\times K$, $A$ is $K\times L$. For the product $DA$, each row $i$ is equal to the $i$-th row of $A$ multiplied by $D_{ii}$. 

右乘 (post-multiply) 一个对角矩阵: $A$ is $K\times L$, $D$ is $L\times L$. For the product $DA$, each column $j$ is equal to the $j$-th column of $A$ multiplied by $D_{jj}$. 

**Definiteness**

Let  $S$ be the space of all  $Kx1$ vectors having real entries. A  $K	\times K$ real symmetric matrix  $A$ is said to be:

1. positive definite iff  $x^{T}Ax>0$ for any non-zero  $x \in S$;
2. positive semi-definite iff  $x^{T}Ax\geq 0$ for any  $x \in S$;
3. negative definite iff  $x^{T}Ax<0$ for any non-zero  $x \in S$;
4. negative semi-definite iff  $x^{T}Ax\leq 0$ for any  $x \in S$;
5. indefinite iff there exist  $x,y\in S$ such that  $x^{T}Ax>0$ and  $y^{T}Ay<0$.

Let $A$ be a  $K	\times K$ matrix. If  $A$ is positive definite, then it is full-rank.

A real symmetric  $K	\times K$ matrix  $A$ is positive definite if and only if all its eigenvalues are strictly positive real numbers. \
A real symmetric  $K	\times K$ matrix  $A$ is positive semi-definite if and only if all its eigenvalues are positive real numbers.


**Matrix Diagonalization - Eigen Deceomposition**

Let $A\in \mathbb{R}^{K\times K}$ be a square matrix. Then 

<ul>
<li> All the eigenvalues of $A$ are real; </li>
<li>  $A$ is orthogonally diagonalizable, i.e., there exists an orthogonal matrix $P$ and a diagonal matrix $\Lambda$ such that 

$$
A = P\Lambda P^{-1}
$$

$\Lambda = \text{diag}(\lambda_1, \ldots, \lambda_K)$ is a diagonal matrix with eigenvalues being the diagonal. 

$$
\Lambda = \begin{bmatrix} \lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 &  \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 &  \cdots & \lambda_K
\end{bmatrix}
$$

$P=[X_1, \ldots, X_K]$ be the matrix of eigenvectors corresponding to $\lambda_1, \ldots, \lambda_K$.

$$
\begin{align*}
P &= \begin{bmatrix} X_1 & X_2 & \cdots & X_K \end{bmatrix}
&=\begin{bmatrix} x_{11} & x_{21} & \cdots & x_{K1} \\
x_{12} & x_{22} &  \cdots & x_{K2} \\
\vdots & \vdots & \ddots & \vdots \\
x_{1K} & x_{2K} &  \cdots & x_{KK}
\end{bmatrix}
\end{align*}
$$

Then we have

$$
\begin{align*}
AP &= A \begin{bmatrix} X_1 & X_2 & \cdots & X_K \end{bmatrix} \\

&= \begin{bmatrix} AX_1 & AX_2 & \cdots & AX_K \end{bmatrix} \\

&= \begin{bmatrix} \lambda_1X_1 & \lambda_1X_2 & \cdots & \lambda_1X_K \end{bmatrix} \\

&=\begin{bmatrix} \lambda_1x_{11} & \lambda_2x_{21} & \cdots & \lambda_kx_{K1} \\
\lambda_1x_{12} & \lambda_2x_{22} &  \cdots & \lambda_Kx_{K2} \\
\vdots & \vdots & \ddots & \vdots \\
\lambda_1x_{1K} & \lambda_2x_{2K} &  \cdots & \lambda_Kx_{KK} \\
\end{bmatrix} \\

&= \begin{bmatrix} x_{11} & x_{21} & \cdots & x_{K1} \\
x_{12} & x_{22} &  \cdots & x_{K2} \\
\vdots & \vdots & \ddots & \vdots \\
x_{1K} & x_{2K} &  \cdots & x_{KK} \end{bmatrix}
\begin{bmatrix} \lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 &  \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 &  \cdots & \lambda_K
\end{bmatrix} \\

&= P\Lambda

\end{align*}
$$

Hence

$$
A = P\Lambda P^{-1}
$$


An important application of the eigenvalue decomposition is to calculate the power of matrices.

$$
\begin{align*}
A^2 &= (P\Lambda P^{-1}) (P\Lambda P^{-1}) \\
&= P\Lambda^2 P^{-1}
\end{align*}
$$ 

By induction,

$$
A^n = P\Lambda^n P^{-1}
$$

</li>

<li>
For <strong>symmetric matrices</strong> $A$, the eigenvalue decomposition is also called the <em>spectral decomposition</em>.

$A$ is orthogonally diagonalizable, i.e., there exists and orthogonal matrix $Q$ and a diagonal matrix $\Lambda$ such that 

$$
A = Q\Lambda Q^{T},
$$

or equivalently written as

$$
A = \sum_{i=1}^K \lambda_i q_i q_i^{T}.
$$

The converse is also true. Therefore, a matrix is symmetric if and only if it is orthogonally diagonalizable.

</li>
</ul>

An **orthogonal matrix** is a square matrix whose columns and rows are both orthogonal unit vectors (i.e., orthonormal vectors):

$$
Q^TQ = QQ^T = I,
$$

or equivalently, 

$$
Q^{-1} = Q^T.
$$


___


**Change of Variable Formula**

Given the distribution of $X$, we can obtain the distribution of a continuous function of $X$, e.g. $Y=g(X)$.


$$
\begin{align*}
F_Y(y)&=P(Y\le y)=P\left(g(X)\le y\right) \\
&=\left\{
	\begin{array}{ll}
	P\left(X\le g^{-1}(y)\right) = F_X(g^{-1}(y)) & \text{when $g(x)$ is $\uparrow$} \\
	P\left(X\ge g^{-1}(y)\right) = 1- F_X(g^{-1}(y))  & \text{when $g(x)$ is $\downarrow$}
	\end{array} \right. \\
f_Y(y) &= f_X(g^{-1}(y)) \cdot \left\vert \frac{\partial }{\partial y} g^{-1}(y) \right\vert
\end{align*}
$$


Change of Variable for a **Double Integral**

Let $X$ and $Y$ be two jointly continuous random variables. Let $(Z, W) = g(X,Y) = (g_1(X,Y), g_2(X,Y))$, where $g$: $\mathbb{R}^2 \mapsto \mathbb{R}^2$ is a continuous one-to-one (invertiable) funtion with continuous partial derivatives.

Let $h=g^{-1}$, i.e., the inverse function that takes $(Z,W)$ and returns $(X,Y)$, $(X,Y)=h(Z,W)=(h_1(Z,W),h_2(Z,W))$. 

Then $Z$ and $W$ are jointly continuous and their joint PDF, $f_{ZW}(z,w)$, for $(z,w)\in R_{ZW}$ is given by

$$
f_{ZW}(z,w)=f_{XY}(h_1(z,w),h_2(z,w)) \cdot \vert \boldsymbol{J}\vert,
$$

where $\boldsymbol{J}$ is the Jacobian of $h$, defined by 

$$
\boldsymbol{J} =
\text{det} \begin{bmatrix}
\frac{\partial h_1}{\partial z} & \frac{\partial h_1}{\partial w} \\
\frac{\partial h_2}{\partial z} & \frac{\partial h_2}{\partial w}
\end{bmatrix} =
\frac{\partial h_1}{\partial z} \cdot \frac{\partial h_2}{\partial w} - \frac{\partial h_1}{\partial w} \cdot \frac{\partial h_2}{\partial z}
$$

Let $X$ and $Y$ be two random variables with joint PDF $f_{XY}(x,y)$. Let $Z=X+Y$. Find $f_Z(z)$.

To apply the change of variable, we need two random variables $Z$ and $W$. Define

$$
\begin{align*}
\left\{ 
	\begin{array}{ll}
	z = x+y & \text{i.e., }g_1(x,y)\\
	w = x & \text{i.e., }g_2(x,y)
	\end{array}
\right.
\end{align*}
$$

Then we can find the inverse transform:

$$
\begin{align*}
\left\{ 
	\begin{array}{ll}
	x = w & \text{i.e., }h_1(x,y)\\
	y = z-w & \text{i.e., }h_2(x,y)
	\end{array}
\right.
\end{align*}
$$

Then, we have absolute value of the Jacobian

$$
\vert \boldsymbol{J} \vert = 
\vert \text{det} \begin{bmatrix}
0 & 1 \\
1 & -1
\end{bmatrix} \vert 
=
\vert 
0-1
\vert =
1
$$

Thus,

$$
f_{ZW}(z,w)=f_{XY}(w,z−w).
$$

But since we are interested in the marginal PDF, $f_Z(z)$, we have

$$
f_Z(z)=\int_{-\infty}^{\infty}f_{XY}(w,z−w)dw.
$$

Note that, if $X$ and $Y$ are independent, then $f_{XY}(x,y)=f_X(x)fY(y)$ and we conclude that
$$
f_Z(z)=\int_{-\infty}^{\infty}f_X(w)f_Y(z−w)dw.
$$

The above integral is called the *convolution* of $f_X$ and $f_Y$, and we write

$$
f_Z(z)=f_X(z)*f_Y(z) = \int_{-\infty}^{\infty}f_X(w)f_Y(z−w)dw = \int_{-\infty}^{\infty}f_Y(w)f_X(z−w)dw.
$$

<div class = "boxed">
<strong>Theorem</strong>  If X and Y are two jointly continuous random variables and $Z=X+Y$, then

$$
f_Z(z)=\int_{-\infty}^{\infty}f_{XY}(w,z−w)dw.
$$

If X and Y are also independent, then

$$
f_Z(z) = \int_{-\infty}^{\infty}f_Y(w)f_X(z−w)dw.
$$
</div>

Let  $X$ and  $Y$ be two independent discrete random variables. Denote their respective pmfs (probability mass function) by  $p_X(x)$ and  $p_Y(y)$, and their supports by  $R_X$ and  $R_{Y}$. Let

$$
Z=X+Y
$$

and denote the pmf of  Z by  $p_Z(z)$. Then,

$$
\begin{align*}
p_Z(z) &= \sum_{k=-\infty}^{\infty} p_X(x=k)\cdot p_Y(y=z-k) \\
&= \sum_{x\in R_X} p_X(x=k)\cdot p_Y(y=z-k)
\end{align*}
$$

or

$$
p_Z(z) = \sum_{y\in R_y} p_X(x=z-k)\cdot p_Y(y=k).
$$


___


**Law of iterated expectations** LIE  

$$
\begin{align*}
\mathbb{E}_Y(Y) = \mathbb{E}_X\left[\mathbb{E}_{Y\vert X}\right(Y\vert X=x\left)\right]
\end{align*}
$$

(the subscript in $\mathbb{E}_Y$ and $\mathbb{E}_X$ indicate on which variable the expectation is taken)
or more succinctly  

$$
\begin{align*}
\mathbb{E}[Y] = \mathbb{E}\left[\mathbb{E}\right(Y\vert X=x\left)\right].
\end{align*}
$$

It repsents a transformation from condictional to unconditional expectaion.
The expected value (this expectation is with respect to  $X$) of the conditional expectation of $Y$ given $X$ is the expected value of $Y$.

Suppose $\mathbb{E}(Y\vert X)=0$, then   

$$
\begin{align*}
1. \quad & \mathbb{E}[Y] = \mathbb{E}\left[\mathbb{E}\right(Y\vert X=x\left)\right] = 0 \\
2. \quad & \mathbb{E}[g(X)\cdot Y] = \mathbb{E}\left[\mathbb{E}[g(X)\cdot Y\vert X]\right] = \mathbb{E}\left[g(X)\cdot \mathbb{E}[Y\vert X]\right] = \mathbb{E}[g(X)\cdot0]=0
\end{align*}
$$

Note that we start from the conditional expectation being $0$, and conclude that unconditional expectation and its product with a function of $X$ are $0$'s too.\
Conditional expectation is a *stronger* condition than unconditional expectation.

In other words, although conditional expectations can vary arbitrarily for different values of $X$, if you know what the conditional expectations are, the overall expected value of $Y$ is fully determined.

A simple example is one where $X$ takes only two values.  Suppose we are interested in mean birthweight ($Y$) for children of mother's who either drank alcohol during their pregnancy ($X=1$) or who didn't drink alcohol during their pregnancy ($X=0$).  

Suppose the following numbers:

$$
\begin{aligned}
  \mathbb{E}[Y|X=1] &= 7, \;\;\;  \mathbb{P}(X=1) = 0.1\\
  \mathbb{E}[Y|X=0] &= 8, \;\;\;  \mathbb{P}(X=0) = 0.9 \\

\end{aligned}
$$

The law of iterated expectation says that

$$
\begin{aligned}
  \mathbb{E}[Y] &= \mathbb{E}_X \big[ \mathbb{E}[Y|X] \big] \\
  &= \sum_{x \in \mathcal{X}} \mathbb{E}[Y|X=x] \cdot \mathbb{P}(X=x) \\
  &= \mathbb{E}[Y|X=0] \cdot \mathbb{P}(X=0) + \mathbb{E}[Y|X=1] \cdot \mathbb{P}(X=1) \\
  &= (8) \times (0.9) + (7) \times (0.1) \\
  &= 7.9
\end{aligned}
$$

Generalization of LIE in time series

$$
\mathbb{E}\big[\mathbb{E}(y_{t+2}|x_{t+1}) |x_t \big] = \mathbb{E}[y_{t+2} |x_t]
$$

as $x_{t} \subset x_{t+1}$.


More generally, for any random variable $z$ and two information sets $\mathcal{J}$ and $\mathcal{I}$ with $\mathcal{J} \subset \mathcal{I}$, then

$$
\mathbb{E}\big[\mathbb{E}(x|\mathcal{I}) |\mathcal{J} \big] = \mathbb{E}[z |\mathcal{J}]
$$


**Intuition behind the LIE**

Think of $\mathbf{x}$ as a discrete vector taking on possible values $\mathbf{c}_1, \mathbf{c}_2, \ldots, \mathbf{c}_M$ with probabilities $p_1, p_2, \ldots, p_M$. Then LIE says:

$$
\mathbb{E}(y) = p_1 \mathbb{E}(y\vert \mathbf{x}=\mathbf{c}_1) + p_2 \mathbb{E}(y\vert \mathbf{x}=\mathbf{c}_2) + \cdots + p_M \mathbb{E}(y\vert \mathbf{x}=\mathbf{c}_M).
$$

Ths is, $\mathbb{E}(y)$ is simply a weighted average of the $\mathbb{E}(y\vert \mathbf{x}=\mathbf{c}_i)$, where the weight $p_i$ is the probability that $\mathbf{x}$ takes on the value of $\mathbf{c}_i$. In other words, a weighted average of averages.

E.g., suppose we are intrested in average IQ generally, but we have measures of average IQ by gender. We could figure out the quantity of interest by weighting average IQ by the relative proportions of men and women.

**Decomposition of variance**

Or sometimes called **Law of Total Variance**.

$$
\text{Var}(Y) = \text{Var}_\mathbf{x}[\mathbb{E}(y\vert \mathbf{x})]
 + \mathbb{E}_\mathbf{x}[\text{Var}(y\vert \mathbf{x})]
$$

In plain language, the variance of $Y$ deceomposes into the variance of the conditional mean plus the expected variance around the conditional mean.

**Population and Sample**

Population quantities need to know the DGP. Any thing you observe is for samples.

Expectation operator is a linear operator, meaning that we have

$$
\begin{align*}
\mathbb{E}(a+bX)=a+b\,\mathbb{E}(X)
\end{align*}
$$

More generally, let $a_1, \ldots, a_n$ and $b_1, \ldots, b_n$ be sequences of non-random variables and let $X_1, \ldots, X_n$ be a sequence of random variables. Then,  

$$
\begin{align*}
\mathbb{E}\left[\sum_{i=1}^n(a_i+b_iX_i)\right] = \sum_{i=1}^n \mathbb{E}(a_i+b_iX_i) = \sum_{i=1}^n\left(a_i+b_i\mathbb{E}[X_i]\right).
\end{align*}
$$


Linear Transformations of a Random Vector

Let $Y=A+BX$, $X$ is $p\times 1$ random vector, $A$ is $q \times 1$ non-random vector, $B$ is $p\times q$ non-random matrix.

The expected value of this transformation is given by

$$
\mathbb{E}(Y) = A + B\, \mathbb{E}(X)
$$

The variance of this transformation is given by

$$
\text{Var}(Y) = B\, \text{Var}(X)\, B'
$$


A $q \times q$ square matrix $\Sigma$ is called non-negative definite (or *positive semi-definite*) if for any non-zero $q \times 1$ vector $\boldsymbol{a}$ it holds that

$$
\boldsymbol{a}'\Sigma\, \boldsymbol{a} \ge 0
$$

If the square matrix $\Sigma$ is non-negative definite, we write $\Sigma \ge 0$.

Note that all covariance matrix of a random vector is positive semi-definite.

___

**Expectations of Functions of RVs**

If $X$ is a RV, then expected value of $g(X)$ is given by 

$$
\begin{align*}
\mathbb{E}[g(X)] = \left\{
	\begin{array}{ll}
	\int g(x)f(x)dx & \text{for continuous $X$} \\
	\sum_xg(x)f(x) & \text{for discrete $X$}
	\end{array} \right.
\end{align*}
$$

where $f(x)$ is the probability density (mass) function of continuous (discrete) $X$.

Variance is also an expectation by setting $g(X) = (X-\mathbb{E}(X))^2$. In other words, $\text{Var}(X) = \mathbb{E}\left[(X-\mathbb{E}(X))^2\right]$.

$$
\begin{align*}
\text{Var}(X) = \mathbb{E}[(X-\mathbb{E}(X))^2] = \left\{
	\begin{array}{ll}
	\int [x-\mathbb{E}(X)]^2 f(x)dx & \text{for continuous $X$} \\
	\sum_x [x-\mathbb{E}(X)]^2 f(x) & \text{for discrete $X$}
	\end{array} \right.
\end{align*}
$$


Example: **Bernoulli**

Let $X \sim \textrm{Bernoulli}(\theta)$, and recall that we have $\mathbb{E}(X)=\theta$. Then

$$
\begin{align*}
\text{Var}(X) &= \mathbb{E}(X-E[X])^2 \\ 
			 &= \sum_x \left(x-\mathbb{E}[X]\right)^2 f(x) \\
			 &= (0-\theta)^2 \times f(0) + (1-\theta)^2\times f(1) \\
			 &= \theta^2(1-\theta) + (1-\theta)^2\theta \\
			 &= \theta (1-\theta).
\end{align*}
$$

Alternative derivation: Since $0^2=0$ and $1^2=1$, we have $X^2=X$ implying that $\mathbb{E}(X^2)=\mathbb{E}(X)=\theta$. Therefore,

$$
\begin{align*}
\text{Var}(X)=\mathbb{E}[X^2]-(\mathbb{E}[X])^2 = \theta-\theta^2
\end{align*}
$$




**Sample mean** Let $X_1, \ldots, X_n$ denote $n$ observations on a variable $X$, the sample mean is

$$
\begin{align*}
\overline{X}=\frac{1}{n}\sum_{i=1}^nX_i
\end{align*}
$$

$\overline{X}$ is a random variable, as it is the average of random variables.
This is in sharp contrast to $\mathbb{E}[X]$ which is non-random.  

$\overline{X}$ varies with each sample.
If we could repeatedly collect new samples of size $n$ from the same population and each time were able to estimate $\overline{X}$, these estimates would be different from each other.
The distribution of a statistic, like $\overline{X}$, is called its **sampling distribution**.  

One useful feature is  $\mathbb{E}[\overline{X}] = \mathbb{E}[X]$.
This doesn't mean that $\overline{X}$ itself is equal to $\mathbb{E}[X]$.  Rather, it means that, if we could repeatedly obtain (a huge number of times) new samples of size $n$ and compute $\overline{X}$ each time, the average of $\overline{X}$ across repeated samples would be equal to $\mathbb{E}[X]$.

Proof:

$$
\begin{aligned}
  \mathbb{E}[\overline{X}] &= \mathbb{E}\left[ \frac{1}{n} \sum_{i=1}^n X_i \right] \\
  &= \frac{1}{n} \mathbb{E}\left[ \sum_{i=1}^n X_i \right] \\
  &= \frac{1}{n} \sum_{i=1}^n \mathbb{E}[X_i] \\
  &= \frac{1}{n} \sum_{i=1}^n \mathbb{E}[X]  \;\;\;\; (X_i\text{ are iid with mean } \mathbb{E}[X]) \\
  &= \frac{1}{n}\, n\, \mathbb{E}[X] \\
  &= \mathbb{E}[X]
\end{aligned}
$$


**Sample variance** ($\text{Var}(\overline{X})$) use either 

$$
\begin{align*}
\frac{1}{n}\sum_{i=1}^n(X_i-\overline X)^2
\end{align*}
$$

or 

$$
\begin{align*}
\frac{1}{n-1}\sum_{i=1}^n(X_i-\overline X)^2
\end{align*}
$$

The latter subtracts 1 from $n$ in the denominator, which is known as a *degrees of freedom correction*.
See proof [here](https://www.statlect.com/fundamentals-of-statistics/variance-estimation).


**Covariance and Correlation**

*Covariance and correlation* measure the linear association btw two RVs $X$ and $Y$

$$
\begin{aligned}
\gamma &\equiv \text{Cov}(X, Y) = \mathbb{E}\big\{[X-\mathbb{E}(X)][Y-\mathbb{E}(Y)]\big\} \\
\rho &\equiv \frac{\text{Cov}(X, Y)}{\sqrt{\text{Var}(X)\text{Var}(Y)}}
\end{aligned}
$$

where the expected value $\mathbb{E}[\cdot]$ is taken over the joint distribution of $(X,Y)$.

More formally

$$
\textrm{Cov}(X, Y) = \iint[X-\mathbb{E}(X)][Y-\mathbb{E}(Y)]f(x,y) dxdy \quad \textrm{for } X, Y \textrm{ continuous}
$$

and 

$$
\textrm{Cov}(X, Y) = \sum_y\sum_x[X-\mathbb{E}(X)][Y-\mathbb{E}(Y)]f(x,y) \quad \textrm{for } X, Y \textrm{ discrete,}
$$

where the sum and integral are over the supports of $X$ and $Y$.

For linear transformations, we have

$$
\text{Cov}(a+bX, c+dY) = bd\text{Cov}{X,Y}
$$

for known constants $a,b,c,d$.

The additive law of covariance holds that the covariance of a random variable with a sum of random variables
is just the sum of the covariances with each of the random variables.

$$
\text{Cov}(X+Y, Z) = \text{Cov}(X,Z) + \text{Cov}(Y,Z)
$$


More generally,

$$
\text{Cov}\left(\sum_{i=1}^m a_iX_i, \sum_{j=1}^n b_iY_i\right) =
\sum_{i=1}^m\sum_{j=1}^n a_ib_j\text{Cov}(X_i, Y_j).
$$

One of the applications of covariance is finding the variance of a sum of several random variables.
In particular, if $Z=X+Y$, then

$$
\begin{aligned}
\text{Var}(Z) &= \text{Cov}(Z,Z) \\
&= \text{Cov}(X+Y, X+Y) \\
&= \text{Cov}(X,X) + \text{Cov}(X,Y) + \text{Cov}(Y,X) + \text{Cov}(Y,Y) \\
&= \text{Var}(X) + \text{Var}(X) + 2\text{Cov}(X,Y).
\end{aligned}
$$

More generally, for $a_i\in \mathbb{R}, i=1,\ldots,n$, we conclude:

$$
\text{Var}\left(\sum_{i=1}^n a_iX_i \right) = 
\sum_{i=1}^n a_i^2 \text{Var}(X_i) + \sum_{i=1}^n\sum_{j=1}^n a_ia_j \text{Cov}(X_i, X_j).
$$

Or equivalently, 

$$
\text{Var}\left(\sum_{i=1}^n a_iX_i \right) = 
\sum_{i=1}^n a_i^2 \text{Var}(X_i) + 2\sum_{i=2}^n\sum_{j=1}^{i-1} a_ia_j \text{Cov}(X_i, X_j).
$$

If we have either $\mathbb{E}(X)=0$ or $\mathbb{E}(Y)=0$ or both

$$
\text{Cov}(X, Y) = \mathbb{E}{(XY)} - \mathbb{E}{(X)}\mathbb{E}{(Y)} = \mathbb{E}{(XY)}
$$

The *sample covariance*, $\hat{\gamma}$, in a sample of $n$ observations on $(X_i,Y_i)$ is

$$
\hat{\gamma} = \frac{1}{n-1}\sum_{i=1}^n (X_i-\overline{X})(Y_i-\overline{Y})
$$

Division by $n-1$ rather than $n$ is called a degrees of freedom correction.

Correlation is a scaled measure of covariance:

$$
\textrm{Corr}(X,Y)=\frac{\textrm{Cov}(X, Y)}{\sqrt{\text{Var}(X)\text{Var}(Y)}}
$$

If $\textrm{Corr}(X,Y)=0$, we say that $X$ and $Y$ are <span style='color:#32CD32'>uncorrelated</span> or orthogonal, denoted by $X {\color{#32CD32}\perp} Y$ (perpendicular symbol).


$X {\color{#32CD32}\indep} Y$ (double perpendicular symbol) denotes $X$ and $Y$ are <span style='color:#32CD32'>independent</span>.

$X \indep Y \Rightarrow X \perp Y$,  in plain language, independence implies zero correlation. 

Dependent but uncorrelated example

Let $X\sim U(-1,1)$ (任何定义域centered on zero is ok), $Y=f(X)=X^2$. Then $E[X]=0$. 

$$
\begin{aligned}
\text{Cov}(X, Y) &= E[Xf(X)] - E[X]E[f(X)] \\
&= E[Xf(X)] \quad (E[X]=0) \\
&= \int_{-1}^1 x\,f(x)\,p(x)\, dx
\end{aligned}
$$

where $p(x)$ is the pdf of $X$. 

$$
p(x) = \left\{
\begin{array}{ll}
\frac{1}{2} & x\in [-1,1] \\
0 & \text{otherwise}
\end{array}
\right.
$$

Now we have $X$ as an odd funcction and $[-1,1]$ is a symmetric domain. That means as long as $f(x)$ is an even function, we have $xf(x)p(x)$ as on odd function. It then follows that

$$
\int_{-a}^a x\,f(x)\,p(x)\, dx = 0,
$$

and so $\text{Cov}(X, f(X))=0$. 

$f(X)=X^2$ is an even function, which satisfies the condition.

## Joint Distributions and Independence

**Joint CDF**

$$
F(x_1, x_2) =  \left\{
	\begin{array}{ll}
	\int_{-\infty}^{x_1}\int_{-\infty}^{x_2} f(a, b) da db & \text{continuous} \\
	P(X_1=x_1, X_2=x_2) & \text{discrete}
	\end{array} \right.
$$


**Joint Density**

$$
f(x_1, x_2) =  \left\{
	\begin{array}{ll}
	\frac{\partial^2F(x_1, x_2)}{\partial x_1 \partial x_2} & \text{continuous} \\
	\sum_{a\le x_1} \sum_{b\le x_2} f(a,b) & \text{discrete}
	\end{array} \right.
$$

**Marginals**

This is called *marginalizaing* or *integrating out* $X_2$ to get the marginal of $X_1$. \
The marginal of one variable can be obtained by integrating the other variable. This applies to $n$-dimension.

$$
f_{X_1}(k) =  \left\{
	\begin{array}{ll}
	\int_{-\infty}^\infty f(k, x_2) dx_2 & \text{continuous} \\
	\sum_{x_2} f(X_1=k,X_2=x_2) & \text{discrete}
	\end{array} \right.  
$$

Marginalizaing the joint density w.r.t. $X_1$ to get the marginal of $X_2$.

$$
f_{X_2}(k) =  \left\{
	\begin{array}{ll}
	\int_{-\infty}^\infty f(x_1,k) dx_1 & \text{continuous} \\
	\sum_{x_1} f(X_1=x_1,X_2=k) & \text{discrete}
	\end{array} \right. 
$$


**Conditioning**

Conditional density:

$$
\begin{aligned}
f_{X_1\vert X_2}(x_1\vert X_2=x_2) &= \frac{f_{X_1 X_2}(X_1=x_1, X_2=x_2)}{f_{X_2}(X_2=x_2)} \\
f_{X_2\vert X_1}(x_2\vert X_1=x_1) &= \frac{f_{X_1 X_2}(X_1=x_1, X_2=x_2)}{f_{X_1}(X_1=x_1)} 
\end{aligned}
$$

Note that nominator is joint density, denominator is marginal density.\
Conditinal pdf could be written more succinctly as

$$
\begin{aligned}
f(x_1\vert x_2) &= \frac{f(x_1, x_2)}{f(x_2)} \\
f(x_2\vert x_1) &= \frac{f(x_1, x_2)}{f(x_1)} .
\end{aligned}
$$

Conditional cdf is integrated based on conditional pdf:

$$
\begin{aligned}
F_{X_1\vert X_2}(x_1\vert X_2=x_2) &=  P(X_1\le x_1 \vert X_2=x_2) \\
&= \left\{
\begin{array}{ll}
	\int_{-\infty}^{x_1} f_{X_1\vert X_2}(s {\color{#32CD32}\vert X_2=x_2}) ds & \text{continuous} \\
	\sum_{s\le x_1} f_{X_1\vert X_2}(X_1=s {\color{#32CD32}\vert X_2=x_2})  &\text{discrete}
\end{array} \right. 
\end{aligned}
$$

or could be written more succinctly as

$$
\begin{aligned}
F(x_1\vert x_2)  &=  P(X_1\le x_1 \vert X_2=x_2) \\
&=  \left\{
\begin{array}{ll}
	\int_{-\infty}^{x_1} f(s{\color{#32CD32}\vert x_2}) ds & \text{continuous} \\
	\sum_{s\le x_1} f(X_1=s {\color{#32CD32}\vert X_2=x_2})  &\text{discrete}
\end{array} \right. 
\end{aligned}
$$

Expectation 

$$
\mathbb{E}[h(X,Y)] = \int_{-\infty}^\infty\int_{-\infty}^\infty h(x,y) f_{XY}(x,y) dxdy
$$

Conditional expectation on $X$ is indicated using a subscript in $\mathbb{E}_X$, e.g.,

$$
\mathbb{E}_X[h(X, Y)] = \mathbb{E}[h(X, Y)|X] =  \int_{-\infty}^\infty h(x,y) f_{h(X,Y)|X} (h(x,y)|x) dy
$$

Here, we "integrate out" the $Y$ variable, and we are left with a function of $X$.

It is also possible the subscript indicates marginal density.

$$
\mathbb{E}_X[h(X, Y)] = \int_{-\infty}^\infty h(x,y) f_X(x) dx
$$

Here, we "average over" the $X$ variable, and we are left with a function of $Y$.

___


**Moments**


We often summarise properties of distributions using their moments.


The $r^{\text{th}}$ order moment is defined by

$$
\begin{aligned}
\mathbb{E}(X^r) = \left\{
\begin{array}{ll}
	\int_{-\infty}^\infty x^r f(x)dx & \text{continuous} \\
	\sum_x x^r f(x) &\text{discrete}
\end{array} \right.
\end{aligned}
$$


**First order moment**

The first moment is called the expected value or expectation, which is given by 

$$
\begin{aligned}
\mathbb{E}(X) = \left\{
\begin{array}{ll}
	\int_{-\infty}^\infty x f(x)dx & \text{continuous} \\
	\sum_x x f(x)  &\text{discrete}
\end{array} \right. 
\end{aligned}
$$

**Second moment about the mean**

Also called second central moment.
The variance is obtained by setting $g(X)=\mathbb{E}[\left(X-\mathbb{E}(X)\right)^2]$.

$$
\begin{aligned}
\text{Var}(X) = \mathbb{E}[\left(X-\mathbb{E}(X)\right)^2] = \left\{
\begin{array}{ll}
	\int_{-\infty}^\infty \left[X-\mathbb{E}(X)\right]^2 f(x)dx & \text{continuous} \\
	\sum_x \left[X-\mathbb{E}(X)\right]^2 f(x) &\text{discrete}
\end{array} \right. 
\end{aligned}
$$

Unconditional expectation of functions of RVs

$$
\begin{aligned}
\mathbb{E}[g(x)] = \left\{
\begin{array}{ll}
	\int_{-\infty}^\infty g(x){\color{red}f(x)}dx & \text{continuous} \\
	\sum_x g(x){\color{red}f(x)} &\text{discrete}
\end{array} \right.  
\end{aligned}
$$

Conditional expectation of functions of RVs

$$
\begin{aligned}
\mathbb{E}(g(x) \vert Y=y) = \left\{
\begin{array}{ll}
	\int_{-\infty}^\infty g(x){\color{#32CD32}f(x\vert Y=y)}dx & \text{continuous} \\
	\sum_x g(x){\color{#32CD32}f(x\vert Y=y)} &\text{discrete}
\end{array} \right.  
\end{aligned}
$$

Note: 
- For <span style='color:red'>unconditional</span> moments, use the appropriate <span style='color:red'>unconditional</span> density.
- For <span style='color:#32CD32'>conditional</span> moments, use the appropriate <span style='color:#32CD32'>conditional</span> density.
- Expectation or expected value is a population quantity because it requires knowledge of the density function.
- The sample analogue of the expected value is the sample mean or sample average.


Conditional and Unconditional Variance

Unconditional 

$$
\begin{aligned}
\text{Var}(X) &= \mathbb{E} [(X-\mathbb{E}(X))^2] \\
&= \left\{
\begin{array}{ll}
	\int_{-\infty}^{\infty} \left(x-\mathbb{E}(X) \right)^2 f(x) dx & \text{continuous} \\
	\sum_{x} \left(x-\mathbb{E}(X) \right)^2 f(x)  &\text{discrete}
	\end{array} \right. 
\end{aligned}
$$

Conditional variance use conditional expectations

$$
\begin{aligned}
\text{Var}(X{\color{#32CD32}\vert Y}) &= \mathbb{E} [(X-\mathbb{E}(X{\color{#32CD32}\vert Y}))^2 {\color{#32CD32}\vert Y}] \\
&= \left\{
\begin{array}{ll}
	\int_{-\infty}^{\infty} [x-\mathbb{E}(X{\color{#32CD32}\vert Y=y})]^2 f(x{\color{#32CD32}\vert y}) dx & \text{continuous} \\
	\sum_{x} [x-\mathbb{E}(X{\color{#32CD32}\vert Y=y})]^2 f(x{\color{#32CD32}\vert y})  &\text{discrete}
	\end{array} \right. 
\end{aligned}
$$

Alternatively, the conditional variance can be written as 

$$
\text{Var}(X{\color{#32CD32}\vert Y}) = \mathbb{E}[X^2{\color{#32CD32}\vert Y}] - \left(\mathbb{E}[X{\color{#32CD32}\vert Y} ]\right )^2
$$

Independence conditional on other variables

$X_1$ and $X_2$ are said to be independent conditional on $X_3$ if 

$$
f(x_1, x_2 \vert x_3) = f(x_1\vert x_3) f(x_2\vert x_3)
$$

The left-hand-side (LHS) represents the joint behavior of $X_1$ and $X_2$ conditional on $X_3$, the RHS represents the individual behavior conditional on $X_3$.

This is denoted as 

$$
X_1 \indep X_2 \vert X_3
$$

Note that this <span style='color:#32CD32'>does not imply</span> $X_1 \indep X_2$! \
E.g., $X_1$ and $X_2$ can be returns on two equities where $X_3$ is some global macroeconomic factor affecting multiple variables at once (e.g. federal reserve interest rate). \
Another example for $X_1, X_2$ would be wages and level of education, whereas $X_3$ is level of intelligence.

For three or more RVs, the joint PDF, joint PMF, and joint CDF are defined in a similar way to what we have seen for the case of two random variables. \
Let $X_1, X_2, \ldots, X_n$ be $n$ discrete RVs. The joint PMF is defined as 

$$
P_{X_1, X_2, \ldots, X_n} (x_1, x_2, \ldots, x_n) = P(X_1=x_1, X_2=x_2, \ldots, X_n=x_n).
$$

For $n$ jointly continuous RVs $X_1, X_2, \cdots, X_n$, the joint PDF is defined to be the function $f_{X_1, X_2, \cdots, X_n}(x_1, x_2, \cdots, x_n)$ such that the probability of any set $A\in \mathbb{R}^n$ is given by the integral of the PDF over the set $A$. In particular, we can write

$$
P\big((X_1, X_2, \cdots, X_n)\in A\big) = \int \cdots \underset{A}{\int} \cdots \int f_{X_1, X_2, \cdots, X_n}(x_1, x_2, \cdots, x_n) dx_1dx_2\cdots dx_n.
$$

<div class = "boxed">
<strong>Definition</strong>  $X_1, X_2, \cdots, X_n$ are said to be independent and identically distributed (iid) if they are independent, and they have the same marginal distributions:

$$
F_{X_1}(x) = F_{X_2}(x) = \cdots = F_{X_n}(x), \text{for all } x\in\mathbb{R}.
$$

</div>



Linear Algebra \
<https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab>


___

**Convergence**
- Formal definition of convergence is: \
  Let $X_n=c+\frac{1}{n}$ for $n=1,2, \ldots$ and some constant $c$. $X_n$ converges to $c$ iff for $\forall \delta>0$, there exists some values $n^{\ast}$ such that for all $n>n^*$ we have $\vert X_n-c \vert < \delta$.

- Convergence in Probabiliy, $\lim_{n\to\infty}P(\vert X_n-c\vert < \varepsilon) =1$, denoted as $\text{plim}_{n\to\infty}X_n=c$, or $X_n \xrightarrow{p} c$.

- Almost Sure Convergence, $P(\lim_{n\to\infty}\vert X_n-c\vert =0)=1$, denoted as $X_n \xrightarrow{a.s.} c$.

- Convergence in Mean Square, $\lim_{n\to\infty}\mathbb{E}[(X_n-c)^2]=0$,  denoted as $X_n \xrightarrow{m.s.} c$.

- Convergence in Distribution, $P(X_n\le x) \rightarrow P(X\le x)$ as $n\rightarrow \infty$, $X_n\xrightarrow{d}X$. If $X\sim N(\mu, \sigma^2)$, then $X_n \xrightarrow{d} N(\mu, \sigma^2)$.

Note: 
- Convergence in probability is weaker than both a.s. and m.s. convergence. Obtaining any type of convergence is sufficient. In certain cases, proving one type can be easier than another type.
- Convergence in probability implies convergence in distribution. Convergence in probability means that two objects converge to each other. Convergence in distribution means that the distributions of two different objects become the same.

**Consistent estimator**

$\hat{\theta}$ is a consistent estimator of $\theta$ if 

$$
  \hat{\theta} \xrightarrow{p} \theta.
$$


**Law of Large Numbers** (LLN)
- Chebyshev's (week) LLN\
  Let $X_1, \ldots, X_n$ be an iid sequence with mean $\mathbb{E}(X_i)=\mu$ and $\text{Var}(X_i)=\sigma^2$. Then,

  $$
  \begin{align*}
  \frac{1}{n}\sum_{i=1}^nX_i &\xrightarrow{p} \mathbb{E}(X_i). \\
  (\text{i.e., } \overline{X}_n &\xrightarrow{p} \mu )
  \end{align*}
  $$

  LLN tells us that the sample mean is a consistent estimator of the expected value. \
  Note that 3 assumptions need to be satisfied: 
  1. $X_1, \ldots, X_n$ are an iid distributed;
  2. exist finite mean $\mu$; and
  3. exist finite variance $\sigma^2$.


- Kolmogorov's (strong) LLN \
  Let $X_1, \ldots, X_n$ be an iid sequence with mean $\mathbb{E}(X_i)=\mu$. Then

  $$
  \frac{1}{n}\sum_{i=1}^nX_i \xrightarrow{a.s.} \mathbb{E}(X_i).
  $$

  Note that the strong LLN requires *only finite mean*.

  Kolmogorov's LLN is very hard to prove. Weak LLN can be easily proved by showing m.s. convergence, which implies convergence in probability.

  Proof of weak LLN:

  Let $$\overline{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$$ be the sample average. 
  To prove weak LLN, we can show $\lim_{n\to\infty}\mathbb{E}(\overline{X}_n-\mu)^2=0$.

  $$
  \begin{align*}
  \lim_{n\to\infty}\mathbb{E}(\overline{X}_n-\mu)^2 &=
  \lim_{n\to\infty} \text{Var}[\overline{X}_n] \\
  &= \lim_{n\to\infty} \frac{\sigma^2}{n} \\
  &= 0
  \end{align*}
  $$
  
  This shows $\overline{X}_n \xrightarrow{m.s} \mu$, which implies $\overline{X}_n \xrightarrow{p} \mu$.

- LLN for random vectors \
  For $\boldsymbol{y}\in \mathbb{R}^m$, if $\boldsymbol{y}_i$ are independent and identically distributed and $E\,\vert\vert \boldsymbol{y} \vert\vert <\infty$, then as $n\to\infty$,

  $$
  \overline{\boldsymbol{y}} = \frac{1}{n}\sum_{i=1}^n\boldsymbol{y}_i \xrightarrow{p} E\,[\boldsymbol{y}].
  $$

  Note: convergence in probability of a vector can be defined as convergence in probability of all elements in the vector.

  $E\,\vert\vert \boldsymbol{y} \vert\vert <\infty \Leftrightarrow E\,\vert y_j \vert <\infty $. Saying that the expected value of Euclidean norm is finite is equivalent to say that the expected value of each element is finite.

  $$
  \overline{\boldsymbol{y}} = \frac{1}{n}\sum_{i=1}^n\boldsymbol{y}_i = \begin{pmatrix} 
  \overline{y}_1 \\
  \overline{y}_2 \\
  \vdots         \\
  \overline{y}_m \\
  \end{pmatrix}
  $$

  - <span style='color:#797D7F'> $E\,\vert\vert \boldsymbol{y} \vert\vert <\infty$ indicates 1st moment finite; </span>
  - <span style='color:#797D7F'> $E\,\vert\vert \boldsymbol{y} \vert\vert^2 <\infty$ indicates 2nd moment finite.  </span>
  

  Ergodic Theorem \
  If $\boldsymbol{y}_t$ is strictly stationary, ergodic, and $E\,\vert\vert \boldsymbol{y} \vert\vert <\infty $, then as $n\to\infty$,

  $$
  E\vert\vert \overline{\boldsymbol{y}}-\boldsymbol{\mu} \vert\vert \to 0
  $$

  and

  $$
  \overline{\boldsymbol{y}} \xrightarrow{p} \boldsymbol{\mu}
  $$

  where $\boldsymbol{\mu}=E[\boldsymbol{y}_t]$.

  The ergodic theorem shows that ergodicity is sufficient for consistent estimation.

  Note that instead of requireing iid, ergodicity imposes a weaker assumption which requires only stationarity and ergodicity. That is, serial dependence is allowed for in the time series.



**Unbiasedness vs Consistency**

- Unbiasedness, $\mathbb{E}(\hat{\theta})=\theta$, is a finite sample property, that holds for any sample size.
- Consistency, $\hat{\theta}\xrightarrow{p}\theta$, is a asymptotic property, that holds in the limit as $n\to \infty$.
- Note: neither property implies the other. 
  + If we are interested in bias, we take the **expectation** on both sides of the equation.
  + When we are interested in consistency we take the **probability limit**.

**Central Limit Theorem** (CLT)

Suppose that $X_1, \ldots, X_n$ is an iid sequence with mean $\mathbb{E}(X_i)=\mu$ and $\text{Var}(X_i)=\sigma^2$. Let $\overline{X}=\sum_{i=1}^n X_i$ Then,

$$
\frac{\overline{X}-\mathbb{E}[\overline{X}]}{\sqrt{\text{Var}[\overline{X}]}} 
= \frac{\overline{X}-\mu}{\sqrt{\sigma^2/n}} 
= \sqrt{n}\cdot\frac{\overline{X}-\mu}{\sigma} 
\xrightarrow{d} N(0,1)
$$

equivalently, we can write 

$$
\sqrt{n}\cdot\frac{\overline{X}-\mu}{\sigma} 
\overset{a}{\sim} N(0,1)
$$

$\overset{\rm a}{\sim}$ means "*approximately distributed with*". \
Or we can also write as

$$
\begin{align*}

\begin{array}{rlrl}
	\sqrt{n} (\overline{X}-\mu)  &\xrightarrow{d} N(0,\sigma^2),  &
  \sqrt{n} (\overline{X}-\mu)  &\overset{a}{\sim} N(0,\sigma^2) \\
  
  \overline{X} -\mu  &\xrightarrow{d} N(0,\sigma^2/n), &
  \overline{X} -\mu  &\overset{a}{\sim} N(0,\sigma^2/n) \\

  \overline{X} &\xrightarrow{d} N(\mu,\sigma^2/n), &
  \overline{X} &\overset{a}{\sim} N(\mu,\sigma^2/n) .
\end{array} 

\end{align*}
$$

Note: The CLT is a very powerful result. $X_1, \ldots, X_n$ can be from any possible distribution (*iid* with *finite mean and variance*), and still their normalised sample mean will be standard normal.

In practice, we replace $\sigma$ with $\widehat{\sigma}$ because we do not observe $\sigma$ but we do observe $\widehat{\sigma}$.

Define the *partial sum* $S_n := \sum_{i=1}^n X_i = n\overline{X}_n$. By LLN, we have

$$
\frac{\overline{X}-\mu}{\sigma/\sqrt{n}} \xrightarrow{d} N(0,1) 
$$

Multiply the denominator and numerator by $n$, we have

$$
\begin{align*}
\frac{n\overline{X}-n\mu}{n\cdot\sigma/\sqrt{n}}  = \frac{S_n-n\mu}{\sigma\sqrt{n}} 
\end{align*}
$$

which converges in distribution to

$$
\frac{S_n-n\mu}{\sigma \sqrt{n}} \xrightarrow{d} N(0,1) .
$$

## Big-O Little-o Notation

Consider a sequence of random variables $X_n$ and a sequence of constants $a_n$ for $n = 1, 2, . . .$\
If $X_n/a_n \xrightarrow{p} 0$, we say $(X_n/a_n)=o_p(1)$ or $X_n=o_p(a_n)$.\
Consequently:
1. If $X_n\xrightarrow{p}0$, we say $X_n=o_p(1)$.
2. If $n^\alpha X_n\xrightarrow{p}0$ for some $\alpha$, we say $X_n/n^{-\alpha}=o_p(1)$ or $X_n=o_p(n^{-\alpha})$.

E.g., For $X_1, X_2, \ldots, X_n$ iid with mean $\mu$ and variance $\sigma^2$, by the LLN we have $\overline{X}\xrightarrow{p}\mu$. Then, $\overline{X}-\mu\xrightarrow{p}0$ and so $\overline{X}-\mu = o_p(1)$.

Big-O notation relaxes the convergence to a finite limit (zero or non-zero). \
If $X_n/a_n \xrightarrow{d} X$ or $X_n/a_n \xrightarrow{p} X$, we say $(X_n/a_n)=O_p(1)$ or $X_n=O_p(a_n)$.\
Consequently:
1. If $X_n\xrightarrow{d}X$ or $X_n\xrightarrow{p}X$, we say $X_n=O_p(1)$.
2. If $n^\alpha X_n\xrightarrow{d}X$ or $n^\alpha X_n\xrightarrow{p}X$ for some $\alpha$, we say $X_n/n^{-\alpha}=O_p(1)$ or $X_n=O_p(n^{-\alpha})$.

E.g., For $X_1, X_2, \ldots, X_n$ iid with mean $\mu$ and variance $\sigma^2$, define $Z=\frac{\overline{X}-\mu}{\sigma}$. Then, by the CLT we have $\sqrt{n}Z\xrightarrow{d}N(0,1)$ and so $\sqrt{n}Z = O_p(1)$ or equivalently $Z=O_p(n^{-1/2})$.


## Type I and II Errors

Type I error: rejecting a true $H_0$. Corresponds to level of significance, $\alpha$, $\alpha = P(\text{reject } H_0 \vert H_0 \text{ is true})$.

Type II error: failing to reject a false $H_0$. The probability of committing a Type II error is called $\beta$. $\beta=P(\text{fail to reject} H_0\vert H_0 \text{ is false})$. $\beta$ is related to the *Power of a test*.
$\beta = 1-\text{Power of a test} = 1-P(\text{reject } H_0\vert H_0 \text{ is false})$. 

In hypothesis testing, the *size of a test* is the (maximum) probability of committing a Type I error, that is, of incorrectly rejecting the null hypothesis when it is true.

<img src="https://drive.google.com/thumbnail?id=1U8Hk_KJfWT5fL6eUgEcPNiiSrueLSfC3&sz=w1000" alt="type-i-and-type-ii-error" style="display: block; margin-right: auto; margin-left: auto; zoom:50%;" />


Note:
- If $\alpha$ increases that means the chances of making a type I error will increase. It is more likely that a type I error will occur. It makes sense that you are less likely to make type II errors, only because you will be rejecting H0 more often. You will be failing to reject H0 less, and therefore, the chance of making a type II error will decrease. Thus, as $\alpha$ increases, $\beta$ will decrease, and vice versa. That makes them seem like complements, but they are not complements.
- For a constant sample size, $n$, if  $\alpha$  increases, $\beta$ decreases. \
For a constant significance level,  $\alpha$ , if $n$ increases, $\beta$ decreases.



___

## Stochastic Process

A stochastic process $X_t$ is a family of random variables. At a specific time point $t$, $X_t$ is a random variable with a specific density function. A stochastic process is defined in a probability space $(\Omega, \mathcal{F}, P)$.

Mean function $\mu_t$ 

$$
\begin{align*}
\mu_t = \mathbb{E}[X_t] = \int_{\mathbb{R}}xdF_t(X)
\end{align*}
$$

$\mu_t$ depends on time $t$, as, for example, processes with a seasonal or periodical structure or processes with a deterministic trend.

**Autocovariance Function**
$$
\begin{align*}
\gamma(t,\tau)=\text{Cov}(X_t, X_{t-\tau})
\end{align*}
$$

If we define <span style='color:red'>**covariance stationary**</span>, then $\gamma(t,\tau)=\gamma_\tau$, means covaraince only depends on time interval apart, not start point.


Autocorrelation Function (ACF)

$$
\begin{align*}
\rho_{\tau}=\frac{\gamma_{\tau}}{\gamma_0}
\end{align*}
$$

The autocorrelation function $\rho$ of a covaraince stochastic process is normalized on the interval [-1,1].  $\rho$ depends only on one parameter, the lag $\tau$.



**White Noise (WN)**

If $X_t$ is white noise, then

$$
\begin{align*}
1.&\ \mu_t=0,  and \\
2.&\ \gamma_\tau=\left\{
	\begin{array}{ll}
	\sigma^2 & \text{when $\tau=0$} \\
	0 & \text{(uncorrelated) when $\tau\neq0$}
	\end{array} \right.
\end{align*}
$$

In short, WN is with expectation 0 and finite variance. denoted as $X_t\sim \text{WN} (0, \sigma^2)$.

Note that every $\text{IID}\, (0, \sigma^2)$ sequence is $\text{WN} (0, \sigma^2)$, but not conversely.

**Random Walk**
$$
\begin{align*}
X_t=c+X_{t-1}+\epsilon_t
\end{align*}
$$

with a constant $c$ and **white noise** $\epsilon_t$. 

$Z_t=X_t-X_{t-1}=c+\epsilon_t$ , if $c$ is not zero, then we say $X_t$  has a drift, 

$c>0$ we say drift upward,

$c<0$ we say drift downward.

$\epsilon_t$ is called disturbances or innovations in time series.

Assume that the constant $c$ and the initial value $X_0$ are set to zero, through recursice substitution we will get the representation:
$$
\begin{align*}
X_t=\sum^t_{i=1}\epsilon_i
\end{align*}
$$
Moment functions:

1. $\mu_t=0$
2. $\text{Var}(X_t)=t\sigma^2$
3. $\gamma(t,\tau) = \text{Cov}(X_t,X_{t-\tau})=(t-\tau)\sigma^2$, for $\tau\lt t$.
4. $\rho(t,\tau)=\sqrt{1-\frac{\tau}{t}}$

Notice that autocovariance is strictly positive, and since it depends on $t$ not only on the lags $\tau$, the random walk is not covariance stationary.

As $\tau$ gets larger, $\rho$ gets smallers. In words, neighboring time points are more and more strongly and positively correlated as time goes by. On the other hand, the values of $X$ at distant time points are less and less correlated.



**AR(1) process**

$$
\begin{align*}
X_t=c+\alpha X_{t-1}+\epsilon_t
\end{align*}
$$

with $ \vert\alpha \vert<1$.

By iterative substitutions, 

$$
\begin{align*}
X_t=c \frac{1-\alpha^k}{1-\alpha}+\alpha^kX_{t-k}+\sum^{k-1}_{i=0}\alpha^i\epsilon_{t-i}
\end{align*}
$$

For $K\to \infty$,

$$
\begin{align*}
X_t=c\frac{1}{1-\alpha}+\sum^\infty_{i=0}\alpha^i\epsilon_{t-i}
\end{align*}
$$

Moment functions:

1. $\mu_t=c\frac{1}{1-\alpha}$
2. $\gamma_\tau=\frac{\sigma^2}{1-\alpha^2}\alpha^\tau$
3. $\rho_\tau=\alpha^\tau$

For ACF $\rho_\tau$, if $\alpha>0$, this function is strictly positive, for $\alpha<0$, it alternates around zero. For small $\alpha$, like 0.5, it converges very fast; for large $\alpha$, like 0.99, it converges quite slow.



**Markov Process**

A stochastic process has the Markov Property if for all $t\in \mathbb{Z}$ and $k\geq 1$

$$
\begin{align*}
F_{t|t-1,\ldots,t-k}(x_t|x_{t-1},\ldots, x_{t-k})=F_{t|t-1}(x_t|x_{t-1})
\end{align*}
$$

In other words, the conditional distribution of a Markov process at a specific point in time is entirely determined by the condition of the system at the previous date.

Two examples: random walk with independent $\epsilon_t$ and the AR(1) process with independent white noise.



**Martingale**

$$
\begin{align*}
E[X_t|X_{t-1}=x_{t-1},\ldots,X_{t-k}=x_{t-k}]=x_{t-1}
\end{align*}
$$

For martingale, only one statement about the conditional expectation is made; while for Markov process, statements on the entire conditional distribution are made.



**Lag Operator**

$LX_t=X_{t-1}$ and  $L^kX_t=X_{t-k}$

$\Delta=1-L$, $\Delta X_t=X_t-X_{t-1}$ and $\Delta^k=(1-L)^k$



**Unit Root Tests**
$$
\begin{align*}
X_t=c+\alpha X_{t-1}+\epsilon_t
\end{align*}
$$
For $|\alpha|<1$, the process is stationary or after the "decaying process";

for $\alpha=1$, the process is **non-stationary.**



### Kernel Smoothing

<https://atmos.washington.edu/~breth/classes/AS552/lect/lect24.pdf>

Python code: <https://matthew-brett.github.io/teaching/smoothing_intro.html>







## GMM	

`gmm(g, x, t0=NULL, gradv=NULL, type=c("twoStep","cue","iterative"), wmatrix = c("optimal","ident"), vcov=c("HAC","MDS","iid","TrueFixed"), ..., data)`

* `g`     A function of the form $g(\theta,x)$ and which returns a $n\times q$ matrix with element $g_i(\theta,x_t)$ for $i=1,\ldots,q$ and $t=1,\dots,n$.  This matrix is used to build the $q$ sample moment conditions. 
* `x`     The matrix or vector of data from which the function $g(\theta,x)$is computed. If "g" is a formula, it is an n × Nh matrix of instruments or a formula.
* `wmatrix`     Which weighting matrix should be used in the objective function. 
  * By default, it is the inverse of the covariance matrix of $g(\theta,x)$, `optimal`. 
  * The other choice is the identity matrix which is usually used to obtain a first step estimate of $\theta$. `ident`



**Vector Autoregressive**

VAR model allows feedback to occur between the variables in the model. For example, we could use a VAR model to show how real GDP is a function of policy rate and how policy rate is, in turn, a function of real GDP.

-   A systematic but flexible approach for capturing complex real-world behavior.
    Better forecasting performance.
    Ability to capture the intertwined dynamics of time series data.





**log-transformed Models**

1.  **Only the dependent/response variable is log-transformed**. Exponentiate the coefficient. This gives the multiplicative factor for every one-unit increase in the independent variable. Example: the coefficient is 0.198. exp(0.198) = 1.218962. For every one-unit increase in the independent variable, our dependent variable increases by a factor of about 1.22, or 22%. Recall that multiplying a number by 1.22 is the same as increasing the number by 22%. Likewise, multiplying a number by, say 0.84, is the same as decreasing the number by 1 – 0.84 = 0.16, or 16%. 
2.  **Only independent/predictor variable(s) is log-transformed**. Divide the coefficient by 100. This tells us that a 1% increase in the independent variable increases (or decreases) the dependent variable by (coefficient/100) units. Example: the coefficient is 0.198. 0.198/100 = 0.00198. For every 1% increase in the independent variable, our dependent variable increases by about 0.002. For x percent increase, multiply the coefficient by log(1.x). Example: For every 10% increase in the independent variable, our dependent variable increases by about 0.198 * log(1.10) = 0.02.
3.  **Both dependent/response variable and independent/predictor variable(s) are log-transformed**. Interpret the coefficient as the percent increase in the dependent variable for every 1% increase in the independent variable. Example: the coefficient is 0.198. For every 1% increase in the independent variable, our dependent variable increases by about 0.20%. For x percent increase, calculate 1.x to the power of the coefficient, subtract 1, and multiply by 100. Example: For every 20% increase in the independent variable, our dependent variable increases by about (1.20 0.198 – 1) * 100 = 3.7 percent.







___

Semi-parametric models

-   Method of Moments
-   quantile regression



**Textbooks**

-   **Econometric Analysis** , 5th Edition, by William H. Greene, Prentice Hall, 2003. \
    **Time Series Analysis**, by J. D. Hamilton, Princeton University Press, 1994. \
    **Estimation and Inference in Econometrics**, by R. Davidon and J. MacKinnon, Oxford University Press, 1993. \
    **Econometric Analysis of Cross Section and Panel Data**, by J. Wooldridge, MIT Press, 1999. \
    **Microeconometrics: Methods and Applications**, Cameron, A. C. and Trivedi, P. K., Cambridge University Press, 2005.

-   **Core Metrics textbooks**

    - Casella, G. and Berger, R.L. (2002) ***Statistical Inference***. 2nd ed. Duxbury.
    - Hendry, D.F. and Nielsen, B. (2007) ***Econometric Modeling***. Princeton.
    - Hoel, P.G., Port, S.C. and Stone, C.J. (1971) ***Introduction to Probability***. Boston: Houghton-Mifflin.

