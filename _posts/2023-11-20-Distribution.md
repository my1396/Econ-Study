---
layout: post
title: Distribution
tag: study
date: 2023-11-20
---

<a class="top-link hide" href="#" id="js-top">↑</a>

## Standard Normal Distribution


Normal Distribution $\mathcal{N}(\mu, \sigma^2)$. The 2nd parameter is the *variance*. Normal distribution is also called the *Gaussian distribution*.

$\phi(.)$ usually denotes the pdf of the standard normal (standard Gaussian) distribution.
$\Phi(.)$ usually the cdf of the standard normal.
Figure 1 shows the $\Phi$ and $\phi$ functions.

If $z\sim N(0,1)$, then its pdf is given by:

$$
\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}}.
$$

The cdf is denoted by the $\Phi$ function:

$$
\Phi(x) = P(Z\le x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^x \exp\{-\frac{u^2}{2}\} du.
$$

<figure> 
<img src="https://drive.google.com/thumbnail?id=1nxfdIKXgZvOqXVSeA3h_hf0yxmsM361l&sz=w1000" alt="Phi_b" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />
<figcaption>Fig.1 The $\Phi$ and $\phi$ ($f_Z(.)$) functions (CDF and pdf of standard normal).</figcaption>
</figure>


## Normal Distribution

If $Z$ is standard normal and $X=\mu+\sigma Z$, then $X\sim N(\mu, \sigma^2)$. 

To fin the cdf of $X$, we caan write

$$
\begin{aligned}
F_X(x) &= P(X\le x) \\
&= P( \sigma Z+\mu \leq x) \hspace{20pt} \big(\textrm{where }Z \sim N(0,1)\big) \\
&= P\left(Z \leq \frac{x-\mu}{\sigma}\right) \\
&= \Phi\left(\frac{x-\mu}{\sigma}\right).
\end{aligned}
$$

To find the pdf, we can take the derivative of $F_X$,

$$
\begin{aligned}
f_X(x) &= \frac{d}{dx} F_X(x) \\
& =\frac{d}{dx} \Phi\left(\frac{x-\mu}{\sigma}\right) \\
& = \frac{1}{\sigma} \Phi'\left(\frac{x-\mu}{\sigma}\right) \hspace{20pt} \textrm{(chain rule for derivative)} \\
&= \frac{1}{\sigma} f_Z\left(\frac{x-\mu}{\sigma}\right) \\
&= \frac{1}{\sqrt{2 \pi\sigma^2} } \exp\left \{-\frac{1}{2}\left(\frac{x-\mu}{\sigma^2}\right)^2 \right\}.
\end{aligned}
$$

## Derivative Distributions from $N(0,1)$

[Seeing Theory](https://seeing-theory.brown.edu/probability-distributions/)

The $n\times 1$ random vector $z \sim N(0,I)$, where $I$ is an $n\times n$ identity matrix, is called a standard normal vector, with elements $z_i \sim N(0,1)$ for $i=1,2,\ldots,n$ that are independent standard normal random variables.

<ol>
  <li> The scalar $w=z'z=\sum_{i=1}^n z_i^2 \sim \chi^2(n)$. <br/>

  The sum of squares of $n$ independent standard normal random variables has <span style='color:#32CD32; font-style:italic;'>chi-squared distribution</span> with $n$ degress of freedom. </li>

  <li> If the random variables $w_1 \sim \chi^2(m)$ and $w_2 \sim \chi^2(n)$ and $w_1$ and $w_2$ are independent, then the scalar

  $$
  v=\frac{w_1/m}{w_2/n} \sim F(m,n)
  $$

  The ratio of two independent chi-squared random variables, each divided by their respective degrees of freedom, has a <span style='color:#32CD32; font-style:italic;'>F-distibution</span>.

  <div class = "boxed">
  <strong>Theorem</strong>  If $v \sim F(m,n)$, the limiting distribution of $mv$ as $n\to\infty$ is the $\chi^2(m)$.
  </div>

  Proof: 
  $$
  mv = \frac{w_1}{w_2/n} \sim F(m,n)
  $$

  Since $w_2$ is a $\chi^2$ variable with $n$ degrees of freedom, it can be written as the sum of $n$ iid $\chi^2(1)$, the denominator can be written as

  $$
  w_2/n = \frac{Y_1+Y_2+\cdots+Y_{n}}{n}
  $$

  with $Y_1,Y_2,\ldots,Y_{n}$ mutually independent $\chi^2(1)$.

  By the Strong Law of Large Numers,

  $$
  w_2/n = \frac{Y_1+Y_2+\cdots+Y_{n}}{n} \xrightarrow{a.s} \text{E}(Y_1) \quad \text{as } n\to\infty
  $$

  and $\text{E}(Y_1)=1$, which means

  $$
  mv = \frac{w_1}{w_2/n} \xrightarrow{a.s} w_1 \quad \text{as } n\to\infty
  $$

  <div>
  proving the desired result.   <span style="float:right">$\square$</span>
  </div>


  </li>

  <li> If the random variable $z\sim N(0,1)$ and $w\sim \chi^2(n)$ are independent, then the scalar 

  $$
  u=\frac{z}{\sqrt{w/n}} \sim t(n)
  $$

  The ratio of a standard normal random variable to the square root of an independent chi-squared random variable divided by its degrees of freedom has a <span style='color:#32CD32; font-style:italic;'>Student t-distribution</span> with that degrees of freedom. <br/>

  $$
  u^2 = \frac{z}{w/n}= \frac{z/1}{w/n} \sim F(1,n)
  $$

  The square of a RV with a $t(n)$ distribution has a $F(1,n)$ distribution. <br/><br/>

  $t$-distribution approximates standard normal in the limit. In practice, at a degree of freedom of 30, the $t$-distribution is regarded as closely enough to the standard normal distribution.<br/><br/>

  For example, $t_{0.975}(20)=2.086$, $t_{0.975}(40)=2.031$, $t_{0.975}(100)=1.984$. As $df=n-K$ increases, $c_{0.025}(n-K)$ approaches 1.96 from above (as $t$-distribution has fatter tails).<br/><br/>

  That means, in very large samples, we could use the 97.5% percentile of standard normal distibution to obtain the 95% CI.

  </li>
</ol>


**Two properties** of quadratic forms of normally distributed random vectors:

<ol>
<li>
If the $n\times 1$ vector $y\sim N(\mu,\Sigma)$ and the scalar $w=(y-\mu)'\Sigma^{-1}(y-\mu)$, then $w\sim \chi^2(n)$.
</li>

<li>
If the $n\times 1$ vector $z\sim N(0,I)$ and the non-stochastic $n\times n$ matrix $G$ is symmetric and idempotent with $\text{rank}(G)=r\le n$, then the scalar $w=z'Gz \sim \chi^2(r)$.
</li>
</ol>


**Application of property 2**

Let $u=\sigma Z$, $u\vert X \sim N(0, \sigma^2I)$, $Z\vert X \sim N(0,I)$.

$$
\hat{u} = My = M(X\beta+u) = Mu = M\sigma Z =\sigma Mz
$$


$$
\hat{u}'\hat{u} = \sigma^2 z'M'Mz = \sigma^2 z'Mz 
$$

Given that $\text{rank}(M)=n-k$,

$$
z'Mz  \sim \chi^2(n-K).
$$

Therefore

$$
\frac{\hat{u}'\hat{u}}{\sigma^2} = z'Mz \sim \chi^2(n-K).
$$

**F-test**

The F-test is used to test joint restrictions.

$$
\begin{align*}
H_0: H\beta=\theta^0 \\
H_0: H\beta\neq\theta^0 
\end{align*}
$$

$H$ is $p\times K$. $p$ is the number of restrictions. 

We use the estimator $\hat{\theta}_{OLS} = H \hat{\beta}\_{OLS}$ and construct the scalar test statistic

$$
v=\left(\frac{1}{p}\right) (\hat{\theta}_{OLS}-\theta^0)' \left[\hat{\text{Var}}(\hat{\theta}_{OLS} \vert X)\right]^{-1} (\hat{\theta}_{OLS}-\theta^0)
$$

where $\hat{\text{Var}}(\hat{\theta}\_{OLS} \vert X) = H\, \hat{\text{Var}}(\hat{\beta}\_{OLS} \vert X)\,H'$.

If $H_0$ is true, we have

$$
v\sim F(p, n-K).
$$


## Goodness of fit

$$
\begin{align*}
R^2 &= \frac{\sum_{i=1}^n (\hat{y}_i - \bar{y})^2}{\sum_{i=1}^n (y_i - \bar{y})^2} = 1- \frac{\sum_{i=1}^n \hat{u}_i^2}{\sum_{i=1}^n (y_i - \bar{y})^2} \\

&= \frac{ESS}{TSS} = 1-\frac{RSS}{TSS}
\end{align*}
$$

provided $\bar{\hat{u}}=0$, i.e., the model has an intercept term.

When a model only contains the intercept, $R^2=0$.

**Using $R^2$ to test exclusion restrictions**

Denote $R_U^2$ to be the $R^2$ from the unrestricted model, $R_R^2$ to be from the restricted model.

$$
v = \left(\frac{n-K}{p}\right) \left(\frac{R_U^2-R_R^2}{1-R_U^2}\right) \sim F(p, n-K)
$$

The null hypothesis is rejected if the exclusion of these $p$ explanatory variables results in a su¢ ciently large fall in the $R^2$ goodness of fit measure, or in a sufficiently large deterioration in the fit of the model.


This can be used to test the restriction that all $K-1$ of the slope coefficients in a linear model are equal to zero, i.e. to test the exclusion of all the explanatory variables except the intercept.

The restricted model $y_i=\beta_1+u_i$ has $R_R^2=0$.

The test statisti simplifies to 

$$
v = \left(\frac{n-K}{K-1}\right) \left(\frac{R^2}{1-R^2}\right) \sim F(K-1, n-K).
$$

This is sometimes referred to as the "F-test" for the model.

___


## Families of Densities

Standard Normal: $Z \sim N(0,1)$

$$
\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}
$$

Normal distribution $X \sim N(\mu,\sigma^2)$

$$
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}
$$

### Multivariate normal random vecctors (MV-N)

MV-N is a linear transformation of a random vector whos entries are mutually **independent** univariate normal random variables.

Let $X$ be a $K\times 1$ continuous random vector with multivariate normal distribution with mean $\mu$ and covariance $\Sigma$, denoted $X\sim N(\mu, \Sigma)$. 

$$
X = \begin{bmatrix}
X_1 \\
\vdots \\
X_K
\end{bmatrix}
$$

$$
\mu = \begin{bmatrix}
\mu_1 \\
\vdots \\
\mu_K
\end{bmatrix}
$$


$$
\Sigma = \begin{bmatrix}
\sigma_1^2 & 0 & \cdots & 0 \\
0 & \sigma_2^2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots &\\
0 & 0 & \cdots & \sigma_K^2 \\
\end{bmatrix}
$$

In other words, covariance matrix $\Sigma$ is diagonal. In the case of standard MV-N, each $X_k$ is standard normal, the covariance matrix will be an identity matrix of order $K$.

Its joint probability density function is 

$$
f_X(x) = (2\pi)^{-\frac{K}{2}} \vert \text{det}(\Sigma) \vert ^{-\frac{1}{2}} \exp \left ( -\frac{1}{2} (X-\mu)'\Sigma^{-1}(X-\mu) \right )
$$

The $K$ random variables $X_1, \ldots, X_K$ constituting the vector $X$ are said to be **jointly normal**.