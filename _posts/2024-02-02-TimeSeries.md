---
layout: post
title: Time Series
tag: study
update: 2024-02-04
---

$$
\newcommand{\indep}{\perp \!\!\! \perp}
$$

## Ergodicity

A **realization** is a particular instance of a time series. It is one of the infinitely many possible time series that could have been observed. As a time series is a stochastic process, each one could be entirely different. The realization Is the one that was actually observed.

An **ensemble** is the theoretical totality of all possible realizations. It is the *ensemble of realizations*. We can think of that as the population of realizations. When we are thinking of means and variances, we think of them in terms of the ensemble, even though we may only be able to look at a single realization.

Say we have a process ${Z_t}$, we want to estimate the mean of the process, $\mu(Z_t)$. We have two candiate estimators: *ensemble average* and *time average*.

- Ensemble Average $\;\overline{\overline{z}} = \frac{\sum_{i=1}^m Z_i}{m}$, where $m$ is the number of realizations we have in the ensemble.

- Time Series Average $\;\overline{z} = \frac{\sum_{t=1}^n Z_t}{n}$

Q: Which estimator is the most appropriate" \
A: Ensemble Average. But, it is impossible to calculate. We only observe one realization of $Z_t$.

Q: Under which circumstances we can use the time average (only one realization of ${Z_t}$)? Is the time average an unbiased and consistent estimator of the mean? \
A: The Ergodic Theorem gives us the answer.

- Erogodic Definition: A covariance-stationary process is ergodic for the mean if

  $$
  \text{plim}\; \overline{z} = E[Z_t] = \mu
  $$

  A sufficient condition for ergodicity for the mean is 

  $$
  \rho_k \to 0 \text{  as  } k\to\infty.
  $$
  
  A sufficient condition for ergodicity for the second moment is 

  $$
  \sum_k \vert\rho_k\vert < \infty \text{  as  } k\to\infty.
  $$

  A process which is ergodic in the first and second moments is usually referred as *ergodic in the wide sense*.


- Ergodic Theorem \
  If $Z_t$ is strictly stationary and ergodic and $E[Z_t]<\infty$, and if $\overline{Z}\_T = \frac{1}{T}\sum_{t=1}^T Z_t$, then as $T\to\infty$

  $$
  \sqrt{T}\, \overline{Z}_T \xrightarrow{p} E[Z_t].
  $$

  These results allow us to consistently estimate parameters using time series moments. Recall that consistency of an estimator means:
  - the estimator is asymptotically unbiased, and
  - its variance asymptotically collapeses to zero.

  Q: Is the time average is asympototically unbiased? Yes. Stationarity ensures that.

  $$
  \begin{aligned}
  E[\overline{Z}_T] &= \frac{1}{T} \sum_{t=1}^T E[Z_t] \;\; \text{  by stationarity } E[Z_t] = \mu \\
  &= \frac{1}{T} \sum_{t=1}^T \mu \\ 
  &= \mu
  \end{aligned}
  $$

  Q: Is the variance going to zero as $T$ grows? Yes. 
  
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

  $\gamma(t-s)$ is called the auto-covariance funtion. $\gamma(0)$ is the variance, $\gamma(0)=\sigma^2$.

  $\rho(t-s)$ is the auto-correlation function. 

  $$
  \rho(t-s) = \frac{\gamma(t-s)}{\sqrt{\sigma_t^2}\sqrt{\sigma_s^2}}
  $$

  <span style='color:#797D7F'>
  If stationarity holds, then $\sigma_t^2=\sigma_s^2=\sigma^2=\gamma_0$. And we have </span>
  
  $$
  {\color{#797D7F} \rho (t-s)=\frac{\gamma (t-s)}{\gamma(0)}.}
  $$

  

  Take the limit

  $$
  \begin{aligned}
  \lim_{T\to\infty} \text{Var}(\overline{Z}_T) &= \lim_{T\to\infty} \frac{\gamma_0}{T} \sum_k (1-\frac{\vert k \vert}{T})\rho_k \\
  &= 0 \;\;\;\text{by Ergodicity, } \rho_k \to 0 \text{ as } k\to\infty.
  \end{aligned}
  $$
  