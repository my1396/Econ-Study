---
layout: post
title: Characteristic Roots and Vectors
tag: study
update: 2025-06-19
---


For a $K\times K$ square matrix $\bA$, given the set of equations

$$
\begin{equation}\label{eq-characteristic}
\bA \bc = \lambda \bc .
\end{equation} 
$$

The solutions of the equation give the characteristic vectors, $\bc,$ and characteristic roots, $\lambda.$ 

If $\bc$ is any solution vector, then $k\bc$ is also for any value of $k.$
To remove indeterminancy, $\bc$ is **normalized** so that $\bc'\bc=1.$


To solve $\eqref{eq-characteristic}$

$$
\begin{split}
\bA \bc &= \lambda \bI \bc  \\
(\bA-\lambda \bI)\bc &= 0
\end{split}
$$

The equation has a nonzero equation only if the matrix $(\bA-\lambda \bI)$ has a zero determinant (or *singular*).

Therefore, if $\lambda$ is a solution, then

$$
\begin{equation}\label{eq-ploynomial}
\vert \bA-\lambda \bI \vert = 0.
\end{equation} 
$$

Eq. $\eqref{eq-ploynomial}$ is called as the characteristic equation of $\bA$, which gives a polynomial in $\lambda.$ 

___

General Results for Characteristic Roots and Vectors

A $K\times K$ **symmetric** matrix $\bA$ has $K$ distinct characteristic vectors, $\bc_1,$ $\bc_2,$ $\ldots,$ $\bc_K.$ 

- The characteristic vectors of a symmetric matrix are orthogonal.

$$
\bc_i'\bc_j' = 0 \text{ for } i \ne j.
$$

The corresponding characteristic roots, $\lambda_1,$ $\lambda_2,$ $\ldots,$ $\lambda_K,$ although real, need NOT be distinct.


Collect the $K$ characteristic vectors in a $K\times K$ matrix whose $j$th column is the $\bc_j$ corresponding to $\lambda_j,$

$$
\bC = \begin{bmatrix} 
\bc_1 & \bc_2 & \ldots & \bc_K
\end{bmatrix},
$$

and the $K$ characteristic roots in the same order, in a diagonal matrix,

$$
\bLambda = 
\begin{bmatrix}
\lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_k
\end{bmatrix}.
$$

Then the full set of equations

$$
\bA \bc_k = \lambda_k \bc_k
$$

is contained in

$$
\begin{equation}
\bA \bC = \bC\bLambda .
\end{equation}
$$


Since the vectors are orthogonal and $\bc_i'\bc=1,$ we have

$$
\bC' \bC = \begin{bmatrix}
\bc_1'\bc_1 & \bc_1'\bc_2 & \cdots & \bc_1'\bc_K \\
\bc_1'\bc_2 & \bc_2'\bc_2 & \cdots & \bc_2'\bc_K \\
\vdots & \vdots & \ddots & \vdots \\
\bc_1'\bc_K & \bc_2'\bc_K & \cdots & \bc_K'\bc_K
\end{bmatrix} = \bI.
$$

Hence 

$$
\bC'= \bC^{-1} .
$$

Consequently

$$
\bC \bC' = \bC \bC^{-1} = \bI ,
$$

so the ros as well as the columns of $\bC$ are orthogonal.

___


Diagonalization of a Matrix

$$
\bC'\bA\bC = \bC'\bC \bLambda = \bI\bLambda = \bLambda
$$

Spectral Decomposition of a Matrix

$$
\bA = \bC \bLambda \bC' = \sum_{k=1}^K \lambda_k \bc_k\bc_k'
$$


___

**References**

-  *Appendix A*, pp 825–826, **Econometric Analysis** , 5th Edition, by William H. Greene, Prentice Hall, 2003. 