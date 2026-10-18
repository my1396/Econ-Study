---
layout: post
title: Partitioned Regression
tag: study
update: 2023-12-07
---

## Frisch-Waugh-Lovell Theorem

Let the regressors be partitioned as

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
\begin{align} 
y &= \bX \bbeta + u \notag \\
&= \bX_1\bbeta_1 + \bX_2\bbeta_2 + u \\ \label{eq-partition}
E(\bX u) &= \symbf{0} \notag
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
For the following model partition
$$
\by = \bX_1\bbeta_1 + \bX_2\bbeta_2 + \bu .
$$
the OLS estimator of $\bbeta_2$ and the OLS residuals $
\hat{\bu}$ may be computed via the following algorithm:
<ol>
<li>Regress $\by$ on $\bX_1,$ obtain the residuals $\widetilde{\bu}_1$; </li>
<li>Regress $\bX_2$ on $\bX_1,$ obtain the residuals $\widetilde{\bX}_2$; </li>
<li>Regress $\widetilde{\bu}_1$ on $\widetilde{\bX}_2$, obtain the OLS estimates $\bbeta_2$ and residuals $\hat{\bu}$. </li>
</ol>
</div>

--------------------------------------------------------------------------------

## Omitted Variable Bias

If $\bX_2$ is not observed, then the regression model becomes
$$
y = \bX_1\bgamma_1 + v
$$
where $v = \bX_2\bbeta_2 + u$ is the new error term. The OLS estimator of $\bgamma_1$ is
$$
\begin{split}
\bgamma_1 &= \left(E(\bX_1\bX_1)\right)^{-1}E(\bX_1y) \\
&= \left(E(\bX_1\bX_1)\right)^{-1}E(\bX_1(\bX_1\bbeta_1 + \bX_2\bbeta_2 + u)) \\
&= \bbeta_1 + \left(E(\bX_1\bX_1)\right)^{-1}E(\bX_1\bX_2)\bbeta_2 + \left(E(\bX_1\bX_1)\right)^{-1}E(\bX_1 u) \\
&= \bbeta_1 + \left(E(\bX_1\bX_1)\right)^{-1}E(\bX_1\bX_2)\bbeta_2 \quad (E(\bX_1 u) = 0) \\
&= \bbeta_1 + \bGamma_{12}\bbeta_2
\end{split}
$$
where 
$$
\begin{split}
\bGamma_{12} &= \left(E(\bX_1\bX_1)\right)^{-1}E(\bX_1\bX_2) \\
&= Q^{-1}_{11} Q_{12}
\end{split}
$$
is the coefficient matrix from a projection of $\bX_2$ on $\bX_1.$ 

Observe that $\bGamma_1 = \bbeta_1 + \bGamma_{12}\bbeta_2 \ne \bbeta_1$ unless $\bGamma_{12} = 0$ or $\bbeta_2 = 0.$ 

- $\bGamma_{12} = 0$ means that $\bX_1$ and $\bX_2$ are uncorrelated
- $\bbeta_2 = 0$ means that $\bX_2$ has no effect on $y.$

If one of these two conditions is satisfied, then the omitted variable bias is zero, that is, omitting $\bX_2$ from the regression has no effect on the OLS estimator of $\bbeta_1.$ 


For example, suppose $y$ is log wages, $X_1$ is education, and $X_2$ is intellectual ability. It seems reasonable to suppose that education and intellectual ability are positively correlated highly able individuals attain higher levels of education) which means $\bGamma_{12} > 0$. It also seems reasonable to suppose that conditional on education, individuals with higher intelligence will earn higher wages on average, so that $\beta_2 > 0.$
This implies that $\bGamma_{12}\beta_2 > 0$ and $\Gamma_1 = \beta_1 + \bGamma_{12}\beta_2 > \beta_1$. Therefore, it seems reasonable to expect that in a regression of wages on education with ability omitted, the coefficient on education is higher than in a regression where ability is included. 
In other words, in this context the omitted variable biases the regression coefficient upwards. 
It is possible, for example, that $\beta_1 = 0$ so that education has no direct effect on wages yet $\gamma_1 = \bGamma_{12}\beta_2 > 0$ meaning that the regression coefficient on education alone is positive, but is a consequence of the unmodeled correlation between education and intellectual ability.




