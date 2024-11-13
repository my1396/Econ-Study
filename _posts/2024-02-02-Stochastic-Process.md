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

A stochastic process $X_t$ is a family of random variables. At a specific time point $t$, $X_t$ is a random variable with a specific density function. A stochastic process is defined in a probability space $(\Omega, \mathcal{F}, P)$.

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

If we define <span style='color:red'>**covariance stationary**</span>, then $\gamma(t,\tau)=\gamma_\tau$, means covaraince only depends on the time interval apart $\tau$, not the start point $t$.


**Autocorrelation Function** (ACF)

$$
\begin{align*}
\rho_{\tau}=\frac{\gamma_{\tau}}{\gamma_0}
\end{align*}
$$

The autocorrelation function $\rho$ of a covaraince stochastic process is normalized on the interval $[-1,1]$.  $\rho$ depends only on one parameter, the lag $\tau$.



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



**AR(1) process**

$$
\begin{align*}
X_t=c+\alpha X_{t-1}+\varepsilon_t
\end{align*}
$$

with $ \vert\alpha \vert<1$.

By iterative substitutions, 

$$
\begin{align*}
X_t = c \frac{1-\alpha^k}{1-\alpha}+\alpha^kX_{t-k}+\sum^{k-1}_{i=0}\alpha^i\varepsilon_{t-i}
\end{align*}
$$

For $K\to \infty$,

$$
\begin{align*}
X_t = \frac{c}{1-\alpha}+\sum^\infty_{i=0}\alpha^i\varepsilon_{t-i}
\end{align*}
$$

Moment functions:

1. Expectation: $\mu_t = \frac{c}{1-\alpha}$
2. Autocovariance function of lag $\tau$: $\gamma_\tau=\frac{\sigma^2}{1-\alpha^2}\alpha^\tau$
3. Autocorrelation function of lag $\tau$: $\rho_\tau=\alpha^\tau$

For ACF, $\rho_\tau$, 

- if $\alpha>0$, this function is strictly positive, 
- for $\alpha<0$, it alternates around zero. 

When we have $\alpha>0$, for small $\alpha$, like 0.5, it converges very fast; for large $\alpha$, like 0.99, it converges quite slow.


**Autocovariance Matrix**

If $\{X_t \}$ is a stantionary process, we define a $p\times 1$ random vector $X$:

$$
X' = [X_t, X_{t+1}, \ldots, X_{t+p} ] \,.
$$

We define $\Sigma_{XX}$ as the $p\times p$ autocovaraince matrix of the random vector $X$ that has the following form:

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

**Markov Process**

A stochastic process has the Markov Property if for all $t\in \mathbb{Z}$ and $k\geq 1$

$$
\begin{align*}
F_{t|t-1,\ldots,t-k}(x_t|x_{t-1},\ldots, x_{t-k})=F_{t|t-1}(x_t|x_{t-1})
\end{align*}
$$

In other words, the conditional distribution of a Markov process at a specific point in time is entirely determined by the condition of the system at the previous date.

Two examples: random walk with independent $\varepsilon_t$ and the AR(1) process with independent white noise.



**Martingale**

Let $\{X_t\}$ denote a sequence of random variables and let $\mathcal F_{t} = \{X_{t}, X_{t-1},\ldots, X_0\}$ denote a set of conditioning information or *information set* based on the past history of $X_{t}.$ The sequence $\{X_t, \mathcal F_t\}$ is called a martingale if

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

since $E[\varepsilon_t | \mathcal F_{t-1}]=0.$


**Martingale Difference Sequence** (MDS)

Let $\{\varepsilon_t\}$ be a sequence of random variables with an associated information set $\{\mathcal F_t\}$. The sequence $\{\varepsilon_t, \mathcal F_t\}$ is called a *martingale difference sequence* (MDS) if

$$
E[\varepsilon_t | \mathcal F_{t-1}] = 0 \,.
$$

If $\{X_t, \mathcal F_t\}$ is a martingale, a MDS $\{\varepsilon_t, \mathcal F_t\}$ may be constructed by defining

$$
\varepsilon_t = y_t - E[y_t|\mathcal F_{t-1}] \,.
$$

By construction, a MDS is an uncorrelated process. 

$$
\begin{aligned}
E[\varepsilon_t\varepsilon_{t-k}] &= E[E[\varepsilon_t\varepsilon_{t-k} | \mathcal F_{t-1}]] \\
&= E[\varepsilon_{t-k} E[\varepsilon_t| \mathcal F_{t-1}]] \\
&= 0
\end{aligned}
$$

Also, a MDS is mean zeros.

$$
E[\varepsilon_t] = E \left[E[\varepsilon_t | \mathcal F_{t-1}]\right] =0 
$$


**Lag Operator**

$LX_t=X_{t-1}$ and  $L^kX_t=X_{t-k}$

$\Delta=1-L$, $\Delta X_t=X_t-X_{t-1}$ and $\Delta^k=(1-L)^k$


Sometimes also called as "backshift operator", and denoted as $B$.

**Autoregressive Polynomial**

$$
\phi(L) = 1 - \phi_1 L - \phi_2 L^2 - \cdots - \phi_p L^p
$$

Using an AR(1) model, $X_t=\phi_1 X_{t-1} + \varepsilon_t$, as an example.  

Let $\phi(L)=1-\phi_1 L\,,$ then we can express the innovation as

$$
\varepsilon_t = \phi(L) X_t \,.
$$

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
  * The other choice is the identity matrix which is usually used to obtain a first step estimate of $\theta$. `ident`



**Vector Autoregressive**

VAR model allows feedback to occur between the variables in the model. For example, we could use a VAR model to show how real GDP is a function of policy rate and how policy rate is, in turn, a function of real GDP.

-   A systematic but flexible approach for capturing complex real-world behavior.
    Better forecasting performance.
    Ability to capture the intertwined dynamics of time series data.




