---
layout: post
title: OLS Asymptotics
tag: study
update: 2023-12-07
---

$$
\newcommand{\indep}{\perp \!\!\! \perp}
$$

<a class="top-link hide" href="#" id="js-top">↑</a>


The asymptotic properties of estimators are their properties as the number of observations in a sample becomes very large and tends to infinity.

Q: Why are we interested in large sample properties, like consistency, when in practice we have finite samples? \
A: As a first approximation, the answer is that if we can show that an estimator has good large sample properties, then we may be optimistic about its finite sample properties. For example, if an estimator is inconsistent, we know that for finite samples it will definitely be biased.


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
\widehat{M}^{-1}_{XX} = \frac{1}{n} \sum_{i=1}^n x_ix_i' \xrightarrow{P} \text{E}[x_ix_i'] = M_{XX}
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
<li id="ass4"> The $K\times K$ moment matrix $\color{#008B45}M_{X\Omega X}=\mathbb{E}[u_i^2x_ix_i']$ exists and is non-singular, where $\color{#008B45}\Omega=\mathbb{E}[uu'\vert X]$ is the <strong>error covariance matrix</strong>. (this assumption ensures asymptotic normality) </li>
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

<div style='margin-top:-2em; margin-bottom:3em'><span style='float:right; margin-right:10px; '>&#9633;</span></div>


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
\begin{equation} \label{eq-beta-distribution-hansen}
\sqrt{n} (\hat{\beta}_{OLS}-\beta) \xrightarrow{d} N(0, V_\beta), 
\end{equation}
$$
 
or equivalently,

$$
\begin{equation} \label{eq-beta-distribution-greene}
\hat{\beta}_{OLS} \overset{a}{\sim} N(\beta, V_\beta/n)
\end{equation}
$$

where 

$$
V_\beta=\sigma^2M^{-1}_{XX}
$$ 

is the variance of the asymptotic distribution of $$\sqrt{n} (\hat{\beta}_{OLS}-\beta).$$ 
Consequently, $V_\beta$ is often referred to as the **asymptotic covariance matrix** of $$\sqrt{n} \hat{\beta}_{OLS}.$$ $\sqrt{n}\beta$ can be omitted, as adding or subtracting a constant does not change the covariance.

In practice, $\sqrt{n}$ is often omitted too, you may see $V_\beta$ referred to as the asymptotic variance of $ \hat{\beta}_{OLS},$ with $\sqrt{n}$ omitted. This is indeed confusing, but it is the common convention used in the literature. You have to determine whether the asymptotic variance is stabilized.

- Eq $\eqref{eq-beta-distribution-hansen}$ is used in Hansen's textbook. Always implies stabilized variance with a factor of $\sqrt{n},$ whether or not written explicitly. 

- Eq $\eqref{eq-beta-distribution-greene}$ is used in Greene's textbook and in the core econometric course at Oxford. Unstabilized variance. The variance of the estimator depends on the sample size. But the benefit with this notation is that $V_\beta/n$ coincides with the finite sample variance.

**Alternative notation** for the asymptotic variance of $\sqrt{n} (\hat{\beta}_{OLS}-\beta):$

$$
V_\beta = \color{#008B45}\text{aVar}\left(\sqrt{n} (\hat{\beta}_{OLS}-\beta) \right)
$$


$\overset{a}{\sim}$ stands for "approximate (asymptotic)" distribution.


Distinguish the asymptotic variance $V_\beta$ from the finite-sample conditional variance (or exact variance) $V_{\hat{\beta}}$:

$$
\begin{split}
V_\beta &= \text{aVar}\left(\sqrt{n} (\hat{\beta}-\beta) \right) = \sigma^2M^{-1}_{XX} \\
V_{\hat{\beta}} &= \var{(\hat{\beta} \mid X)} = \sigma^2 (X'X)^{-1} .
\end{split}
$$

Notice that $V_{\hat{\beta}}$ is the exact conditional variance of $\hat{\beta}$ and $V_\beta$ is the asymptotic variance of $\sqrt{n} (\hat{\beta}-\beta).$

Given 

$$
\frac{1}{n}(X'X) \xrightarrow{p} M_{XX}
$$

then 

$$
n(X'X)^{-1} \xrightarrow{p} M_{XX}^{-1}  .
$$

$V_\beta$ should be (roughly) $n$ times as large as $V_{\hat{\beta}}$, or $V_\beta \approx n V_{\hat{\beta}}.$
As $n\to \infty$

$$
n V_{\hat{\beta}} \xrightarrow{p} V_\beta .
$$

- $V_{\hat{\beta}}$ is useful for practical inferences (such as computation of standard errors and test) since it is the variance of the estimator $\hat{\beta}.$

- $V_\beta$ is useful for asymptotic theory as it is well defined in the limit as $n$ goes to infinity. 


___


## Covariance Matrix Estimation

We have shown that $\sqrt{n}(\hat{\beta}-\beta)$ is asymptotically normal with asymptotic covariance matrix $B_\beta.$ For asymptotic inferences (such as confidence intervals and tests) we need a consistent estimator of $V_\beta.$ 

The standard moment estimator of $M_{XX}$ is $\widehat{M}_{XX}$ defined as

$$
\widehat{M}_{XX} = \frac{1}{n} \sum_{i=1}^n x_i x_i'
$$

and an estimator for $$M^{-1}_{XX}$$ is $\widehat{M}^{-1}_{XX}.$

$$
\widehat{M}^{-1}_{XX} = \left(\frac{1}{n}\sum_{i=1}^nx_ix_i'\right)^{-1} \xrightarrow{p} \E(x_ix_i') = M^{-1}_{XX}
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

Using Slutsky's theorem (continuous mapping theorem), a natural plug-in estimator for $V_\beta$ is

$$
\widehat{V}_\beta = \hat{\sigma}^2_{OLS} \left(\frac{X'X}{n}\right)^{-1} \xrightarrow{p} \sigma^2 M_{XX}^{-1} = V_\beta .
$$

So that $$\widehat{V}_\beta$$ is consistent for $V_\beta,$ as desired.

Replacing $V$ with $\hat{V}$ in the asymptotic distribution, we have

$$
\hat{\beta}_{OLS} \overset{a}{\sim} N(\beta, \widehat{V}_\beta/n)
$$

which is the form used to construct approximate confidence intervals and asymptotically valid test statistics.

Note that 

$$
\begin{align*}
\widehat{V}_\beta/n &= \left(\frac{1}{n}\right) \hat{\sigma}^2_{OLS} \left(\frac{X'X}{n}\right)^{-1} \\
&= \left(\frac{1}{n}\right) \hat{\sigma}^2_{OLS}\, n\, \left({X'X}\right)^{-1} \\
&= \hat{\sigma}^2_{OLS}\left({X'X}\right)^{-1}  \\
&= \widehat{V}_{\hat{\beta}}
\end{align*}
$$

which is the same as the exact finite sample conditional variance $\text{Var}(\hat{\beta}_{OLS}\vert X)$ that we obtained in the classical linear regression model with normally distributed errors.

___

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



___


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

has the asymptotic distribution

$$
w \overset{\text{a}}{\sim} \chi^2(p).
$$


In the conditional homoskedasticity case, we have $\hat{V}/n = \hat{\sigma}^2_{OLS} (X'X)^{-1}$. In this case we have

$$
w = (\hat{\theta}_{OLS}-\theta)'\left[\hat{\sigma}^2_{OLS} H(X'X)^{-1}H' \right]^{-1} (\hat{\theta}_{OLS}-\theta)
$$

This test only has an asymptotic justification, and we know that $p$ times a $F(p, n-K)$ random variable converges in distribution to a $\chi^2(p)$ as $n\to\infty$.

$w$ is called an Wald statistic, the corresponding test is called an **Wald test**.



___


## The Delta Method

More complicated inferences for arbitrary nonlinear functions of the estimator $\hat{\boldsymbol{\theta}}$ may be performed via Taylor's Theorem or the *delta method*.

If $\sqrt{T}(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}\_0) \overset{\text{a}}{\sim} \mathcal{N}(0, \boldsymbol{V}_\theta)$, then a nonlinear function $f(\hat{\boldsymbol{\theta}})$ has the following asymptotic distribution:

$$
\sqrt{T}\big(f(\hat{\boldsymbol{\theta}}) - f(\boldsymbol{\theta}_0) \big)  \overset{\text{a}}{\sim} \mathcal{N}(0, \boldsymbol{V}_f), \quad\quad  
\boldsymbol{V}_f \equiv \frac{\partial f}{\partial \boldsymbol{\theta}'} \boldsymbol{V}_\theta \frac{\partial f}{\partial \boldsymbol{\theta}}
$$

which follows from first-order Taylor series approximation for $f(\boldsymbol{\theta})$ around $\boldsymbol{\theta}_0$. 
Higher-order terms converge to zero faster than $1/\sqrt{T}$ hence only the first term of the expansion matters for the asymptotic distribution of $f(\hat{\boldsymbol{\theta}})$.

{% cite Hausman1978 %} exploits the fact that any asymptotically efficient estimator of a parameter $\theta$, say $\hat{\theta}_e$, must possess the property that it is asymptotically <u>uncorrelated</u>
with the difference $\hat{\theta}_a - \hat{\theta}_e$, where $\hat{\theta}_a$ is any other estimator of $\theta$. 

If not, then there exists a a linear combination of $\hat{\theta}_e$ and $\hat{\theta}_a - \hat{\theta}_e$ that is more efficient than $\hat{\theta}_e$, contradicting the assumed eae e
efficiency of $\hat{\theta}_e$. The result follows directly, then, since:

$$
\begin{aligned}
\text{aVar} [\hat{\theta}_a] &= \text{aVar} [\hat{\theta}_e + \hat{\theta}_a - \hat{\theta}_e] = \text{aVar} [\hat{\theta}_e] + \text{aVar} [\hat{\theta}_a - \hat{\theta}_e] \\
& \Longrightarrow \text{aVar} [\hat{\theta}_a - \hat{\theta}_e] = \text{aVar} [\hat{\theta}_a] - \text{aVar} [\hat{\theta}_e]
\end{aligned}
$$


Let's say you are interested in knowing the variance of $\widehat{VD}\equiv \frac{\hat{\sigma}_b^2}{\hat{\sigma}_a^2}$, and you know the distributions of $\hat{\sigma}_a^2$ and $\hat{\sigma}_b^2$. The variance of the limiting distribution is not apparent since the two variance estimators are clearly *not* asymptotically uncorrelated. 

Then you could apply the delta method to $f(\hat{\theta}_1, \hat{\theta}_2) \equiv \frac{\hat{\theta}_1}{\hat{\theta}_2}$, where $\hat{\theta}_1\equiv \hat{\sigma}_b^2-\hat{\sigma}_a^2$, $\hat{\theta}_2\equiv \hat{\sigma}_a^2$, and observe that $\hat{\sigma}_b^2-\hat{\sigma}_a^2$ and $\hat{\sigma}_a^2$ are asymptotically uncorrelated because $\hat{\sigma}_a^2$ is an efficient estimator.

**References**

- Chapter 7 Asymptotic Theory for Least Squares. **Econometrics**. by Bruce Hansen, 2022. 
-  Chapter 5 Large-Sample Properties. **Econometric Analysis** , 5th Edition, by William H. Greene, Prentice Hall, 2003. 
- Simulation of OLS estimators: 
    - Introduction to Econometrics with R: <https://www.econometrics-with-r.org/4.5-tsdotoe.html>
    - Asymptotic Theory, Regression Analysis and Potential Outcomes: <https://rpubs.com/SSJ/991088>

{% bibliography --cited %}