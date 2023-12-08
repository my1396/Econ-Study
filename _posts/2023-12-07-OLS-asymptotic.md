---
layout: post
title: OLS Asymptotics
tag: study
update: 2023-12-07
---


For OLS estimator to be *consistent*, a set of assumptions need to be met:
<ol type="p1">
<li id="ass1"> $y_i=x_i'\beta+u_i$ for $i=1, \ldots, n$ or $y=X\beta+u$. In other words, DGP is correctly specified.</li>
<li id="ass2"> $(y_i, x_i')$ are iid distributed with $\mathbb{E}[x_iu_i]=\vec{0}$ for all $i=1, \ldots, n$, $\vec{0}$ is a vector of zeros of order $K$. (Orthogonality Assumption $\mathbb{E}[x_iu_i]=\vec{0}$ ) </li>
<li id="ass3"> The $K\times K$ moment matrix $M_{XX}=\mathbb{E}[x_ix_i']$ exists and is non-singular. </li>
</ol>
Then $\hat{\beta}_{OLS} \xrightarrow{p} \beta$. This set of assumptions ensures the applicability of LLN such that consistency is ensured too.

We have 

$$
\begin{align*}
\hat{\beta}_{OLS} &= (X'X)^{-1}X'y \\
&= (X'X)^{-1}X'(X\beta + u) \\
&= \beta + (X'X)^{-1}X'u \\
&= \beta + \left(\frac{X'X}{n}\right)^{-1}  \left(\frac{X'u}{n}\right)
\end{align*}
$$

and

$$
\left(\frac{X'u}{n}\right) = \frac{1}{n}X'u = \frac{1}{n} \sum_{i=1}^n x_iu_i
$$

With iid data and assumption <a href="#ass2">2)</a>, by LLN, the $K\times 1$ vector of sample means converges in probability to the population parameter.

$$
\frac{1}{n} \sum_{i=1}^n x_iu_i \xrightarrow{P} \text{E}[x_iu_i] = \vec{0}
$$

Hence we have

$$
\left(\frac{X'u}{n}\right) \xrightarrow{P} \vec{0}
$$

Similarly,

$$
\left(\frac{X'X}{n}\right) = \frac{1}{n}X'X = \frac{1}{n} \sum_{i=1}^n x_ix_i'
$$

With iid data and assumption <a href="#ass3">3)</a>, by LLN, the $K\times K$ matrix of sample means converges in probability to the moment matrix.

$$
\frac{1}{n} \sum_{i=1}^n x_ix_i' \xrightarrow{P} \text{E}[x_ix_i'] = M_{XX}
$$

Hence we have

$$
\left(\frac{X'X}{n}\right) \xrightarrow{P} M_{XX}
$$


Note that consistency $(\mathbb{E}[\hat{\theta}]\xrightarrow{p}\theta)$ is a "large sample" or asymptotic property, i.e., a property that holds in the limit as $n$ tends to infinity. \
By contrast, unbiasedness $(\mathbb{E}[\hat{\theta}]=\theta)$ is a "finite sample" or "small sample" property.

An unbiased estimator will usually be consistent, but need not be. \
Consistency *further* requires that $\text{Var}(\hat{\theta})\rightarrow 0$ as $n\rightarrow \infty$. 
<span style='float:right'>$\square$</span>



For OLS estimator to have a limit distribution which is normal (aka *asyptotic normality*), the following set of assumptions need to be met:

&emsp;&ensp;Conditions <a href="#ass1">**1)**</a> to <a href="#ass3">**3)**</a> in the consistency assumptions above; in additon to a new assumption:

<ol type="p1" start="4">
<li id="ass4"> The $K\times K$ moment matrix $M_{X\Omega X}=\mathbb{E}[u_i^2x_ix_i']$ exists and is non-singular, where $\Omega=\mathbb{E}[uu'\vert X]$ is the error covariance matrix. (this assumption ensures asymptotic normality) </li>
</ol>

Conditions <a href="#ass4">**4)**</a> satisfies the 2nd order moment requirement, combining with <a href="#ass3">**3)**</a>, the 1st order moment condition, we can apply the Central Limit Theorem to $\frac{1}{n}X'u$.


$x_iu_i$ are iid (assumption <a href="#ass2">2)</a>, and we have $E(x_iu_i)=0$ (assumption <a href="#ass3">3)</a> and $\text{Var}(x_iu_i)=E[(x_iu_i)(x_iu_i)']=E(u_i^2x_ix_i')=M_{X\Omega X}$ finite (assumption <a href="#ass4">4)</a>. 

Using the <a href="#CLT random vector">*CLT for random vectors*</a>, 

$$
\sqrt{n}\left(\frac{1}{n}\sum_{i=1}^nx_iu_i\right) = \frac{1}{\sqrt{n}}\sum_{i=1}^nx_iu_i \xrightarrow{d} N(0,M_{X\Omega X}).
$$

That is,

$$
\sqrt{n}\left(\frac{1}{n}X'u\right) = \frac{X'u}{\sqrt{n}}  \xrightarrow{d} N(0,M_{X\Omega X}).
$$

In order to construct the form $\frac{X'u}{\sqrt{n}}$, we form the following expression

$$
\sqrt{n} (\hat{\beta}-\beta) = \left(\frac{X'X}{n}\right)^{-1}  \left(\frac{X'u}{\sqrt{n}}\right)
$$

We also have $\left(\frac{X'X}{n}\right)^{-1} \xrightarrow{p} M_{XX}^{-1} $. Then using generalized Slutsky's Thm., and the symmetry of $M_{XX}^{-1}$, we obtain the limit distibution of the product

$$
\left(\frac{X'X}{n}\right)^{-1}  \left(\frac{X'u}{\sqrt{n}}\right) \xrightarrow{d} N(0, M_{XX}^{-1} M_{X\Omega X} M_{XX}^{-1}).
$$

And hence 

$$
\sqrt{n} (\hat{\beta}-\beta) \xrightarrow{d} N(0, M_{XX}^{-1} M_{X\Omega X} M_{XX}^{-1}).
$$ 
<span style="float:right">$\square$</span>


Multiplying $(\hat{\beta}-\beta)$ by $\sqrt{n}$ is a stabilizing transformation — i.e., the moments do not depend on $n$.

- stabilize the variance: $\text{Var}(\sqrt{n}\hat{\beta}) \xrightarrow{p} M_{XX}^{-1} M_{X\Omega X} M_{XX}^{-1}$
- stabilize the mean: $\text{E}[\sqrt{n}(\hat{\beta}-\beta)] = 0$


<div id="CLT random vector"><strong>CLT for random vectors</strong></div>

Suppose that $z_1, \ldots, z_n$ are iid distributed $K\times 1$ random vectors, with $E(z_i)=\mu$ and $\text{Var}(z_i)=\Sigma$ finite. \
Let $\bar{z}\_n = \frac{1}{n}\sum_{i=1}^n z_i$ donote the $K\times 1$ vector os sample means for a sample of size $n$, and let $w_n = \sqrt{n}(\bar{z}\_n-\mu) = \frac{1}{\sqrt{n}}\sum_{i=1}^n(\bar{z}\_n-\mu)$. Then

$$
w_n \xrightarrow{d} N(\vec{0},\Sigma).
$$



Note that, we do NOT require any of the following in order to ensure aymptotic normality:
1. conditional homoskedasticity $(\text{Var}(u_i\vert x_i) = \sigma^2)$;
2. linear conditional expectation $(\mathbb{E}(y_i\vert x_i) = x_i'\beta$ or the stronger form $\mathbb{E}(y\vert X) = X'\beta)$;
3. normal conditional distribution $(y\vert X \sim N(X\beta, \sigma^2I))$.

The limit distribution is

$$
\sqrt{n} (\hat{\beta}_{OLS}-\beta) \xrightarrow{d} N(0, \sigma^2M^{-1}_{XX})
$$

also can be written as 

$$
\sqrt{n} (\hat{\beta}_{OLS}-\beta) \xrightarrow{d} N(0, V), \text{or}
$$

$$
\hat{\beta}_{OLS} \overset{a}{\sim} N(\beta, V/n)
$$

where $V=\sigma^2M^{-1}_{XX}$. \
$V/n$ is called the asymptotic variance. \
$\overset{a}{\sim}$ stands for "approximate (asymptotic)" distribution.

$$
\left(\frac{1}{n}\sum_{i=1}^nx_ix_i'\right)^{-1} \xrightarrow{p} M^{-1}_{XX}
$$

or

$$
\left(\frac{X'X}{n}\right)^{-1} \xrightarrow{p} M^{-1}_{XX}
$$

gives us a consistent estimator for $M^{-1}_{XX}$.

Both 

$$
\hat{\sigma}^2_{OLS} = \frac{\hat{u}'\hat{u}}{n-K}
$$

and 

$$
\hat{\sigma}^2_{ML} = \frac{\hat{u}'\hat{u}}{n}
$$

are consistent estimators of $\sigma^2$ (only $\hat{\sigma}^2_{OLS}$ is unbiased).

Using Slutsky's theorem, 

$$
\hat{V} = \hat{\sigma}^2_{OLS} \left(\frac{X'X}{n}\right)^{-1} \xrightarrow{p} V.
$$

Replacing $V$ with $\hat{V}$ in the asymptotoic distribution, we have

$$
\hat{\beta}_{OLS} \overset{a}{\sim} N(\beta, \hat{V}/n)
$$

which is the form used to construct approximate confidence intervals and asymptotically valid test statistics.

Note that 

$$
\begin{align*}
\hat{V}/n &= \left(\frac{1}{n}\right) \hat{\sigma}^2_{OLS} \left(\frac{X'X}{n}\right)^{-1} \\
&= \left(\frac{1}{n}\right) \hat{\sigma}^2_{OLS}\, n\, \left({X'X}\right)^{-1} \\
&= \hat{\sigma}^2_{OLS}\left({X'X}\right)^{-1}
\end{align*}
$$

which is the same as the exact finite sample conditional variance $\text{Var}(\hat{\beta}_{OLS}\vert X)$ that we obtianed in the classical linear regression model with nomally distributed errors.



## Hypothesis testing

Without knowing the distribution of $u\vert X$, we use asymptotic results to approximate the distribution of $\hat{\beta}_{OLS}$ in large finite sample.

Let the scalar $\hat{v}_{kk}$ denote the $k^{\text{th}}$ element of the main diagonal of the variance matrix. 

$\hat{V}/n=\hat{\sigma}^2_{OLS}(X'X)^{-1}$. 

Since 

$$
\hat{\beta}_k \overset{\text{a}}{\sim} \text{N}(\beta_k, \hat{v}_{kk})
$$

we also have 

$$
t_k=\frac{\hat{\beta}_k-\beta_k}{\sqrt{\hat{v}_{kk}}} = \frac{\hat{\beta}_k-\beta_k}{se_k} \overset{\text{a}}{\sim} \text{N}(0,1)
$$

$t_k$ will be compared with the crit. value of $\text{N}(0,1)$ at the desired sig. level.


Why can we treat $t_k$ here as a draw from the standard normal distribution, even though we have estimated the unknown $\sigma_2$? \
This is justified by an asymptotic approximation that a $t(n-K)$ random variable converges in distribution to a $\text{N}(0,1)$ as $n\to\infty$.


## Multiple linear restrictions

$H$ is restriction matrix $p\times K$ with $\text{rank}(H)=p$.

$$
\hat{\theta}_{OLS} = H\hat{\beta}_{OLS} \overset{\text{a}}{\sim} \text{N}(H\beta, H(\hat{V}/n)H')
$$

The test statistic

$$
\begin{align*}
w &= (\hat{\theta}_{OLS}-\theta)'\left[\widehat{\text{Var}}(\hat{\theta}_{OLS \vert X}) \right]^{-1} (\hat{\theta}_{OLS}-\theta) \\
&= (\hat{\theta}_{OLS}-\theta)'\left[H(\hat{V}/n)H' \right]^{-1} (\hat{\theta}_{OLS}-\theta)
\end{align*}
$$

has the aymptotic distrbution

$$
w \overset{\text{a}}{\sim} \chi^2(p).
$$


In the conditional homoskedasticity case, we have $\hat{V}/n = \hat{\sigma}^2_{OLS} (X'X)^{-1}$. In this case we have

$$
w = (\hat{\theta}_{OLS}-\theta)'\left[\hat{\sigma}^2_{OLS} H(X'X)^{-1}H' \right]^{-1} (\hat{\theta}_{OLS}-\theta)
$$

This test only has an asymptotic justification, and we know that $p$ times a $F(p, n-K)$ random variable converges in distribution to a $\chi^2(p)$ as $n\to\infty$.

$w$ is called an Wald statistic, the corresponding test is called an **Wald test**.
