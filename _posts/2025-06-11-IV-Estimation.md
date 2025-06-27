---
layout: post
title: Instrumental Variables Estimation
tag: study
update: 2025-06-11
---


## Structural Equation 

Model setup

$$
\begin{equation}
\begin{split}
y_i &= \bx_i'\bbeta + e_i \\
\by &= \bX\bbeta + \be \quad \text{(or in matrix form)}
\end{split}\label{eq:model-struct}
\end{equation}
$$

where 

$$
\E(\bx_ie_i) = 0
$$

$\bx_i$ is said to be endogenous for $\bbeta.$ We call $\eqref{eq:model-struct}$ a **structural equation** and $\bbeta$ a **structural parameter**.

We introduce a $\ell\times 1$ random vector $\bz_i$ as an instrumental variable for $\bx_i$. $\bz_i$ needs to satisfy the following conditions:

$$
\begin{align}
\E(\bz_ie_i) &= 0 \label{eq:con-exo} \\
\E(\bz_i\bz_i') &> 0 \label{eq:con-collinearity} \\
\rank{\left(\E(\bz_i\bx_i')\right)} &= K. \label{eq:con-relevance}
\end{align}
$$

- Condition $\eqref{eq:con-exo}$ requires that the instruments are uncorrelated with the regression error.
- Condition $\eqref{eq:con-collinearity}$ is a normalization which excludes linearly redundant instruments.
- Condition $\eqref{eq:con-relevance}$ is called the **relevance condition**. A necessary condition is that $\ell\geq K.$

## Reduced Form

The reduced form is the relationship between the regressors $\bx_i$ and the instruments $\bz_i:$

$$
\begin{equation}
\begin{split}
\bx_i &= \Gamma'\bz_i + \bu_i \\
\bX &= \bZ\Gamma + \bU \quad \text{(or in matrix form)}
\end{split}\label{eq:model-reduced}
\end{equation}
$$

where $\bu_i$ is a $K\times 1$ vector and $\bU$ is a $n\times K$ matrix.

$\bz_i$ is exogenous:

$$
\E(\bz_i\bu_i') = \boldsymbol{0}.
$$

$\Gamma$ can be obtained by

$$
\underbrace{\Gamma}_{\ell\times K} = \underbrace{\E(\bz_i\bz_i')^{-1}}_{\ell\times \ell} \;\underbrace{\E(\bz_i\bx_i')}_{\ell\times K}.
$$

We can also construct a reduced form equation for $y_i$. Substituting $\eqref{eq:model-reduced}$ into $\eqref{eq:model-struct},$ we get

$$
\begin{equation}
\begin{split}
y_i &= (\Gamma'\bz_i + \bu_i)'\bbeta + e_i \\
&= \bz_i'\blambda + v_i
\end{split}\label{eq:model-reduced-y}
\end{equation}
$$

where

$$
\begin{aligned}
\underbrace{\blambda}_{\ell \times 1} &= \underbrace{\Gamma}_{\ell\times K}\; \underbrace{\bbeta}_{K\times 1} \\
\text{and}\quad v_i &= \bu_i'\bbeta + e_i
\end{aligned}
$$

Observe that 

$$
\E(\bz_i v_i) = \E(\bz_i\bu_i')\bbeta + \E(\bz_ie_i) = \boldsymbol{0}.
$$

Eq. $\eqref{eq:model-reduced-y}$ is the reduced form for $y_i,$ as it expresses $y_i$ as a function of exogenous variables only.

The reduced form coefficient $\blambda$ can be obtained by

$$
\blambda = \E(\bz_i\bz_i')^{-1}\E(\bz_iy_i).
$$

So far, the reduced form coefficient matrices $\Gamma$ and $\blambda$ are identified based on the moments of the observables $(y_i, \bx_i, \bz_i).$ That is,

$$
\begin{equation}
\begin{split}
\Gamma = \E(\bz_i\bz_i')^{-1} \E(\bz_i\bx_i') \\
\blambda = \E(\bz_i\bz_i')^{-1} \E(\bz_iy_i) .
\end{split}\label{eq:reduced-coef}
\end{equation}
$$

These are uniquely determined by the probability distribution of $(y_i, \bx_i, \bz_i).$

We are interested in the structural parameter $\bbeta.$ It relates to $(\blambda, \Gamma)$ through

$$
\begin{align}
\blambda = \Gamma\bbeta .
\label{eq:lambda}
\end{align}
$$

$\bbeta$ is identified if it is uniquely determined by this relation. This is a set of $\ell$ equations with $K$ unknowns with $\ell\geq K.$ There is a unique solution *if and only if* $\Gamma$ has full rank $K:$

$$
\begin{align}
\rank{(\Gamma)} = K.
\label{eq:full-rank1}
\end{align}
$$

Under $\eqref{eq:full-rank1},$ $\bbeta$ can be uniquely solved fromThe linear system $\blambda = \Gamma\bbeta.$

On the other hand, if $\rank{(\Gamma)} < K$ then $\blambda = \Gamma\bbeta$ has fewer mutually independent linear equations than coefficients so there is not a unique solution. 

Plugging $\eqref{eq:reduced-coef}$ into $\eqref{eq:lambda}$ we have

$$
\E(\bz_iy_i) = \E(\bz_i\bx_i') \bbeta
$$

which is again a set of $\ell$ equations with $K$ unknowns. This has a unique solution *if and only if*

$$
\begin{align}
\rank{\left( \E(\bz_i\bx_i') \right)} = K .
\label{eq:full-rank2}
\end{align}
$$

$\eqref{eq:full-rank1}$ and $\eqref{eq:full-rank2}$ are equivalent ways of expressing the same requirement.

Two scenarios for the solution $\bbeta:$

- Just identification $\ell = K$

    $\ell = K$ implies $\Gamma$ is invertible, so the structural parameter equals 
    
    $$
    \begin{split}
    \bbeta &= \Gamma^{-1}\blambda \\
    &=  \E(\bz_i\bx_i')^{-1} \E(\bz_iy_i).
    \end{split}
    $$

    This solution assumes that the matrix $\bZ'\bX$ is invertible, which holds under the relevance condition.

    The **instrumental variables** (IV) estimator $\hat{\bbeta}_{\mathrm{iv}}$ replaces the population moments by their sample versions. That is

    $$
    \begin{equation}
    \begin{split}
    \hat{\bbeta}_{\mathrm{iv}} 
    &= \underbrace{\left[(\bZ'\bZ)^{-1}(\bZ'\bX)\right]^{-1}}_{\Gamma^{-1}} \; \underbrace{(\bZ'\bZ)^{-1}(\bZ'\by)}_{\blambda} \\
    &= (\bZ'\bX)^{-1}(\bZ'\bZ)(\bZ'\bZ)^{-1}(\bZ'\by) \\
    &= (\bZ'\bX)^{-1}(\bZ'\by).
    \end{split} \label{eq:IV-beta}
    \end{equation}
    $$

    More generally, it is common to refer to any estimator of the form 

    $$
    \color{#008B45} \hat{\bbeta}_{\mathrm{iv}} = (\bW'\bX)^{-1} (\bW'\by)
    $$

    given an $n\times K$ matrix $\bW$ as an IV estimator for $\bbeta$ using the instrument $\bW.$

- Over identification $\ell > K$

    We can solve for $\bbeta$ by applying least-squares to the system of equations $\blambda = \Gamma\bbeta.$ The least-squares solution is 

    $$
    \bbeta = (\Gamma'\Gamma)^{-1}\Gamma'\blambda .
    $$

    Under $\eqref{eq:full-rank1}$, the matrix $\Gamma'\Gamma$ is invertible so the solution is unique.


___

## Two-Stage Least Squares

Model set up

$$
\begin{equation}
\begin{split}
& \text{vector form}   & & \text{matrix form} \\
y_i &= \bx_i'\bbeta + e_i \qquad\quad  & \by &= \bX\bbeta + \be \\
\bx_i &= \Gamma'\bz_i + \bu_i \qquad\quad  & \bX &= \bZ\Gamma + \bU
\end{split}
\end{equation}
$$

Reformulate the model as 

$$
\begin{equation}
\begin{split}
y_i &= \bz_i'\Gamma \bbeta + v_i \\
\E(\bz_iv_i) &= \boldsymbol{0}.
\end{split} \label{eq:2sls1}
\end{equation}
$$

Define

$$
\begin{aligned}
\underbrace{\bw_i}_{K\times 1} &= \underbrace{\Gamma'}_{K\times \ell} \; \underbrace{\bz_i}_{\ell\times 1} \\
\underbrace{W}_{n\times K} &= \underbrace{\bZ}_{n\times \ell} \;\underbrace{\Gamma}_{\ell \times K}  \quad \text{(or in matrix form)}
\end{aligned}
$$

We can rewrite $\eqref{eq:2sls1}$ as

$$
\begin{equation}
\begin{split}
y_i &= \bw_i' \bbeta + v_i \\
\E(\bw_iv_i) &= \boldsymbol{0}.
\end{split} \label{eq:2sls}
\end{equation}
$$

Suppose that $\Gamma$ were known. Then we would estimate $\bbeta$ by least-squares of $y_i$ on $\bw_i$

$$
\begin{equation}
\begin{split}
\hat{\bbeta} &= (\bW'\bW)^{-1}(\bW'y) \\
&= (\Gamma'\bZ'\bZ\Gamma)^{-1} (\Gamma'\bZ'y) 
\end{split} \label{eq:2sls-beta}
\end{equation}
$$

While this is infeasible, we can estimate $\Gamma$ from the reduced form regression 

$$
\bX = \bZ\Gamma + \bU .
$$

The OLS estimate of $\Gamma$ is

$$
\widehat{\Gamma} = (\bZ'\bZ)^{-1} (\bZ'\bX)
$$

Replacing $\Gamma$ with $\widehat{\Gamma}$ in $\eqref{eq:2sls-beta}$, we obtain

$$
\begin{equation}
\begin{split}
\color{#008B45} \widehat{\bbeta}_{2\text{sls}} 
&= (\widehat{\Gamma}'\bZ'\bZ\widehat{\Gamma})^{-1} (\widehat{\Gamma}'\bZ'y) \\
&= \left[\bX'\bZ (\bZ'\bZ)^{-1} (\bZ'\bZ) (\bZ'\bZ)^{-1} \bZ'\bX \right]^{-1} \left[\bX'\bZ (\bZ'\bZ)^{-1} \bZ'\by \right] \\
&= \color{#008B45} \left[\bX'\bZ (\bZ'\bZ)^{-1} \bZ'\bX \right]^{-1} \left[\bX'\bZ (\bZ'\bZ)^{-1} \bZ'\by \right] .
\end{split} 
\end{equation}
$$

This is called the two-stage-least squares (2SLS) estimator. 

If the model is just-identified, so that $K=\ell,$ then 2SLS simplifies to the IV estimator in $\eqref{eq:IV-beta}.$

Since the matrices $\bX'\bZ$ and $\bZ'\bX$ are square, we can factor

$$
\left[\bX'\bZ (\bZ'\bZ)^{-1} \bZ'\bX \right]^{-1} 
= (\bZ'\bX)^{-1}(\bZ'\bZ)(\bX'\bZ)^{-1}.
$$

Then

$$
\begin{equation}
\begin{split}
\widehat{\bbeta}_{2\text{sls}} 
&= (\bZ'\bX)^{-1}(\bZ'\bZ)(\bX'\bZ)^{-1} \bX'\bZ (\bZ'\bZ)^{-1} \bZ'\by \\
&= (\bZ'\bX)^{-1} \bZ'\by \\
&= \widehat{\bbeta}_{\text{iv}} 
\end{split} 
\end{equation}
$$

as claimed. This shows that the 2SLS estimator is a generalization of the IV estimator.

**Alternative representation of the 2SLS estimator**

Define the projection matrix

$$
\bP_\bZ = \bZ(\bZ'\bZ)^{-1}\bZ'.
$$

We can write the 2SLS estimator more compactly as 

$$
\widehat{\bbeta}_{2\text{sls}} = (\bX'\bP_\bZ\bX)^{-1} \bX'\bP_\bZ \by . 
$$

Define the fitted values for $\bX$ from the reduced form

$$
\widehat{\bX} = \bP_\bZ\bX = \bZ \widehat{\Gamma} .
$$

Then the 2SLS estimator can be written as

$$
\begin{equation}
\begin{split}
\widehat{\bbeta}_{2\text{sls}} 
&= (\bX'\bP_\bZ\bX)^{-1} \bX'\bP_\bZ \by \\
&= (\bX'\bP_\bZ'\bP_\bZ\bX)^{-1} \bX'\bP_\bZ' \by  \quad \text{($\bP_\bZ$ is symmetric and idempotent)} \\
&= (\widehat{\bX}'\widehat{\bX})^{-1}\widehat{\bX}'\by
\end{split} 
\end{equation}
$$

which is the least-squares estimator obtained by regressing $\by$ on the fitted values $\widehat{\bX}.$

This is the source of the "two-stage" name since it can be computed as follows.

1. Regress $\bX$ on $\bZ$, get

    $$
    \begin{aligned}
    \widehat{\Gamma} = (\bZ'\bZ)^{-1} (\bZ'\bX)
    \end{aligned}
    $$

    and the fitted values

    $$
    \widehat{\bX} = \bZ\widehat{\Gamma} = \bP_\bZ\bX .
    $$

2. Regress $\by$ on $\widehat{\bX}$

    $$
    \widehat{\bbeta}_{2\text{sls}} = (\widehat{\bX}'\widehat{\bX})^{-1}\widehat{\bX}'\by .
    $$