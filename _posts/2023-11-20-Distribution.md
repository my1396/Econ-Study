---
layout: post
title: Distribution
tag: study
date: 2023-11-20
---

<a class="top-link hide" href="#" id="js-top">↑</a>

## Derivative Distributions from $N(0,1)$

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
If the $n\times 1$ vector $y\sim N(0,I)$ and the non-stochastic $n\times n$ matrix $G$ is symmetric and idempotent with $\text{rank}(G)=r\le n$, then the scalar $w=z'Gz \sim \chi^2(r)$.
</li>
</ol>

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