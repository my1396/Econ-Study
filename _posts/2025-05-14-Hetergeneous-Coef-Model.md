---
layout: post
title: Models with Heterogeneous Slopes
tag: study
update: 2025-05-14
---

## Models with Homogeneous Slopes

We start with the "standard" linear models considered in such courses often assume homogeneity in individual responses to covariates. A common cross-sectional specification is:

$$
\begin{equation}\label{eq-standard_linear}
y_i = \bbeta'\bx_i + u_{i},
\end{equation}
$$
where $i=1, \dots, N$ indexes cross-sectional units. 

In panel data, models often include unit-specific $(i)$ and time-specific $(t)$ intercepts while maintaining a common slope vector $\bbeta$:

$$
\begin{equation}\label{eq-panel_linear} 
y_{it} = \alpha_i + \delta_t +  \bbeta'\bx_{it} + u_{it}.
\end{equation}
$$

## Models with Heterogeneous Slopes

Modern economic theory rarely supports the assumption of homogeneous slopes $\boldsymbol{\beta}$. Theoretical models recognize that observationally identical individuals, firms, and countries can respond differently to the same stimulus. In a linear model, this requires us to consider more flexible models with heterogeneous coefficients: 


1. Cross-sectional model ($\ref{eq-standard_linear}$) generalizes to 

   $$
   \begin{equation}\label{eq-cross_sectional_hetero}
y_i = \boldsymbol{\beta}_{i}'\boldsymbol{x} + u_i.
   \end{equation}
   $$

2. Panel data model (\ref{eq-panel_linear}) generalizes to 

   $$
   \begin{equation}\label{eq-panel_hetero}
   y_{it}  = \boldsymbol{\beta}_{it}'\boldsymbol{x}_{it} + u_{it},
   \end{equation}
   $$

   or assuming time-invariant coefficients

   $$
    \begin{equation}\label{eq-time_invariant}
   \color{red} y_{it}  = \boldsymbol{\beta}_{i}'\boldsymbol{x}_{it} + u_{it}.
   \end{equation}
   $$

For identification purposes, we will generally focus on the case where the number $N$ of units is large, while the number $T$ of observations per unit is fixed and not necessarily large.


Note that model (\ref{eq-time_invariant}) includes a particular special case — the random intercept model (confusingly also called the "fixed effects model"). 

> In the panel data literature, approaches that **do not restrict the dependence between the unobserved and the observed components** are called "fixed effects". 

The random intercept model imposes homogeneity on all parameters except the intercept term. In the one-way case, the model takes the form: 

$$
\begin{equation}\label{eq-random_intercept}
y_{it} = \alpha_i + \bbeta'\bx_{it} + u_{it}.
\end{equation}
$$

Model (\ref{eq-random_intercept}) is one of the oldest ways of including unobserved heterogeneity in linear models and goes back at least to {% cite Mundlak1961EmpiricalProductionFunction %}.



---
**References**:

- <https://vladislav-morozov.github.io/econometrics-heterogeneity/linear/linear-introduction.html>
- <https://github.com/vladislav-morozov/econometrics-heterogeneity/blob/fix/linear/src/linear/linear-introduction.qmd>

{% bibliography --cited %}