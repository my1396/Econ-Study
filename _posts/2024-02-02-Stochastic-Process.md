---
layout: post
title: Stochastic Process
tag: study
update: 2024-02-02
---

$$
\newcommand{\indep}{\perp \!\!\! \perp}
$$

<a class="top-link hide" href="#" id="js-top">↑</a>

A stochastic process $X_t$ is a family/sequence of random variables indexed by time $t$. "Stochastic"  is a synonym for random. 

When we collect time series data set, we obtain one possible outcome, or *realization*, of the stochastic process. We can only see a single realization, because we cannot go back in time and start the process over again. (This is analogous to cross-sectional analysis where we can collect only one random sample.)

At a specific time point $t$, $X_t$ is a random variable with a specific density function. A stochastic process is defined in a probability space $(\Omega, \mathcal{F}, P)$.

Mean function $\mu_t$ 

$$
\begin{align*}
\mu_t = \mathbb{E}[X_t] = \int_{\mathbb{R}}x \, \mathrm dF_t(X)
\end{align*}
$$

$\mu_t$ depends on time $t$, as, for example, processes with a seasonal or periodical structure or processes with a deterministic trend.

**Autocovariance Function**
$$
\begin{align*}
\gamma(t,\tau)=\text{Cov}(X_t, X_{t-\tau})
\end{align*}
$$

If we define <span style='color:red'>**covariance stationary**</span>, then $\gamma(t,\tau)=\gamma_\tau$, means covariance only depends on the time interval apart $\tau$, not the start point $t$.


**Autocorrelation Function** (ACF)

$$
\begin{align*}
\rho_{\tau}=\frac{\gamma_{\tau}}{\gamma_0}
\end{align*}
$$

The autocorrelation function $\rho$ of a covariance stochastic process is normalized on the interval $[-1,1]$.  $\rho$ depends only on one parameter, the lag $\tau$.  The sequence, $\lbrace\rho_\tau\rbrace,$ is called correlogram.



## White Noise (WN)

If $X_t$ is white noise, then

$$
\begin{align*}
1.&\ \mu_t=0,  and \\
2.&\ \gamma_\tau=\left\lbrace
	\begin{array}{ll}
	\sigma^2 & \text{when $\tau=0$} \\
	0 & \text{(uncorrelated) when $\tau\neq0$}
	\end{array} \right.
\end{align*}
$$

In short, WN is with expectation 0 and finite variance. denoted as $X_t\sim \text{WN} (0, \sigma^2)$.

Note that every $\text{IID}\, (0, \sigma^2)$ sequence is $\text{WN} (0, \sigma^2)$, but not conversely.


___


**Random Walk**

$$
X_t=c+X_{t-1}+\varepsilon_t
$$

with a constant $c$ and **white noise** $\varepsilon_t$. 

$Z_t=X_t-X_{t-1}=c+\varepsilon_t$ , if $c$ is not zero, then we say $X_t$  has a drift, 

$c>0$ we say drift upward,

$c<0$ we say drift downward.

$\varepsilon_t$ is called <span style='color:#337ab7'>*disturbances*</span> or <span style='color:#337ab7'>*innovations*</span> in time series.

Assume that the constant $c$ and the initial value $X_0$ are set to zero, through recursive substitution we will get the representation:

$$
\begin{align*}
X_t=\sum^t_{i=1}\varepsilon_i
\end{align*}
$$

Moment functions:

1. $\mu_t=0$
2. $\text{Var}(X_t)=t\sigma^2$
3. $\gamma(t,\tau) = \text{Cov}(X_t,X_{t-\tau})=(t-\tau)\sigma^2$, for $\tau\lt t$.
4. $\rho(t,\tau)=\sqrt{1-\frac{\tau}{t}}$

Notice that autocovariance is strictly positive, and since it <span style='color:#337ab7'>depends on $t$ not only on the lags $\tau$</span>, the random walk is NOT covariance stationary.

As $\tau$ gets larger, $\rho$ gets smallers. In words, neighboring time points are more and more strongly and positively correlated as they get closer in time. 
On the other hand, the values of $X$ at distant time points are less and less correlated.



## AR(1) process

Model set up

$$
X_t = c+\alpha X_{t-1}+\varepsilon_t, \quad \varepsilon_t\sim \mathrm{WN}(0, \sigma^2).
$$

In order for $\lbrace x_t\rbrace$ to converge, we need $ \vert\alpha \vert<1$.

By iterative substitutions, 

$$
\begin{align*}
X_t = c \frac{1-\alpha^k}{1-\alpha}+\alpha^kX_{t-k}+\sum^{k-1}_{i=0}\alpha^i\varepsilon_{t-i}
\end{align*}
$$

For $K\to \infty$,

$$
\begin{align}
X_t = \frac{c}{1-\alpha}+\sum^\infty_{i=0}\alpha^i\varepsilon_{t-i} \label{eq:ma-representation}
\end{align}
$$

Eq. $\eqref{eq:ma-representation}$ is called the moving-average representation, MA($\infty$).

Moment functions:

1. Expectation: $\mu_t = \frac{c}{1-\alpha}$
2. Autocovariance function of lag $\tau$: $\gamma_\tau=\frac{\sigma^2}{1-\alpha^2}\alpha^\tau$
3. Autocorrelation function of lag $\tau$: $\rho_\tau=\alpha^\tau$

For ACF, $\rho_\tau$, 

- if $\alpha>0$, this function is strictly positive, 
- for $\alpha<0$, it alternates around zero. 

When we have $\alpha>0$, for small $\alpha$, like 0.5, it converges very fast; for large $\alpha$, like 0.99, it converges quite slow.

___


There are cases where $\abs{\phi}\ge1$:

- if $\abs{\phi}>1$ the AR(1) process is stationary but not causal.

- if $\abs{\phi}=1$ we have a non-stationary process (called random walk when $\phi=1$) and we say that this process has a unit root.

___

**Autocovariance Matrix**

If $\lbrace X_t \rbrace$ is a stationary process, we define a $p\times 1$ random vector $X$:

$$
X' = [X_t, X_{t+1}, \ldots, X_{t+p} ] \,.
$$

We define $\Sigma_{XX}$ as the $p\times p$ autocovariance matrix of the random vector $X$ that has the following form:

$$
\Sigma_{XX} = {\color{#008B45FF}\sigma^2} \begin{bmatrix}
1 & \rho(1) & \rho(2) & \cdots & \rho(p-1) \\
\rho(1) & 1 & \rho(1) & \cdots & \rho(p-2) \\
\rho(2) & \rho(1) & 1 & \cdots & \rho(p-3) \\
\vdots & \vdots & \vdots &\ddots & \vdots \\
\rho(p-1) & \rho(p-2) & \rho(p-3) & \cdots & 1 \\
\end{bmatrix}
$$

Consider now the following linear combination of the elements of $X$

$$
Z = a'X = \sum_{i=1}^p a_i X_i
$$

where 

$$
a' = [a_1, a_2, \ldots, a_p]
$$

Note that $Z$ is scalar here. The variance of $Z$ is 

$$
a'\Sigma_{XX}a \,.
$$

The variance of $Z$ cannot be negative, so 

$$
a'\Sigma_{XX}a \ge 0
$$

for all nonzero $a$.

We say that $\Sigma_{XX}$  is "<span style='color:#008B45FF'>positive semi-definite</span>". This implies

$$
\sum_{r=1}^p\sum_{s=1}^p a_r\, a_s\, \rho(r-s) \ge 0 \,.
$$



**MA($\bold{\infty}$) representation**

Leg $\lbrace\varepsilon_t\rbrace$ be white noise and $\lbrace\psi_j\rbrace$ be a sequence of real numbers that is absolutely summable. Then

1. For each $t$,
	
	$$
	y_t = \mu + \sum_{j=0}^\infty\psi_j\varepsilon_{t-j}
	$$

    converges in mean square. $\lbrace y_t\rbrace$ is covariance-stationary. (The process $\lbrace y_t\rbrace$ is called the infinite-order moving-average process (MA($\infty$)).)

2. The mean of $y_t$ is $\mu.$ The autocovariances $\lbrace\gamma_j\rbrace$ are given by 

    $$
    \gamma_j = \sigma^2\sum_{k=0}^\infty \psi_{j+k}\psi_k \quad (j=0,1,2,\dots).
    $$

3. The autocovariances are absolutely summable:

    $$
    \sum_{j=0}^\infty \vert \gamma_j \vert < \infty.
    $$

4. If, in addition, $\lbrace\varepsilon_t\rbrace$ is i.i.d, then the process $\lbrace y_t\rbrace$ is (strictly) stationary and ergodic.


$$
y_t = c + \phi y_{t-1} + \varepsilon_{t}
$$


$$
y_t = \mu - \sum_{j=1}^\infty \phi^{-j}\varepsilon_{t+j}
$$


**Markov Process**

A stochastic process has the Markov Property if for all $t\in \mathbb{Z}$ and $k\geq 1$

$$
\begin{align*}
F_{t|t-1,\ldots,t-k}(x_t|x_{t-1},\ldots, x_{t-k})=F_{t|t-1}(x_t|x_{t-1})
\end{align*}
$$

In other words, the conditional distribution of a Markov process at a specific point in time is entirely determined by the condition of the system at the previous date.

Two examples: random walk with independent $\varepsilon_t$ and the AR(1) process with independent white noise.



## Martingale

Let $\lbrace X_t\rbrace$ denote a sequence of random variables and let $\mathcal F_{t} = \lbrace X_{t}, X_{t-1},\ldots, X_0\rbrace$ denote a set of conditioning information or *information set* based on the past history of $X_{t}.$ The sequence $\lbrace X_t, \mathcal F_t\rbrace$ is called a martingale if

$$
E[X_t \mid X_{t-1}=x_{t-1}, \ldots, X_{t-k}=x_{t-k}] = x_{t-1}
$$

or more succinctly,

$$
E[X_t | \mathcal F_{t-1}] = x_{t-1}
$$


For martingale, only one statement about the *conditional expectation* is made; while for Markov process, statements on the entire *conditional distribution* are made.


The most common example of a martingale is the random walk model

$$
X_t = X_{t-1} + \varepsilon_t, \quad \varepsilon_t \sim WN(0, \sigma^2).
$$

We have

$$
E[X_t | \mathcal F_{t-1}] = X_{t-1}
$$

since $E[\varepsilon_t \vert \mathcal F_{t-1}]=0.$


**Martingale Difference Sequence** (MDS)

Let $\lbrace \varepsilon_t\rbrace$ be a sequence of random variables with an associated information set $\lbrace\mathcal F_t\rbrace$. The sequence $\lbrace\varepsilon_t, \mathcal F_t\rbrace$ is called a *martingale difference sequence* (MDS) if

$$
E[\varepsilon_t | \mathcal F_{t-1}] = 0 \,.
$$

If $\lbrace X_t, \mathcal F_t\rbrace$ is a martingale, then its first difference sequence $\lbrace \Delta X_t, \mathcal F_t\rbrace$ is 
a MDS. Define

$$
\varepsilon_t \equiv \Delta X_t = X_t - X_{t-1} ,
$$

$\lbrace\varepsilon_t, \mathcal F_t\rbrace$ is a MDS.

To show that $\lbrace\varepsilon_t, \mathcal F_t\rbrace$ is MDS, we need

$$
\begin{split}
E[\varepsilon_t | \mathcal F_{t-1}] 
&= E[X_t|\mathcal F_{t-1}] - E[X_t|\mathcal F_{t-1}] \\
&= X_{t-1} -  X_{t-1} \\
&= 0 \,.
\end{split}
$$

<div style='margin-top:-1em; margin-bottom:3em'><span style='float:right; margin-right:10px; '>&#9633;</span></div>


**Useful properties of a MDS**:

1. A MDS is mean zero.

    $$
    E[\varepsilon_t] = E \left[E[\varepsilon_t | \mathcal F_{t-1}]\right] =0 
    $$

2. By construction, a MDS is an uncorrelated process. The covariance of $\varepsilon_t$ and $\varepsilon_{t-k}$, for $k>0$, is 

    $$
    \begin{aligned}
    \text{Cov}(\varepsilon_t, \varepsilon_{t-k}) 
    &= E[\varepsilon_t\varepsilon_{t-k}] \\
    &= E[E[\varepsilon_t\varepsilon_{t-k} | \mathcal F_{t-1}]] \\
    &= E[\varepsilon_{t-k} E[\varepsilon_t| \mathcal F_{t-1}]] \\
    &= E[\varepsilon_{t-k} 0] \\
    &= 0
    \end{aligned}
    $$


    The term "martingale difference sequence" refers to the fact that the summed process (assuming $S_0=0$)

    $$
    S_t = \sum_{j=1}^t \varepsilon_j
    $$

    is a martingale, and $\varepsilon_t$ is its first difference. We can verify that 

    $$
    \begin{split}
    E[S_t | \mathcal F_{t-1}] 
    &= E[S_{t-1} + \varepsilon_t | \mathcal F_{t-1}]  \\
    &= E[S_{t-1} | \mathcal F_{t-1}] + E[\varepsilon_t | \mathcal F_{t-1}] \\
    &= S_{t-1} + 0 \\
    &= S_{t-1} \,,
    \end{split}
    $$

    which satisfies the martingale property.

3. If $\varepsilon_t$ is i.i.d. and mean zero, then it is a MDS, but the reverse is not true.

    Example: 

    Let $u_t$ be i.i.d. $N(0,1)$ and set 

    $$
    \varepsilon_t = u_tu_{t-1}
    $$


___

## Lag Operator

The lag operator, $L$, shifts a time value $X_t$ back by one period. For example, $LX_t=X_{t-1}$ and  $L^kX_t=X_{t-k}.$

Sometimes also called as "backshift operator", and denoted as $B$.

Useful results of $L$:

- $L^0=1$
- The lag of a constant is the same constant: 

	$$
  La=a .
  $$
  
- The lag operator is commutative:

  $$
	L(\beta y_t) = \beta L y_t.
  $$
  
- The lag operator is distributive:

  $$
	L(x_t+y_t) = L z_t = z_{t-1} = x_{t-1} + y_{t-1} = L x_t + L
  y_t,
  $$

  where $z_t=x_t+y_t.$

- Factorizing polynomials

  $$
  1-\phi_1 z - \phi_2 z^2 - \ldots - \phi_p z^p =
  (1-\lambda_1z)(1-\lambda_2z) \cdots (1-\lambda_pz).
  $$

  - $\lbrace\frac{1}{\lambda_i}\rbrace_{i=1}^p$ are the $p$ roots of the polynomial. 
  - Some of the roots may be complex and some may be identical.

  If we factor the $p$-th order lag polynomial in the same way as a real-valued polynomial:

  $$
  \begin{split}
  & (1-\phi_1 L - \phi_2 L^2 - \ldots - \phi_p L^p)y_t \\
  & \hspace{0.5in} = (1-\lambda_1 L)(1-\lambda_2 L) \cdots
  (1-\lambda_p L) y_t = w_t.
  \end{split}
  $$

  If $\abs{\lambda_i}<1,$

  $$
  (1 - \lambda_i L)^{-1} = \sum_{j=0}^{\infty} \lambda_i^j L^j,
  \,\,\,\,\, \forall i.
  $$

More properties: <https://ealdrich.github.io/Teaching/Econ211C/LectureNotes/Unit1-ARMA/lagOperators.html>

**Autoregressive Polynomial**
$$
\begin{equation}
\phi(L) = 1 - \phi_1 L - \phi_2 L^2 - \cdots - \phi_p L^p \label{lag-poly}
\end{equation}
$$

Eq. $\eqref{lag-poly}$ is common to see in ARMA process. 

Using an AR(1) model, 
$$
\begin{equation}
Y_t=\phi_1 Y_{t-1} + \varepsilon_t,\label{AR1}
\end{equation}
$$

as an example.  

Let $\phi(L)=1-\phi_1 L\,,$ then we can express the innovation in $\eqref{AR1}$ as

$$
\begin{equation}
\varepsilon_t = Y_t-\phi_1 Y_{t-1} = (1-\phi_1L)Y_t = \phi(L) Y_t \,.
\end{equation}
$$

Other common lag polynomials:

- General form: $\beta(L)=\beta_0 + \beta_1L + \beta_2L^2 + \cdots$
- $\alpha(L)=1 + \alpha L + (\alpha L)^2 + (\alpha L)^3 + \cdots$

We also call these lag polynomials "filters."

**Product** of two filters $\alpha(L)$ and $\beta(L)$ 
$$
\delta(L) = \alpha(L)\beta(L)
$$

If follows the same rules as common polynomials. For example, for $\alpha(L)=1+\alpha_1L$ and $\beta(L)=1+\beta_1L$, we have

$$
\delta(L)=(1+\alpha_1L)(1+\beta_1L) = 1+ (\alpha_1+\beta_1)L + \alpha_1\beta_1L^2.
$$

The product of two filters is called "convolution" of $\lbrace\alpha_{j}\rbrace$ and $\lbrace\beta_{j}\rbrace.$

$$
\begin{gathered}
\delta_0 = \alpha_0\beta_0 \\
\delta_1 = \alpha_0\beta_1 + \alpha_1\beta_0 \\
\delta_2 = \alpha_0\beta_2 + \alpha_1\beta_1 + \alpha_2\beta_0 \\
\vdots
\end{gathered}
$$

**Inverses** of $\alpha(L)$ is to find $\beta(L)$ such that $\alpha(L)\beta(L)=1$, we say $\beta(L)$ is the inverse of $\alpha(L)$, denoted as $\alpha(L)^{-1}$ or $1/\alpha(L).$



**Difference Operator**: $\Delta=1-L$, $\Delta X_t=X_t-X_{t-1}$ and $\Delta^k=(1-L)^k$

**Unit Root Tests**
$$
X_t = c+\alpha X_{t-1}+\varepsilon_t
$$

- For $\vert \alpha \vert<1$, the process is stationary.
- For $\vert \alpha \vert=1$, the process is **non-stationary.**



### Kernel Smoothing

<https://atmos.washington.edu/~breth/classes/AS552/lect/lect24.pdf>

Python code: <https://matthew-brett.github.io/teaching/smoothing_intro.html>







## GMM

`gmm(g, x, t0=NULL, gradv=NULL, type=c("twoStep","cue","iterative"), wmatrix = c("optimal","ident"), vcov=c("HAC","MDS","iid","TrueFixed"), ..., data)`

* `g`     A function of the form $g(\theta,x)$ and which returns a $n\times q$ matrix with element $g_i(\theta,x_t)$ for $i=1,\ldots,q$ and $t=1,\dots,n$.  This matrix is used to build the $q$ sample moment conditions. 
* `x`     The matrix or vector of data from which the function $g(\theta,x)$is computed. If "g" is a formula, it is an n × Nh matrix of instruments or a formula.
* `wmatrix`     Which weighting matrix should be used in the objective function. 
  * By default, it is the inverse of the covariance matrix of $g(\theta,x)$, `optimal`. 
  * The other choice is the identity matrix which is usually used to obtain a first step estimate of $\theta$. 



**Vector Autoregressive**

VAR model allows feedback to occur between the variables in the model. For example, we could use a VAR model to show how real GDP is a function of policy rate and how policy rate is, in turn, a function of real GDP.

-   A systematic but flexible approach for capturing complex real-world behavior.
    Better forecasting performance.
    Ability to capture the intertwined dynamics of time series data.


___

**Conventions**

$\Delta$ means "change" or "difference." If an original variable is named $y$ then its change of difference is often denoted $cy$ or $dy.$ For example, the change in $price$ might be denoted $cprice.$

If an original variable is named $y$ then its growth rate is often denoted $gy,$ so that for each $t,$ $gy_t=\log(y_t)- \log(y_{t-1})$ or $gy_t=(y_t-y_{t-1})/y_t.$



