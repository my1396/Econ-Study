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


## Variance of Least Squares Estimator

Define

$$
\bV_{\hat\bbeta} \overset{def}{=} \var(\hat\bbeta \mid \bX)
$$

as the **conditional covariance matrix of the regression coefficient estimates**.


Assuming homoskedastic errors, we have the conditional covariance matrix of the $n\times 1$ regression error $\bu$ is the $n\times n$ matrix

$$
\var(\by\mid \bX) = {\color{#008B45}\E(\bu\bu'\mid \bX) \overset{def}{=} \bD} = \mathbf I_n \sigma^2.
$$


For any $n \times r$ matrix $\bA = \bA(\bX)$,

$$
\mathrm{Var}(\bA'\by \mid \bX) = \mathrm{Var}(\bA'\bu \mid \bX) = \bA'\bD\bA.
$$

In particular, we can write $\hat{\bbeta} = \bA'\by$ where $\bA = \bX(\bX'\bX)^{-1}$, and thus

$$
\bV_{\hat{\bbeta}} = \mathrm{Var}(\hat{\bbeta} \mid \bX) = \bA'\bD \bA = (\bX'\bX)^{-1} \bX'\bD\bX (\bX'\bX)^{-1}.
$$

It is useful to note that

$$
\bX'\bD\bX = \sum_{i=1}^{n} \bx_i \bx_i' \sigma_i^2
$$

is a weighted version of $\bX'\bX$.

In the special case of the linear homoskedastic regression model, $\bD = I_n \sigma^2$, so $\bX'\bD\bX = \bX'\bX \sigma^2$, and the variance matrix simplifies to

$$
\bV_{\hat{\bbeta}} = (\bX'\bX)^{-1} \sigma^2.
$$


<div class = "boxed">
<strong>Theorem Variance of Least-Squares Estimator</strong><br/>

In the linear regression model and i.i.d. sampling:  

$$
\color{#008B45} V_{\hat{\bbeta}} = \mathrm{var}(\hat{\bbeta} \mid \bX) = (\bX'\bX)^{-1} (\bX'\bD\bX)(\bX'\bX)^{-1} 
$$

where $\bD=\E(\bu\bu'\mid \bX).$
In the homoskedastic linear regression model and i.i.d. sampling:  

$$
\bV_{\hat{\bbeta}} = \sigma^2 (\bX'\bX)^{-1}.
$$

</div>

___

## Properties of the OLS Estimator

<ol>
<li> The observed values of $X$ are uncorrelated with the residuals. 
$$
\begin{aligned}
\hat{\bu} &= \by-\bX\hat{\bbeta} \\
\bX'\hat{\bu} &= \bold{0}
\end{aligned}
$$ 
</li>
<li> The sum of the residuals is zero. <br/>
If there is a constant, then the first column in $X$ (i.e. $X_1$) will be a column of ones. This means that for the first element in the $X'\bu$ vector to be zero, it must be the case that $\sum_{i}\hat{u}_i=0$. </li>
<li> The sample mean of the residuals is zero. 
$$
\overline{\hat{u}} = 0
$$
</li>
<li> The regression hyperplane passes through the means of the observed values ($\overline{X}$ and $\overline{y}$). 
Given
$$
\hat{\bu} = \by - \bX \hat{\bbeta}
$$
Sum all observations and divide by $n:$
$$
\overline{\hat{u}} = \overline{y} - \overline{\bX}\hat{\bbeta} .
$$
Given $\overline{\hat{u}}$, we have $\overline{y} = \overline{\bX}\hat{\bbeta}.$  That is, the regression hyperplane passes through the means of the observed values, $(\overline{\bX}, \overline{y})$.
</li>
<li> The predicted values of y are uncorrelated with the residuals. <br/>
The predicted values of y are equal to $X\hat{\beta}$, i.e. $\hat{y}=X\hat{\beta}$. From this we have
$$
\hat{y}'\hat{u} = (X\hat{\beta})'\hat{u} = \hat{\beta}X'\hat{u} = 0
$$
This last development takes account of the fact that $X'\hat{u}= 0$. </li>

<li> The mean of the predicted $Y$’s for the sample will equal the mean of the observed $Y$’s i.e. $\overline{\hat{y}} = \overline{y}$. 
$$
\begin{aligned}
\overline{y} &= \frac{1}{n} \sum_{i=1}^n y_i \\
&= \frac{1}{n} \sum_{i=1}^n (\hat{y}_i+\hat{u}_i) \qquad (y_i=\hat{y}_i+\hat{u}_i) \\
&= \frac{1}{n} \sum_{i=1}^n \hat{y}_i + \frac{1}{n} \sum_{i=1}^n \hat{u}_i \qquad (\overline{\hat{u}}=0) \\
&= \overline{\hat{y}}
\end{aligned}
$$
</li>
</ol>

These properties *always hold true*. You should be careful not to infer anything from the residuals about the disturbances/ errors. For example, you cannot infer that the sum of the disturbances is zero or that the mean of the disturbances is zero just because this is true of the residuals - this is true of the residuals just because we decided to minimize the sum of squared residuals.


___


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



___


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


## Goodness-of-fit

We can define the **total sum of squares** (SST), the **explained
sum of squares** (SSE), and the **residual sum of squares** or sum of squared residuals (SSR) as

$$
\begin{aligned}
SST &\equiv \sum_{i=1}^n (y_i-\overline{y})^2  \\
SSE &\equiv \sum_{i=1}^n (\hat{y}_i-\overline{y})^2  \\
SSR &\equiv \sum_{i=1}^n (\hat{u}_i)^2 .
\end{aligned}
$$

We can see that 

$$
SST = SSE + SSR .
$$

In other words, the total variation in $\{y_i\}$ is the sum of the total variations in $\{\hat{y}_i\}$ and in $\{\hat{u}_i\}.$


A commonly reported measure of regression fit is the regression **R-squared** is defined to be

$$
R^2 = \frac{SSE}{SST} = 1-\frac{SSR}{SST} ,
$$

and it is interpreted as the proportion of the sample variation in $\{y_i\}$ that is explained by the OLS regression line. By definition, $R^2$ is a number between zero and one.

$R^2$ is called the **coefficient of determination**.

$R^2$ can be viewed as an estimator of the population parameter

$$
\rho^2 = \frac{\var(\bx_i'\bbeta)}{\var{y_i}} = 1-\frac{\sigma^2_u}{\sigma^2_y} ,
$$

where $\sigma^2_u$ denotes the population variance of the error term, $u,$ and $\sigma^2_y$ as the population variance of $y.$ $\rho^2$ measures the proportion of the variation in $y$ in the population explained by the independent variables.

$R^2$ estimate $\sigma^2_u$ by $SSR/n$ and $\sigma^2_y$ by $SST/n,$ which we known to be biased. 

$R^2$ can also be shown to equal the squared correlation coefficient between the actual $y_i$ and the fitted values $\hat{y}_i$. That is,

$$
R^2 = \frac{ \left(
\sum_{i=1}^{n} (y_i - \bar{y})(\hat{y}_i - \bar{\hat{y}}) \right)^2
}{
\left(\sum_{i=1}^{n} (y_i - \bar{y})^2\right) \left( \sum_{i=1}^{n} (\hat{y}_i - \bar{\hat{y}})^2 \right)
}
$$

$R^2$ never decreases when any variable is added to a regression: this is because SSR never goes up as more independent variables are added.
This fact makes it a poor tool for deciding whether one variable or several variables should be added to a model. The factor that should determine whether an explanatory variable belongs in a model is whether the explanatory variable has a nonzero partial effect on $y$ in the population.

$R^2$ allows us to test a group of variables to see if it is important for explaining $y.$

We introduced an **adjusted R-squared** or **R-bar-squared**, $\overline{R}^2$, which imposes a penalty for adding additional independent variables to a model.

$\overline{R}^2$ uses the unbiased estimators for $\sigma^2_u$ and $\sigma^2_y:$

$$
\overline{R}^2 = 1 - \frac{\frac{SSR}{n-K}}{\frac{SST}{n-1}}.
$$

It relates to the $R^2$ as

$$
\overline{R}^2 = 1 - \frac{n-1}{n-K}(1-R^2) .
$$


___


## Hypothesis testing

In finite sample, we know that error follows normal distribution $u\mid X \sim N(0, \sigma^2I)$.

1. When we know error variance $\sigma^2$, we use standard normal test.
2. When we do not know error variance, then we estimate using 

    $$
    \hat{\sigma}^2_{OLS} =\frac{\hat{u}'\hat{u}}{n-K} = \frac{\sum_{i=1}^n (\hat{u}_i)^2}{n-K}.
    $$

    Then use $t$-distribution.

    Note that $K$ here is the number of independent variables *including* the intercept. $df$ is essentially the number of observations minus the number of estimated parameters.

    $\hat{\sigma}$ is called the <span style='color:#008B45'>**standard error of the regression**</span> (SER), or standard error of the estimate. The SER is an estimator of the standard deviation of the error term.

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




___

## Mean-Square Forecast Error


One use of an estimated regression is to predict out-of-sample values. Consider an out-of-sample $(y_{n+1}, \bx_{n+1})$ where $\bx_{n+1}$ is observed but not $y_{n+1}.$ The point estimate of $y_{n+1}$ is the expected value of $y_{n+1}$ given $x_{n+1}$, i.e., $\E(y_{n+1}\mid \bx_{n+1}) = \bx_{n+1}'\bbeta,$ which we estimate from the OLS regression line:

$$
\tilde{y}_{n+1} = \bx_{n+1}'\hat\bbeta
$$

The **forecast error** is 

$$
\begin{align}
\tilde{u}_{n+1} &= y_{n+1} - \tilde{y}_{n+1} \nonumber \\
&= \bx_{n+1}'\bbeta + u_{n+1} - \tilde{y}_{n+1} \label{eq-forecast_error1} \\ 
&= \bx_{n+1}'\bbeta + u_{n+1} - \bx_{n+1}'\hat\bbeta  , \label{eq-forecast_error2} 
\end{align}
$$

which is the difference between the actual value $y_{n+1}$ and the point forecast $\tilde{y}_{n+1}.$

Because the unobserved error $u_{n+1}$ has zero mean and $\hat\bbeta$ is unbiased,

$$
\E(\tilde{u}_{n+1}\mid \bx_{n+1}) = 0 .
$$

We have shown that the expected prediction error is zero.


The **mean-squared forecast error** (MSFE) is its expected squared value:

$$
\text{MSFE}_n = \E(\tilde{u}_{n+1}^2)
$$

MSFE is essentially the variance of the prediction error.
Because $u_{n+1}$ and $\tilde{y}_{n+1}$ are uncorrelated, Eq $\eqref{eq-forecast_error1}$ shows that 

$$
\begin{align}
\var(\tilde{u}_{n+1}) &= \var(u_{n+1}) + \var(\tilde{y}_{n+1}) \nonumber \\
&= \sigma^2 + \var(\tilde{y}_{n+1}) \label{eq-var_decomp}
\end{align}
$$

We have shown that there are two sources of variation in $\tilde{u}_{n+1}:$

- $\sigma^2=\var(u_{n+1})$ is the variance of the error in the population.

- $$\var(\tilde{y}_{n+1})$$ is the sampling error in $\tilde{y}_{n+1},$ which arises because we have estimated $\bbeta.$

    $$\var(\tilde{y}_{n+1})$$ is proportional to $1/n.$ This means that, for large samples, $\var(\tilde{y}_{n+1})$ can be very small.

- By contrast, $\sigma^2$ does not change with the sample size. In many examples, $\sigma^2$ will be the dominant term in $\eqref{eq-var_decomp}.$


Plug in $\tilde{u}_{n+1}$ $\eqref{eq-forecast_error2},$ we have


$$
\begin{align} 
\text{MSFE}_n &= \E(\bx_{n+1}'\bbeta + u_{n+1} - \bx_{n+1}'\hat\bbeta)^2 \nonumber \\
&= \E [\bx_{n+1}'(\bbeta-\hat\bbeta) + u_{n+1} ]^2 \nonumber \\
&= \E [\bx_{n+1}'(\bbeta-\hat\bbeta)(\bbeta-\hat\bbeta)\bx_{n+1} ] + 2\E[u_{n+1}\bx_{n+1}'(\bbeta-\hat\bbeta)] + \E[u_{n+1}^2] \label{eq-msfe}
\end{align}
$$

The second item in $\eqref{eq-msfe}$ is zero and the first item can be simplified to

$$
\E(\bx_{n+1}'\bV_{\hat\bbeta}\bx_{n+1}) .
$$

Thus,

$$
\begin{align} 
\text{MSFE}_n = \sigma^2 + \E(\bx_{n+1}'\bV_{\hat\bbeta}\bx_{n+1}) . \label{eq-msfe2}
\end{align}
$$


We can interpret as the variance of the forecast error $$\left( \E(\tilde{u}_{n+1}^2) \right)$$ is equal to the sum of the variance of the regression $(\sigma^2)$ and the variance of the forecast $\left( \E(\bx_{n+1}'\bV_{\hat\bbeta}\bx_{n+1}) \right)$.

Under conditional homoskedasticity, $\eqref{eq-msfe2}$ simplifies to

$$
\text{MSFE}_n = \sigma^2 \left( 1 + \E(\bx_{n+1}' (\bX'\bX)^{-1} \bx_{n+1}) \right) .
$$


A simple estimator for the MSFE is obtained by averaging the squared prediction errors

$$
\begin{align} \label{eq-MSFE_estimator}
\tilde{\sigma}^2 = \frac{1}{n} \sum_{i=1}^{n} \tilde{u}_i^2 ,
\end{align}
$$

where $\tilde{u}_i$ is the leave-one-out residual, prediction error, or prediction residual given by:

$$
\begin{align} 
\tilde{u}_i 
&= y_i - \tilde{y}_i  \\
&= y_i - \bx_i' \hat{\bbeta}_{(-i)} \label{eq-prediction_error_leave_one_out}  \\
&= \color{#008B45} \hat{u}_i (1 - h_{ii})^{-1}, \label{eq-prediction_error}
\end{align}
$$ 

where $h_{ii}$ are the leverage values defined as

$$
h_{ii} = \bx_i'(\bX'\bX)\bx_i ,
$$

and 

$$
\hat{u}_i = y_i - \hat{y}_i .
$$

$\hat{u}_i$ is the residual from the full sample regression, while $\tilde{u}_i$ is the forecast error.

$h_{ii}$ is a normalized length of the observed regressor vector $\bx_i.$ It measures how unusual the $i$-th observation $\bx_i$ is relative to the other values in the sample. A high $h_{ii}$ occurs when $\bx_i$ is quite different from the other sample values. 



Eq $\eqref{eq-prediction_error_leave_one_out}$ means that the predicted value $\tilde{y}_i$ is obtained by 

1. First estimate $\bbeta$ on the sample <span style='color:#008B45'>without observation $i:$</span> 

    $$
    \begin{split}
    \hat{\bbeta}_{(-i)} &= \left(\bX_{(-i)}'\bX_{(-i)}\right)^{(-1)} \left(\bX_{(-i)}\by_{(-i)}\right)  \\
    &= \left(\sum_{j\ne i} \bx_j\bx_j' \right)^{-1} \left(\sum_{j\ne i} \bx_jy_j' \right) .
    \end{split}
    $$

    Here $\bX_{(-i)}$ and $\by_{(-i)}$ are the data matrices omitting the $i$th row. $\hat{\bbeta}_{(-i)}$ denotes an estimator with the $i$th observation omitted.


2. Then use the covariate vector $\bx_i$ to predict $y_i.$

    $$
    \tilde{y}_i = \bx_i' \hat{\bbeta}_{(-i)}
    $$

Note that $\tilde{y}_i$ is an *authentic prediction* as $y_i$ is not used to construct $\tilde{y}_i.$ This is in contrast to the fitted value $\hat{y}_i$ which are functions of $y_i.$ The consequence of this is that the prediction errors $$\tilde{u}_i$$ are better estimates than the residuals $$\hat{u}_i,$$ since the former are based on authentic predictions.


Eq $\eqref{eq-prediction_error_leave_one_out}$ gives the unfortunate impression that the leave-one-out coefficients and errors are computationally cumbersome, requiring $n$ separate regressions. But fortunately, Eq $\eqref{eq-prediction_error}$ gives us a simple linear expression for $\tilde{u}_i$.


Eq $\eqref{eq-prediction_error}$ relates prediction errors to residuals.
Note that the prediction errors $$\tilde{u}_i$$ are a simple scaling of the residuals $$\hat{u}_i,$$ with the scaling depending on the leverage value $h_{ii}.$

- If $h_{ii}$ is large, then $\tilde{u}_i$ can be quite different from $\hat{u}_i.$
- If $h_{ii}$ is small, then $\tilde{u}_i \approx \hat{u}_i.$

Thus, the difference between the residuals and predicted values depends on the leverage values, that is, how unusual $\bx_i$ is relative to the other observations.


Moreover, we can write $\hat{\bbeta}_{(-i)}$ as

$$
\hat{\bbeta}_{(-i)} = \hat{\bbeta} - (\bX'\bX)^{-1}\bx_i\tilde{u}_i
$$

We can rewrite $\eqref{eq-MSFE_estimator}$ as

$$
\tilde{\sigma}^2 = \frac{1}{n} \sum_{i=1}^{n} \tilde{u}_i^2 = \frac{1}{n} \sum_{i=1}^{n} \hat{u}_i^2 (1 - h_{ii})^{-2} .
$$

This is also known as the **sample mean squared prediction error**. Its square root 

$$
\tilde{\sigma} = \sqrt{\tilde{\sigma}^2}
$$

is the **prediction standard error**.


We can calculate that

$$
\begin{split}
\mathbb{E}(\tilde{\sigma}^2) &= \mathbb{E}(\tilde{u}_i^2) \\
&= \mathbb{E} \left( u_i - x_i' \left(\hat{\bbeta}_{(-i)} - \bbeta \right) \right)^2  \\
&= \sigma^2 + \mathbb{E} \left[ x_i' \left(\hat{\bbeta}_{(-i)} - \bbeta\right)\left(\hat{\bbeta}_{(-i)} - \bbeta\right)' x_i \right] ,
\end{split}
$$

where $\hat{\bbeta}_{(-i)}$ is the regression coefficient with the $i$th observation omitted.

We find

$$
\mathbb{E}(\tilde{\sigma}^2) = \sigma^2 + \mathbb{E} \left( \bx_i' \bV_{\hat{\bbeta}_{(-i)}} \bx_i \right) = \text{MSFE}_{n-1} .
$$

This is the MSFE based on a sample of size $n - 1$, rather than size $n$. 
The difference arises because the in-sample prediction errors $$\tilde{e}_i$$ for $i \leq n$ are calculated using an effective sample size of $n - 1$, while the out-of-sample prediction error $$\tilde{e}_{n+1}$$ is calculated from a sample with the full $n$ observations. 
Unless $n$ is very small, we should expect $\text{MSFE}_{n-1}$ (the MSFE based on $n - 1$ observations) to be close to $\text{MSFE}_n$ (the MSFE based on $n$ observations). Thus $\tilde{\sigma}^2$ is a reasonable estimator for $\text{MSFE}_n$.


<div class = "boxed">
<strong>Theorem Mean-Square Forecast Error (MSFE)</strong> <br/>
In the linear regression model and i.i.d. sampling :  

$$
\text{MSFE}_n = \mathbb{E}(u_{n+1}^2) = \sigma^2 + \mathbb{E} \left( x_{n+1}' V_{\hat{\beta}} x_{n+1} \right)
$$

where $V_{\hat{\beta}} = \mathrm{var}(\hat{\beta} \mid x)$. <br/>

Furthermore, $\tilde{\sigma}^2$ defined in $\eqref{eq-MSFE_estimator}$ is an unbiased estimator of $\text{MSFE}_{n-1}$:

$$
\mathbb{E}(\tilde{\sigma}^2) = \text{MSFE}_{n-1}.
$$
</div>


**Reference**: Chapter 4.12, pp.112, Hansen, Econometrics.

___

## Regression Intervals

The conditional mean of $y_i$ given $\bx_i = \bx$ is

$$
m(x) = \E(y_i\mid \bx_i = \bx) = \bx'\bbeta .
$$

The point estimate under OLS estimator is the conditional mean:

$$
\widehat{m}(\bx) = \bx'\hat\bbeta
$$

The variance is given by 

$$
\var(\widehat{m}(\bx)) = \bx'\bV_{\hat{\bbeta}}\bx .
$$

The 95% confidence interval for $m(\bx)$ is

$$
\left[\widehat{m}(\bx) \pm t_{.025}\cdot \mathrm{se}\left(\widehat{m}(\bx)\right) \right] ,
$$

where 

$$
\mathrm{se}\left(\widehat{m}(\bx)\right) = \sqrt{\bx'\bV_{\hat{\bbeta}}\bx}
$$

and 

$$
\P\left( -t_{.025}\leq \frac{\widehat{m}(\bx) - m(\bx)}{\mathrm{se}\left(\widehat{m}(\bx)\right)} \leq t_{.025} \right) = .95 .
$$

$t_{.025}$ is the $97.5$th percentile in the $t_{n-K}$ distribution. 

The 95% confidence interval is given by

$$
\left[ \widehat{m}(\bx) \pm t_{.025} \cdot\mathrm{se}\left(\widehat{m}(\bx)\right) \right] .
$$

For large $n-K,$ recall that $t_{.025} \approx 1.96.$
Thus an asymptotic 95% confidence interval for $m(\bx)$ is 

$$
\begin{align}
\left[ \bx'\hat\bbeta \pm 1.96 \sqrt{\bx'\bV_{\hat{\bbeta}}\bx} \right] \label{eq-regression_interval},
\end{align}
$$

which is a function of $\bx;$ the width of the confidence interval is dependent on $\bx.$

Unless for small $df,$ $\left[ \widehat{m}(\bx) \pm 1.96 \cdot\mathrm{se}\left(\widehat{m}(\bx)\right) \right]$ is a good approximation.


___


## Forecast Interval

Suppose we are given a value of the regressor vector $\bx_{n+1}$ for an individual outside the sample, and we want to forecast (guess) $y_{n+1}$ for this individual. This is equivalent to forecasting $y_{n+1}$ given $\bx_{n+1}=\bx,$ which will generally be a function of $\bx.$


The forecast error is

$$
\tilde{u}_{n+1} = y_{n+1} - \tilde{y}_{n+1} = y_{n+1} 
$$

and it has the conditional variance

$$
\mathbb{E}(\tilde{\sigma}^2 \mid \bx_{n+1}=\bx) = \sigma^2(\bx) +  \bx' \bV_{\hat{\bbeta}} \bx .
$$

A simple estimator is

$$
\var(\tilde{u}_{n+1} \mid \bx) = \hat{\sigma}^2 + \bx' \hat{\bV}_{\hat{\bbeta}} \bx .
$$

The conventional 95% forecast interval for $y_{n+1}$ uses a normal approximation and sets

$$
\begin{align}
\left[ \bx'\hat\bbeta \pm 1.96 \sqrt{ \hat{\sigma}^2 + \bx'\hat{\bV}_{\hat{\bbeta}}\bx} \right] . \label{eq-forecast_interval}
\end{align}
$$

The prediction interval $\eqref{eq-forecast_interval}$ is often much wider than the regression interval $\eqref{eq-regression_interval}$ because of the regression error $\hat{\sigma}^2.$
___

## Partitioned Regression

Partition 

$$
\bX = \begin{bmatrix} \bX_1 & \bX_2
\end{bmatrix}
$$

and 

$$
\bbeta = \begin{bmatrix} \bbeta_1 \\ \bbeta_2
\end{bmatrix} .
$$

Then the regression model can be rewritten as

$$
\begin{align} \label{eq-partition}
\by = \bX_1\bbeta_1 + \bX_2\bbeta_2 + \bu .
\end{align}
$$

The least-squares estimator $(\hat{\bbeta}_1, \hat{\bbeta}_2)$ has the algebraic solution

$$
\begin{aligned}
\hat{\bbeta}_1 &= (\bX_1'\bM_2\bX_2)^{-1}(\bX_1'\bM_2\by)  \\
\hat{\bbeta}_2 &= (\bX_2'\bM_1\bX_1)^{-1}(\bX_2'\bM_1\by)  \\
\end{aligned}
$$

where 

$$
\bM_1 = \mathbf{I}_n - \bX_1(\bX_1'\bX_1)^{-1}\bX_1'
$$

is the orthogonal projection matrix (residual maker) for $\bX_1,$ and 

$$
\bM_2 = \mathbf{I}_n - \bX_2(\bX_2'\bX_2)^{-1}\bX_2'
$$

is the orthogonal projection matrix (residual maker) for $\bX_2.$ 

Since the residual make is idempotent, $\bM_1 = \bM_1\bM_1$ and thus

$$
\begin{split}
\hat{\bbeta}_2 &= (\bX_2'\bM_1\bX_1)^{-1}(\bX_2'\bM_1\by) \\
&= (\bX_2'\bM_1\bM_1\bX_1)^{-1}(\bX_2'\bM_1\bM_1\by) \\
&= (\widetilde{\bX}_2'\widetilde{\bX})^{-1} (\widetilde{\bX}_2' \widetilde{\bu}_1)
\end{split}
$$

where

$$
\widetilde{\bX}_2 = \bM_1 \bX_2, 
$$

the columns of $\bX_2$ are the least-squares residuals from the regressions of the columns of $\bX_2$ on $\bX_1.$ And

$$
\widetilde{\bu}_1 = \bM_1\by ,
$$

which is the least-squares residual from a regression of $\by$ on $\bX_1.$

<div class = "boxed">
<strong>Frisch-Waugh-Lovell (FWL) Theorem</strong> <br/>

In the model $\eqref{eq-partition},$ the OLS estimator of $\bbeta_2$ and the OLS residuals $
\hat{\bu}$ may be computed via the following algorithm:
<ol>
<li>Regress $\by$ on $\bX_1,$ obtain the residuals $\widetilde{\bu}_1$; </li>
<li>Regress $\bX_2$ on $\bX_1,$ obtain the residuals $\widetilde{\bX}_2$; </li>
<li>Regress $\widetilde{\bu}_1$ on $\widetilde{\bX}_2$, obtain the OLS estimates $\bbeta_2$ and residuals $\hat{\bu}$. </li>
</ol>
</div>















