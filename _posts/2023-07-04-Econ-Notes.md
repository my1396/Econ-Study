---
layout: post
title: Econometric Notes
tag: study
modified_date: 2023-10-05
---
## Notation

$\mathbb{E}_Y$ and $\mathrm{Var}_Y$ denote expectation over $Y$ and variance over $Y$.

Blackboard bold 黑板粗体 (`\mathbb`) is often used to denote **sets of numbers**, e.g. $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{O}$, or a general field $\mathbb{F}$ or $\mathbb{K}$, and in probability to denote expectation of a random variable $\mathbb{E}(X)$ or probability of an event $\mathbb{P}(E)$. Sometimes you see a sphere denoted $\mathbb{S}$ or a torus denoted $\mathbb{T}$. 

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

- $f(x) = O(g(x))$  We say that  ``$f(x)$ is at most of order $g(x)$", if $\vert f(x)/g(x)\vert$ is bounded from above in some neighborhood of *x* = *c* (possibly *c* = ±∞). 

- $f(x) = o(g(x))$  we say that ``$f(x)$ is of order less than $g(x)$", if $f(x)/g(x)$→ 0 when *x* → *c*. 
- $f(x)\sim g(x)$ (`\sim`) if $f(x)/g(x)$ → 1 when *x* → *c*. The two functions are then said to be ``asymptotically equal". Notice that when $f(x)$ and $g(x)$ are asymptotically equal, then  $f(x)\approx g(x)$ and also $f(x) = O(g(x))$, but not vice versa.

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

-   从小到大，表示大数字减小数字。
-   从大到小，表示大数字加小数字。
-   常见罗马数字 **IV(4)**, V (5), Ⅵ (6), Ⅶ (7), ⅦI (8), **IX(9)**.

domain 定义域

range 值域



**Sample and population**

- DGP (data generating process) generates the data that we observe.
- Any quantity, the calculation of which requires one to know the DGP, is a population quantity



## **Geometry**

**Quadrant** (plane geometry)

The axes of a two-dimensional Cartesian system divide the plane into four infinite regions, called quadrants, each bounded by two half-axes.

-   the numbering goes counter-clockwise starting from the upper right ("northeast") quadrant.

<img src="https://drive.google.com/uc?id=1FlWhw7t0EIuk4PAV5-CTsLJGR0WZWGsl" alt="quadrant geometry" style="zoom:50%;" />

orthographic projection (正射投影): top view, front view, (right) side view.

锐角 acute angel

钝角 obtuse angel

直角 right angel

complementary angel 互余角 $\alpha+\beta=\frac{\pi}{2}$.

supplementary angel 互补角 $\alpha+\beta=\pi$.

<img src="https://drive.google.com/uc?id=1FlFGD-wVxC1UacQiLtg4W3NKAOcie-z7" alt="triangel" style="zoom:60%;" />

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

tetrahedron / ˌtetrəˈhiːdrən/ 四面体, also called "tiangular pyramid", 三角锥, is a polyhedron composed of four triangular faces

polyhedron 多面体

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
  \vec{A}\cdot\vec{B} &= \sum a_ib_i \\
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

$A^B$ A is base, B is exponent.

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



## **Trig identities**

$\mathrm{sin}\theta$ 奇函数

$\mathrm{cos}\theta$ 偶函数

$\mathrm{sin}(\theta\pm\frac{k\pi}{2})$,  $\mathrm{cos}(\theta\pm\frac{k\pi}{2})$ 奇变偶不变，符号看象限。 

-   根据$k$ ，决定是否变函数。 $k$ 为奇数，$\mathrm{sin}$ 变 $\mathrm{cos}$，$\mathrm{cos}$ 变 $\mathrm{sin}$。$k$ 为偶数，则函数名不变。
-   符号由原函数决定, assuming $0<\theta<\frac{\pi}{2}$为锐角，看$\theta\pm\frac{k\pi}{2}$在原函数的正负。实际上 $\theta$ 可以是任意角度，但如果是钝角，完全可以$k:=k+1$化为锐角；否则，函数处于未化简完全的状态。
-   e.g., $\mathrm{cos}(\frac{\pi}{2}-\theta)=\mathrm{sin}\theta$, $k=1$为奇数, 函数名变为$\mathrm{sin}$; 当$\theta$为锐角时，$\frac{\pi}{2}-\theta$ 在第一象限，$\mathrm{cos}(\frac{\pi}{2}-\theta)$为正。 



double-angel formula 倍角公式

-   $\mathrm{cos}(2\theta)=\mathrm{cos}^2\theta-\mathrm{sin}^2\theta$

-   $\mathrm{sin}(2\theta)=2\mathrm{sin}\theta\cdot \mathrm{cos}\theta$, 2 不要落下了！

half-angel formula 半角公式 (降幂公式) used to get rid of the power

-   $\mathrm{cos}^2\theta=\frac{1+\mathrm{cos}(2\theta)}{2}$

-   $\mathrm{sin}^2\theta=\frac{1-\mathrm{cos}(2\theta)}{2}$



**和差公式** Angle sum and difference identities

$\mathrm{sin}(\alpha+\beta)=\mathrm{sin}\alpha\cdot\mathrm{cos}\beta+\mathrm{cos}\alpha\cdot\mathrm{sin}\beta$

$\mathrm{sin}(\alpha-\beta)=\mathrm{sin}\alpha\cdot\mathrm{cos}\beta-\mathrm{cos}\alpha\cdot\mathrm{sin}\beta$

$\mathrm{cos}(\alpha+\beta)=\mathrm{cos}\alpha\cdot\mathrm{cos}\beta-\mathrm{sin}\alpha\cdot\mathrm{sin}\beta$

$\mathrm{cos}(\alpha-\beta)=\mathrm{cos}\alpha\cdot\mathrm{cos}\beta+\mathrm{sin}\alpha\cdot\mathrm{sin}\beta$



**积化和差**公式可以由和差公式得来。(product-to-sum identities)



**和差化积**公式 (sum-to-product identities)

正加正，正在前； $\mathrm{sin}\alpha +\mathrm{sin}\beta=2\, \mathrm{sin}\frac{\alpha+\beta}{2}\cdot\mathrm{cos}\frac{\alpha-\beta}{2}$

正减余在先； $\mathrm{sin}\alpha - \mathrm{sin}\beta=2\, \mathrm{cos}\frac{\alpha+\beta}{2}\cdot\mathrm{sin}\frac{\alpha-\beta}{2}$

余加全是余；$\mathrm{cos}\alpha +\mathrm{cos}\beta=2\, \mathrm{cos}\frac{\alpha+\beta}{2}\cdot\mathrm{cos}\frac{\alpha-\beta}{2}$

余减负正弦；$\mathrm{cos}\alpha - \mathrm{cos}\beta=-2\, \mathrm{sin}\frac{\alpha+\beta}{2}\cdot\mathrm{sin}\frac{\alpha-\beta}{2}$





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
	\sigma^2 & \mbox{when $\tau=0$} \\
	0 & \mbox{when $\tau\neq0$}
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





## Calculus

1st derivative

$y'(x)=0$ max/min point, change of directions (from up to down if max, from down to up if min).

2nd derivative

$y^{\prime\prime}=0$ inflection point, change of concavity.



How to find **min/max** pt.

-   look at critical points (where $f'=0$), end points, and discontinuities. Critical values are the values of the function where $x$ equal to critical points.

    -   1st derivative rule, then you get critical points. Have to check whether it is min or max. Two ways of doing it

        1.   calculate end points and compare to critical points;
        2.   calculate $f^{\prime\prime}$, if $f^{\prime\prime}<0$ then max; if $f^{\prime\prime}>0$ then min; (2nd derivate tell how 1st derivative changes. If at min, the func will increase, i.e., $f'$ $\uparrow$; if at max, the func will decrease, i.e., $f' \downarrow$. )

        -   Note: it is NOT recomended to calculate the 2nd derivative b/c usually it is easier to calculate the end points. 2nd derivatives are usually difficult to find if you have a complicated func.

-   max/min point corresponds to critical points; alternatively, where is max/min achieved?

-   max/min value corresponds to critical value;



**Newton's Method**
$$
\begin{align*}
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
\end{align*}
$$
Newton's method works well if $i$) $\vert f'\vert$ is not too small;  $ii$) $\vert f^{\prime\prime}\vert$ is not too big; and $iii$) $x_0$ is nearby $x$.

Newton's method fails: $i$) find an unexpected root (depending on where the initial guess is); $ii$) completely fail. It repeats in a cycle, and never converges to a single value.

<img src="https://drive.google.com/uc?id=1B7LjCAsBGxIGPKAHy-ogyZtuxjr-Qf5D" alt="Fail of Newton method illustration" style="zoom:30%;" />





**MVT vs. IVT**

-   The **mean value theorem** is all about the differentiable functions and derivatives, whereas the **intermediate value theorem** is about the continuous function. 
-   The mean value theorem guarantees that the derivatives have certain values, whereas the intermediate value theorem guarantees that the function has certain values between two given values.



Anti-differentiation used interchangeablely with Integration.

Anti-derivatives $\Longleftrightarrow$ Indefinite Integrals



### **Integral formulas**

Trigonometric integrals

1.   $\int \frac{1}{\sqrt{1-x^2}} dx=\mathrm{sin}^{-1}x+c$, note that $\mathrm{sin}^{-1}x$ denotes "inverse sin" or $\mathrm{arcsin}(x)$, not $\frac{1}{\mathrm{sin}x}$.
2.   $\int -\frac{1}{\sqrt{1-x^2}} dx=\mathrm{cos}^{-1}x+c$
3.   $\int \frac{1}{1+x^2} dx=\mathrm{tan}^{-1}x+c$
4.   $(\tan x)'=\sec^2x$, or $\int \mathrm{sec}^2x\,dx=\mathrm{tan}x+c$.
5.   $\sec(x)'=\sec x\tan x$, or $\int \sec x\tan x\, dx=\sec x +c$.
6.   $\int \mathrm{tan}x\,dx=-\ln(\cos x)+c$.
7.   $\int \sec x\,dx=\ln(\sec x+\tan x)+c$, substitution $u=\sec x+\tan x$.



Common integrals/ derivatives

$\int\frac{1}{y}dy=\ln\vert y\vert +c$

$\sqrt{x}=\frac{1}{2\sqrt{x}}$

**Trig Identities**

$\sec^2=1+\tan^2$.



**FTC2**

$f$ is continuous
$$
\begin{align*}
\frac{d}{dx}\int_a^x f(t)dt=f(x)
\end{align*}
$$

-   important to differentiate variable of integrand $t$ from the upper limit $x$. Use different letters!



**Trig integrals and Substitution**

To integrate  $\int$cos$^j$𝑥 sin$^k$𝑥 𝑑𝑥  use the following strategies:

1. If  𝑘  is odd, rewrite  sin$^k$𝑥=sin$^{𝑘−1}$𝑥sin𝑥  and use the identity  sin$^2$𝑥=1−cos$^2$𝑥  to rewrite  sin$^{𝑘−1}$𝑥  in terms of  cos𝑥 . Integrate using the substitution  𝑢=cos𝑥 . This substitution makes  𝑑𝑢=−sin𝑥𝑑𝑥. 

2. If  𝑗  is odd, rewrite  cos$^𝑗$𝑥=cos$^{𝑗−1}$𝑥cos𝑥  and use the identity  cos$^2$𝑥=1−sin$^2$𝑥  to rewrite  $\mathrm{cos}^{𝑗−1}x$  in terms of  sin𝑥 . Integrate using the substitution  𝑢=sin𝑥 . This substitution makes  𝑑𝑢=cos𝑥𝑑𝑥.  (Note: If both  𝑗  and  𝑘  are odd, either strategy 1 or strategy 2 may be used.)

3. If both  𝑗  and  𝑘  are even, use  sin$^2$𝑥=$\frac{1−\cos(2𝑥)}{2}$  and  cos$^2$𝑥=$\frac{1+\cos(2𝑥)}{2}$ . After applying these formulas, simplify and reapply strategies 1 through 3 as appropriate.

>   Summary: 
>
>   1.   integrand only includes powers of $\mathrm{sin}x$ and $\mathrm{cos}x$.
>
>   2.   find the odd power and separate 1 as derivative of the substitution. Rewrite the integrand as a function of the other trig.
>   3.   if only even exponents are present, use half-angel fornula to lower the power (double the trig angel) until you have an odd exponent.



Integrating ∫tan$^𝑘$𝑥sec$^𝑗$𝑥𝑑𝑥

1.   If 𝑗 is even and 𝑗≥2, rewrite sec$^𝑗$𝑥=sec$^{𝑗−2}$𝑥sec$^2$𝑥 and use sec$^2$𝑥=tan$^2$𝑥+1 to rewrite sec$^{𝑗−2}$𝑥 in terms of tan𝑥. Let 𝑢=tan𝑥 and 𝑑𝑢=sec$^2$𝑥.

2.   If 𝑘 is odd and 𝑗≥1, rewrite tan$^𝑘$𝑥sec$^𝑗$𝑥=tan$^{𝑘−1}$𝑥sec$^{𝑗−1}$𝑥sec𝑥tan𝑥 and use tan$^2$𝑥=sec$^2$𝑥−1 to rewrite tan$^{𝑘−1}$𝑥 in terms of sec𝑥. Let 𝑢=sec𝑥 and 𝑑𝑢=sec𝑥tan𝑥𝑑𝑥. (Note: If 𝑗 is even and 𝑘 is odd, then either strategy 1 or strategy 2 may be used.)

3.   If 𝑘 is odd where 𝑘≥3 and 𝑗=0, rewrite tan$^𝑘$𝑥=tan$^{𝑘−2}$𝑥tan$^2$𝑥=tan$^{𝑘−2}$𝑥(sec$^2$𝑥−1)=tan$^{𝑘−2}$𝑥sec$^2$𝑥−tan$^{𝑘−2}$𝑥. It may be necessary to repeat this process on the tan$^{𝑘−2}$𝑥 term.

4.   If 𝑘 is even and 𝑗 is odd, then use tan$^2$𝑥=sec$^2$𝑥−1 to express tan$^𝑘$𝑥 in terms of sec𝑥. Use integration by parts to integrate odd powers of sec𝑥.



**Reduction formulas**

1.   $\int \sec^n xdx=\frac{1}{n-1}\sec^{n-2}x\tan x+\frac{n-2}{n-1}\int \sec^{n-2}xdx$, $n$​ is odd. Verified by applying integration by parts.
2.   $\int \tan ^n xdx=\frac{1}{n-1}\tan ^{n-1}x-\int\tan^{n-2}x dx$, $n$ is odd.



**Method of Substitution**

1.   The original integrand (in $g(x)dx$ or $h(t)dt$ ... ) can be expressed as $f(u)\,du$.
2.   Usually $g(x)$ and $h(t)$ coule be a mess, but it is much easier to find the anti-derivative of $f(u)$.



___

Semi-parametric models

-   Method of Moments
-   quantile regression



**Textbooks**

-   **Econometric Analysis** , 5th Edition, by William H. Greene, Prentice Hall, 2003.
    
    **Time Series Analysis**, by J. D. Hamilton, Princeton University Press, 1994.
    
    **Estimation and Inference in Econometrics**, by R. Davidon and J. MacKinnon, Oxford University Press, 1993.
    
    **Econometric Analysis of Cross Section and Panel Data**, by J. Wooldridge, MIT Press, 1999.



