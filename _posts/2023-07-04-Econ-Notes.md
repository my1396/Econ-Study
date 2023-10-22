---
layout: post
title: Econometric Notes
tag: study
modified_date: 2023-10-05
---

$$
\newcommand{\indep}{\perp \!\!\! \perp}
$$

## Notation

$\mathbb{E}_Y$ and $\mathrm{Var}_Y$ denote expectation over $Y$ and variance over $Y$.

Blackboard bold 黑板粗体 (`\mathbb`) is often used to denote **sets of numbers**, e.g. $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{O}$, or a general field $\mathbb{F}$ or $\mathbb{K}$, and in probability to denote expectation of a random variable $\mathbb{E}(X)$ , written as `\mathbb{E}(X)`, or probability of an event $\mathbb{P}(E)$, written as `\mathbb{P}(E)`. Sometimes you see a sphere denoted $\mathbb{S}$ or a torus denoted $\mathbb{T}$. 

Mathematical calligraphic font 花体 (`\mathcal`), uppercase only, font for categories and sheaves.

-   $\mathcal L$（`\mathcal L`）常用来表示损失函数;
-   $\mathcal D$（`\mathcal D`）表示样本集;
-   $\mathcal N$（`\mathcal N`）常用来表示高斯分布;

-   $\ell$（`\ell`）：用于和 $l$ 和 数字 1 相区分。



**Upper- and lower-case letters**

Vectors are lowercase and matrices are uppercase symbols. Both vectors and matrices are written in bold-italic. 

- Vectos $\mathbfit a, \mathbfit b, \mathbfit c$  are produced by`\mathbfit a` ... ; vectors can also be denoted by Greek lowercase letters: $\boldsymbol{\alpha, \ldots \omega}$
- Matrices $\mathbfit A, \mathbfit B, \mathbfit C$ by `\mathbfit A` ... ; matrices can be deonoted by Greek uppercase letters: $\boldsymbol{\Gamma, \ldots, \Theta}$
- Random variables are uppercase italic Latin letters $X, Y, X$. Lower case letters $x, y,z$ mean values of random variables. Sometimes, $X_i$ also denotes a value. If $X$ is a RV, then $X$ is written in words, and $x$ is given as a number.
  - Sample data use lowercase.
  - Population data use uppercase.
- Use Greek letters $\boldsymbol\theta, \boldsymbol\phi$ for parameters or $\alpha, \beta, \gamma$ for hyperparameters.



- $f(x) \approx g(x)$ (`\approx`) if the two functions are approximately equal in some sense depending on the context. 

- $f(x) \propto g(x)$ (`\propto`) If $f(x)$ is proportional to $g(x)$ we write. 

- $f(x) = O(g(x))$  We say that  “$f(x)$ is at most of order $g(x)$," if $\vert f(x)/g(x)\vert$ is bounded from above in some neighborhood of *x* = *c* (possibly *c* = ±∞). 

- $f(x) = o(g(x))$  we say that "$f(x)$ is of order less than $g(x)$," if $f(x)/g(x)$→ 0 when *x* → *c*. 
- $f(x)\sim g(x)$ (`\sim`) if $f(x)/g(x)$ → 1 when *x* → *c*. The two functions are then said to be "asymptotically equal". Notice that when $f(x)$ and $g(x)$ are asymptotically equal, then  $f(x)\approx g(x)$ and also $f(x) = O(g(x))$, but not vice versa.

Reference: <https://www.principlesofeconometrics.com/poe5/writing/abadir_magnus.pdf>



`crit pt`: critical point.

`cts`: continuous.

`def'n`: definition.

`cont'd`: continued.

`iff`: if and only if.

`Thm`: theorem

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



**Sample and population**

- DGP (data generating process) generates the data that we observe.
- Any quantity, the calculation of which requires one to know the DGP, is a population quantity



Normal Distribution $N(\mu, \sigma^2)$. The 2nd parameter is variance.

Degenerate distribution: sometimes called a constant distribution, is a distribution of a degenerate random variable — a constant with probability of 1. In other words, a random variable X has a single possible value. E.g., a weighted die (or one that has a number 6 on all faces) always lands on the number six, so the probability of a six (P(6)) is 1.


## **Geometry**

**Quadrant** (plane geometry)

The axes of a two-dimensional Cartesian system divide the plane into four infinite regions, called quadrants, each bounded by two half-axes.

-   the numbering goes counter-clockwise starting from the upper right ("northeast") quadrant.

<img src="https://drive.google.com/uc?id=1FlWhw7t0EIuk4PAV5-CTsLJGR0WZWGsl" alt="quadrant geometry" style="display: block; margin-right: auto; margin-left: auto; zoom:50%;" />

orthographic projection (正射投影): top view, front view, (right) side view.

锐角 acute angel

钝角 obtuse angel

直角 right angel

complementary angel 互余角 $\alpha+\beta=\frac{\pi}{2}$.

supplementary angel 互补角 $\alpha+\beta=\pi$.

<img src="https://drive.google.com/uc?id=1FlFGD-wVxC1UacQiLtg4W3NKAOcie-z7" alt="triangel" style="display: block; margin-right: auto; margin-left: auto; zoom:60%;" />

斜边 hypotenuse  /haɪˈpɑːtənuːs/

邻边 adjacent side

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

polyhedron 多面体

cube 正方体

cuboid 长方体

sector 扇形  

已知弧长 $A=\frac{1}{2}l\cdot r$。 $l$ 为扇形弧长，$r$ 为半径。与三角形面积类比，$\frac{1}{2}$底$\times$高，半径可看作底，弧长看作高。

已知圆心角 $A=\frac{n}{360}\pi r^2=\frac{1}{2}\theta\cdot r^2$。$n$单位为度数degree， $\theta$ 为圆心角，单位为弧度radian。

-   度数弧度转换公式：$\frac{n}{180}\pi=\theta$。

-   弧长公式：$l=\theta \cdot r$ (圆心角弧度 $\times$ 半径)。

    圆周长$C=2\pi r$，弧长$l=\frac{\theta}{2\pi}\cdot C=\frac{\theta}{2\pi}\cdot 2\pi r=\theta r$。

Volume of a sphere (ball) $V=\frac{4}{3}\pi r^3$, $r$ is radius. Surface $S=4\pi r^2$.



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

  

- cross product is a vector, used to calculate area of parallelogram, get normal vector; if $\vec{A}\times\vec{B}=0$, then $\vec{A}\parallel\vec{B}$ (<span style='color:#32CD32'>parallel</span>);

  - The magnitude of the cross product is the same as the magnitude of one of them, multiplied by the component of one vector that is perpendicular to the other. 
  - If $\vec{A}\parallel\vec{B}$, no component is perpendicular to the other vector. Hence, the cross product is 0 although you can still find a perpendicular vector to both of these. 

  $$
  \begin{align*}
  \vec{A}\times\vec{B} &=\vert\vec{A}\vert\vert\vec{B}\vert \sin\theta\cdot\vec{n},\; \vec{n} \textrm{ decided by right-hand rule.} \\
  \vec{A}\times\vec{A}&=0 \quad (\sin0=0\textrm{, area of a line is 0})
  \end{align*}
  $$



**Polynomial and Exponential**

$A^B$: $A$ is called the base, $B$ is exponent.

Polynomials, $x$ in the base. constant ($x^0$), linear ($x$), quadratic ($x^2$), cubic ($x^3$), quartic terms ($x^4$).

$x^4$ read as $x$ to the 4th or the quartic term.

 $2^{16}$ is read as "2 to the 16th power" or "2 to the power of 16" in formal speech. Commonly, a ellipsis of the first expression is used "2 to the 16th" (ordinal) or "2 to the 16" (w/o ordinal).

For example, a polynomial $x^{109} + 9x^5 − 2x^2$ is most likely pronounced:

>   x to the hundred and nine plus nine x to the fifth minus two x squared.

**Exponential** $x$ in the exponent.

If there is a variable in the exponent, the ordinal is not used. $x^y$ is read as "x to <span style='color:#32CD32'>*the*</span> y". The -th is dropped.



1 micrometer = $10^{-6}$ meter

1 nanometer = $10^{-9}$ meter



**Arithmetic Sequence/Progression** 等差数列

$a_1, a_2, ..., a_n$ has common difference $d$, $n$ is the number of terms. Some useful formulas:

-   the $n$-th term $a_n=a_1+(n-1)d$ 
-   sum of $n$ terms $S_n=\frac{(a_1+a_n)n}{2}=na_1+\frac{n(n-1)}{2}d$
-   number of terms $n=\frac{a_n-a_1}{d}+1$
-   common difference $d=\frac{a_n-a_1}{n-1}$

**Geometric Sequence/Progression** 等比数列

$a_1, a_2, ..., a_n$ has common ratio $q$.

-   $a_n=a_1\cdot q^{n-1}$
-   $S_n= \frac{a_1(1-q^n)}{1-q}$



**Distribution Functions**

Visualization tool: <https://seeing-theory.brown.edu/probability-distributions/>

Plot a function: <https://www.desmos.com/calculator>



**Change of variable formula**

Given the distribution of $X$, we can obtain the distribution of a continuous function of $X$, e.g. $Y=g(X)$.


$$
\begin{align*}
F_Y(y)&=P(Y\le y)=P\left(g(X)\le y\right) \\
&=\left\{
	\begin{array}{ll}
	P\left(X\le g^{-1}(y)\right) = F_X(g^{-1}(y)) & \text{when $g(x)$ is $\uparrow$} \\
	P\left(X\ge g^{-1}(y)\right) = 1- F_X(g^{-1}(y))  & \text{when $g(x)$ is $\downarrow$}
	\end{array} \right. \\
f_Y(y) &= f_X(g^{-1}(y))\left\vert \frac{\partial }{\partial y} g^{-1}(y) \right\vert
\end{align*}
$$


**Law of iterated expectations** LIE  


$$
\begin{align*}
\mathbb{E}_Y(Y) = \mathbb{E}_X\left[\mathbb{E}_{Y\vert X}\right(Y\vert X=x\left)\right]
\end{align*}
$$

or more succinctly  

$$
\begin{align*}
\mathbb{E}[Y] = \mathbb{E}\left[\mathbb{E}\right(Y\vert X=x\left)\right].
\end{align*}
$$

Suppose $\mathbb{E}(Y\vert X)=0$, then   

$$
\begin{align*}
1. \quad & \mathbb{E}[Y] = \mathbb{E}\left[\mathbb{E}\right(Y\vert X=x\left)\right] = 0 \\
2. \quad & \mathbb{E}[g(X)\cdot Y] = \mathbb{E}\left[\mathbb{E}[g(X)\cdot Y\vert X]\right] = \mathbb{E}\left[g(X)\cdot \mathbb{E}[Y\vert X]\right] = \mathbb{E}[g(X)\cdot0]=0
\end{align*}
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


Expectations of Functions of RVs

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


Variance is also an expectation by setting $g(X)=(X-\mathbb{E}(X))^2$. In other words, $Var(X)=\mathbb{E}\left[(X-\mathbb{E}(X))^2\right]$.

$$
\begin{align*}
Var(X) = \mathbb{E}[(X-\mathbb{E}(X))^2] = \left\{
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
Var(X) &= \mathbb{E}(X-E[X])^2 \\ 
			 &= \sum_x (x-\mathbb{E}[X])^2 f(x) \\
			 &= (0-\theta)^2 \times f(0) + (1-\theta)^2\times f(1) \\
			 &= \theta^2(1-\theta) + (1-\theta)^2\theta \\
			 &= \theta (1-\theta).
\end{align*}
$$

Alternative derivation: Since $0^2=0$ and $1^2=1$, we have $X^2=X$ implying that $\mathbb{E}(X^2)=\mathbb{E}(X)=\theta$. Therefore,

$$
\begin{align*}
Var(X)=\mathbb{E}[X^2]-(\mathbb{E}[X])^2 = \theta-\theta^2
\end{align*}
$$




**Sample mean** Let $X_1, \ldots, X_n$ denote $n$ observations on a variable $X$, the sample mean is

$$
\begin{align*}
\overline{Y}=\frac{1}{n}\sum_{i=1}^nX_i
\end{align*}
$$


Sample variance use either 

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



**Covariance and Correlation**

Covariance and correlaation measure the linear association btw two RVs $X$ and $Y$

$$
\textrm{Cov}(X, Y) = \mathbb{E}\{[X-\mathbb{E}(X)][Y-\mathbb{E}(Y)]\}
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

Correlation is a scaled measure of covariance:

$$
\textrm{Corr}(X,Y)=\frac{\textrm{Cov}(X, Y)}{\sqrt{\text{Var}(X)\text{Var}(Y)}}
$$

If $\textrm{Corr}(X,Y)=0$, we say that $X$ and $Y$ are <span style='color:#32CD32'>uncorrelated</span> or orthogonal, denoted by $X {\color{#32CD32}\perp} Y$ (perpendicular symbol).


$X {\color{#32CD32}\indep} Y$ (double perpendicular symbol) denotes $X$ and $Y$ are <span style='color:#32CD32'>independent</span>.

$X \indep Y \Rightarrow X \perp Y$,  in plain language, independence implies zero correlation. 


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

Marginals

This is called marginalizaing or integrating out $X_2$ to get the marginal of $X_1$.

$$
f_1(k) =  \left\{
	\begin{array}{ll}
	\int_{-\infty}^\infty f(k, x_2) dx_2 & \text{continuous} \\
	\sum_{x_2} f(X_1=k,X_2=x_2) & \text{discrete}
	\end{array} \right.  
$$

Marginalizaing the joint density w.r.t. $X_1$ to get the marginal of $X_2$.
$$
f_2(k) =  \left\{
	\begin{array}{ll}
	\int_{-\infty}^\infty f(x_1,k) dx_1 & \text{continuous} \\
	\sum_{x_1} f(X_1=x_1,X_2=k) & \text{discrete}
	\end{array} \right. 
$$


**Conditioning**

Conditional density:

$$
f(x_1\vert x_2)=\frac{f(X_1=x_1, X_2=x_2)}{f(X_2=x_2)} \\
f(x_2\vert x_1)=\frac{f(X_1=x_1, X_2=x_2)}{f(X_1=x_1)} 
$$

or more succinctly

$$
f(x_1\vert x_2)=\frac{f(x_1, x_2)}{f(x_2)} \\
f(x_2\vert x_1)=\frac{f(x_1, x_2)}{f(x_1)} .
$$

Conditional cdf:

$$
\begin{aligned}
F_{X_1}(x_1\vert X_2=x_2) &=  P(X_1\le x_1 \vert X_2=x_2) \\
&= \left\{
\begin{array}{ll}
	\int_{-\infty}^{x_1} f(s,x_2) ds & \text{continuous} \\
	\sum_{x\le x_1} f(X_1=s,X_2=x2)  &\text{discrete}
	\end{array} \right. 
\end{aligned}
$$

**Moments**

Unconditional Moments

$$
\begin{aligned}
\mathbb{E}(g(x)) &= \int_{-\infty}^\infty g(x){\color{red}f(x)}dx &\text{continuous} \\
\mathbb{E}(g(x)) &= \sum_x g(x){\color{red}f(x)} & \text{discrete}
\end{aligned}
$$

Conditional Moments

$$
\begin{aligned}
\mathbb{E}(g(x) \vert Y=g) &= \int_{-\infty}^\infty g(x){\color{#32CD32}f(x\vert Y=g)}dx &\text{continuous} \\
\mathbb{E}(g(x) \vert Y=g) &= \sum_x g(x){\color{#32CD32}f(x\vert Y=g)} & \text{discrete}
\end{aligned}
$$

Note: 
- For <span style='color:red'>unconditional</span> moments, use the appropriate <span style='color:red'>unconditional</span> density.
- For <span style='color:#32CD32'>conditional</span> moments, use the appropriate <span style='color:#32CD32'>conditional</span> density.


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

Note that this <span style='color:#32CD32'>does not imply</span> $X_1 \indep X_2$!
E.g., $X_1$ and $X_2$ can be returns on two equities where $X_3$ is some global macroeconomic factor affecting multiple variables at once (e.g. federal reserve interest rate).

Another example for $X_1, X_2$ would be wages and level of education, whereas $X_3$ is level of intelligence.



Linear Algebra
<https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab>


**Convergence**

- Convergence in Probabiliy, $\lim_{n\to\infty}P(\vert X_n-c\vert < \varepsilon) =1$, denoted as $\plim_{n\to\infty}X_n=c$, or $X_n \xrightarrow{p} c$.
- Almost Sure Convergence, $P(\lim_{n\to\infty}\vert X_n-c\vert =0)=1$, denoted as $X_n \xrightarrow{a.s.} c$.
- Convergence in mean square, $\lim_{n\to\infty}\mathbb{E}[(X_n-c)^2]=0$,  denoted as $X_n \xrightarrow{m.s.} c$.
- Convergence in distribution, $P(X_n\le x) \rightarrow P(X\le x)$ as $n\rightarrow \infty$, $X_n\xrightarrow{d}X$. If $X\sim N(\mu, \sigma^2)$, then $X_n \xrightarrow{d} N(\mu, \sigma^2)$.

Note: 
- Convergence in probability is weaker than both a.s. and m.s. convergence. Obtaining any type of convergence is sufficient. In certain cases, proving one type can be easier than another type.
- Convergence in probability implies convergence in distribution. Convergence in probability means that two objects converge to each other. Convergence in distribution means that the distributions of two different objects become the same.

**Consistent estimator**

$\hat{\theta}$ is a consistent estimator of $\theta$ if 

$$
  \hat{\theta} \xrightarrow{p} \theta.
$$


**Law of Large Numbers** (LLN)
- Week LLN\
  Let $X_1, \ldots, X_n$ be an iid sequence with mean $\mathbb{E}(X_i)=\mu$ and $\text{Var}(X_i)=\sigma^2$. Then,

  $$
  \frac{1}{n}\sum_{i=1}^nX_i \xrightarrow{p} \mathbb{E}(X_i).
  $$

  LLN tells us that the sample mean is a consistent estimator of the expected value.

- Kolmogorov's LLN 

  $$
  \frac{1}{n}\sum_{i=1}^nX_i \xrightarrow{a.s.} \mathbb{E}(X_i).
  $$

Unbiasedness vs Consistency
- Unbiasedness, $\mathbb{E}(\hat{\theta})=\theta$, is a finite sample property, that holds for any sample size.
- Consistency, $\hat{\theta}\xrightarrow{p}\theta$, is a asymptotic property, that holds in the limit as $n\to \infty$.
- Note: neither property implies the other.

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
\sqrt{n} (\overline{X}-\mu) \xrightarrow{d} N(0,\sigma^2).
$$

Note: The CLT is a very powerful result. $X_1, \ldots, X_n$ can be from any possible distribution (with finite mean and variance), and still their normalised sample mean will be standard normal.


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
\gamma(t,\tau)=Cov(X_t, X_{t-\tau})
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
1.&\ \mu_t=0, \ and \\
2.&\ \gamma_\tau=\left\{
	\begin{array}{ll}
	\sigma^2 & \text{when $\tau=0$} \\
	0 & \text{when $\tau\neq0$}
	\end{array} \right.
\end{align*}
$$

In short, WN has expectation 0 and finite variance.



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

Assume that the constant $c$ and the initial value $X_0$ are set to zero, through recursice substitution we will get the representation:
$$
\begin{align*}
X_t=\sum^t_{i=1}\epsilon_i
\end{align*}
$$
Moment functions:

1. $\mu_t=0$
2. $Var(X_t)=t\sigma^2$
3. $\gamma(t,\tau)=Cov(X_t,X_{t-\tau})=(t-\tau)\sigma^2$, for $\tau\lt t$.
4. $\rho(t,\tau)=\sqrt{1-\frac{\tau}{t}}$

Notice that autocovariance is strictly positive, and since it depends on $t$ not only on the lags $\tau$, the random walk is not covariance stationary.



AR(1) process

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

https://atmos.washington.edu/~breth/classes/AS552/lect/lect24.pdf

Python code: https://matthew-brett.github.io/teaching/smoothing_intro.html







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

-   **Econometric Analysis** , 5th Edition, by William H. Greene, Prentice Hall, 2003.

    **Time Series Analysis**, by J. D. Hamilton, Princeton University Press, 1994.

    **Estimation and Inference in Econometrics**, by R. Davidon and J. MacKinnon, Oxford University Press, 1993.

    **Econometric Analysis of Cross Section and Panel Data**, by J. Wooldridge, MIT Press, 1999.

    **Microeconometrics: Methods and Applications**, Cameron, A. C. and Trivedi, P. K., Cambridge University Press, 2005.

-   **Core Metrics textbooks**

    - Casella, G. and Berger, R.L. (2002) ***Statistical Inference***. 2nd ed. Duxbury.
    - Hendry, D.F. and Nielsen, B. (2007) ***Econometric Modeling***. Princeton.
    - Hoel, P.G., Port, S.C. and Stone, C.J. (1971) ***Introduction to Probability***. Boston: Houghton-Mifflin.



