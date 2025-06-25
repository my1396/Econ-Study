---
layout: post
title: Linear Algebra
tag: study
update: 2024-10-27
---

<a class="top-link hide" href="#" id="js-top">↑</a>

## Identity Matrix

**Identity/unit matrix** $I$: A diagonal matrix with all its diagonal elements equal to 1, and 0 everywhere else. A subscript indicates the size of the identify matrix, e.g., 

$$
I_2 = \begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
$$


If $A$ is an $m\times n$ matrix, then

$$
I_mA = AI_n = A
$$

This shows that as long as the size of the matrix is considered, multiplying by the identity is like multiplying by 1 with numbers.

**Examples**

左乘 $I_mA=A$

$$
\begin{bmatrix}
\color{red}1 & \color{red}0 \\
\color{blue}0 & \color{blue}1
\end{bmatrix}
\begin{bmatrix}
1 & 2 & 3 & 4 \\
5 & 6 & 7 & 8
\end{bmatrix} 
= \begin{bmatrix}
\color{red}1 & \color{red}2 & \color{red}3 & \color{red}4 \\
\color{blue}5 & \color{blue}6 & \color{blue}7 & \color{blue}8
\end{bmatrix}
$$

右乘 $AI_n=A$

$$
\begin{bmatrix}
1 & 2 & 3 & 4 \\
5 & 6 & 7 & 8
\end{bmatrix}
\begin{bmatrix}
\color{red}1 & \color{blue}0 & \color{#008B45}0 & \color{purple}0 \\
\color{red}0 & \color{blue}1 & \color{#008B45}0 & \color{purple}0 \\
\color{red}0 & \color{blue}0 & \color{#008B45}1 & \color{purple}0 \\
\color{red}0 & \color{blue}0 & \color{#008B45}0 & \color{purple}1 \\
\end{bmatrix} 
= \begin{bmatrix}
\color{red}1 & \color{blue}2 & \color{#008B45}3 & \color{purple}4 \\
\color{red}5 & \color{blue}6 & \color{#008B45}7 & \color{purple}8
\end{bmatrix}
$$

___

## Vector of Ones

$\bi$ is often used to denote a **column of ones**. Then

- $\bi'\bi = n$
- $\bi'\bx = \sum_{i=1}^n x_i $
- $\frac{1}{n} \bi'\bx = \bar{x}$
- $\bi\bi'$ is a $n\times n$ matrix of ones.
  
    Let $n=3$

    $$
    \bi\bi' = \begin{bmatrix}
    1 \\
    1 \\ 
    1
    \end{bmatrix}  
     \begin{bmatrix}
    1 & 1 & 1
    \end{bmatrix}  
    = \begin{bmatrix}
    1 & 1 & 1 \\
    1 & 1 & 1 \\ 
    1 & 1 & 1
    \end{bmatrix}  
    $$

    Postmultiplying $\bi'\bi$ by a vector $\bx$ gives the sum of the elements in the vector. 

    $$
    \bi'\bi \bx = \begin{bmatrix}
    1 & 1 & 1 \\
    1 & 1 & 1 \\ 
    1 & 1 & 1
    \end{bmatrix} \begin{bmatrix}
    x_1 \\
    x_2 \\ 
    x_3
    \end{bmatrix} =  \begin{bmatrix}
    \sum_{i=1}^3x_i \\
    \sum_{i=1}^3x_i \\ 
    \sum_{i=1}^3x_i
    \end{bmatrix}
    $$


$(\bI - \frac{1}{n}\bi\bi')\bX$ transforms a matrix $\bX$ to deviations from its column mean. Using one column vector $\bx$ as an example. First,

$$
\bi\bar{x} = \bi \frac{1}{n}\bi'\bx = 
\begin{bmatrix}
\bar{x} \\
\bar{x} \\
\vdots \\
\bar{x}
\end{bmatrix} 
= \color{#008B45} \frac{1}{n} \bi\bi'x
$$

The matrix $1/n\bi\bi'$ is an $n\times n$ matrix with every element equal to $1/n.$
The set of values in deviations form is 

$$
\begin{bmatrix}
x_1 - \bar{x} \\
x_2 - \bar{x} \\
\vdots \\
x_n - \bar{x}
\end{bmatrix}  
= [\bx - \bi\bar{x}]
= \begin{bmatrix}
\bx - \frac{1}{n}\bi\bi'\bx 
\end{bmatrix} 
= \begin{bmatrix}
\color{#008B45} \bI - \frac{1}{n}\bi\bi'  
\end{bmatrix} \bx
$$

$\mathbf{1}_n$ is also used to denote a $n\times 1$ vector of ones. But $\mathbf{1}_n$ can seem similar to $\mathbf{I}_n$ (identity matrix), which causes confusion. One difference is that the identity matrix is italic, but the matrix of one is upright.

___

## Differencing Matrix

A **differencing matrix** (also called a **difference operator matrix**) is a matrix that, when multiplied by a vector, computes the differences between successive elements of that vector.

For a time series vector $ \by = [y_1, y_2, \dots, y_n]' $, the **first-order differencing matrix** $ D $ produces $ \Delta \by = D\by $, where:

$$
\Delta y_t = y_t - y_{t-1}
$$

The first-order differencing matrix should be  $ (n-1) \times n .$ 

For $ n = 4 $:

$$
D = 
\begin{bmatrix}
1 & -1 & 0 & 0 \\
0 & 1 & -1 & 0 \\
0 & 0 & 1 & -1
\end{bmatrix}
$$

So if 

$$
\by = 
\begin{bmatrix}
y_1 \\
y_2 \\
y_3 \\
y_4
\end{bmatrix}
$$

then

$$
D\by = \begin{bmatrix}
1 & -1 & 0 & 0 \\
0 & 1 & -1 & 0 \\
0 & 0 & 1 & -1
\end{bmatrix} \begin{bmatrix}
y_1 \\
y_2 \\
y_3 \\
y_4
\end{bmatrix}
= \begin{bmatrix}
y_2 - y_1 \\
y_3 - y_2 \\
y_4 - y_3
\end{bmatrix} .
$$



___

## Diagonal Matrix

对角线

╲  Major, Principal, Primary, Main; diagonal ╲

╱ Minor, Counter, Secondary, Anti-; diagonal ╱


Define a **diagonal matrix** $A=\diag{(a_1, a_2, \ldots, a_n)}$, then

- Postmultiply by a vector

$$
\begin{bmatrix}
a_1 & & & & \\
& \ddots & & & \\
& & a_i & & \\ 
& & & \ddots & \\
& & & & a_n\\
\end{bmatrix}
\begin{bmatrix}
\color{red}{x_1}  \\
\vdots \\
\color{blue}{x_i} \\ 
\vdots \\
\color{#008B45}{x_n} \\ 
\end{bmatrix}
= {\color{red}x_1} \begin{bmatrix}
a_1  \\
 \\
 \\ 
 \\
 \\ 
\end{bmatrix} 
+ \cdots 
+ {\color{blue}x_i} \begin{bmatrix}
  \\
 \\
a_i  \\ 
 \\
 \\ 
\end{bmatrix} 
+ \cdots 
+ {\color{#008B45}x_n} \begin{bmatrix}
  \\
 \\
  \\ 
 \\
a_n \\ 
\end{bmatrix} 
$$


- Product of diagonal matrices

    $$
    \begin{bmatrix}
    a_1 & & & & \\
    & \ddots & & & \\
    & & a_i & & \\ 
    & & & \ddots & \\
    & & & & a_n\\
    \end{bmatrix}
    \begin{bmatrix}
    b_1 & & & & \\
    & \ddots & & & \\
    & & b_i & & \\ 
    & & & \ddots & \\
    & & & & b_n\\
    \end{bmatrix}
    = \begin{bmatrix}
    a_1b_1 & & & & \\
    & \ddots & & & \\
    & & a_ib_i & & \\ 
    & & & \ddots & \\
    & & & & a_nb_n\\
    \end{bmatrix}
    $$

- Inverse of a diagonal matrix

    $$
    \begin{bmatrix}
    a_1 & & & & \\
    & \ddots & & & \\
    & & a_i & & \\ 
    & & & \ddots & \\
    & & & & a_n\\
    \end{bmatrix}^{-1}
    = \begin{bmatrix}
    a_1^{-1} & & & & \\
    & \ddots & & & \\
    & & a_i^{-1} & & \\ 
    & & & \ddots & \\
    & & & & a_n^{-1}\\
    \end{bmatrix}
    $$

    Note that $A$ is invertible if and only if all diagonal entries are nonzero.

___

## Matrix Multiplication

**Postmultiply a column vector**

Define $A$ as a $m\times n$ matrix, $\bb$ as a $n\times 1$ column vector, then

$$
\begin{equation} \label{postmultiply-column}
\begin{split}
A\bb &= \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn} \\
\end{bmatrix} 
\begin{bmatrix}
{\color{red}b_1} \\
{\color{blue}b_2} \\
\vdots \\
{\color{#008B45}b_n} \\
\end{bmatrix} \\
&= {\color{red}b_1} \begin{bmatrix}
a_{11} \\
a_{21} \\
\vdots \\
a_{m1} \\
\end{bmatrix} 
+ {\color{blue}b_2} \begin{bmatrix}
a_{12} \\
a_{22} \\
\vdots \\
a_{m2} \\
\end{bmatrix} 
+ \cdots
+ {\color{#008B45}b_n} \begin{bmatrix}
a_{1n} \\
a_{2n} \\
\vdots \\
a_{mn} \\
\end{bmatrix} \\
&= [{\color{red}b_1}\ba_{\cdot 1}] + [{\color{blue}b_2}\ba_{\cdot 2}] + \cdots + [{\color{#008B45}b_n}\ba_{\cdot n}]
\end{split}
\end{equation}
$$

That is, postmultiplying a column vector to a matrix is like a linear combination of <span style='color:#337ab7'>**columns**</span> of the matrix.

Note that in linear regression, we often encounter the following form:

$$
\by = \bX \bbeta
$$

where $\by\in \R^n$ is the dependent variable, $\bX\in \R^{n\times K}$ is the independent variable, and $\bbeta\in \R^K$ is the coefficient vector. One way to think about this equation is that $\bX$ represents a system of $n$ linear equations, each with $K$ variables, and $\bbeta$ represents a solution to this system.

___

**Premultiply a row vector**

Define $\ba$ as a $1\times n$ row vector, $B$ as a a $n\times p$ matrix, then

$$
\begin{equation}\label{premultiply-row}
\begin{split}
\ba B &= \begin{bmatrix}
\color{red}a_1 & \color{blue}a_2 & \cdots & \color{#008B45}a_n
\end{bmatrix} 
\begin{bmatrix}
b_{11} & b_{12} & \cdots & b_{1p} \\
b_{21} & b_{22} & \cdots & b_{2p} \\
\vdots & \vdots & \ddots & \vdots \\
b_{n1} & b_{n2} & \cdots & b_{np} \\
\end{bmatrix} \\
&= {\color{red}a_1} \begin{bmatrix}
b_{11} & b_{12} & \cdots & b_{1p}
\end{bmatrix} 
+ {\color{blue}a_2} \begin{bmatrix}
b_{21} & b_{22} & \cdots & b_{2p}
\end{bmatrix}  
+ \cdots \\
&\phantom{=} \quad
+ {\color{#008B45}a_n} \begin{bmatrix}
b_{n1} & b_{n2} & \cdots & b_{np} 
\end{bmatrix} \\
&= [{\color{red}a_1}\bb_{1\cdot}] + [{\color{blue}a_2}\bb_{2\cdot}] + \cdots + [{\color{#008B45}a_n}\bb_{n\cdot}]
\end{split}
\end{equation}
$$

That is, premultiplying a row vector to a matrix is like a linear combination of <span style='color:#337ab7'>**rows**</span> of the matrix.

___

Define $A$ as a $m\times n$ matrix, $B$ as a $n\times p$ matrix, then

- If writing $B$ in terms of columns vectors

    $$
    AB = A \begin{bmatrix}
    \color{red}\bb_{\cdot 1} & \color{blue}\bb_{\cdot 2} & \cdots & \color{#008B45}\bb_{\cdot p}
    \end{bmatrix} 
    = \begin{bmatrix}
    \color{red}A\bb_{\cdot 1} & \color{blue}A\bb_{\cdot 2} & \cdots & \color{#008B45}A\bb_{\cdot p}
    \end{bmatrix}_{m\times p} ,
    $$

    where $\bb_{\cdot j}$ is the $j$-th columns of $B:$ 

    $$
    \bb_{\cdot j} = \begin{bmatrix}
    b_{1j} \\
    b_{2j} \\
    \vdots \\
    b_{nj} \\
    \end{bmatrix} \text{ for } j = 1, 2, \ldots, p
    $$

    Refer to $\eqref{postmultiply-column}$ for $A\bb_{\cdot j}.$

    Expanding $\bb_{\cdot j}$

    $$
    \begin{split}
    AB &= \begin{bmatrix}
    a_{\cdot 1} & a_{\cdot 2} & \cdots & a_{\cdot n}
    \end{bmatrix}
    \begin{bmatrix}
    \color{red}b_{11} & \color{blue}b_{12} & \cdots & \color{#008B45}b_{1p} \\
    \color{red}b_{21} & \color{blue}b_{22} & \cdots & \color{#008B45}b_{2p} \\
    \vdots & \vdots & \ddots & \vdots \\
    \color{red}b_{n1} & \color{blue}b_{n2} & \cdots & \color{#008B45}b_{np} \\
    \end{bmatrix} \\
    &= \begin{bmatrix}
    \color{red}b_{11}a_{\cdot 1} + b_{21}a_{\cdot 2} + \cdots + b_{n1}a_{\cdot n} & 
    \color{blue}b_{12}a_{\cdot 1} + b_{22}a_{\cdot 2} + \cdots + b_{n2}a_{\cdot n} &
    \color{#008B45}b_{1p}a_{\cdot 1} + b_{2p}a_{\cdot 2} + \cdots + b_{np}a_{\cdot n}
    \end{bmatrix}
    \end{split}
    $$

    Each column in $AB$ is a linear combination of columns in $A.$

- Alternatively, writing $A$ in terms of row vectors

    $$
    AB = \begin{bmatrix}
    \color{red}\ba_{1\cdot} \\
    \color{blue}\ba_{2\cdot} \\
    \vdots \\
    \color{#008B45}\ba_{m\cdot} \\
    \end{bmatrix} B
    = \begin{bmatrix}
    {\color{red}\ba_{1\cdot}}B \\
    {\color{blue}\ba_{2\cdot}}B \\
    \vdots \\
    {\color{#008B45}\ba_{m\cdot}}B \\
    \end{bmatrix}
    $$

    where $\ba_{i\cdot}$ is the $i$-th row of $A:$

    $$
    \ba_{i\cdot} = 
    \begin{bmatrix}
    a_{i1} & a_{i2} & \cdots & a_{in}
    \end{bmatrix} \text{ for } i = 1, 2, \ldots, m.
    $$

    Expanding $\ba_{i\cdot}$

    $$
    AB = \begin{bmatrix}
    \color{red}a_{11} & \color{red}a_{12} & \cdots & \color{red}a_{1n} \\
    \color{blue}a_{21} & \color{blue}a_{22} & \cdots & \color{blue}a_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    \color{#008B45}a_{m1} & \color{#008B45}a_{m2} & \cdots & \color{#008B45}a_{mn} \\
    \end{bmatrix} 
    \begin{bmatrix}
    \bb_{1\cdot} \\
    \bb_{2\cdot} \\
    \vdots \\
    \bb_{n\cdot} \\
    \end{bmatrix} 
    = \begin{bmatrix}
    \color{red}a_{11}\bb_{1\cdot} + a_{12}\bb_{2\cdot} + \cdots + a_{1n}\bb_{n\cdot} \\
    \color{blue}a_{21}\bb_{1\cdot} + a_{22}\bb_{2\cdot} + \cdots + a_{2n}\bb_{n\cdot} \\
    \vdots \\
    \color{#008B45}a_{m1}\bb_{1\cdot} + a_{m2}\bb_{2\cdot} + \cdots + a_{mn}\bb_{n\cdot} \\
    \end{bmatrix} 
    $$

    Each row in $AB$ is a linear combination of rows in $B.$
    


___

**Matrix by Matrix Multiplication**

Let  $A$  be an  $m\times n$  matrix and let  $B$  be an  $n\times p$  matrix of the column-form

$$
B = \begin{bmatrix} b_{1} & \cdots & b_{p} \end{bmatrix}
$$

Then the  $m\times p$  matrix  $AB$  is defined as follows:

$$
AB = A \begin{bmatrix} b_{1} & \cdots & b_{p} \end{bmatrix} 
= \begin{bmatrix} Ab_{1} & \cdots & Ab_{p} \end{bmatrix}
$$

where $Ab_{j}$ is the $j$-th column of $AB$.

Writing $A$ in a **row vector** form

$$
AB = \begin{bmatrix} a_{1} & \cdots & a_{n} \end{bmatrix}
\begin{bmatrix} b_{1} \\ \vdots  \\ b_{n} \end{bmatrix} 
= [a_1b_1 + a_2b_2 + \cdots + a_nb_n]
$$

Writing $A$ in a **column vector** form

$$
AB = \begin{bmatrix} a_{1} \\ \vdots  \\ a_{m} \end{bmatrix} B
= \begin{bmatrix} a_{1}B \\ \vdots  \\ a_{m}B \end{bmatrix} 
$$

General rules for matrix multiplication:

- Associative law: $(AB)C = A(BC)$
- Distributive law: $A(B+C) = AB + BC$
- Transpose of a product: $(AB)' = B'A'$
- Transpose of an extended product: $(ABC)' = C'B'A'$ 
- Matrix multiplication is NOT commutative: $AB \ne BA$

___

## Useful Notations

Let $\bX$ be a $n\times K$ matrix

$$
\bX = \begin{pmatrix}
\bx_1\color{red}^\prime\\
\bx_2\color{red}^\prime\\
\vdots \\
\bx_n\color{red}^\prime\\ 
\end{pmatrix}
= \begin{pmatrix}
x_{11} & x_{12} &  \cdots & x_{1K} \\
x_{21} & x_{22} & \cdots & x_{2K} \\
\vdots & \vdots & \ddots & \vdots \\
x_{n1} & x_{n2} & \cdots & x_{nK} 
\end{pmatrix}_{n\times K},
$$

where

$$
\boldsymbol{x}_i = \begin{pmatrix}
x_{i1} \\
x_{i2} \\
\vdots \\
x_{iK}
\end{pmatrix}_{K\times 1} .
$$

Then 

$$
\bX' = \begin{pmatrix}
\bx_1 & \bx_2 & \cdots & \bx_n
\end{pmatrix}
$$

and 

$$
\begin{split}
\bX'\bX 
&= \begin{pmatrix}
\bx_1 & \bx_2 & \cdots & \bx_n
\end{pmatrix}
\begin{pmatrix}
\bx_1'\\
\bx_2'\\
\vdots \\
\bx_n'\\ 
\end{pmatrix}  \\
&= \sum_{i=1}^n \bx_{i} \bx_{i}'
\end{split}
$$


Define $\bZ$ as a $n\times L$ matrix, $\bX$ as a $n\times K$ matrix, then

- $\bZ'\bX$ is a $L\times K$ matrix

$$
\bZ'\bX = \begin{pmatrix}
\bz_1 & \bz_2 & \cdots & \bz_n
\end{pmatrix} 
\begin{pmatrix}
\bx_1'\\
\bx_2'\\
\vdots \\
\bx_n'\\ 
\end{pmatrix}
= \sum_{i=1}^n \bz_{i} \bx_{i}'
$$

- $\bX'\bZ$ is a $K\times L$ matrix 

$$
\bX'\bZ = \begin{pmatrix}
\bx_1 & \bx_2 & \cdots & \bx_n
\end{pmatrix}
\begin{pmatrix}
\bz_1'\\
\bz_2'\\
\vdots \\
\bz_n'\\ 
\end{pmatrix}
= \sum_{i=1}^n \bx_{i} \bz_{i}'
$$


___

## Inverse

$A^{-1} = \frac{1}{\vert A \vert} \text{Adj}(A)$ where $\text{Adj}(A)$ is the adjoint matrix. The inverse of matrix $A$ can be computed by dividing the adjoint of a matrix by the determinant of the matrix.  </br>

Steps to find the inverse of $A$:

<ol>
<li> Calculate the matrix of minors $M$. <br/>
  The minor is defined for every element of a matrix. The minor of a particular element is the determinant, denoted as $M_{ij}$, obtained after eliminating the $i$-th row and $j$-th column. For instance
  $$
  A = \begin{bmatrix} 
  a_{11}  & a_{12}  & a_{13} \\
  a_{21}  & a_{22}  & a_{23} \\
  a_{31}  & a_{32}  & a_{33} \\
  \end{bmatrix}
  $$
  The minor of the element $a_{11}$, i.e., $M_{11}$, is:

$$
  \text{Minor of }a_{11} = 
  \begin{vmatrix} 
  a_{22}  & a_{23} \\
  a_{32}  & a_{33} \\
  \end{vmatrix}
$$
</li>
<li> Add the sign $(-1)^{i+j}$ to minors, then you get a cofactor matrix $C_{ij} = (-1)^{i+j}M_{ij}$. </li>
<li> Take the transpose of the cofactor matrix, then you get the adjoint matrix. $\text{Adj}(A)=C^T$ </li>
<li> Divide the $\text{Adj}(A)$ by the determinant.</li>
</ol>

**Properties of inverse**: 

- $(A^T)^{-1} = (A^{-1})^T$ Transpose of inverse equal to inverse of transpose.

- $(ABC)^{-1}=C^{-1}B^{-1}A^{-1}$ The inverse of a product is the product of the inverse in the *opposite* order. This holds only on the condition that all matrices are invertible.

- If $A$ is symmetric, then $A^{-1}$ is symmetric. The inverse of a symmetric matrix is still symmetric.



**Inverse of a 2$\times$2 matrix**

$$
\begin{aligned}
A &= \begin{bmatrix}
a & b \\
c & d
\end{bmatrix} \\
A^{-1} &= \frac{1}{ad-bc}  \begin{bmatrix}
d & -b \\
-c & a
\end{bmatrix}
\end{aligned}
$$

___

## Kronecker Product

If $\bA$ is an $m \times n$ matrix and $\bB$ is a $p \times q$ matrix, then the Kronecker product $A \otimes B$ is the $pm \times qn$ block matrix:

$$
A \otimes B = \begin{bmatrix}
a_{11}B & a_{12}B & \cdots & a_{1n}B \\
a_{21}B & a_{22}B & \cdots & a_{2n}B \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1}B & a_{m2}B & \cdots & a_{mn}B \\
\end{bmatrix}
$$

where

$$
a_{11}B = \begin{bmatrix}
a_{11}b_{11} & a_{11}b_{12} & \cdots & a_{11}b_{1q} \\ 
a_{11}b_{21} & a_{11}b_{22} & \cdots & a_{11}b_{2q} \\ 
\vdots & \vdots & \ddots & \vdots \\
a_{11}b_{p1} & a_{11}b_{p2} & \cdots & a_{11}b_{pq} \\ 
\end{bmatrix}
$$

In other words, the Kronecker product $A\otimes B$ is a block matrix whose $(i,j)$-th block is equal to the $(i,j)$-th entry of $A$ multiplied by the matrix $B.$

Note that, unlike the ordinary product between two matrices, the Kronecker product is defined *regardless of the dimensions* of the two matrices  $A$ and  $B$.

Example: Let $\bI$ be the $2\times 2$ identity matrix and $B$ be any matrix. Then their Kronecker product is the block matrix

$$
\bI \otimes B = \begin{bmatrix}
B & 0 \\
0 & B
\end{bmatrix}
$$

Example: Let $a$ be a scalar and $B$ be any matrix. Then their Kronecker product is the same as multiplying $B$ by the scalar:

$$
a \otimes B = aB
$$


Kronecker products satisfy the **distributive rule**

$$
(A\otimes B)(C\otimes S) = AC \otimes BD,
$$

assuming all matrix products are well defined.

**Inverses** of Kronecker products:

$$
(A\otimes B)^{-1} = A^{-1} B^{-1} ,
$$

assuming both $A$ and $B$ are invertible.

___