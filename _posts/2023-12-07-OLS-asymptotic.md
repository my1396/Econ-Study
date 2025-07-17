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



For OLS estimator to have a limit distribution which is normal (aka *asymptotic normality*), the following set of assumptions need to be met:

&emsp;&ensp;Conditions <a href="#ass1">**1)**</a> to <a href="#ass3">**3)**</a> in the consistency assumptions above; in addition to a new assumption:

<ol type="p1" start="4">
<li id="ass4"> The $K\times K$ moment matrix $\color{#008B45}M_{X\Omega X}=\mathbb{E}[x_iu_iu_i'x_i']$ exists and is non-singular, where $\color{#008B45}\Omega=\mathbb{E}[uu'\vert X]$ is an $n\times n$ <strong>error covariance matrix</strong>. (this assumption ensures asymptotic normality) </li>
</ol>

Different forms of error covariance matrices:

- **Homoskedasticity and Non-Autocorrelation** (spherical disturbances)

$$
\bOmega = \sigma^2\begin{bmatrix}
1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 1
\end{bmatrix} = \sigma^2 \bI_n
$$

- **Heteroskedasticity and Non-Autocorrelation**

$$
\bOmega = \sigma^2\begin{bmatrix}
\omega_{11} & 0 & \cdots & 0 \\
0 & \omega_{22} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \omega_{nn}
\end{bmatrix} = \begin{bmatrix}
\sigma^2_1 & 0 & \cdots & 0 \\
0 & \sigma^2_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \sigma^2_n
\end{bmatrix}
$$


- **Autocorrelation and Homoskedasticity**

$$
\bOmega = \sigma^2\begin{bmatrix}
1 & \rho_1 & \cdots & \rho_{n-1} \\
\rho_1 & 1 & \cdots & \rho_{n-2} \\
\vdots & \vdots & \ddots & \vdots \\
\rho_{n-1} & \rho_{n-2} & \cdots & 1
\end{bmatrix} 
$$


- **Autocorrelation and Heteroskedasticity**

$$
\bOmega = \begin{bmatrix}
\sigma_{11} & \sigma_{12} & \cdots & \sigma_{1n} \\
\sigma_{12} & \sigma_{22} & \cdots & \sigma_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
\sigma_{1n} & \sigma_{2n} & \cdots & \sigma_{nn}
\end{bmatrix} 
$$

Conditions <a href="#ass4">**4)**</a> satisfies the 2nd order moment requirement, combining with <a href="#ass3">**3)**</a>, the 1st order moment condition, we can apply the Central Limit Theorem to $\frac{1}{n}X'u$.


$x_iu_i$ are iid (assumption <a href="#ass2">2)</a>, and we have $E(x_iu_i)=0$ (assumption <a href="#ass3">3)</a> and 

$$
\begin{aligned}
\text{Var}(x_iu_i) 
&= E[(x_iu_i)(x_iu_i)'] \\
&= E(u_i^2x_ix_i') \\
&= M_{X\Omega X}
\end{aligned}
$$ 

finite (assumption <a href="#ass4">4)</a>. 

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

We also have $\left(\frac{X'X}{n}\right)^{-1} \xrightarrow{p} M_{XX}^{-1} $. Then using generalized Slutsky's Thm., and the symmetry of $M_{XX}^{-1}$, we obtain the limit distribution of the product

$$
\color{#008B45} \left(\frac{X'X}{n}\right)^{-1}  \left(\frac{X'u}{\sqrt{n}}\right) \xrightarrow{d} N(0, M_{XX}^{-1} M_{X\Omega X} M_{XX}^{-1}).
$$

And hence 

$$
\sqrt{n} (\hat{\beta}-\beta) \xrightarrow{d} N(0, M_{XX}^{-1} M_{X\Omega X} M_{XX}^{-1}).
$$

<div style='margin-top:-2em; margin-bottom:3em'><span style='float:right; margin-right:10px; '>&#9633;</span></div>


Multiplying $(\hat{\beta}-\beta)$ by $\sqrt{n}$ is a stabilizing transformation — i.e., the moments do not depend on $n$.

- stabilize the variance: $\text{Var}(\sqrt{n}\hat{\beta}) \xrightarrow{p} M_{XX}^{-1} M_{X\Omega X} M_{XX}^{-1}$
- stabilize the mean: $\text{E}[\sqrt{n}(\hat{\beta}-\beta)] = 0$

<div class = "boxed">
<div id="CLT random vector"><strong>CLT for random vectors</strong></div>

Suppose that $z_1, \ldots, z_n$ are iid distributed $K\times 1$ random vectors, with $E(z_i)=\mu$ and $\text{Var}(z_i)=\Sigma$ finite. <br/>

Let $\bar{z}_n = \frac{1}{n}\sum_{i=1}^n z_i$ denote the $K\times 1$ vector of sample means for a sample of size $n$, and let 

$$
w_n = \sqrt{n}(\bar{z}_n-\mu) = \frac{1}{\sqrt{n}}\sum_{i=1}^n(\bar{z}_n-\mu).
$$ 

Then

$$
w_n \xrightarrow{d} N(\vec{0},\Sigma).
$$
</div>


Note that, we do NOT require any of the following in order to ensure asymptotic normality:
1. conditional homoskedasticity $(\text{Var}(u_i\vert x_i) = \sigma^2)$;
2. linear conditional expectation $(\mathbb{E}(y_i\vert x_i) = x_i'\beta$ or the stronger form $\mathbb{E}(y\vert X) = X'\beta)$;
3. normal conditional distribution $(y\vert X \sim N(X\beta, \sigma^2I))$.

<span style='color:#008B45'>Under classical assumptions</span>, i.e., homoskedastic and no serial correlation errors, 


$$
M_{X\Omega X}=\sigma^2\E(x_ix_i')=\sigma^2M_{XX} .
$$

The asymptotic covariance matrix of $\sqrt{n}(\hat{\beta}-\beta)$ is then

$$
\begin{split}
V_{\beta} 
&= M_{XX}^{-1}M_{X\Omega X}M_{XX}^{-1} \\
&= \sigma^2M_{XX}^{-1}M_{XX}M_{XX}^{-1} \\
&= \sigma^2M_{XX}^{-1} .
\end{split}
$$

Hence, the limit distribution is

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
V_\beta = \color{#008B45}\text{avar}\left(\sqrt{n} (\hat{\beta}_{OLS}-\beta) \right)
$$


$\overset{a}{\sim}$ stands for "approximate (asymptotic)" distribution.


Distinguish the <span style='color:#008B45'>**asymptotic variance** $V_\beta$</span> from the <span style='color:#337ab7'>**finite-sample conditional variance** (or **exact variance**) $V_{\hat{\beta}}$</span>:

$$
\begin{split}
V_\beta &= \text{avar}\left(\sqrt{n} (\hat{\beta}-\beta) \right) = \color{#008B45}\sigma^2M^{-1}_{XX} \\
V_{\hat{\beta}} &= \var{(\hat{\beta} \mid X)} = \color{#337ab7} \sigma^2 (X'X)^{-1} .
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
As $n\to \infty,$

$$
n V_{\hat{\beta}} \xrightarrow{p} V_\beta .
$$

- <span style='color:#337ab7'>$V_{\hat{\beta}}$ is useful for practical inferences</span> (such as computation of standard errors and test) since it is the variance of the estimator $\hat{\beta}.$

- <span style='color:#008B45'>$V_\beta$ is useful for asymptotic theory</span> as it is well defined in the limit as $n$ goes to infinity. 


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

are **consistent** estimators of $\sigma^2$ (only <span style='color:#008B45'>$\hat{\sigma}^2_{OLS}$ is **unbiased**</span>).

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


## Nonspherical disturbances

Under nonspherical disturbances, we need a more general form of the estimator for the asymptotic covariance matrix of $\sqrt{n}(\hat{\beta}-\beta).$

$M_{X\Omega X}$ cannot be simplified to $\sigma^2 M_{XX}$ anymore.

$$
\begin{split}
\text{Var}(\hat{\beta}-\beta)
&= (X'X)^{-1}(X'uu'X)(X'X)^{-1} \\ 
&= \frac{1}{n} \left(\frac{1}{n}X'X\right)^{-1} \left(\frac{1}{n}X'uu'X\right) \left(\frac{1}{n}X'X\right)^{-1}
\end{split}
$$

Multiple by $\sqrt{n}$

$$
\begin{split}
\text{Var}\left(\sqrt{n}(\hat{\beta}-\beta)\right)
&=  \left(\frac{1}{n}X'X\right)^{-1} \left(\frac{1}{n}X'uu'X\right) \left(\frac{1}{n}X'X\right)^{-1}
\end{split}
$$

We still let 

$$
\text{plim} \left(\frac{1}{n}X'X\right)^{-1} = M_{XX}^{-1} .
$$

Now we focus on the central part.

$$
\begin{split}
X'uu'X &= \begin{pmatrix}
x_1 & x_2 & \cdots & x_n
\end{pmatrix}
\begin{pmatrix}
    \sigma_{11} & \sigma_{12} & \cdots & \sigma_{1n} \\
    \sigma_{21} & \sigma_{22} & \cdots & \sigma_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    \sigma_{1n} & \sigma_{2n} & \cdots & \sigma_{nn}
\end{pmatrix}
\begin{pmatrix}
    x_1' \\
    x_2' \\
    \vdots \\
    x_n'
\end{pmatrix} \\
&= \begin{pmatrix} 
x_1\sigma_{11} + x_2\sigma_{21} + \cdots + x_n\sigma_{n1} \\
x_1\sigma_{12} + x_2\sigma_{22} + \cdots + x_n\sigma_{n2} \\
\vdots \\
x_1\sigma_{1n} + x_2\sigma_{2n} + \cdots + x_n\sigma_{nn}
\end{pmatrix}'
\begin{pmatrix}
    x_1' \\
    x_2' \\
    \vdots \\
    x_n'
\end{pmatrix} \\
&= x_1\sigma_{11}x_1' + x_2\sigma_{22}x_1' + \cdots + x_n\sigma_{n1}x_1' \\ 
&\phantom{=} \quad + x_1\sigma_{12}x_2' + x_2\sigma_{22}x_2' + \cdots + x_n\sigma_{n2}x_2' \\
&\phantom{=} \quad + \cdots \\
&\phantom{=} \quad + x_1\sigma_{1b}x_n' + x_2\sigma_{2b}x_n' + \cdots + x_n\sigma_{nn}x_n' \\
&= \sum_{i=1}^n \sum_{j=1}^n x_ix_j'\sigma_{ij} 
\end{split}
$$

**Case 1**: Homoskedastic and no serial correlation

$$
\begin{split}
\sigma_{ij} &= 0 & \quad & \text{ for } i\ne j \text{ and } \\
\sigma_{ii} &= \sigma^2 & \quad & \text{ for } i=1, \ldots, n 
\end{split}
$$

Then we have

$$
\begin{split}
\frac{1}{n} X'uu'X &= \frac{1}{n}\sum_{i=1}^n x_ix_i'\sigma^2 = \frac{\sigma^2}{n} \sum_{i=1}^n x_ix_i' \\
&=  \frac{\sigma^2}{n}X'X  \\
&= \frac{1}{n}X'\begin{pmatrix}
\sigma^2 & 0 & \cdots & 0 \\
0 & \sigma^2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \sigma^2
\end{pmatrix}X
\end{split}
$$

**Case 2**: Heteroskedastic and no serial correlation

$$
\begin{split}
\sigma_{ij} &= 0 & \quad & \text{ for } i\ne j \text{ and } \\
\sigma_{ii} &= \sigma^2_i & \quad & \text{ for } i=1, \ldots, n 
\end{split}
$$

Then we have

$$
\begin{split}
\frac{1}{n} X'uu'X &= \frac{1}{n}\sum_{i=1}^n x_ix_i'\sigma^2_i \\
&= \frac{1}{n}X'\begin{pmatrix}
\sigma_1^2 & 0 & \cdots & 0 \\
0 & \sigma_2^2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \sigma_n^2
\end{pmatrix}X
\end{split}
$$

**Case 3**: Heteroskedastic and serial correlation

$$
\begin{split}
\frac{1}{n} X'uu'X &= \frac{1}{n}\sum_{i=1}^n\sum_{j=1}^n x_ix_j'\sigma_{ij} \\
\end{split}
$$



Recall the asymptotic covariance is given by

$$
V_{\beta} = \text{avar}(\sqrt{n}(\hat{\beta}-\beta)) = M_{XX}^{-1}M_{X\Omega X}M_{XX}^{-1}
$$


The estimator for the asymptotic covariance matrix:

$$
\widehat{V}_\beta = \widehat{M}_{XX}^{-1} \widehat{M}_{X\Omega X} \widehat{M}_{XX}^{-1}
$$

The moment estimators under general dependence are given by:

$$
\begin{split}
\widehat{M}_{XX} &= \frac{1}{n}\sum_{i=1}^n x_ix_i' \xrightarrow{p} \E(x_ix_i) = M_{XX} \\
\widehat{M}_{X\Omega X} &= \frac{1}{n}\sum_{i=1}^n\sum_{j=1}^n x_ix_j'\hat{u}_i\hat{u}_j \xrightarrow{p} \E(x_ix_j'\sigma_{ij}) = M_{X\Omega X} \\
\end{split}
$$


In time series setting, you often see the alternative notation:

$$
\begin{split}
M_{X\Omega X} &= \sum_{\ell=-\infty}^{\infty} \E(x_{t-\ell}x_t'\sigma_{t,t-\ell}) \\
&= \sum_{\ell=-\infty}^{\infty} \E(x_{t-\ell}x_t'u_{t}u_{t-\ell}).
\end{split}
$$

Thus

$$
\begin{equation}\label{eq-V-beta-general}
\widehat{V}_\beta = \left(\frac{1}{n}\sum_{i=1}^n x_ix_i' \right)^{-1} \left(\frac{1}{n}\sum_{i=1}^n x_ix_i'  \hat{u}_i\hat{u}_j \right) \left(\frac{1}{n}\sum_{i=1}^n x_ix_i' \right)^{-1}
\end{equation}
$$

- Under **homoskedasticity and no serial correlation**, we have

    $$
    \widehat{M}_{X\Omega X} = \frac{\hat{\sigma}^2}{n}\sum_{i=1}^n x_ix_i' 
    $$

    where

    $$
    \hat{\sigma}^2 = \frac{\sum_{i=1}^n \hat{u}_i^2}{n-K}
    $$

    and

    $$
    \begin{split}
    \widehat{V}_\beta &= \left(\frac{1}{n}\sum_{i=1}^n x_ix_i' \right)^{-1} \left(\frac{\hat{\sigma}^2}{n}\sum_{i=1}^n x_ix_i' \right) \left(\frac{1}{n}\sum_{i=1}^n x_ix_i' \right)^{-1} \\
    &= \hat{\sigma}^2 \left(\frac{1}{n}\sum_{i=1}^n x_ix_i' \right)^{-1} \\
    &= n\,\hat{\sigma}^2 (X'X)^{-1}  \\
    &= n\, \widehat{V}_{\hat{\beta}} 
    \end{split}
    $$

    where $$\widehat{V}_{\hat{\beta}} = \hat{\sigma}^2 (X'X)^{-1}$$ is the estimator of the finite sample conditional variance of $\hat{\beta}_{OLS}$.

- Under **heteroskedasticity and no serial correlation**, we have

    $$
    \widehat{M}_{X\Omega X} = \frac{1}{n}\sum_{i=1}^n x_ix_i' \hat{u}^2_i
    $$

    and

    $$
    \begin{equation}\label{eq-V-beta-heteroskedasticity}
    \begin{split}
    \widehat{V}_\beta &= \left(\frac{1}{n}\sum_{i=1}^n x_ix_i' \right)^{-1} \left(\frac{1}{n}\sum_{i=1}^n x_ix_i'  \hat{u}^2_i\right) \left(\frac{1}{n}\sum_{i=1}^n x_ix_i' \right)^{-1}  \\
    \widehat{V}_\hat{\beta} &= \widehat{V}_\beta/n 
    \end{split}    
    \end{equation}
    $$

    Eq. \eqref{eq-V-beta-heteroskedasticity} is called the **White heteroskedasticity consistent estimator**. It can be used to estimate the asymptotic covariance matrix of OLS estimator under heteroskedasticity.

- Eq \eqref{eq-V-beta-general} is an extension of White's estimator to the more general case of autocorrelation.

There are two problems wth the following estimator:

$$
\begin{equation}\label{eq-MX-omegaX}
\widehat{M}_{X\Omega X} = \frac{1}{n}\sum_{i=1}^n\sum_{i=h}^n x_ix_j'\hat{u}_i\hat{u}_j
\end{equation}
$$

1. $\widehat{M}_{X\Omega X}$ is $\frac{1}{n}$ times a sum of $n^2$ terms, so it is difficult to conclude yet that it will converge to a finite limit as $n\to\infty$. This is most likely to arise in a time-series setting. 

    To obtain convergence, it is necessary to assume that $\sigma_{ij}$ would diminish as $\abs{i-j}$ increases, i.e., the covariance between $u_i$ and $u_j$ is small for large $\abs{i-j}$. This is a common assumption in time series econometrics, known as **stationarity**.

    In practical terms, observation pairs are progressively less correlated as their separation in time grows.


2. The estimator in Eq. \eqref{eq-MX-omegaX} is not guaranteed to be positive definite, which is a requirement for the covariance matrix. This can be resolved by using a more general form of the estimator. Newey and West (1987) proposed an estimator that overcomes this difficulty:

    $$
    \begin{equation}\label{eq-MX-omegaX-NW}
    \widehat{M}_{X\Omega X} = \frac{1}{n}\sum_{i=1}^n x_tx_t' \hat{u}^2_t + \frac{1}{n}\sum_{\ell=1}^L\sum_{t=\ell+1}^n \left(1-\frac{\ell}{L+1}\right) \hat{u}_t\hat{u}_{t-\ell} \left(x_tx_{t-\ell}'+x_{t-\ell}x_t'\right)
    \end{equation}
    $$

    Eq. \eqref{eq-MX-omegaX-NW} is called the **Newey-West autocorrelation consistent covariance estimator** (or **Heteroskedasticity and Autocorrelation Consistent (HAC) estimator**). It is a generalization of White's heteroskedasticity consistent estimator to the case of autocorrelation.

    In practice, $L\sim T^{1/4}.$

    Note that the term $\left(x_t x_{t-\ell}' + x_{t-\ell} x_t'\right)$ is not always equal to $2 x_t x_{t-\ell}'$, unless $x_t x_{t-\ell}'$ is symmetric (which is only true if $x_t = x_{t-\ell}$ or if $x_t$ and $x_{t-\ell}$ are scalars).




___

## Hypothesis testing

Without knowing the distribution of $u\vert X$, we use asymptotic results to approximate the distribution of $\hat{\beta}_{OLS}$ in **large finite sample**.

Let the scalar $\hat{v}_{kk}$ denote the $k^{\text{th}}$ element of the main diagonal of the variance matrix

$$
\widehat{V}_{\beta}/n=\hat{\sigma}^2_{OLS}(X'X)^{-1} .
$$

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

___

**Sketch proof**

Given Taylor's theorem, as long as $f$ is a continuous and derivable up to the $k$th derivative, where $k\ge ,2$ then at the point $\mu:$

$$
f(X_n)\approx f(\mu) + f'(\mu)(X_n-\mu).
$$

Subtracting $g(\mu),$ we have

$$
f(X_n)- f(\mu)\approx  f'(\mu)(X_n-\mu) .
$$

Assume

$$
X_n - \mu \overset{d}{\to} N(0, \frac{\sigma^2}{n}),
$$


we can rewrite the above as

$$
f(X_n)- f(\mu)\approx  f'(\mu)\, N(0, \frac{\sigma^2}{n}).
$$

Hence, we can write the distribution of $f(X_n)$ as

$$
f(X_n) \sim N\left(f(\mu),  \frac{f'(\mu)^2\sigma^2}{n}\right) .
$$


___

**Example 1** Suppose that a sequence of $2\times 1$ random vector $\{\hat{\btheta}_n\}$ satisfies

$$
\sqrt{n}(\hat{\btheta}_n - \btheta_0) \overset{d}{\to} N(\bold{0},\bV)
$$

where the asymptotic mean is

$$
\btheta_0 = \begin{bmatrix}
1 \\
2
\end{bmatrix}
$$

and the asymptotic covariance matrix is 

$$
\bV = \begin{bmatrix}
2 & 1 \\
1 & 1
\end{bmatrix}
$$

We want to derive the asymptotic distribution of the sequence $$\{\hat{\theta}_{n,1}^2 + \hat{\theta}_{n,2}^3\}.$$


Define the function 

$$
f(\btheta) = f(\theta_1, \theta_2) = \theta_1^2 + \theta_2^3 
$$

is continuously differentiable, so we can apply the delta method. The asymptotic mean of the transformed sequence is

$$
f(\btheta_0) = \hat{\theta}_{0,1}^2 + \hat{\theta}_{0,2}^3 = 1^2+2^3 = 8
$$

In order to compute the asymptotic covariance matrix, we need to compute the Jacobian of the function $f(\btheta)$, which is

$$
\begin{aligned}
\bJ(\btheta) &= \nabla f(\boldsymbol{\theta}) \\
&= \begin{bmatrix}
\frac{\partial f(\theta_1, \theta_2)}{\partial \theta_1} & 
\frac{\partial f(\theta_1, \theta_2)}{\partial \theta_2}
\end{bmatrix}  \\
&= \begin{bmatrix}
2\theta_1 & 
3\theta_2^2
\end{bmatrix}
\end{aligned}
$$

Evaluate at $\btheta_0:$

$$
\begin{aligned}
\bJ(\btheta_0) &= \begin{bmatrix}
2\theta_{0,1} & 
3\theta_{0,2}^2
\end{bmatrix} \\
&= \begin{bmatrix}
2\cdot 1 & 
3\cdot 2^2
\end{bmatrix} \\
&= \begin{bmatrix}
2 & 12
\end{bmatrix}
\end{aligned}
$$


Therefore, the asymptotic variance is

$$
\bJ(\btheta_0) \bV \bJ(\btheta_0)' = \begin{bmatrix}
2 & 12
\end{bmatrix}
\begin{bmatrix}
2 & 1 \\
1 & 1
\end{bmatrix}
\begin{bmatrix}
2 \\ 12
\end{bmatrix} = 200
$$

and we can write

$$
\sqrt{n} \left(\hat{\theta}_{n,1}^2 + \hat{\theta}_{n,2}^3 - 9\right) \overset{d}{\to} N(0, 200)
$$






___

**Example 2** Assume the same setup.
Let $f(\boldsymbol{\theta}) = \theta_1 / \theta_2$. We want the asymptotic distribution of $$\{\hat{\theta}_{n,1}/ \hat{\theta}_{n,2}\}.$$

**Step 1:** Gradient of $f$ at $\boldsymbol{\theta}_0$:

$$
\nabla f(\boldsymbol{\theta}) =
\begin{bmatrix}
\frac{\partial}{\partial \theta_1} \left( \frac{\theta_1}{\theta_2} \right) & \frac{\partial}{\partial \theta_2} \left( \frac{\theta_1}{\theta_2} \right)
\end{bmatrix}
= \begin{bmatrix}
\frac{1}{\theta_2} & -\frac{\theta_1}{\theta_2^2}
\end{bmatrix}
$$

Evaluate at $\boldsymbol{\theta}_0$:

$$
\nabla f(\boldsymbol{\theta}_0) = \begin{bmatrix} \frac{1}{2} & -\frac{1}{4} \end{bmatrix}
$$


**Step 2:** Apply the Delta Method:

$$
\sqrt{n} \left( f(\hat{\boldsymbol{\theta}}_n) - f(\boldsymbol{\theta}_0) \right)
\overset{d}{\to} N\left(0, \nabla f(\boldsymbol{\theta}_0) \boldsymbol{V} \nabla f(\boldsymbol{\theta}_0)^\top \right)
$$


Compute the variance:

$$
\begin{aligned}
\sigma^2 &= \begin{bmatrix} \frac{1}{2} & -\frac{1}{4} \end{bmatrix}
\begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}
\begin{bmatrix} \frac{1}{2} \\ -\frac{1}{4} \end{bmatrix} \\
&=  \frac{5}{16}
\end{aligned}
$$


___

{% cite Hausman1978 %} exploits the fact that any asymptotically efficient estimator of a parameter $\theta$, say $\hat{\theta}_e$, must possess the property that it is asymptotically <u>uncorrelated</u>
with the difference $\hat{\theta}_a - \hat{\theta}_e$, where $\hat{\theta}_a$ is any other estimator of $\theta$. 

If not, then there exists a a linear combination of $\hat{\theta}_e$ and $\hat{\theta}_a - \hat{\theta}_e$ that is more efficient than $\hat{\theta}_e$, contradicting the assumed eae e
efficiency of $\hat{\theta}_e$. The result follows directly, then, since:

$$
\begin{aligned}
\text{avar} [\hat{\theta}_a] &= \text{avar} [\hat{\theta}_e + \hat{\theta}_a - \hat{\theta}_e] = \text{avar} [\hat{\theta}_e] + \text{avar} [\hat{\theta}_a - \hat{\theta}_e] \\
& \Longrightarrow \text{avar} [\hat{\theta}_a - \hat{\theta}_e] = \text{avar} [\hat{\theta}_a] - \text{avar} [\hat{\theta}_e]
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