---
layout: post
title: Multivariate Regression
tag: study
update: 2025-06-19
---


## Introduction

**Multivariate regression** is a system of regression equations. Multivariate regression is commonly used as reduced form models for instrumental variable estimation, vector autoregressions, demand systems (demand for multiple goods), and GMM estimation for a system of equations.

Multivariate regression is also called by the name **systems of regression equations**. Closely related is the method of **Seemingly Unrelated Regressions** (SUR).


Examples where systems of regression equations are useful: There are many settings in which disturbances are correlated across units. In these contexts, it makes sense to consider the several models jointly.


**Example 1**

The CAPM model

$$
r_{it} - r_{ft} = \alpha_i + \beta_{i} (r_{mt}-r_{ft}) + \varepsilon_{it}.
$$

The disturbances can be correlated across securities. The knowledge that the return on security $i$ exceeds the risk-free rate by a given amount gives some information about the excess return of security $j$, at least for some $j$’s. It may be useful to estimate the equations
jointly rather than ignore this connection.


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

where $\by_j$ and $\bvarepsilon_j,$ $j=1,\ldots,M,$ are $N\times 1$ vectors. 
There are $M$ equations and $N$ observations in the sample of data used to estimate them.
$\bX_j$ is an $N\times K_j$ matrix, where 

$$
K_j = \text{dim}(\bbeta_j)
$$

is the number of regressors for the $j$-th regression. 

___


A system of linear regressions assumes that, for each individual observation $i,$ there are $M$ dependent variables, $y_{1i},$ $y_{2i}, \ldots,$ $y_{Mi},$

$$
\begin{equation} \label{eq-sur}
y_{ji} = \underbrace{\bx_{ji}'}_{1\times K_j}\; \underbrace{\bbeta_{j}}_{K_j\times 1} + \varepsilon_{ji}, \quad j=1,\ldots, M,
\end{equation}
$$

$j=1,\ldots, M$ indexes variables; and $i=1,\ldots, N$ indexes *individuals*, *groups*, or *firms*.

**Stacking of observations over** $i$, for each equation $j=1,\ldots,M$, we have

$$
\begin{bmatrix}
y_{j1}  \\
y_{j2}  \\
\vdots \\
y_{jN}  \\
\end{bmatrix}
= \begin{bmatrix}
\bx_{j1}'  \\
\bx_{j2}'  \\
\vdots \\
\bx_{jN}'  \\
\end{bmatrix}
\bbeta_{j} + 
\begin{bmatrix}
\varepsilon_{j1}  \\
\varepsilon_{j2}  \\
\vdots \\
\varepsilon_{jN}  \\
\end{bmatrix}
$$

or

$$
\by_j = \underbrace{\bX_j}_{N\times K_j} \bbeta_j + \bvarepsilon_j , \quad j=1,\ldots,M
$$

It is typical to assume


- $y_{ji}$ independent across observations $i$, namely

    $$
    \cov (\varepsilon_{ji}, \varepsilon_{ji'}) = 0 ,
    $$

    where $i\ne i'.$

    And

    $$
    \var(\varepsilon_{ji}) = \sigma_{jj}
    $$

    In matrix form:

    $$
    \begin{split}
    \E[\bvarepsilon_j\bvarepsilon_j'] 
    &= \begin{bmatrix} 
    \E(\varepsilon_{j1}\varepsilon_{j1}) & \E(\varepsilon_{j1}\varepsilon_{j2})  & \cdots &  \E(\varepsilon_{j1}\varepsilon_{jN}) \\
    \E(\varepsilon_{j1}\varepsilon_{j2}) &  \E(\varepsilon_{j2}\varepsilon_{j2})  & \cdots &  \E(\varepsilon_{j2}\varepsilon_{jN}) \\
    \vdots & \vdots & \ddots & \vdots \\
    \E(\varepsilon_{j1}\varepsilon_{jN}) &  \E(\varepsilon_{j2}\varepsilon_{jN})  & \cdots &  \E(\varepsilon_{jN}\varepsilon_{jN}) \\
    \end{bmatrix} \\
    &= \begin{bmatrix} 
    \sigma_{jj} & 0  & \cdots & 0 \\
    0 & \sigma_{jj}  & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0  & \cdots & \sigma_{jj} \\
    \end{bmatrix} \\
    &= \sigma_{jj} I_N .
    \end{split}
    $$


- but **correlated across variables (equations)** $j$,

    $$
    \cov(\varepsilon_{si}, \varepsilon_{ti}) = \sigma_{st} .
    $$

    That is, for individual $i$, the error terms across equations (variables) $s$ and $k$ are correlated.

    In matrix form:

    $$
    \begin{split}
    \E[\bvarepsilon_s\bvarepsilon_t'] 
     &= \begin{bmatrix} 
    \E(\varepsilon_{s1}\varepsilon_{t1}) & \E(\varepsilon_{s1}\varepsilon_{t2})  & \cdots &  \E(\varepsilon_{s1}\varepsilon_{tN}) \\
    \E(\varepsilon_{s1}\varepsilon_{t2}) &  \E(\varepsilon_{s2}\varepsilon_{t2})  & \cdots &  \E(\varepsilon_{s2}\varepsilon_{tN}) \\
    \vdots & \vdots & \ddots & \vdots \\
    \E(\varepsilon_{s1}\varepsilon_{tN}) &  \E(\varepsilon_{s2}\varepsilon_{tN})  & \cdots &  \E(\varepsilon_{sN}\varepsilon_{tN}) \\
    \end{bmatrix} \\
    &= \begin{bmatrix} 
    \sigma_{st} & 0  & \cdots & 0 \\
    0 & \sigma_{st}  & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0  & \cdots & \sigma_{st} \\
    \end{bmatrix} \\
    &= \sigma_{st} I_N .
    \end{split}
    $$




As an example, the observations $y_{ji}$ could be expenditures by household $i$ on goods $j$. The standard assumptions are that households are mutually independent, but expenditures by an individual household are correlated across goods.


___

## Kronecker Product Notation


The N-vector $\by_j$ can be further stacked into an $MN$-dimensional vector $\by$:

$$
\begin{bmatrix}
\by_{1}  \\
\by_{j}  \\
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
\bbeta_{j}  \\
\vdots \\
\bbeta_{M}  
\end{bmatrix} +
\begin{bmatrix}
\bvarepsilon_{1}  \\
\bvarepsilon_{j}  \\
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
\by_{j}  \\
\vdots \\
\by_{M}  
\end{bmatrix} ,
\underset{(MN\times 1)}{\bvarepsilon} = \begin{bmatrix}
\bvarepsilon_{1}  \\
\bvarepsilon_{j}  \\
\vdots \\
\bvarepsilon_{M}  
\end{bmatrix} ,
\underset{(K\times 1)}{\bbeta} = \begin{bmatrix}
\bbeta_{1}  \\
\bbeta_{j}  \\
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
K\equiv  \sum_{j=1}^M K_j .
$$


With this notation, and the individual assumptions for each equation $j,$ it follows that 

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

and the $N\times N$ identity matrix $\bI_N.$ We can rewrite the covariance matrix as

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
&=  \left[\bX'(\bSigma \otimes \bI_N)^{-1}\bX\right]^{-1} \left[\bX'(\bSigma \otimes \bI_N)^{-1}\by\right] .
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
\sum\limits_{j=1}^{M} \sigma_{1j} \mathbf{X}_1' \mathbf{y}_j \\
\sum\limits_{j=1}^{M} \sigma_{2j} \mathbf{X}_2' \mathbf{y}_j \\
\vdots \\
\sum\limits_{j=1}^{M} \sigma_{Mj} \mathbf{X}_M' \mathbf{y}_j
\end{bmatrix}.
$$

**Relationship with OLS**

1. If the equations are actually unrelated—that is, if $\sigma_{ij}=0$ for $i\ne j$, then there is obviously no payoff to GLS estimation of the full set of equations. Indeed, full GLS is equation by equation OLS.

2. If the equations have identical explanatory variables—that is, if $\bX_i = \bX_j$, then OLS and GLS are identical. 

3. If the regressors in one block of equations are a subset of those in another, then GLS brings no efficiency gain over OLS in estimation of the smaller set of equations; thus, GLS and OLS are once again identical. 

**Two propositions** that apply generally are as follows:

1. The greater is the correlation of the disturbances, the greater is the efficiency gain accruing to GLS.
2. The less correlation there is between the X matrices, the greater is the gain in efficiency in using GLS.

___

**References**

-  Chapters 14 System of Regression Equations. **Econometric Analysis** , 5th Edition, by William H. Greene, Prentice Hall, 2003. 

- Chapter 11 Multivariate Regression. **Econometrics**. by Bruce Hansen, 2022. 