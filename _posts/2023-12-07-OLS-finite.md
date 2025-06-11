---
layout: post
title: OLS Finite Sample
tag: study
update: 2023-12-07
---

$$
\newcommand{\indep}{\perp \!\!\! \perp}
$$

<head>
    <style>
      .boxed {
        background: #FFFAEE;
        color: black;
        border: 1px solid #535353;
        margin: 0px auto;
        width: 526px;
        padding: 10px;
        border-radius: 10px;
      }
    </style>
</head>

<a class="top-link hide" href="#" id="js-top">↑</a>

## Conditional Expectation Function

The conditional mean of logwages given sex, race, and education is a single number for each category.

For example

$$
\mathbb{E}\left[\log (\text{wage})\right | \text{sex=man, race=white, education=12}]
$$

We formulate a generic function to measure the variation in $\log(wage)$, denoted by the letter $y$, given multiple conditioning variables, such as sex, race, and education, deonoted by the letters $x_1,x_2, \ldots,x_k.$

$$
\mathbb{E}[y|x_1,x_2, \ldots,x_k]=m(x_1,x_2, \ldots,x_k) .
$$

We call this the <span style='color:#008B45FF'>**conditional expectation function** (CEF)</span>. The CEF is a function of $(x_1,x_2, \ldots,x_k)$ as it varies with the variables. 

we will typically write the conditioning variables as a vector in $\mathbb{R}^k$:

$$
\boldsymbol{x} = \begin{pmatrix}
x_1 \\
x_2 \\
\vdots \\
x_k
\end{pmatrix} .
$$

Here we follow the convention of using lower case bold italics $\boldsymbol{x}$ to denote a vector. Given this notation, the CEF can be compactly written as

$$
\mathbb{E}(y|\boldsymbol{x}) = m(\boldsymbol{x}) .
$$

The CEF $\mathbb{E}(y\vert\boldsymbol{x})$ is a function of $\boldsymbol{x}$. 

Another commonly seen expression is $\mathbb{E}(y\vert\boldsymbol{x}=\boldsymbol{u})$, which is the conditional expectation of $y$, given that the random variable $\boldsymbol{x}$ equals the specific value $\boldsymbol{u}$. However, sometimes you only see $\mathbb{E}(y\vert\boldsymbol{x})$ to refer to this function.

Express the CEF using the conditional density function 

$$
m(\boldsymbol{x}) = \mathbb{E}(y|\boldsymbol{x}) = \int_{-\infty}^\infty y f_{y|\boldsymbol{x}}(y|\boldsymbol{x}) dy.
$$

Or, in the discrete $\boldsymbol{x}$ case, 

$$
m(\boldsymbol{x}) = \mathbb{E}(y|\boldsymbol{x}) = \sum_{\boldsymbol{y}} y\, f_{y|\boldsymbol{x}}(y|\boldsymbol{x}) .
$$

Intuitively, $m(\boldsymbol{x})$ is the mean of $y$ for the idealized subpopulation where the conditioning variables are fixed at $\boldsymbol{x}$. 

The notation $m(\boldsymbol{x})=\mathbb{E}(y\vert\boldsymbol{x})$ is informative as it shows that the <span style='color:#337ab7'>CEF is a function of $\boldsymbol{x}$</span>.

Differences between $\mathbb{E}(y)$ and $\mathbb{E}(y\vert\boldsymbol{x})$

- The unconditional expectation of $y$, $\mathbb{E}(y)$ is just a number. e.g., $\mathbb{E}(y)=2$ or $\mathbb{E}(y)=2$.
- The conditinoal expectaiont, $\mathbb{E}(y\vert\boldsymbol{x})$, is a number depending on $\boldsymbol{x}$.
  - If $\boldsymbol{x}$ has an influence on the value of $y$, then $\boldsymbol{x}$ will have an influence on the average value of $y$.
  - For instance, we would expect $\mathbb{E}(y\vert\boldsymbol{x}=\boldsymbol{u})$ to be different from $\mathbb{E}(y\vert\boldsymbol{x}=\boldsymbol{v})$.
  - We can therefore view $\mathbb{E}(y\vert\boldsymbol{x})$ as a function of $\boldsymbol{x}$, say $\boldsymbol{x}=m(\boldsymbol{x})$.

To evaluate this function, $m(\boldsymbol{x}) = \mathbb{E}(y\vert\boldsymbol{x}) $, we

<ol type="pi">
  <li> fix $\boldsymbol{x}$ at the chosen value, say $\boldsymbol{u}$; </li>
  <li> find the expectaion of $y$ when $\boldsymbol{x}$ is fixed at this value. </li>
</ol>

Note that 

1. This is idealized since $\boldsymbol{x}$ is continuously distributed so this subpopulation is infinitely small. \
   In practice, we may not be able to observe values at certain levels of $\boldsymbol{x}$, leading to a somewhat *rough* sketch of $\mathbb{E}(y\vert\boldsymbol{x})$.
2. The randomness comes from the randomness in $\boldsymbol{x}$, *not* in $y$.


We usually write the CEF as

$$
m(\boldsymbol{x}) = \boldsymbol{x}'\boldsymbol{\beta}
$$

where

$$
\boldsymbol{\beta} = \begin{pmatrix}
\beta_1 \\
\beta_2 \\
\vdots \\
\beta_k
\end{pmatrix} \text{ and }
\boldsymbol{x} = \begin{pmatrix}
x_1 \\
x_2 \\
\vdots \\
x_k
\end{pmatrix}.
$$

$\boldsymbol{\beta}$ is the coefficient vector and $\boldsymbol{x}$ is the regressor vector.


**Regression Derivative**

In the linear CEF model, the regression derivative is simply the coefficient vector. That is

$$
\nabla m(\boldsymbol{x}) = \boldsymbol{\beta}
$$

This is one of the appealing features of the linear CEF model. The coefficients have simple and natural interpretations as the marginal effects of changing one variable, holding the others constant.


<div class = "boxed">
<p style="text-align:center; font-weight:bold;">Linear CEF Model</p>

$$
\begin{aligned}
y &=  \boldsymbol{x}'\boldsymbol{\beta} + u \\
\mathbb{E}(u|\boldsymbol{x}) &= 0
\end{aligned}
$$
</div>


If in addition the error is homoskedastic, we call this the homoskedastic linear CEF model.

<div class = "boxed">
<p style="text-align:center; font-weight:bold;">Homoskedastic Linear CEF Model</p>

$$
\begin{aligned}
y &=  \boldsymbol{x}'\boldsymbol{\beta} + u \\
\mathbb{E}(u|\boldsymbol{x}) &= 0 \\
\mathbb{E}(u^2|\boldsymbol{x}) &= \sigma^2 
\end{aligned}
$$
</div>

___

## Classical linear regression models

CLRM (Classical linear regression models) correspond to exact finite sample properties. 

<span style="font-weight:600; font-size:21px">Gauss-Markov Assumptions</span>

1. $y=X\beta+u$. There is a linear relationship between $y$ and $X$. $u$ is called *disturbances* or *errors*.

2. $\text{E}[u\vert X] = 0$ or equivalently $\text{E}[y\vert X]=X\beta$. This is called *linear conditional expectation* or zero *conditional mean* assumption. The linear conditional expectation assumption is sometimes referred to as "strict exogeneity."

3. $\text{Var}[u\vert X] = \sigma^2I$. This is a *conditional homoskedasticity assumption*.

4. $X$ has full rank $\text{rank}(X)=K$.

5. $X$ may be fixed or random, but must be generated by a mechanism that is unrelated to $u$.

Assumption 2 can be re-written as

$$
E(u_i\vert x_1, x_2, \ldots, x_n)=0 \quad \text{for } i=1,\ldots, n
$$

This implies that the error term $u_i$ is not only uncorrelated with $x_i$, but also uncorrelated with the explanatory variables for all other observations $j$, $j=1,\ldots,n$. Therefore, called "strict exogeneity".

Strict exogeneity implies

1. Orthogonality  
  
    That is, $\E[\bx u_i] = \bold{0}$ or $\mathrm{Cov}[u_i, \bx]=0$

    $$
    \begin{split}
    \E[\bx u_i] &=  \E \left[\E[\bx u_i \vert \bx] \right] \quad \text{(by LIE)} \\
    &=  \E \left[\bx \,\E[ u_i \vert \bx] \right] \\
    &=  \E \left[\bx \, 0 \right] \\
    &= 0
    \end{split}
    $$

2. $\E[u_i]=0$ the unconditional mean is also zero.

    $$
    \E[u_i] = \E \left[\E[ u_i \vert \bx]\right] = 0
    $$

Given that assumption 3 assumes diagonal covariance matrix, meaning observations on $(y_i, x_i')$ are *independent* over $i=1,\ldots, n
$, so that

$$
\begin{align*}
\text{E}(u_i\vert x_1,\ldots, x_n) &= \text{E}(u_i \vert x_i) = 0 \\
\text{or } \text{E}(y_i\vert x_1,\ldots, x_n) &= \text{E}(y_i \vert x_i) = x_i'\beta
\end{align*}
$$

Independence also implies that 

$$
\begin{align*}
\text{Cov}(u_i, u_j\vert x_1,\ldots, x_n) &= 0 \quad \text{for all } i\neq j \\
\text{or } \text{Cov}(y_i, y_j\vert x_1,\ldots, x_n) &= 0
\end{align*}
$$


Classical linear regression models with **normally distributed errors**

In addition to the above assumptions, we now assume $u\vert X \sim N(0, \sigma^2I)$.

With the normally distributed errors, we can derive the distribution of $\hat{\beta}_{OLS}\sim N(\beta, \sigma^2(X'X)^{-1})$.

Without the assumption that $u\vert X$ (or equivalently $y\vert X$) has a normal distribution, we can still characterize the distribution of $\hat{\beta}_{OLS}$ in large samples by using the asymptotic distribution results.

Under Assumptions 1–5, the OLS estimator is the <span style='color:#337ab7'>**best linear unbiased estimator**</span> (BLUE). "Best" in terms of *having the smallest variance*.


___

## Linear projection model

If we replace the strict exogeneity assumption $\text{E}(u\vert X)$ by the weaker orthogonality assumption that $\text{E}[X'u]=\vec{0}$ (a $K\times 1$ column zero vector), we have a **linear projection model**.

$\text{E}[X'u]=\vec{0}$ can be written as $\text{E}[x_iu_i]=\vec{0}$, which implies $\text{E}[x_{ki}u_i]=0$ for each $k=1,\ldots, K$. \
With an intercept, e.g., $x_{1i}=1$ for all $i$, $\text{E}[x_1iu_i]$ implies $\text{E}[u_i]=0$.

$\text{E}[x_{ki}u_i]=0$ for $k=1,\ldots, K$ then implies $\text{Cov}(x_{ki}, u_i)=0$. \
$\Rightarrow$ Zero covariance implies zero correlation. \
$\Rightarrow$ So $\text{E}[x_iu_i]=\vec{0}$ implies that each of the included explanatory variables is *uncorrelated with*, or *orthogonal to*, the error term $u_i$ in the linear projection model.

Difference between strict exogeneity $(\text{E}(u\vert X)=\vec{0})$ and orthogonality assumptions $(\text{E}[X'u]=\vec{0})$:

- The linear conditional expectation assumption $\text{E}(u\vert X)=\vec{0}$ implies that the error term $u$ is uncorrelated with any function of each of the included explanatory variables. \
  For example, $u_i$ is uncorrelated with $x_{3i}^2$ or $\exp(x_{4i})$
- Theses properties are NOT implied by the orthogonality assumption $\text{E}[X'u]=\vec{0}$. \
  Unless $x_{3i}^2$ and $\exp(x_{4i})$ happen to be included as additional explanatory variables in the model.
- Strict exogeneity $(\text{E}(u\vert X)=\vec{0})$ implies orthogonality assumptions $(\text{E}[X'u]=\vec{0})$.


___


## OLS estimator

OLS estimator minimizes the *sum of the squared residuals* (**RSS**).

Residuals are given

$$
\hat{u} = y-X\hat{\beta}.
$$

Let $\hat{\beta}$ denote an estimator of $\beta$.

It is important to differentiate $u$ from $\hat{u}$. 
- $u$ refers to **errors** that cannot be observed. 
- $\hat{u}$ refers to **residuals** that can be observed. 

We can write the sum of squared residuals as:

$$
\begin{align*}
S(\hat{\beta}) = \sum_{i=1}^n\hat{u}_i^2
\end{align*}
$$

In matrix form, $S(\hat{\beta})$ can be re-written as

$$
\begin{align*}
S(\hat{\beta}) = \hat{u}'\hat{u} &= (y-X'\hat{\beta})'(y-X'\hat{\beta}) \\
&=y'y - 2\hat{\beta}'X'y + \hat{\beta}'X'X\hat{\beta}
\end{align*}
$$


Apply FOC to $S(\hat{\beta})$, then we get an OLS estimator.

$$
\hat{\beta}_{OLS} = \underset{\hat{\beta}}{\text{argmin}}\, S(\hat{\beta})
$$

Take 1st derivative and set it to zero 

$$
\frac{\partial \hat{u}'\hat{u}}{\partial \hat{\beta}} = -2X'y+2X'X\hat{\beta} = \vec{0},
$$

which gives us the so-called the "normal equations":

$$
X'y = X'X\hat{\beta}.
$$

A variation of the normal equations is 

$$
X'(y-X'\hat{\beta}) = X'\hat{u} = \vec{0},
$$

$\vec{0}$ here is a $K\times 1$ zero vector.


Hence the OLS estimator is given as

$$
\hat{\beta} = (X'X)^{-1}X'y.
$$

Note: The primary property of OLS estimators is that they satisfy the criteria of minimizing the sum of squared residuals. However, there are other properties. These properties do NOT depend on any assumptions - they will always be true so long as we compute them in the manner just shown.


**Properties of the OLS Estimator**:

<ol>
<li> The observed values of $X$ are uncorrelated with the residuals. 
$$
\begin{aligned}
\hat{u} &= y-X\hat{\beta} \\
X'\hat{u} &= \vec{0}
\end{aligned}
$$ 
</li>
<li> The sum of the residuals is zero. <br/>
If there is a constant, then the first column in $X$ (i.e. $X_1$) will be a column of ones. This means that for the first element in the $X′e$ vector to be zero, it must be the case that $\sum_{i}\hat{u}_i=0$. </li>
<li> The sample mean of the residuals is zero. </li>
<li> The regression hyperplane passes through the means of the observed values ($\overline{X}$ and $\overline{y}$). </li>
<li> The predicted values of y are uncorrelated with the residuals. <br/>
The predicted values of y are equal to $X\hat{\beta}$, i.e. $\hat{y}=X\hat{\beta}$. From this we have
$$
\hat{y}'\hat{u} = (X\hat{\beta})'\hat{u} = \hat{\beta}X'\hat{u} = 0
$$
This last development takes account of the fact that $X'\hat{u}= 0$. </li>

<li> The mean of the predicted $Y$’s for the sample will equal the mean of the observed $Y$’s i.e. $\overline{\hat{y}} = \overline{y}$. </li>
</ol>

These properties *always hold true*. You should be careful not to infer anything from the residuals about the disturbances/ errors. For example, you cannot infer that the sum of the disturbances is zero or that the mean of the disturbances is zero just because this is true of the residuals - this is true of the residuals just because we decided to minimize the sum of squared residuals.


**Projection Matrix**

Define the matrix 

$$
P = X(X'X)^{-1}X',
$$

then 

$$
PX = X(X'X)^{-1}X'X = X,
$$

and 

$$
Py = X(X'X)^{-1}X'y = X\hat{\beta} = \hat{y}.
$$

Note that $Py$ gives the fitted value in a OLS regression.

A special case is when $X=\mathbf{1}_n$ is an $n$-vector of ones. Then

$$
\begin{aligned}
P &= \mathbf{1}_n (\mathbf{1}_n'\mathbf{1}_n)^{-1}\mathbf{1}_n' \\
&= \frac{1}{n} \mathbf{1}_n\mathbf{1}_n' \qquad\qquad (\mathbf{1}_n'\mathbf{1}_n = n)
\end{aligned}
$$

Note that in this case

$$
\begin{aligned}
Py &= \mathbf{1}_n (\mathbf{1}_n'\mathbf{1}_n)^{-1}\mathbf{1}_n'y \\
&= \mathbf{1}_n \bar{y}
\end{aligned}
$$

creates an $n$-vector whose elements are the sample mean $\bar{y}$ of $y_i.$


$\mathbf{P} = \mathbf{X} (\mathbf{X}' \mathbf{X})^{-1} \mathbf{X}'$  for any $ n \times K $ matrix $ \mathbf{X} $ with $ n \geq K $ has the following algebraic properties:

1. $ \mathbf{P} $ is **symmetric** ($ \mathbf{P}' = \mathbf{P} $).
2. $ \mathbf{P} $ is **idempotent** ($ \mathbf{P} \mathbf{P} = \mathbf{P} $).
3. $ \mathrm{tr}(\mathbf{P}) = K $.
4. The **eigenvalues** of $ \mathbf{P} $ are 1 and 0. There are $ k $ eigenvalues equal to 1, and $ n - k $ equal to 0.
5. $ \mathrm{rank}(\mathbf{P}) = K $.


**Residual Maker**

Define 

$$
\begin{aligned}
M &= I_n - P \\
&= I_n -  X(X'X)^{-1}X'
\end{aligned}
$$

where $I_n$ is the $n\times n$ identity matrix.

We have

- $MX = 0$
- $M$ creates the OLS residuals: $My = y-Py = y-X\hat{\beta} = \hat{u}$
- $M$ is symmetric ($M'=M$) and idempotent ($MM=M$)
- $\mathrm{tr}(M) = n-K$



___



## Hypothesis testing

In finite sample, we know that error follows normal distribution $u\vert X \sim N(0, \sigma^2I)$.

1. When we know error variance $\sigma^2$, we use standard normal test.
2. When we do not know error variance, then we estimate using 

    $$
    \hat{\sigma}^2_{OLS} =\frac{\hat{u}'\hat{u}}{n-K}.
    $$

    Then use $t$-distribution.

    Note that $K$ here is the number of independent variables *including* the intercept. $df$ is essentially the number of observations minus the number of estimated parameters.

    $\hat{\sigma}$ is called the **standard error of the regression** (SER), or standard error of the estimate. The SER is an estimator of the standard deviation of the error term.

    Under the Gauss-Markov assumptions 1–5, $\hat{\sigma}^2_{OLS}$ is an **unbiased** estimator of $\sigma^2,$ that is, 
    
    $$\E(\hat{\sigma}^2_{OLS})=\sigma^2.$$



**Joint hypothesis** with one or more restrictions

$$
\begin{align*}
H_0&: \hat{\theta} = H\hat{\beta} \\
H_1&: \hat{\theta} \neq H\hat{\beta} 
\end{align*}
$$

With normally distributed errors, we have 

$$\hat{\theta}\vert X \overset{\text{a}}{\sim} \text{N}\left(\theta,\sigma^2 H(X'X)^{-1}H'\right). $$

We estimate $\text{Var}(\hat{\theta}\vert X)$ using 

$$\widehat{\text{Var}}(\hat{\theta}\vert X) = H \widehat{\text{Var}}(\hat{\beta}\vert X)H' = H\left[\hat{\sigma}^2(X'X)^{-1}\right]H'=\hat{\sigma}^2D^{-1},$$ 

where $D^{-1}=H(X'X)^{-1}H'$.

We have the test statistic

$$
\begin{align*}
v &= \left(\frac{1}{p}\right) (\hat{\theta}-\theta)' \left[\widehat{\text{Var}}(\hat{\theta}\vert X)\right]^{-1} (\hat{\theta}-\theta) \\
&= \left(\frac{1}{p\hat{\sigma}^2}\right) (\hat{\theta}-\theta)'D(\hat{\theta}-\theta) \\
&\sim \; F(p, n-K).
\end{align*}
$$



___

## Practical versus Statistical Significance

- The sign and magnitude of $\bar{y}$ determine its **practical significance** and allow us to discuss the direction of an intervention or policy effect, and whether the estimated effect is  "large" or "small." 

- On the other hand, statistical significance of $\bar{y}$ depends on the magnitude of its $t$ statistic. 

  For testing $H_0: \mu = 0$, the $t$ statistic is simply $t = \bar{y}/\text{se}(\bar{y})$. In other words, statistical significance depends on the ratio of $\bar{y}$ to its standard error. Consequently, a $t$ statistic can be large because $\bar{y}$ is large or $\text{se}(\bar{y})$ is small. 

In applications, it is important to discuss <u>both practical and statistical significance</u>, being aware that an estimate can be statistically significant without being especially large in a practical sense. Whether an estimate is practically important depends on the context as well as on one’s judgment, so there are no set rules for determining practical significance.

























