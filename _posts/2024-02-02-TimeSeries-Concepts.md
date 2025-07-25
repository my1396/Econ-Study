---
layout: post
title: Time Series Concepts
tag: study
update: 2024-02-04
---


$$
\newcommand{\indep}{\perp \!\!\! \perp}
$$

<a class="top-link hide" href="#" id="js-top">↑</a>


## Convergent Series

A series $S_N=\sum_{j=0}^N a_j$ is convergent if it has a finite limit as $N\to\infty$; thus $S_N\to S=\sum_{j=0}^N a_j$ with $\abs{S}<\infty.$

$S_N$ is **absolutely convergent** if $\sum_{j=0}^N \abs{a_j}$ has a finite limit, which holds if $\sum_{j=0}^N \abs{a_j}<\infty .$ Absolutely convergence implies convergence.

<div class = "boxed">
<strong>Silverman-Toeplitz Theorem</strong> If $a_\ell\to A$ as $\ell\to\infty$, and for weights $w_{n\ell}$ such that $\sum_{\ell=1}^n w_{n\ell} \to 1$ for each $\ell$ as $n\to\infty$, then

$$
\lim_{n\to\infty} \sum_{\ell=1}^n w_{n\ell} a_\ell = A.
$$
</div>

Setting  $w_{n\ell} = 1/n$ we obtain the following.

<div class = "boxed">
<strong>Theorem of Cesàro Means</strong> If $a_\ell\to A$ as $\ell\to\infty$, then

$$
\lim_{n\to\infty} \frac{1}{n}\sum_{\ell=1}^n a_\ell = A.
$$
</div>


Now we present a useful property. The Cesàro sum of the autocovariances limits to zero.

<div class = "boxed">
<strong>Cesàro Mean of Autocovariances</strong> If $Z_t$ is strictly stationary, ergodic, and $\E(Z_t^2)<\infty$, then 

$$
\lim_{n\to\infty} \frac{1}{n}\sum_{\ell=1}^n \cov(Z_t, Z_{t-\ell}) = 0.
$$
</div>


The result can be interpreted as that the covariances "on average" tend to zero.


___

## Ergodicity

A **realization** is a particular instance of a time series. It is one of the infinitely many possible time series that could have been observed. As a time series is a stochastic process, each one could be entirely different. The realization Is the one that was actually observed.

An **ensemble** is the theoretical totality of all possible realizations. It is the *ensemble of realizations*. We can think of that as the population of realizations. When we are thinking of means and variances, we think of them in terms of the ensemble, even though we may only be able to look at a single realization.

Say we have a stochastic process $\\{Z_t\\}_{t=1}^\infty$, we want to estimate the mean of the process, $\mu(Z_t)$. We have two candidate estimators: *ensemble average* and *time average*.

- Ensemble Average $\;\overline{\overline{z}} = \frac{1}{N}\sum_{k=1}^N Z_{t_0}^{(k)}$, where $N$ is the number of realizations we have in the ensemble; $t_0$ is any point in time.

- Time Series Average $\;\overline{z} = \frac{1}{T}\sum_{t=1}^T Z_t$

Q: Which estimator is the most appropriate? \
A: Ensemble Average. But, it is <span style='color:#EE0000FF'>impossible</span> to calculate. <span style='color:#337ab7'>We only observe one realization of $Z_t$.</span>

Q: Under which circumstances we can use the time average (only one realization of ${Z_t}$)? Is the time average an unbiased and consistent estimator of the mean? \
A: The Ergodic Theorem ensures we can use time average converges to the ensemble average as $N$ and $T$ go to infinity.


___

**Mean and Variance**

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
    - the mean is $\mu_t = E[Z_t] = \int_{-\infty}^\infty z_t f_{Z_t}(z_t)\, dz_t,$ where $f_{Z_t}(z_t)$ denotes the unconditional density of $Z_t$.
    - the variance is $\gamma_{0t} \equiv E(Z_t-\mu_t)^2 = \int_{-\infty}^\infty (z_t-\mu_t)^2 f_{Z_t}(z_t)\, dz_t $
  - Discrete case: $\mu_t = E[Z\_t] = \text{plim}_{N\to\infty} \frac{1}{N} \sum\_{i=1}^N  Z_t^{(i)}$

  Given covariance-stationarity, the 1st moment should be constant. That is 
  
  $$
  E[Z_t] = \mu_t=\mu \quad \text{for all } t.
  $$ 
  
  A condition for ergodicity for the mean is 

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

  <div class = "boxed">
  <strong>Ergodic Theorem </strong>
  If $\{Z_t\}_{t=-\infty}^{t=\infty}$ is a time series process which is strictly stationary and ergodic, and $E[\abs{Z_t}]<\infty$, and if $\overline{Z}_T = \frac{1}{T}\sum_{t=1}^T Z_t$, then as $T\to\infty$

  $$
  \overline{Z}_T \xrightarrow{a.s.} E[Z_t].
  $$
  </div>

  The ergodic theorem is a LLN for stochastic processes. It is a substantial generalization of Kolmongorov’s LLN because it allows for serial dependence in the time series.

  These results allow us to consistently estimate parameters using time series moments. Recall that consistency of an estimator means:
  - the estimator is asymptotically unbiased, and
  - its variance asymptotically collapses to zero.

  Q: Is the time average is asymptotically unbiased? \
  A: Yes. Stationarity ensures that.

  $$
  \begin{aligned}
  E[\overline{Z}_T] &= \frac{1}{T} \sum_{t=1}^T E[Z_t] \;\; \text{  by stationarity, we have constant mean, } E[Z_t] = \mu \\
  &= \frac{1}{T} \sum_{t=1}^T \mu \\ 
  &= \mu
  \end{aligned}
  $$

  Q: Is the variance going to zero as $T$ grows? \
  A: Yes. Ergodicity ensures that.
  
  $$
  \begin{aligned}
  \text{Var}[\overline{Z}_T] &= \text{Var} \left[\frac{1}{T}\sum_{t=1}^TZ_t\right] \\
  &= \frac{1}{T^2}  \text{Var} \left[\sum_{t=1}^TZ_t\right] \\
  &= \frac{1}{T^2} \sum_{t=1}^T\sum_{s=1}^T \text{Cov}(Z_t, Z_s) \\
  &= \color{#008B45} \frac{1}{T^2} \sum_{t=1}^T\sum_{s=1}^T \gamma(t-s) \\
  &= \frac{\gamma_0}{T^2} \sum_{t=1}^T\sum_{s=1}^T \rho_{t-s} \\
  &= \frac{\gamma_0}{T^2} \sum_{t=1}^T (\rho_{t-1}+\rho_{t-2}+\cdots+\rho_{t-n}) \\
  &= \frac{\gamma_0}{T^2} \left(T\rho_0 + 2(T-1)\rho_1 + 2(T-2)\rho_2 + \cdots + 2\,\rho_{T-1} \right) \\
  &= \color{#008B45}\frac{\gamma_0}{T} \sum_{k=1-T}^{T-1} (1-\frac{\vert k \vert}{T})\rho_k
  \end{aligned}
  $$

  $\gamma(t-s)$ is called the auto-covariance function. It is a function of the time shift, $k$. 
  
  $\gamma(0)$ is the variance, $\gamma(0)=\sigma^2$.

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

Alternative notation of $\text{Var}(\overline{Z}_T)$ using $\gamma(\ell)$

$$
\begin{equation}\label{eq-var-time-average}
\text{Var}(\overline{Z}_T) = \frac{\sigma^2}{T} + \frac{2}{T^2} \color{#008B45}\sum_{\ell=1}^{T-1} (T-\ell) \gamma(\ell)
\end{equation}
$$

This is a rather intriguing expression. It shows that the variance of the time average is not just the variance of the process divided by $T$, but also includes a term that accounts for the autocovariances at different lags.

- The first term $\frac{\sigma^2}{T}$ is the variance of the sample mean under i.i.d. sampling.
- The second term is a weighted Cesàro Mean of the autocovariances. It equals zero under i.i.d. sampling, but is non-zero when there is serial correlation in the data.

    We will show in what follows that it converges to zero under ergodicity. Hence,

    $$
    \var(\overline{Z}_T) \to 0 \text{ as } T\to\infty.
    $$

    Markov's inequality establishes that

    $$
    \overline{Z}_T \xrightarrow{a.s.} \mu.
    $$

We can rewrite the second term in \eqref{eq-var-time-average} using Cesàro Means:

$$
\begin{equation}\label{eq-var-time-average-cesaro}
\boxed{\frac{2}{T^2} \sum_{\ell=1}^{T-1} (T-\ell) \gamma(\ell) 
= \sum_{\ell=1}^{T-1} w_{Tl}\left(\frac{1}{\ell}\sum_{j=1}^\ell\gamma(j) \right) }
\end{equation}
$$

where

$$
w_{Tl} = \frac{2\ell}{T^2} .
$$

To shows this, let 

$$
S = \frac{2}{T^2} \sum_{\ell=1}^{T-1} (T-\ell) \gamma(\ell) ,
$$

then

$$
\text{Var}(\overline{Z}_T) = \frac{\sigma^2}{T} + S .
$$

Given

$$
\sum_{\ell=1}^{T-1} (T-\ell) \gamma(\ell) = \sum_{\ell=1}^{T-1}\sum_{j=1}^\ell \gamma(j) ,
$$

we can rewrite $S$ using a double sum

$$
S = \frac{2}{T^2} \sum_{\ell=1}^{T-1}\sum_{j=1}^\ell \gamma(j) .
$$

This is not exactly the same as the RHS of \eqref{eq-var-time-average-cesaro}, we need to get $\frac{1}{\ell}\sum_{j=1}^\ell\gamma(j)$ in order to apply the Theorem of the Cesàro Means.

Therefore, we multiply and divide $S$ by $\ell$:

$$
\begin{align*}
S &= \frac{2}{T^2} \sum_{\ell=1}^{T-1} \ell \cdot \frac{1}{\ell} \sum_{j=1}^\ell \gamma(j) \\
&= \sum_{\ell=1}^{T-1} \frac{2\ell}{T^2} \cdot \left(\frac{1}{\ell} \sum_{j=1}^\ell \gamma(j)\right) \\
&= \sum_{\ell=1}^{T-1} w_{Tl} \left(\frac{1}{\ell}\sum_{j=1}^\ell\gamma(j) \right)  
\end{align*} 
$$

where $w_{Tl} = \frac{2\ell}{T^2}$. <span style='float:right; margin-right:10px'>&#9633;</span>



Now we need to show convergence of $\sum_{\ell=1}^Tw_{Tl} \to 1$ as $T\to\infty .$

$$
\begin{split}
\sum_{\ell=1}^T w_{Tl} 
&= \frac{2}{T^2}\sum_{\ell=1}^T \ell \\
&= \frac{2}{T^2} \cdot \frac{T(T+1)}{2} \\
&= \frac{T+1}{T} \to 1 \text{ as } T\to\infty.
\end{split}
$$

Given $\frac{1}{\ell}\sum_{j=1}^\ell\gamma(j) \to 0$ (ergodicity implies $\gamma(j)\to 0$ as $j\to\infty$), we have

$$
S \to 0 \text{ as } T\to\infty.
$$

___

Let's take a closer look at the expression $\color{#008B45}\sum_{\ell=1}^{T-1} (T-\ell) \gamma(\ell).$ 


$$
\begin{split}
\sum_{\ell=1}^{T-1} (T-\ell) \gamma(\ell) &= (T-1)\gamma(1) + (T-2)\gamma(2) + \cdots \\
&\phantom{=} \quad + 2\cdot\gamma(T-2) + 1\cdot\gamma(T-1).
\end{split}
$$

Each $\gamma(\ell)$ appears $T-\ell$ times.

It is related to the **Toeplitz covariance matrix** given by:

$$
\boldsymbol{\Gamma}_T =
\begin{bmatrix}
\gamma(0)      & \color{#008B45}{\gamma(1)}      & \color{#008B45}{\gamma(2)}      & \cdots & \color{#008B45}{\gamma(T-2)}     & \color{#008B45}{\gamma(T-1)} \\
\gamma(1)      & \gamma(0)      & \color{#008B45}{\gamma(1)}      & \cdots & \color{#008B45}{\gamma(T-3)}     & \color{#008B45}{\gamma(T-2)} \\
\gamma(2)      & \gamma(1)      & \gamma(0)      & \cdots & \color{#008B45}{\gamma(T-4)}     & \color{#008B45}{\gamma(T-3)} \\
\vdots         & \vdots         & \vdots         & \ddots & \vdots          & \color{#008B45}{\vdots}      \\
\gamma(T-2)    & \gamma(T-3)    & \gamma(T-4)    & \cdots & \gamma(0)       & \color{#008B45}{\gamma(1)}   \\
\gamma(T-1)    & \gamma(T-2)    & \gamma(T-3)    & \cdots & \gamma(1)       & \gamma(0)
\end{bmatrix}_{T\times T},
$$

which is usually used to denote the $T\times T$ autocovariance matrix of a stationary time series $\lbrace Z_t\rbrace_{t=1}^T$ with autocovariance function $\gamma(\ell).$ 

Its $(t,j)$ element is $\gamma(\abs{t-j}).$
The diagonal elements are $\gamma(0)=\sigma^2,$ the first off-diagonal elements are $\gamma(1),$ the second off-diagonal elements are $\gamma(2)$ and so on.

There are $T$ diagonal elements of $\sigma^2,$ $2(T-1)$ elements of $\gamma(1).$ 

For $T=4$, the Toeplitz matrix is given by:

$$
\boldsymbol{\Gamma}_4 =
\begin{bmatrix}
\gamma(0) & \gamma(1) & \gamma(2) & \gamma(3) \\
\gamma(1) & \gamma(0) & \gamma(1) & \gamma(2) \\
\gamma(2) & \gamma(1) & \gamma(0) & \gamma(1) \\
\gamma(3) & \gamma(2) & \gamma(1) & \gamma(0)
\end{bmatrix} .
$$

$\var(Z_t)$ can be expressed as the sum of all components in $\boldsymbol{\Gamma}_T$ scaled by $\frac{1}{T^2}$:

$$
\begin{split}
\var(Z_t) &= \frac{1}{T^2} \sum_{\ell=0}^{T-1} (T-\ell) \gamma(\ell) \\
&= \frac{1}{T^2} \bold{1}_T' \boldsymbol{\Gamma}_T \bold{1}_T ,
\end{split}
$$

where $\bold{1}_T$ is a $T\times 1$ column of ones.




___

## Stationarity

Broadly speaking, a time series is said to be stationary if 
- there is no systematic change in mean (no trend), 
- if there is no systematic change in variance, and 
- if strictly periodic variations have been removed. 

In other words, the properties of one section of the data are much like those of any other section.

Measure of dependence for a stochastic process $\lbrace Z_t: t=0,1,2,\ldots, n \rbrace$
- mean function $\mu_t = E(Z_t)$
- autocovariance function at lag $k$ is given by
    
    $$
    \gamma_t(k)=\text{Cov}(Z_t, Z_{t-k})=E\big[(Z_t-\mu_t)(Z_{t-k}-\mu_{t-k})\big],
    $$ 
    
    where $k$ is the time lag; sometimes also denoted by two time points, $t$ and $t-k$, as in $\gamma_{t, t-k}\,.$
- autocorrelation function $\rho_t(k)=\text{Corr}(Z_t, Z_{t-k})$. Also denoted as $\rho_{t, t-k}$.

___

## Weakly Stationary

Consider a time series $\lbrace \bZ_t\rbrace_{t=0}^n$ with $m$-dimensional random vectors $\bZ_t = (Z_{t1}, Z_{t2}, \ldots, Z_{tm})'$, where $Z_{ti}$ is the $i$-th component of the vector at time $t$.
The time series $\lbrace \bZ_t\rbrace_{t=0}^n$ is <span style='color:#008B45FF'>*(weakly, second-order, or covariance) stationary*</span> if
1. $E[\bZ_t] = \bmu \,.$ \
The mean function $\mu_t$ is independent of $t$;
2. $\var(\bZ_t) = \E\left[(\bZ_t-\bmu)(\bZ_t-\bmu)'\right] = \bSigma$ \
The variance matrix $\Sigma$ is independent of $t.$
3. $\text{Cov}(\bZ_t, \bZ_{t-k}) = \E\left[(\bZ_t-\mu)(\bZ_{t-k}-\mu)'\right] = \bGamma_k \text{ for } \forall \,k \,.$\
 The autocovariance between two observations, $\bGamma_t(k)$, <span style='color:#337ab7'>depends only on the time lag $k$ and is independent of $t$</span>.


By symmetry, we have 

$$
\text{Cov}(\bZ_t, \bZ_{t-k}) = \bGamma(k) = \bGamma(-k)' = \text{Cov}(\bZ_{t-k}, \bZ_t)'.
$$

The symmetry property $\bGamma(k) = \bGamma(-k)'$ follows from the identity

$$
\color{#008B45}\cov(\bX, \bY) = \cov(\bY, \bX)' .
$$

___

We calculate the lag-$k$ covariance matrix as

$$
\begin{split}
\bGamma(k) &= \text{Cov}(\bZ_t, \bZ_{t-k}) \\
&= \E\left(\bZ_t \bZ_{t-k}'\right) - \E(\bZ_t)\E(\bZ_{t-k})' \\
&= \E\left(\bZ_t \bZ_{t-k}'\right) - \bmu \bmu'
\end{split}
$$

where

$$
\begin{split}
\E\left(\bZ_t \bZ_{t-k}'\right) 
&= \E\left\{
\begin{pmatrix}
Z_{t1} \\ 
Z_{t2} \\
\vdots \\
Z_{tm}
\end{pmatrix}
\begin{pmatrix}
Z_{t-k,1} &
Z_{t-k,2} &
\cdots &
Z_{t-k,m}
\end{pmatrix}
\right\} \\
&= 
\begin{pmatrix}
\E[Z_{t1} Z_{t-k,1}] & \E[Z_{t1} Z_{t-k,2}] & \cdots & \E[Z_{t1} Z_{t-k,m}] \\
\E[Z_{t2} Z_{t-k,1}] & \E[Z_{t2} Z_{t-k,2}] & \cdots & \E[Z_{t2} Z_{t-k,m}] \\
\vdots & \vdots & \ddots & \vdots \\
\E[Z_{tm} Z_{t-k,1}] & \E[Z_{tm} Z_{t-k,2}] & \cdots & \E[Z_{tm} Z_{t-k,m}]
\end{pmatrix}
\end{split}
$$

Covariance of the reverse time order is given by

$$
\begin{split}
\bGamma(-k) &= \text{Cov}(\bZ_{t-k}, \bZ_t) \\
&= \E\left(\bZ_{t-k}\bZ_t' \right) - \E(\bZ_{t-k})\E(\bZ_{t})' \\
&= \E\left(\bZ_{t-k}\bZ_t'\right) - \bmu \bmu'
\end{split}
$$

where

$$
\begin{split}
\E\left(\bZ_{t-k} \bZ_t'\right) 
&= \E\left\{
\begin{pmatrix}
Z_{t-k,1} \\ 
Z_{t-k,2} \\
\vdots \\
Z_{t-k,m}
\end{pmatrix}
\begin{pmatrix}
Z_{t1} &
Z_{t2} &
\cdots &
Z_{tm}
\end{pmatrix}
\right\} \\
&= 
\begin{pmatrix}
\E[Z_{t-k,1} Z_{t1}] & \E[Z_{t-k,1} Z_{t2}] & \cdots & \E[Z_{t-k,1} Z_{tm}] \\
\E[Z_{t-k,2} Z_{t1}] & \E[Z_{t-k,2} Z_{t2}] & \cdots & \E[Z_{t-k,2} Z_{tm}] \\
\vdots & \vdots & \ddots & \vdots \\
\E[Z_{t-k,m} Z_{t1}] & \E[Z_{t-k,m} Z_{t2}] & \cdots & \E[Z_{t-k,m} Z_{tm}]
\end{pmatrix}
\end{split}
$$

This is simply the transpose of the earlier moment matrix due to the reversal of the time indices. As expected from the symmetry property:

$$
\E\left(\bZ_t \bZ_{t-k}'\right) = \left[\E\left(\bZ_{t-k} \bZ_t'\right)\right]' 
$$

Thus

$$
\text{Cov}(\bZ_t, \bZ_{t-k}) = \bGamma(k) = \bGamma(-k)' = \text{Cov}(\bZ_{t-k}, \bZ_t)'. \tag*{\(\square\)}
$$

___

In the *univariate* cases where $Z_t$ is a scaler, the above conditions can be simplified as follows:

- $E[Z_t] = \mu$ 
- $\var(Z_t) = \E\left[(Z_t-\mu)(Z_t-\mu)'\right] = \sigma^2$
- $\cov(Z_t,Z_{t-k}) = \E\left[(Z_t-\mu)(Z_{t-k}-\mu)'\right] = \gamma(k)$

*Nothing* is assumed about the collection of *joint distributions* of the process. Instead, we only are specifying the characteristics of the <span style='color:#337ab7'>first two **moments**</span> of the process.

___

## Strictly Stationary

We say $\lbrace Z_t\rbrace_{t=0}^n$ is <span style='color:#008B45'>*strictly (or strongly) stationary*</span> if the <span style='color:#337ab7'>joint distribution</span> of

$$
(Z_{t_1}, \ldots, Z_{t_n})
$$

is the same as 

$$
(Z_{t_1-k}, \ldots, Z_{t_n-k})
$$

for all time points $t_1, t_2, \ldots, t_n$ and for all time lags $k$.

In other words, shifting the time origin by an amount $k$ has no effect on the joint distributions, which must therefore depend only on the intervals between $t_1, t_2, \ldots, t_n$. This is a very strong condition.

If $\lbrace Z_t\rbrace_{t=0}^n$ is strictly stationary, then the joint distribution of any finite collection of time points is invariant to shifts in time. 

Mathematically, the joint distribution of $(Z_t, \ldots, Z_{t+\ell})$ is independent of $t$ for all $\ell.$

This means that the statistical properties of the process do not change over time.



Basic properties of a strictly stationary time series $\lbrace Z_t\rbrace$:
1. $Z_t$'s are from the same distribution.\
   Since the above condition holds for all sets of time points $t_1, t_2, \ldots, t_n$, it must hold when $n = 1$; i.e., there is only one time point. This implies $Z_t$ and $Z_{t-k}$ have the same marginal distribution for all $t$ and $k$.
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


___

**Useful properties of stationarity**

<div class = "boxed">
<strong>Theorem</strong>  If $\boldsymbol{y}_t$ is strictly stationary and $\boldsymbol{x}_t=\boldsymbol{\phi}(\boldsymbol{y}_t, \boldsymbol{y}_{t-1}, \boldsymbol{y}_{t-2}, \ldots) \in \mathbb{R}^q$ is a random vector, then $\boldsymbol{x}_t$ is strictly stationary.
</div>

- **Stationarity is preserved by transformation.** That is,
transformations of strictly stationary processes are also strictly stationary.

  As an example, the theorem applies to the infinite-order moving average transform:

  $$
  x_t = \sum_{j=0}^\infty a_j y_{t-j}
  $$

  where $a_j$ are coefficients and are absolutely convergent ($\sum_{j=0}^\infty \abs{a_j} <\infty$). 

  Then if $y_t$ is strictly stationary, then $x_t$ is also strictly stationary.

- This is useful for the study of stochastic processes which are constructed from underlying errors, and for the study of sample statistics such as linear regression estimators which
are functions of sample averages of squares and cross-products of the original data.


<div class = "boxed">
<strong>Ergodicity of Functions Theorem</strong>  Any transformation $g(.)$ of a stationary and ergodic process $\{Y_t\}$ is also stationary and ergodic. That is,  $\{g(Y_t)\}$ is stationary and ergodic. Therefore, if $E[g(Y_t)]$ exists then the ergodic theorem gives

$$
\overline{g} = \frac{1}{T} \sum_{t=1}^T g(Y_t) \xrightarrow{p} E[g(Y_t)]
$$
</div>

Application of the theorem: the <span style='color:#337ab7'>sample autocovariances</span> 

$$
\hat{\gamma}_{t}(j) = \frac{1}{T} \sum_{t=j+1}^T (Y_t-\overline{Y})(Y_{t-j}-\overline{Y})
$$

converge in probability to the <span style='color:#337ab7'>population autocovariances</span> 

$$
\gamma_{t}(j) = \text{Cov}(Y_t, Y_{t-j}) = E[(Y_t-\mu)(Y_{t-j}-\mu)].
$$

That is

$$
\hat{\gamma}_{t}(j) \xrightarrow{p} \gamma_{t}(j)
$$

- $\gamma$ denotes *autocovariance* coefficients; $\rho$ denotes *autocorrelation* coefficients. 
  
  - $\gamma(1)$ is called the autocovariance function of lag 1 and
  - $\rho(1)$ the autocorrelation function of lag 1.

- $\gamma(0)=\var(Y_t)$ is the variance of the process.



References:

- Chapter 14 Time Series, Econometrics, Hansen, pp 511. 
- Chapter 12.4 Serial Correlation, Greene, Econometric Analysis, 5ed, pp 259.