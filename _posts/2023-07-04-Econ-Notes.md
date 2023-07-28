---
layout: post
title: Econometric Notes
category: learning
update: 2023-07-05
---
## Notation

$\mathbb{E}_Y$ and $\mathrm{Var}_Y$ denote expectation over $Y$ and variance over $Y$.

It seems that blackboard bold (`\mathbb`) is often used to denote **sets of numbers**, e.g. $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{O}$, or a general field $\mathbb{F}$ or $\mathbb{K}$, and in probability to denote expectation of a random variable $\mathbb{E}(X)$ or probability of an event $\mathbb{P}(E)$. Sometimes you see a sphere denoted $\mathbb{S}$ or a torus denoted $\mathbb{T}$. 



Crit pt: critical point.

cts: continuous.

def'n: definition.

con't: continued.

**Q.E.D**: Latin words to indicate this is the *end* of a mathematical proof. At the begining, you simply write `Proof:`.

Ceteris paribus:  Latin phrase that generally means "all other things being equal."

axiom or postulate: a fundamental assumption that is accepted without proof.

theorem: a statement that has been proven to be true based on axioms and other theorems.

preposition: a theorem of less importance, or one that is considered so elementary or immediately obvious, that it may be stated without proof.

lemma: an "accessory preposition" - a preposition with little applicability outside its use in a particular proof. Over time a lemma may gain in importance and be considered a *theorem*, though the term "lemma" is usually kept as part of its name.

corollary: is a theorem of less importance which can be readily deduced from a previous, more notable statement.  A corollary may also be a restatement of a theorem in a simpler form, or for a special case. 

orthographic projection (正射投影): top view, front view, (right) side view.



**Polynomial and Exponential**

$A^B$ A is base, B is exponent.

Polynomials, $x$ in the base. constant ($x^0$), linear ($x$), quadratic ($x^2$), cubic ($x^3$), quartic terms ($x^4$).

$x^4$ read as $x$ to the 4th or the quartic term.

 $2^{16}$ is read as "2 to the 16th power" or "2 to the power of 16" in formal speech. Commonly, a ellipsis of the first expression is used "2 to the 16th" (ordinal) or "2 to the 16" (w/o ordinal).

For example, a polynomial $x^{109} + 9x^5 − 2x^2$ is most likely pronounced:

>   x to the hundred and nine plus nine x to the fifth minus two x squared.

**Exponential** $x$ in the exponent.

If there is a variable in the exponent, the ordinal is not used. $x^y$ is read as "x to *the* y". The -th is dropped.



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





## Stochastic Process

A stochastic process $X_t$ is a family of random variables. At a specific time point $t$, $X_t$ is a random variable with a specific density function. A stochastic process is defined in a probability space $(\Omega, \mathcal{F}, P)$.

Mean function $\mu_t$ 

$$
\mu_t = \mathbb{E}[X_t] = \int_{\mathbb{R}}xdF_t(X)
$$

$\mu_t$ depends on time $t$, as, for example, processes with a seasonal or periodical structure or processes with a deterministic trend.

**Autocovariance Function**

$$
\gamma(t,\tau)=Cov(X_t, X_{t-\tau})
$$

If we define <span style='color:red'>**covariance stationary**</span>, then $\gamma(t,\tau)=\gamma_\tau$, means covaraince only depends on time interval apart, not start point.


Autocorrelation Function (ACF)

$$
\rho_{\tau}=\frac{\gamma_{\tau}}{\gamma_0}
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
X_t=c+X_{t-1}+\epsilon_t
$$

with a constant $c$ and **white noise** $\epsilon_t$. 

$Z_t=X_t-X_{t-1}=c+\epsilon_t$ , if $c$ is not zero, then we say $X_t$  has a drift, 

$c>0$ we say drift upward,

$c<0$ we say drift downward.

Assume that the constant $c$ and the initial value $X_0$ are set to zero, through recursice substitution we will get the representation:
$$
X_t=\sum^t_{i=1}\epsilon_i
$$
Moment functions:

1. $\mu_t=0$
2. $Var(X_t)=t\sigma^2$
3. $\gamma(t,\tau)=Cov(X_t,X_{t-\tau})=(t-\tau)\sigma^2$, for $\tau\lt t$.
4. $\rho(t,\tau)=\sqrt{1-\frac{\tau}{t}}$

Notice that autocovariance is strictly positive, and since it depends on $t$ not only on the lags $\tau$, the random walk is not covariance stationary.



AR(1) process

$$
X_t=c+\alpha X_{t-1}+\epsilon_t
$$

with $ \vert\alpha \vert<1$.

By iterative substitutions, 

$$
X_t=c \frac{1-\alpha^k}{1-\alpha}+\alpha^kX_{t-k}+\sum^{k-1}_{i=0}\alpha^i\epsilon_{t-i}
$$

For $K\to \infty$,

$$
X_t=c\frac{1}{1-\alpha}+\sum^\infty_{i=0}\alpha^i\epsilon_{t-i}
$$

Moment functions:

1. $\mu_t=c\frac{1}{1-\alpha}$
2. $\gamma_\tau=\frac{\sigma^2}{1-\alpha^2}\alpha^\tau$
3. $\rho_\tau=\alpha^\tau$

For ACF $\rho_\tau$, if $\alpha>0$, this function is strictly positive, for $\alpha<0$, it alternates around zero. For small $\alpha$, like 0.5, it converges very fast; for large $\alpha$, like 0.99, it converges quite slow.



**Markov Process**

A stochastic process has the Markov Property if for all $t\in \mathbb{Z}$ and $k\geq 1$

$$
F_{t|t-1,\ldots,t-k}(x_t|x_{t-1},\ldots, x_{t-k})=F_{t|t-1}(x_t|x_{t-1})
$$

In other words, the conditional distribution of a Markov process at a specific point in time is entirely determined by the condition of the system at the previous date.

Two examples: random walk with independent $\epsilon_t$ and the AR(1) process with independent white noise.



**Martingale**

$$
E[X_t|X_{t-1}=x_{t-1},\ldots,X_{t-k}=x_{t-k}]=x_{t-1}
$$

For martingale, only one statement about the conditional expectation is made; while for Markov process, statements on the entire conditional distribution are made.



**Lag Operator**

$LX_t=X_{t-1}$ and  $L^kX_t=X_{t-k}$

$\Delta=1-L$, $\Delta X_t=X_t-X_{t-1}$ and $\Delta^k=(1-L)^k$



**Unit Root Tests**
$$
X_t=c+\alpha X_{t-1}+\epsilon_t
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











**log-transformed Models**

1.  **Only the dependent/response variable is log-transformed**. Exponentiate the coefficient. This gives the multiplicative factor for every one-unit increase in the independent variable. Example: the coefficient is 0.198. exp(0.198) = 1.218962. For every one-unit increase in the independent variable, our dependent variable increases by a factor of about 1.22, or 22%. Recall that multiplying a number by 1.22 is the same as increasing the number by 22%. Likewise, multiplying a number by, say 0.84, is the same as decreasing the number by 1 – 0.84 = 0.16, or 16%. 
2.  **Only independent/predictor variable(s) is log-transformed**. Divide the coefficient by 100. This tells us that a 1% increase in the independent variable increases (or decreases) the dependent variable by (coefficient/100) units. Example: the coefficient is 0.198. 0.198/100 = 0.00198. For every 1% increase in the independent variable, our dependent variable increases by about 0.002. For x percent increase, multiply the coefficient by log(1.x). Example: For every 10% increase in the independent variable, our dependent variable increases by about 0.198 * log(1.10) = 0.02.
3.  **Both dependent/response variable and independent/predictor variable(s) are log-transformed**. Interpret the coefficient as the percent increase in the dependent variable for every 1% increase in the independent variable. Example: the coefficient is 0.198. For every 1% increase in the independent variable, our dependent variable increases by about 0.20%. For x percent increase, calculate 1.x to the power of the coefficient, subtract 1, and multiply by 100. Example: For every 20% increase in the independent variable, our dependent variable increases by about (1.20 0.198 – 1) * 100 = 3.7 percent.



___

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
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$
Newton's method works well if $i$) $\vert f'\vert$ is not too small;  $ii$) $\vert f^{\prime\prime}\vert$ is not too big; and $iii$) $x_0$ is nearby $x$.

Newton's method fails: $i$) find an unexpected root (depending on where the initial guess is); $ii$) completely fail. It repeats in a cycle, and never converges to a single value.

<img src="{{ site.baseurl}}/images/image-20230709110507061.png" alt="image-20230709110507061" style="zoom:30%;" />





**MVT vs. IVT**

-   The **mean value theorem** is all about the differentiable functions and derivatives, whereas the **intermediate value theorem** is about the continuous function. 
-   The mean value theorem guarantees that the derivatives have certain values, whereas the intermediate value theorem guarantees that the function has certain values between two given values.



Anti-differentiation used interchangeablely with Integration.

Anti-derivatives $\Longleftrightarrow$ Indefinite Integrals



**Integral formulae**

Trigonometric functions

1.   $\int \mathrm{sec}^2x dx=\mathrm{tan}x+c$
2.   $\int \frac{1}{\sqrt{1-x^2}} dx=\mathrm{sin}^{-1}x+c$
3.   $\int -\frac{1}{\sqrt{1-x^2}} dx=\mathrm{cos}^{-1}x+c$
4.   $\int \frac{1}{1+x^2} dx=\mathrm{tan}^{-1}x+c$

Note that $\mathrm{sin}^{-1}x$ denotes "inverse sin" or $\mathrm{arcsin}(x)$, not $\frac{1}{\mathrm{sin}x}$.

Common integrals

$\int\frac{1}{y}dy=\ln\vert y\vert +c$



**FTC2**

$f$ is continuous
$$
\frac{d}{dx}\int_a^x f(t)dt=f(x).
$$

-   important to differentiate variable of integrand $t$ from the upper limit $x$. Use different letters!



**Geometry**

Volume of a sphere (ball) $V=\frac{4}{3}\pi r^3$, $r$ is radius.



___

Semi-parametric models

-   Method of Moments
-   quantile regression



**Textbooks**

-   **Econometric Analysis** , 5th Edition, by William H. Greene, Prentice Hall, 2003.
    **Time Series Analysis**, by J. D. Hamilton, Princeton University Press, 1994.

    **Estimation and Inference in Econometrics**, by R. Davidon and J. MacKinnon, Oxford University Press, 1993.
    **Econometric Analysis of Cross Section and Panel Data**, by J. Wooldridge, MIT Press, 1999.



