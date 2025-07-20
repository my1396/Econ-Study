---
layout: post
title: Multivariate Regression
tag: study
update: 2025-06-19
---


## Introduction

**Multivariate regression** is a system of regression equations. Multivariate regression is commonly used as reduced form models for instrumental variable estimation, vector autoregressions, demand systems (demand for multiple goods), and GMM estimation for a system of equations.

Multivariate regression is also called by the name <span style="color: #008B45;">
**systems of regression equations**</span>. Closely related is the method of <span style="color: #008B45;">**Seemingly Unrelated Regressions** (SUR)</span>.


Examples where systems of regression equations are useful: There are many settings in which disturbances are correlated across units. In these contexts, it makes sense to consider the several models iointly.


**Example 1**

The CAPM model

$$
r_{it} - r_{ft} = \alpha_i + {\color{#008B45}\beta_{i}} (r_{mt}-r_{ft}) + \varepsilon_{it}.
$$

The disturbances can be correlated across securities. The knowledge that the return on security $i$ exceeds the risk-free rate by a given amount gives some information about the excess return of security $i$, at least for some $i$’s. It may be useful to estimate the equations iointly rather than ignore this connection.


___

**Example 2**

Grunfeld's investment model is

$$
I_{it} = \beta_{1i} + \beta_{2i} F_{it} + \beta_{3i}C_{it} + \varepsilon_{it}
$$

where $i$ indexes firms, $t$ indexes years, and

$$
\begin{split}
I_{it} &= \text{ gross investment}, \\
F_{it} &= \text{market value of the firm at the end of the previous year} , \\
C_{it} &= \text{value of the stock of plant and equipment at the end of the previous year.}
\end{split}
$$

The disturbances in the investment equations certainly include factors that are common to all the firms, such as the perceived general health of the economy, as well as factors that are specific to the particular firm or industry.

___

**Example 3**

In a model of production, the optimization conditions of economic theory imply that if a firm faces a set of factor prices $\bp$, then its set of cost-minimizing factor demands for producing output $Y$ will be a set of equations of the form 

$$
x_m = f_m (Y, \boldsymbol{p:\theta}) + \varepsilon_m , \quad m=1,\ldots, M.
$$


Once again, the disturbances should be correlated. Estimating the equations separately will waste the information that the same set of parameters appears in all the equations.


___


## Model Setup

Multiple regression equations can be written as 

$$
\begin{equation} \label{eq-multivariate}
\begin{split}
\by_1 &= \bX_1 \bbeta_1 + \bvarepsilon_1 , \\
\by_2 &= \bX_2 \bbeta_2 + \bvarepsilon_2 , \\
&\phantom{\;\;} \vdots \\
\by_M &= \bX_M \bbeta_M + \bvarepsilon_M , \\
\end{split}
\end{equation}
$$

where $\by_i$ and $\bvarepsilon_i,$ $i=1,\ldots,M,$ are $N\times 1$ vectors. 
There are $M$ equations and $N$ observations in the sample of data used to estimate them.
$\bX_i$ is an $N\times K_i$ matrix, where 

$$
K_i = \text{dim}(\bbeta_i)
$$

is the number of regressors for the $i$-th regression. 

**Distinguish** from the panel data model, where we assume identical coefficients across equations.

|      | SUR                                 | Panel                                                 |
| ---- | ----------------------------------- | ----------------------------------------------------- |
| $M$  | variables; equations → assume depd. | individuals; firms; units; → assume indepd.           |
| $N$  | observations; → assume indepd.      | Time periods; often denoted $T$ → assume serial depd. |





___

A system of linear regressions assumes that, there are $M$ dependent variables, $\by_{1},$ $\by_{2}, \ldots,$ $\by_{M},$

$$
\underbrace{\by_{i}}_{N\times 1} = \begin{pmatrix}
y_{i1} \\ 
y_{i2} \\
\vdots \\
y_{iN}
\end{pmatrix} \quad \text{ for } i = 1,\ldots, M,
$$

where

$$
\begin{equation} \label{eq-sur}
y_{it} = \underbrace{\bx_{it}'}_{1\times K_i}\; \underbrace{\color{#008B45}\bbeta_{i}}_{K_i\times 1} + \varepsilon_{it}, \quad t = 1,\ldots, N,
\end{equation}
$$

- $i=1,\ldots, M$ indexes variables, equations; 
- and $t=1,\ldots, N$ indexes observations.

**Stacking of observations over** $i$, for each equation $i=1,\ldots,M$, we have

$$
\begin{bmatrix}
y_{i1}  \\
y_{i2}  \\
\vdots \\
y_{iN}  \\
\end{bmatrix}
= \begin{bmatrix}
\bx_{i1}'  \\
\bx_{i2}'  \\
\vdots \\
\bx_{iN}'  \\
\end{bmatrix}
\bbeta_{i} + 
\begin{bmatrix}
\varepsilon_{i1}  \\
\varepsilon_{i2}  \\
\vdots \\
\varepsilon_{iN}  \\
\end{bmatrix}
$$

or

$$
\by_i = \underbrace{\bX_i}_{N\times K_i} \bbeta_i + \bvarepsilon_i , \quad i=1,\ldots,M
$$

It is typical to assume


- $y_{it}$ independent between observations $t$ and $t'$, namely

    $$
    \cov (\varepsilon_{it}, \varepsilon_{it'}) = 0 ,
    $$

    where $t\ne t'.$

    And 

    $$
    \var(\varepsilon_{it}) = \sigma_{ii}
    $$

    In matrix form:

    $$
    \begin{split}
    \E[\bvarepsilon_i\bvarepsilon_i'] 
    &= \begin{bmatrix} 
    \E(\varepsilon_{i1}\varepsilon_{i1}) & \E(\varepsilon_{i1}\varepsilon_{i2})  & \cdots &  \E(\varepsilon_{i1}\varepsilon_{iN}) \\
    \E(\varepsilon_{i1}\varepsilon_{i2}) &  \E(\varepsilon_{i2}\varepsilon_{i2})  & \cdots &  \E(\varepsilon_{i2}\varepsilon_{iN}) \\
    \vdots & \vdots & \ddots & \vdots \\
    \E(\varepsilon_{i1}\varepsilon_{iN}) &  \E(\varepsilon_{i2}\varepsilon_{iN})  & \cdots &  \E(\varepsilon_{iN}\varepsilon_{iN}) \\
    \end{bmatrix} \\
    &= \begin{bmatrix} 
    \sigma_{ii} & 0  & \cdots & 0 \\
    0 & \sigma_{ii}  & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0  & \cdots & \sigma_{ii} \\
    \end{bmatrix} \\
    &= \sigma_{ii} I_N .
    \end{split}
    $$


- but **correlated across variables (equations)** $i$ and $j$,

    $$
    \cov(\varepsilon_{it}, \varepsilon_{jt}) = \sigma_{ij} .
    $$

    where $i\ne j$.
    That is, for observation (time period) $t$, the error terms across equations (variables) $i$ and $j$ are correlated.

    $$
    \cov(\varepsilon_{it}, \varepsilon_{jt'}) = 0 .
    $$

    where $t\ne t'$.
    
    This means that error terms across different equations are uncorrelated when they occur in different time periods or observations. In other words, the error in equation $i$ at time $t$ is independent of the error in equation $j$ at a different time $t'$. 
    
    This assumption maintains temporal independence across equations while still allowing for contemporaneous correlation (at the same time $t$) between different equations.

    In matrix form:

    $$
    \begin{split}
    \E[\bvarepsilon_i\bvarepsilon_j'] 
    &= \begin{bmatrix} 
    \E(\varepsilon_{i1}\varepsilon_{j1}) & \E(\varepsilon_{i1}\varepsilon_{j2})  & \cdots &  \E(\varepsilon_{i1}\varepsilon_{jN}) \\
    \E(\varepsilon_{i2}\varepsilon_{j1}) &  \E(\varepsilon_{i2}\varepsilon_{j2})  & \cdots &  \E(\varepsilon_{i2}\varepsilon_{jN}) \\
    \vdots & \vdots & \ddots & \vdots \\
    \E(\varepsilon_{iN}\varepsilon_{j1}) &  \E(\varepsilon_{iN}\varepsilon_{j2})  & \cdots &  \E(\varepsilon_{iN}\varepsilon_{jN}) \\
    \end{bmatrix} \\
    &= \begin{bmatrix} 
    \sigma_{ij} & 0  & \cdots & 0 \\
    0 & \sigma_{ij}  & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0  & \cdots & \sigma_{ij} \\
    \end{bmatrix} \\
    &= \sigma_{ij} I_N .
    \end{split}
    $$




As an example, let the observations $y_{it}$ be expenditures on goods $i$ by household $t.$

- The standard assumptions are that households are mutually independent.

    $$
    \cov(\varepsilon_{it}, \varepsilon_{it'}) = 0 , \text{ for } t\ne t'.
    $$

    Household 1's spending decisions are independent of household 2's decisions.

- Expenditures by an individual household are correlated across goods.

    $$
    \cov(\varepsilon_{1t}, \varepsilon_{2t}) = \sigma_{12} \neq 0
    $$

    If household $t$ has an unexpectedly high food expenditure (positive $\varepsilon_{1t}$), they might also have high housing expenditure (positive $\varepsilon_{2t}$) due to higher income or different preferences.

Summary: This correlation structure captures the economic reality that spending decisions across different categories are related for the same household, but spending patterns are independent across different households.

___

## Kronecker Product Notation


The N-vector $\by_i$ can be further stacked into an $MN$-dimensional vector $\by$:

$$
\begin{bmatrix}
\by_{1}  \\
\by_{2}  \\
\vdots \\
\by_{M}  
\end{bmatrix}
= \begin{bmatrix}
\bX_{1} & 0  & \cdots & 0 \\
0 & \bX_{2} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0  & \cdots & \bX_{M} \\
\end{bmatrix}
\begin{bmatrix}
\bbeta_{1}  \\
\bbeta_{2}  \\
\vdots \\
\bbeta_{M}  
\end{bmatrix} +
\begin{bmatrix}
\bvarepsilon_{1}  \\
\bvarepsilon_{2}  \\
\vdots \\
\bvarepsilon_{M}  
\end{bmatrix}
$$

or

$$
\by = \bX \bbeta + \bvarepsilon ,
$$

where


$$
\underset{(MN\times 1)}{\by} = \begin{bmatrix}
\by_{1}  \\
\by_{2}  \\
\vdots \\
\by_{M}  
\end{bmatrix} ,
\underset{(MN\times 1)}{\bvarepsilon} = \begin{bmatrix}
\bvarepsilon_{1}  \\
\bvarepsilon_{2}  \\
\vdots \\
\bvarepsilon_{M}  
\end{bmatrix} ,
\underset{(K\times 1)}{\bbeta} = \begin{bmatrix}
\bbeta_{1}  \\
\bbeta_{2}  \\
\vdots \\
\bbeta_{M}  
\end{bmatrix} 
$$

and 

$$
\underset{(MN\times K)}{\bX} = 
\begin{bmatrix}
\bX_{1} & 0  & \cdots & 0 \\
0 & \bX_{2} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0  & \cdots & \bX_{M} \\
\end{bmatrix} ,
$$

with 

$$
K\equiv  \sum_{i=1}^M K_i .
$$


With this notation, and the individual assumptions for each equation $i,$ it follows that 

$$
\E[\by] = \bX\bbeta
$$

and 

$$
\var(\by) = \E(\bvarepsilon\bvarepsilon') = \bOmega =
\begin{bmatrix}
\sigma_{11}\bI_{N} & \sigma_{12}\bI_{N}  & \cdots & \sigma_{1M}\bI_{N} \\
\sigma_{21}\bI_{N} & \sigma_{22}\bI_{N} & \cdots & \sigma_{2M}\bI_{N} \\
\vdots & \vdots & \ddots & \vdots \\
\sigma_{M1}\bI_{N} & \sigma_{M2}\bI_{N}  & \cdots & \sigma_{MM}\bI_{N} \\
\end{bmatrix} .
$$


Let

$$
\bSigma = \begin{bmatrix}
\sigma_{11} & \sigma_{12}  & \cdots & \sigma_{1M} \\
\sigma_{21} & \sigma_{22} & \cdots & \sigma_{2M} \\
\vdots & \vdots & \ddots & \vdots \\
\sigma_{M1} & \sigma_{M2}  & \cdots & \sigma_{MM} \\
\end{bmatrix} 
$$

and the $N\times N$ identity matrix $\bI_N.$ We can rewrite the error covariance matrix as

$$
\bOmega = \bSigma \otimes \bI_N .
$$

___

## GLS Estimator

The GLS estimator is

$$
\begin{split}
\hat{\bbeta} 
&= [\bX'\bOmega^{-1}\bX]^{-1} [\bX'\bOmega^{-1}\by] \\
&=  \left[\bX'(\bSigma \otimes \bI_N)^{-1}\bX\right]^{-1} \left[\bX'(\bSigma \otimes \bI_N)^{-1}\by\right] \\
&= \left[\bX'(\bSigma^{-1} \otimes \bI_N)\bX\right]^{-1} \left[\bX'(\bSigma^{-1} \otimes \bI_N)\by\right] \quad \left((\bSigma \otimes \bI_N)^{-1} = \bSigma^{-1} \otimes \bI_N \right) 
\end{split}
$$

Expanding the **Kronecker products** produces  

$$
\hat{\boldsymbol{\beta}} =
\begin{bmatrix}
\sigma_{11} \mathbf{X}_1' \mathbf{X}_1 & \sigma_{12} \mathbf{X}_1' \mathbf{X}_2 & \cdots & \sigma_{1M} \mathbf{X}_1' \mathbf{X}_M \\
\sigma_{21} \mathbf{X}_2' \mathbf{X}_1 & \sigma_{22} \mathbf{X}_2' \mathbf{X}_2 & \cdots & \sigma_{2M} \mathbf{X}_2' \mathbf{X}_M \\
\vdots & \vdots & \ddots & \vdots \\
\sigma_{M1} \mathbf{X}_M' \mathbf{X}_1 & \sigma_{M2} \mathbf{X}_M' \mathbf{X}_2 & \cdots & \sigma_{MM} \mathbf{X}_M' \mathbf{X}_M
\end{bmatrix}^{-1}
\begin{bmatrix}
\sum\limits_{i=1}^{M} \sigma_{1i} \mathbf{X}_1' \mathbf{y}_i \\
\sum\limits_{i=1}^{M} \sigma_{2i} \mathbf{X}_2' \mathbf{y}_i \\
\vdots \\
\sum\limits_{i=1}^{M} \sigma_{Mi} \mathbf{X}_M' \mathbf{y}_i
\end{bmatrix}.
$$

**Relationship with OLS**

1. If the equations are actually unrelated—that is, if $\sigma_{ii}=0$ for $i\ne i$, then there is obviously no payoff to GLS estimation of the full set of equations. Indeed, full GLS is equation by equation OLS.

2. If the equations have identical explanatory variables—that is, if $\bX_i = \bX_i$, then OLS and GLS are identical. 

3. If the regressors in one block of equations are a subset of those in another, then GLS brings no efficiency gain over OLS in estimation of the smaller set of equations; thus, GLS and OLS are once again identical. 

**Two propositions** that apply generally are as follows:

1. The greater is the correlation of the disturbances, the greater is the efficiency gain accruing to GLS.
2. The less correlation there is between the X matrices, the greater is the gain in efficiency in using GLS.

___

**References**

-  Chapters 14 System of Regression Equations. **Econometric Analysis** , 5th Edition, by William H. Greene, Prentice Hall, 2003. 

- Chapter 15 Multivariate Regression. **Econometrics**. by Bruce Hansen, 2022. 