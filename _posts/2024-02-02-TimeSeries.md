---
layout: post
title: Time Series
tag: study
update: 2024-02-04
---

$$
\newcommand{\indep}{\perp \!\!\! \perp}
$$

<a class="top-link hide" href="#" id="js-top">↑</a>

## Ergodicity

A **realization** is a particular instance of a time series. It is one of the infinitely many possible time series that could have been observed. As a time series is a stochastic process, each one could be entirely different. The realization Is the one that was actually observed.

An **ensemble** is the theoretical totality of all possible realizations. It is the *ensemble of realizations*. We can think of that as the population of realizations. When we are thinking of means and variances, we think of them in terms of the ensemble, even though we may only be able to look at a single realization.

Say we have a stochastic process $\\{Z_t\\}_{t=1}^\infty$, we want to estimate the mean of the process, $\mu(Z_t)$. We have two candiate estimators: *ensemble average* and *time average*.

- Ensemble Average $\;\overline{\overline{z}} = \frac{1}{N}\sum_{k=1}^N Z_{t_0}^{(k)}$, where $N$ is the number of realizations we have in the ensemble; $t_0$ is any point in time.

- Time Series Average $\;\overline{z} = \frac{1}{T}\sum_{t=1}^T Z_t$

Q: Which estimator is the most appropriate? \
A: Ensemble Average. But, it is impossible to calculate. We only observe one realization of $Z_t$.

Q: Under which circumstances we can use the time average (only one realization of ${Z_t}$)? Is the time average an unbiased and consistent estimator of the mean? \
A: The Ergodic Theorem ensures we can use time average converges to the ensemble average as $N$ and $T$ go to infinity.

Mean and Variance

- $\mu_t$ is the mean of all possible realization of $Z_t$ **for a fixed t**. Since we have only one realization, we use the long run average to estimate the expected value.

- $\sigma_t^2$ is the variance of all possible realization of $Z_t$ **for a fixed t**.


- Ergodic **Definition**: A covariance-stationary process is ergodic for the mean if

  $$
  \text{plim}_{T\to\infty}\; \overline{Z}_T = E[Z_t] = \mu
  $$

  In plain language, ergodicity says if a sample path is observed long enough, provided the process is ergodic and stationary, the time average ($\overline{Z}_T$) converges in probability to the (ensemble) mean value of the process ($E[Z_t]$) as $T\to\infty$.

  $\overline{Z}_T$ stands for the time average value of a sample path, i.e., the physical realization that you observe:

  - Continuous case: $\overline{Z}\_T = \frac{1}{2T} \int_{-T}^T Z(t)\,dt$.
  - Discrete case: $\overline{Z}\_T = \frac{1}{T}\sum_{t=1}^T Z_t$

  $E[Z_t] = \mu_t$ stands for the (cross-sectional) mean value of the process at a fixed $t$; corresponds to the distribution of $Z_t$ in the ensemble.

  - Continuous case: 
    - the mean is $\mu_t = E[Z_t] = \int_{-\infty}^\infty z_t f_{Z_t}(z_t)\, dz_t$. $f_{Z_t}(z_t)$ denotes the unconditional density of $Z_t$.
    - the variance is $\gamma_{0t} \equiv E(Z_t-\mu_t)^2 = \int_{-\infty}^\infty (z_t-\mu_t)^2 f_{Z_t}(z_t)\, dz_t $
  - Discrete case: $\mu_t = E[Z\_t] = \text{plim}_{N\to\infty} \frac{1}{N} \sum\_{i=1}^N  Z_t^{(i)}$

  Given covariance-stationarity, the 1st moment should be constant. That is $E[Z_t] = \mu_t=\mu$ for all $t$.

  A sufficient condition for ergodicity for the mean is 

  $$
  \rho_k \to 0 \text{  as  } k\to\infty.
  $$
  
  A sufficient condition for ergodicity for the second moment is 

  $$
  \sum_k \vert\rho_k\vert < \infty \text{  as  } k\to\infty.
  $$

  $$
  {\color{#797D7F} \text{Equivalently, we can write} \sum_{k=0}^{\infty} \vert\rho_k\vert < \infty.}
  $$

  In the special case where $\\{Z_t\\}$ is a stationary Gaussian process, condition $\sum_{k=0}^{\infty} \vert\rho_k\vert < \infty$ is sufficient to ensure ergodicity for all moments.

  A process which is ergodic in the first and second moments is usually referred as *ergodic in the wide sense*.

  Stationarity is a necessary but not sufficient condition for ergodicity. 

  $$
  \text{Erogodicity} \Rightarrow \text{Stationarity}
  $$

  Meaning that 
  - a process can be stationary but not ergodic. 
  - If NOT stationary, then NOT ergodic.
  - An ergodic process is always stationary.

  Examples where a process is stationary but not ergodic. 
  
  **Ex 1**.
  Imagine a stochastic process where each X is a Bernoulli binary R.V., hence it takes values 1 or 0. Plus, our process is such that it takes a value (0 or 1) at the initial moment and stays fixed at this value for ever. Hence, our time series will look like a straight line at either 1 or 0. We know that the true (ensemble) average of our process is something between 0 and 1, however, the average computed across time (time average) will return always 1 or 0.

  The idea behind ergodicity is that, while collecting more and more observations, we keep learning something new about the process. In other words, if I pick two random variables of the process which are sufficiently ‘far apart’, their distributions should be independent among each others. If you think about the example above, you can now see how that process is clearly not ergodic: no matter how many observations we collect, there is no further information we are gathering, since everything is known since the beginning (from the initial value taken by our process).

  **Ex 2**. Let $Y_t = Z + \varepsilon_t$. $Z_t$ is a R.V. generated from $N(0,\lambda^2)$. $\\{\varepsilon_t\\}$ is a Gaussian white noise process with mean zero and variance $\sigma^2$ that is independent of $Z$.

  Notice that

  $$
  E[Y_t] = E[Z] + E[\varepsilon_t] = 0.
  $$

  Also,

  $$
  \gamma_{0t} = E[(Z+\varepsilon_t)^2] = \lambda^2 + \sigma^2
  $$

  and

  $$
  \gamma_{jt} = E[(Z+\varepsilon_t)(Z+\varepsilon_{t-j})] = \lambda^2 \;\;\text{ for } j\ne 0.
  $$

  Thus the process $\{Y_t\}$ is covariance-stationary. 

  We check ergodicity now.

  $$
  \sum_{j=0}^\infty \vert \gamma_{jt} \vert = \lim_{l\to\infty} \sum_{j=0}^l \gamma_{jt} = \lim_{l\to\infty} l\cdot \lambda^2 = \infty
  $$

  It does not satisfy the sufficient condition $\sum_{k=0}^{\infty} \vert\rho_k\vert < \infty$ for ergodicity. Indeed, the time average

  $$
  \frac{1}{T} \sum_{t=1}^T Y_t = \frac{1}{T} (T\cdot Z + \sum_{t=1}^T \varepsilon_t) = Z + \frac{1}{T} \sum_{t=1}^T \varepsilon_t
  $$

  converges to $Z$ rather than to $E[Y_t]$.

  Reference for Ex.1: <https://datasciencechalktalk.wordpress.com/2019/10/30/time-series-why-do-we-need-stationarity-and-ergodicity/>

  Ergodicity vs. Stationarity: <https://dsp.stackexchange.com/a/1169>

  Q: Is stationarity sufficient for using time average as an estimator to the real mean? \
  A: No. Stationarity does not rule out autocorrelation, that is the covariance/correlation depends on how far apart the two time points are. Therefore, we need *Ergodicity* to reach this goal.

- Ergodic **Theorem** \
  If $Z_t$ is strictly stationary and ergodic and $E[Z_t]<\infty$, and if $\overline{Z}\_T = \frac{1}{T}\sum_{t=1}^T Z_t$, then as $T\to\infty$

  $$
  \sqrt{T}\, \overline{Z}_T \xrightarrow{p} E[Z_t].
  $$

  The ergodic theorem is a LLN for stochastic processes. It is a substantial generalization of Kolmongorov’s LLN because it allows for serial dependence in the time series.

  These results allow us to consistently estimate parameters using time series moments. Recall that consistency of an estimator means:
  - the estimator is asymptotically unbiased, and
  - its variance asymptotically collapeses to zero.

  Q: Is the time average is asympototically unbiased? Yes. Stationarity ensures that.

  $$
  \begin{aligned}
  E[\overline{Z}_T] &= \frac{1}{T} \sum_{t=1}^T E[Z_t] \;\; \text{  by stationarity, we have constant mean, } E[Z_t] = \mu \\
  &= \frac{1}{T} \sum_{t=1}^T \mu \\ 
  &= \mu
  \end{aligned}
  $$

  Q: Is the variance going to zero as $T$ grows? Yes. Ergodicity ensures that.
  
  $$
  \begin{aligned}
  \text{Var}[\overline{Z}_T] &= \text{Var} \left[\frac{1}{T}\sum_{t=1}^TZ_t\right] \\
  &= \frac{1}{T^2}  \text{Var} \left[\sum_{t=1}^TZ_t\right] \\
  &= \frac{1}{T^2} \sum_{t=1}^n\sum_{s=1}^n \text{Cov}(Z_t, Z_s) \\
  &= \frac{1}{T^2} \sum_{t=1}^n\sum_{s=1}^n \gamma(t-s) \\
  &= \frac{\gamma_0}{T^2} \sum_{t=1}^n\sum_{s=1}^n \rho_{t-s} \\
  &= \frac{\gamma_0}{T^2} \sum_{t=1}^n (\rho_{t-1}+\rho_{t-2}+\cdots+\rho_{t-n}) \\
  &= \frac{\gamma_0}{T^2} \left(T\rho_0 + 2(T-1)\rho_1 + 2(T-2)\rho_2 + \cdots + 2\,\rho_{T-1} \right) \\
  &= \frac{\gamma_0}{T} \sum_{k=1-T}^{T-1} (1-\frac{\vert k \vert}{T})\rho_k
  \end{aligned}
  $$

  $\gamma(t-s)$ is called the auto-covariance funtion. It is a function of the time shift, $k$. $\gamma(0)$ is the variance, $\gamma(0)=\sigma^2$.

  $\rho(t-s)$ is the auto-correlation function. 

  $$
  \rho(t-s) = \frac{\gamma(t-s)}{\sqrt{\sigma_t^2}\sqrt{\sigma_s^2}}
  $$

  <span style='color:#797D7F'>
  If stationarity holds, then we have constant variance, $\sigma_t^2=\sigma_s^2=\sigma^2=\gamma_0$. And we have </span>
  
  $$
  {\color{#797D7F} \rho (k)=\frac{\gamma (k)}{\gamma_0}.}
  $$

  

  Take the limit

  $$
  \begin{aligned}
  \lim_{T\to\infty} \text{Var}(\overline{Z}_T) &= \lim_{T\to\infty} \frac{\gamma_0}{T} \sum_k (1-\frac{\vert k \vert}{T})\rho_k \\
  &= 0 \;\;\;\text{by Ergodicity, } \rho_k \to 0 \text{ as } k\to\infty.
  \end{aligned}
  $$
  
  Hence $\text{Var}(\overline{Z}_T)\to 0$ as $T\to 0$.

## Stationarity

Broadly speaking, a time series is said to be stationary if 
- there is no systematic change in mean (no trend), 
- if there is no systematic change in variance, and 
- if strictly periodic variations have been removed. 

In other words, the properties of one section of the data are much like those of any other section.

Measure of dependence for a stochastic process $\lbrace Z_t: t=0,1,2,\ldots, n \rbrace$
- mean function $\mu_t = E(Z_t)$
- autocovariance function $\gamma_t(k)=\text{Cov}(Z_t, Z_{t-k})=E\big[(Z_t-\mu_t)(Z_{t-k}-\mu_{t-k})\big]$, where $k$ is the time lag; sometimes also denoted by two time points, $t$ and $t-k$, as in $\gamma_{t, t-k}\,.$
- autocorrelation function $\rho_t(k)=\text{Corr}(Z_t, Z_{t-k})$. Also denoted as $\rho_{t, t-k}$.

___

## Weakly Stationary

The time series $\lbrace Z_t\rbrace_{t=0}^n$ is <span style='color:#008B45FF'>*(weakly, second-order, or covariance) stationary*</span> if
1. $E[X_t] = \mu \,.$ \
The mean function $\mu_t$ is independent of $t$;
2. $\text{Cov}(X_t, X_{t-j}) = \Gamma_j \text{ for } \forall j\ge 0 \,.$\
 The covariance between two observations, $\gamma_t(k)$, <span style='color:#337ab7'>depends only on the time lag $k$ and is independent of $t$</span>.

*Nothing* is assumed about the collection of *joint distributions* of the process. Instead, we only are specifying the characteristics of the first two **moments** of the process.

___

## Strictly Stationary

We say $\lbrace Z_t\rbrace_{t=0}^n$ is <span style='color:#008B45FF'>*strictly (or strongly) stationary*</span> if the same joint distribution of

$$
(Z_{t_1}, \ldots, Z_{t_n})
$$

is the same as 

$$
(Z_{t_1-k}, \ldots, Z_{t_n-k})
$$

for all time points $t_1, t_2, \ldots, t_n$ and for all time lags $k$.

In other words, shifting the time origin by an amount $k$ has no effect on the joint distributions, which must therefore depend only on the intervals between $t_1, t_2, \ldots, t_n$. This is a very strong condition.

Basic properties of a strictly stationary time series $\lbrace Z_t\rbrace$:
1. $Z_t$'s are from the same distribution.\
   Since the above condition holds for all sets of time points $t_1, t_2, \ldots, t_n$, it must hold when $n = 1$; i.e., there is only one time point. This implies $Z_t$ and $Z_{t-k}$ have the same margianl distribution for all $t$ and $k$.
2. Because these marginal distributions are the same,

    $$
    \begin{aligned}
    E[Z_t] &= E[Z_{t-k}] \\
    \text{Var}[Z_t] &= \text{Var}[Z_{t-k}]
    \end{aligned}
    $$

    for all $t$ and $k$.

    Therefore, for a strictly stationary process, both $\mu_t=E[Y_t]$ and $\gamma_t(0)$ are constant over time; i.e., $\mu_t$ and $\gamma_t(0)$ are free of $t$.
3. Since the above condition holds for all sets of time points $t_1, t_2, \ldots, t_n$, it must hold when $n = 2$; i.e., there are only two time points. \
This implies 

    $$
    (Y_t, Y_s) \overset{\rm d}{=} (Y_{t-k}, Y_{s-k}).
    $$

    for all $t,s,$ and $k$.

    $\overset{\rm d}{=}$ means having th same distribution.

    $\gamma_{t, t-k}$ can be simplied as $\gamma(k)$ as the covariance between any two observations depends only on the time lag between them, not on $t$.

4. An IID sequence is strictly stationary.

*REMARK*: Strict stationarity is a condition that is much *too restrictive* for most applications. Moreover, it is difficult to assess the validity of this assumption in practice. Rather than imposing conditions on all possible (marginal and joint) distributions of a process, we will use a milder form of stationarity that only deals with the first two moments — Weak Stationarity.


Clearly, strict stationarity implies weak stationarity. It is also clear that the converse to statement is not true, in general. \
However, if we append the additional assumption of multivariate normality (for the $Z_t$ process), then the two definitions do coincide; that is,

$$
\text{weak stationarity + multivariate normality} \Longrightarrow \text{strict stationarity.}
$$


*CONVENTION*: For the purpose of modeling time series data in this course, we will rarely (if ever) make the distinction between strict stationarity and weak stationarity. When we use the term “stationary process,” this is understood to mean that the process is *weakly stationary*.

In many situations, a nonstationary process $\{Y_t\}$ can be “transformed” into a stationary process by *taking (first) differences*. For example, the random walk $Y_t = Y_{t−1} + \varepsilon_t$, where $\varepsilon_t \sim \text{iid } N (0, \sigma_\varepsilon^2)$, is not stationary. However, the first difference process $\Delta Y_t = Y_t − Y_{t−1} = \varepsilon_t$ is zero mean white noise, which is stationary.

<span style='color:#337ab7'>Stationarity does NOT mean</span>
- limited dependence \
  The autocovariance relies on the time shift.
- absence of periodic patterns \
  For instance, $y_t=(-1)^tZ$ and $y_t=Z\cos(\theta t)$ are stationary processes for a random variable $Z$ symmetrically distributed about 0.


Useful properties of stationarity

<div class = "boxed" style="margin-bottom: 40px;">
<strong>Theorem</strong>  If $\boldsymbol{y}_t$ is strictly stationary and $\boldsymbol{x}_t=\boldsymbol{\phi}(\boldsymbol{y}_t, \boldsymbol{y}_{t-1}, \boldsymbol{y}_{t-2}, \ldots) \in \mathbb{R}^q$ is a random vector, then $\boldsymbol{x}_t$ is strictly stationary.
</div>


- Stationarity is preserved by transformation. That is,
transformations of strictly stationary processes are also strictly stationary.
- This is useful for the study of stochastic processes which are constructed from underlying errors, and for the study of sample statistics such as linear regression estimators which
are functions of sample averages of squares and cross-products of the original data.


<div class = "boxed">
<strong>Theorem</strong>  Any transformation $g(.)$ of a stationary and ergodic process $\{Y_t\}$ is also stationary and ergodic. That is,  $\{g(Y_t)\}$ is stationary and ergodic. Therefore, if $E[g(Y_t)]$ exists then the ergodic theorem gives

$$
\overline{g} = \frac{1}{T} \sum_{t=1}^T g(Y_t) \xrightarrow{p} E[g(Y_t)]
$$
</div>

Application of the theorem: the sample autocovariances 

$$
\hat{\gamma}_{t}(j) = \frac{1}{T} \sum_{t=j+1}^T (Y_t-\overline{Y})(Y_{t-j}-\overline{Y})
$$

converge in probability to the population autocovariances 

$$
\gamma_{t}(j) = \text{Cov}(Y_t, Y_{t-j}) = E[(Y_t-\mu)(Y_{t-j}-\mu)].
$$

- $\gamma$ denotes *autocovariance* coefficients; $\rho$ denotes *autocorrelation* coefficients. \
  $\gamma(1)$ is called the autocovariance function of lag 1 and $\rho(1)$ the autocorrelation function or lag 1.