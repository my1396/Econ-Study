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


Define a $n\times n$ **diagonal matrix** $D = \diag{(d_1, d_2, \ldots, d_n)}$, then

- **Premultiply a vector**

$$
\begin{bmatrix}
d_1 & & & & \\
& \ddots & & & \\
& & d_i & & \\ 
& & & \ddots & \\
& & & & d_n\\
\end{bmatrix}
\begin{bmatrix}
\color{red}{x_1}  \\
\vdots \\
\color{blue}{x_i} \\ 
\vdots \\
\color{#008B45}{x_n} \\ 
\end{bmatrix}
= {\color{red}x_1} \begin{bmatrix}
d_1  \\
 \\
 \\ 
 \\
 \\ 
\end{bmatrix} 
+ \cdots 
+ {\color{blue}x_i} \begin{bmatrix}
  \\
 \\
d_i  \\ 
 \\
 \\ 
\end{bmatrix} 
+ \cdots 
+ {\color{#008B45}x_n} \begin{bmatrix}
  \\
 \\
  \\ 
 \\
d_n \\ 
\end{bmatrix} 
$$

- **Premultiply a matrix** 

    左乘一个对角矩阵

    $D$ is a $n\times n$ diagonal matrix, $A$ is $n\times K$. For the product $DA$, each row $i$ is equal to the $i$-th row of $A$ multiplied by $D_{ii}$. 

    $DA$ is a **row-wise scaling** of A.

    The $i$th row of $DA$ is:

    $$
    (DA)_{i\cdot} = d_{ii}\, a_{i\cdot} \quad (\text{row vector})
    $$

    where each $a_{i\cdot}$ is a row vector in $\mathbb{R}^K.$
    
    $$
    DA = 
    \begin{bmatrix}
      \color{red}d_{11} & & & & \\
      & \ddots & & & \\
      & & \color{blue}d_{ii} & & \\ 
      & & & \ddots & \\
      & & & & \color{#008B45}d_{nn} \\
    \end{bmatrix}
    \begin{bmatrix} a_{1\cdot} \\ \vdots \\ a_{i\cdot} \\ \vdots \\ a_{n\cdot}  \end{bmatrix}
    = \begin{bmatrix}
    \color{red}d_{11} a_{1\cdot} \\
    \vdots \\
    \color{blue}d_{ii} a_{i\cdot} \\
    \vdots \\
    \color{#008B45}d_{nn} a_{n\cdot}
    \end{bmatrix}
    $$

    

- **Postmultiply a matrix**

    左乘一个对角矩阵

    $A$ is $n\times K$, $D$ is $K\times K$. For the product $AD$, each column $j$ is equal to the $j$-th column of $A$ multiplied by $D_{jj}$. 

    $AD$ is a **column-wise** scaling of A.

    The $j$th column of $AD$ is:

    $$
    (AD)_{\cdot j} = a_{\cdot j}\, d_{jj} \quad (\text{column vector})
    $$

    where each $a_{\cdot j}$ is a column vector in $\mathbb{R}^n.$

    $$
    AD = 
    \begin{bmatrix} a_{\cdot 1} & \cdots & a_{\cdot j} & \cdots & a_{\cdot K} \end{bmatrix}
    \begin{bmatrix}
      \color{red}d_{11} & & & & \\
      & \ddots & & & \\
      & & \color{blue}d_{jj} & & \\ 
      & & & \ddots & \\
      & & & & \color{#008B45}d_{KK} \\
    \end{bmatrix}
    = \begin{bmatrix}
    \color{red}a_{\cdot 1} d_{11} & \cdots & \color{blue}a_{\cdot j} d_{jj} & \cdots & \color{#008B45}a_{\cdot K} d_{KK}
    \end{bmatrix}
    $$


- **Product of two diagonal matrices**

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

- **Inverse of a diagonal matrix**

    $$
    D^{-1}_{ii} = \left[\frac{1}{d_{ii}}\right]
    $$

    Inverse is taking the inverse of each entry. 

    $$
    \begin{bmatrix}
    d_1 & & & & \\
    & \ddots & & & \\
    & & d_i & & \\ 
    & & & \ddots & \\
    & & & & d_n\\
    \end{bmatrix}^{-1}
    = \begin{bmatrix}
    d_1^{-1} & & & & \\
    & \ddots & & & \\
    & & d_i^{-1} & & \\ 
    & & & \ddots & \\
    & & & & d_n^{-1}\\
    \end{bmatrix}
    $$

    Note that $D$ is invertible if and only if all diagonal entries are nonzero.


- $D=D^{T}$

- $D_1 \times D_2 = D_2 \times D_1 = C$  

  Diagonal Matrices multiplication are commutative. 

  $$
  c_{ii} = d1_{ii} d2_{ii}
  $$

- $\vert D \vert = \prod_{i=1}^n d_{ii}$ 

  Determinant is the product of the elements of $D$.


___

An **orthogonal matrix** (正交矩阵) is a square matrix whose columns and rows are both orthogonal unit vectors (i.e., orthonormal vectors):

$$
Q^TQ = QQ^T = I,
$$

or equivalently, 

$$
Q^{-1} = Q^T.
$$


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

**General rules for matrix multiplication:**

- Associative law: $(AB)C = A(BC)$ 结合律 ✅
- Distributive law: $A(B+C) = AB + BC$
- Transpose of a product: $(AB)' = B'A'$
- Transpose of an extended product: $(ABC)' = C'B'A'$ 
- Matrix multiplication is NOT commutative: $AB \ne BA$ 交换律 ❌


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
(A\otimes B)^{-1} = A^{-1} \otimes B^{-1} ,
$$

assuming both $A$ and $B$ are invertible.

**Transpose** of Kronecker products:

$$
(A\otimes B)' = A' \otimes B' .
$$

**Trace** of Kronecker products:

$$
\text{tr}(A\otimes B) = \text{tr}(A)\text{tr}(B) .
$$

**Determinant** of Kronecker products:

$$
\vert A \otimes B \vert = \vert A \vert^m \vert B \vert^n ,
$$

where $A$ is an $m \times m$ matrix and $B$ is a $n \times n$ matrix.

___


## Trace Properties 

The trace of a square matrix A, denoted $\text{tr}(A)$, is defined to be the sum of elements on the main diagonal. The trace is only defined for a square matrix ($n \times n$).

$$\text{tr}(A) = \sum_{i=1}^n a_{ii}$$ 

Basic properties: \
$\text{tr}(\boldsymbol{I}_K) = K$ \
$\text{tr}(cA) = c \cdot \text{tr}(A)$ \
$\text{tr}(XA) = \text{tr}(AX)$ \
$\text{tr}(A+B) = \text{tr}(A) + \text{tr}(B)$


For a random vector $z$ with $\mathbb{E}(z)=\mu$ and $\text{Var}(z)=\Sigma$, then 

$$
\mathbb{E}(z'z) = \text{tr} (\Sigma) + \mu'\mu .
$$

Multiplication by a full-rank square matrix preserves rank.
<ul>
<li> Let $A$ be a $K\times L$ matrix and $B$ a square $L\times L$ matrix. If $B$ is full-rank, then

$$
\text{rank}(AB) = \text{rank}(A).
$$
</li>

<li> Let $A$ be a $K\times L$ matrix and $B$ a square $K\times K$ matrix. If $B$ is full-rank, then

$$
\text{rank}(BA) = \text{rank}(A).
$$
</li>
</ul>


___

## Definiteness

Let  $S$ be the space of all  $Kx1$ vectors having real entries. A  $K	\times K$ real symmetric matrix  $A$ is said to be:

1. positive definite iff  $x^{T}Ax>0$ for any non-zero  $x \in S$;
2. positive semi-definite iff  $x^{T}Ax\geq 0$ for any  $x \in S$;
3. negative definite iff  $x^{T}Ax<0$ for any non-zero  $x \in S$;
4. negative semi-definite iff  $x^{T}Ax\leq 0$ for any  $x \in S$;
5. indefinite iff there exist  $x,y\in S$ such that  $x^{T}Ax>0$ and  $y^{T}Ay<0$.

Let $A$ be a  $K	\times K$ matrix. If  $A$ is positive definite, then it is full-rank.

A real symmetric  $K	\times K$ matrix  $A$ is positive definite if and only if all its eigenvalues are strictly positive real numbers. \
A real symmetric  $K	\times K$ matrix  $A$ is positive semi-definite if and only if all its eigenvalues are positive real numbers.



___

## Matrix Diagonalization 

Eigen Decomposition

Let $A\in \mathbb{R}^{K\times K}$ be a square matrix. Then 

<ul>
<li> All the eigenvalues of $A$ are real; </li>
<li>  $A$ is orthogonally diagonalizable, i.e., there exists an orthogonal matrix $P$ and a diagonal matrix $\Lambda$ such that 

$$
A = P\Lambda P^{-1}
$$

$\Lambda = \text{diag}(\lambda_1, \ldots, \lambda_K)$ is a **diagonal matrix with eigenvalues being the diagonal**. 

$$
\Lambda = \begin{bmatrix} \lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 &  \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 &  \cdots & \lambda_K
\end{bmatrix}
$$

$P=[X_1, \ldots, X_K]$ be the **matrix of eigenvectors** corresponding to $\lambda_1, \ldots, \lambda_K$.

$$
\begin{align*}
P &= \begin{bmatrix} X_1 & X_2 & \cdots & X_K \end{bmatrix}  \\
&= \begin{bmatrix} x_{11} & x_{21} & \cdots & x_{K1} \\
x_{12} & x_{22} &  \cdots & x_{K2} \\
\vdots & \vdots & \ddots & \vdots \\
x_{1K} & x_{2K} &  \cdots & x_{KK}
\end{bmatrix}
\end{align*}
$$

Then we have

$$
\begin{align*}
AP &= A \begin{bmatrix} X_1 & X_2 & \cdots & X_K \end{bmatrix} \\
&= \begin{bmatrix} AX_1 & AX_2 & \cdots & AX_K \end{bmatrix} \\
&= \begin{bmatrix} \lambda_1X_1 & \lambda_1X_2 & \cdots & \lambda_1X_K \end{bmatrix} \\
&=\begin{bmatrix} \lambda_1x_{11} & \lambda_2x_{21} & \cdots & \lambda_kx_{K1} \\
\lambda_1x_{12} & \lambda_2x_{22} &  \cdots & \lambda_Kx_{K2} \\
\vdots & \vdots & \ddots & \vdots \\
\lambda_1x_{1K} & \lambda_2x_{2K} &  \cdots & \lambda_Kx_{KK} \\
\end{bmatrix} \\
&= \begin{bmatrix} x_{11} & x_{21} & \cdots & x_{K1} \\
x_{12} & x_{22} &  \cdots & x_{K2} \\
\vdots & \vdots & \ddots & \vdots \\
x_{1K} & x_{2K} &  \cdots & x_{KK} \end{bmatrix}
\begin{bmatrix} \lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 &  \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 &  \cdots & \lambda_K
\end{bmatrix} \\
&= P\Lambda
\end{align*}
$$

Hence

$$
A = P\Lambda P^{-1}
$$


An important application of the eigenvalue decomposition is to calculate the power of matrices.

$$
\begin{align*}
A^2 &= (P\Lambda P^{-1}) (P\Lambda P^{-1}) \\
&= P\Lambda^2 P^{-1}
\end{align*}
$$

By induction,

$$
A^n = P\Lambda^n P^{-1}
$$

</li>

<li>
For <strong>symmetric matrices</strong> $A$, the eigenvalue decomposition is also called the <em>spectral decomposition</em>.

$A$ is orthogonally diagonalizable, i.e., there exists and orthogonal matrix $Q$ and a diagonal matrix $\Lambda$ such that 

$$
A = Q\Lambda Q^{T},
$$

or equivalently written as

$$
A = \sum_{i=1}^K \lambda_i q_i q_i^{T}.
$$

The converse is also true. Therefore, a matrix is symmetric if and only if it is orthogonally diagonalizable.

</li>
</ul>



___


## Expectation and Variance of Random Vectors

A random vector $\vec{X}$ is a vector 

$$
\vec{X}=\begin{bmatrix}
X_1 \\
X_2 \\
\vdots \\
X_p
\end{bmatrix}
$$

of $p$ jointly distributed random variables $X_i,$ where $i=1,\ldots,p$.

- Expectation vector $\mathbb{E}[\vec{X}]$ is given by

  $$
  \mathbb{E}[\vec{X}]=\begin{bmatrix}
  \mathbb{E}[X_1] \\
  \mathbb{E}[X_2] \\
  \vdots \\
  \mathbb{E}[X_p]
  \end{bmatrix}
  $$

  The expected value of a vector or matrix is the vector or matrix of expected values.

- Variance-Covariance Matrix of a random vector $\vec{X}$ is given by:

$$
\begin{align*}
\text{Cov}(\vec{X}) &= \mathbb{E}\left[ (\vec{X}-\mathbb{E}[\vec{X}])(\vec{X}-\mathbb{E}[\vec{X}])^T \right] \\
&= \mathbb{E}[\vec{X}\vec{X}^T] - \mathbb{E}[\vec{X}] (\mathbb{E}[\vec{X}])^T
\end{align*}
$$

$$
\begin{align*}
\text{Cov}(\vec{X}) &= 
\begin{bmatrix}
\text{Var}(X_1) &  \text{Cov}(X_1, X_2) &  \cdots &  \text{Cov}(X_1, X_p) \\
\text{Cov}(X_2, X_1) &  \text{Var}(X_2) &  \cdots &  \text{Cov}(X_2, X_p) \\
\vdots & \vdots & \ddots & \vdots \\
\text{Cov}(X_p, X_1) &  \text{Cov}(X_2, X_p) &  \cdots &   \text{Var}(X_p)
\end{bmatrix}_{p\times p}  \\
&= \begin{bmatrix}
\sigma_{11} & \sigma_{12} &  \cdots & \sigma_{1p} \\
\sigma_{21} & \sigma_{12} &  \cdots & \sigma_{2p} \\ 
\vdots & & \vdots & \\
\sigma_{p1} & \sigma_{p2} &  \cdots & \sigma_{pp} \\
\end{bmatrix} \\
&= \bSigma
\end{align*}
$$


___

**Cross-covariance matrix** is defined for two random vectors $X$ and $Y$, containing the covariances between all possible couples of random variables formed by one entry of $X$ and one entry of $Y$.

Formally, let $X$ be a $K\times 1$ random vector and $Y$ be a $L\times 1$ random vector. The cross-covariance matrix between $X$ and $Y$ is a $K\times L$ matrix, denoted by $\text{Cov}(X,Y)$ and defined as follows:

$$
\text{Cov}(X,Y) = E\left[(X-E[X])(Y-E[Y])^T \right].
$$

Note that in the formula above $(X-E[X])$ is a column vector and $(Y-E[Y])^T$ is a row vector.

Example: $X=[X_1, X_2, X_3]^T$ and $Y=[Y_1, Y_2]^T$.

The cross-covariance matrix between $X$ and $Y$ is:

$$
\begin{aligned}
\text{Cov}(X,Y) &= \begin{bmatrix}
E[(X_1-E[X_1])(Y_1-E[Y_1])] & E[(X_1-E[X_1])(Y_2-E[Y_2])] \\
E[(X_2-E[X_2])(Y_1-E[Y_1])] & E[(X_2-E[X_2])(Y_2-E[Y_2])] \\
E[(X_3-E[X_3])(Y_1-E[Y_1])] & E[(X_3-E[X_3])(Y_2-E[Y_2])] \\
\end{bmatrix} \\
&= \begin{bmatrix}
\text{Cov}(X_1,Y_1) & \text{Cov}(X_1,Y_2) \\
\text{Cov}(X_2,Y_1) & \text{Cov}(X_2,Y_2) \\
\text{Cov}(X_3,Y_1) & \text{Cov}(X_3,Y_2) \\
\end{bmatrix}
\end{aligned}
$$

Note that, in general, the cross-covariance is *not* symmetric.
For example, if $X$ is $K\times 1$ and $Y$ is $L\times 1,$ then $\cov(X,Y)$ is $K\times L$ and $\cov(Y,X)$ is $L\times K.$


When $Y=X$ then the cross-covariance matrix coincides with the covariance matrix of $X:$

$$
\color{#008B45} \cov(X,X) = E\left[(X-E[X])(X-E[X])^T \right] = \var(X).
$$

___


**Autocovariance matrix**

Let $⟨X_t⟩$ be a sequence of random vectors. Then the cross-covariance matrix between $X_t$ and $X_{t-j}$, $\text{Cov}(X_t, X_{t-j})$ is called autocovariance matrix.


**Covariance Stationary**

A sequence of random vectors $⟨X_t⟩$ is said to be *covariance or weakly stationary* if and only if

$$
\begin{aligned}
& E[X_t] = \bmu, \text{ and } \\
& \text{Cov}(X_t, X_{t-j}) = \Gamma_j \text{ for } \forall j\ge 0.
\end{aligned}
$$

where $\bmu$ is a $K\times 1$ vector and $\Gamma_j$ is a $K\times K$ matrix.

- $E[X_t] = \bmu$ means that all the random vectors belonging to the sequence $⟨X_t⟩$ must have the same mean.

- The cross-covariance between a term and the term that is located $j$ positions before it must always be the same. 
That is, <span style='color:#337ab7'>$\text{Cov}(X_t, X_{t-j}) = \Gamma_j$ depends only on the time lag $j$</span> (the number of time periods between the two variables) and *not* on $t$.


If $X_t\in \R,$ the autocovariance matrix $V$ is given by

$$
\begin{aligned}
V &= 
\begin{bmatrix}
\cov(x_1, x_1) & \cov(x_1, x_2) & \cdots & \cov(x_1, x_{T-1}) & \cov(x_1, x_{T}) \\
\cov(x_2, x_1) & \cov(x_2, x_2) & \cdots & \cov(x_2, x_{T-1}) & \cov(x_2, x_{T}) \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
\cov(x_{T-1}, x_1) & \cov(x_{T-1}, x_2) & \cdots & \cov(x_{T-1}, x_{T-1}) & \cov(x_{T-1}, x_{T}) \\
\cov(x_{T}, x_1) & \cov(x_{T}, x_2) & \cdots & \cov(x_{T}, x_{T-1}) & \cov(x_{T}, x_{T}) \\
\end{bmatrix} \\
&= 
\begin{bmatrix}
\gamma_0 & \gamma_1 & \cdots & \gamma_{T-2} & \gamma_{T-1} \\ 
\gamma_1 & \gamma_0 & \cdots & \gamma_{T-3} & \gamma_{T-2} \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
\gamma_{T-2} & \gamma_{T-3} & \cdots & \gamma_{0} & \gamma_{1} \\ 
\gamma_{T-1} & \gamma_{T-2} & \cdots & \gamma_{1} & \gamma_{0} \\ 
\end{bmatrix}
\end{aligned}
$$


Further readings: 

- Taboga, Marco (2021). "Cross-covariance matrix", Lectures on probability theory and mathematical statistics. Kindle Direct Publishing. Online appendix. <https://www.statlect.com/glossary/cross-covariance-matrix>
- Random vectors: <https://www.probabilitycourse.com/chapter6/6_1_5_random_vectors.php>
- Variance-covariance matrix of random vectors: <https://www.math.kent.edu/~reichel/courses/monte.carlo/alt4.7d.pdf>



___


## Moments of Linear Functions

Let

$$
\ba = \begin{bmatrix}
a_1 \\
a_2 \\
\vdots \\
a_n
\end{bmatrix}, \quad
\bx = \begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{bmatrix}, \quad
\bmu = \begin{bmatrix}
\mu_1 \\
\mu_2 \\
\vdots \\
\mu_n
\end{bmatrix}
$$

Mean

$$
\E[\ba'\bx] = \ba'\bmu
$$

Variance

$$
\var(\ba'\bx) = \E\left[\ba'(\bx-\bmu)(\bx-\bmu)'\ba\right] = \ba'\var(\bx)\ba
$$


For a linear function 

$$
\by = \bA\bx ,
$$

the $i$th element of $\by$ is

$$
y_i = \ba_i \bx ,
$$

where $\ba_i$ is a column vector formed by the transpose of the $i$th row of $\bA$.


We have the following results.

$$
\E(\bA\bx) = \bA \bmu
$$

and

$$
\color{#008B45}\var(\bA\bx) = \bA \var(\bx) \bA'.
$$

This matrix will be nonnegative definite.


___

## Moments of Nonlinear Functions

Consider a set of nonlinear functions of $\bx,$ $\by=g(\bx).$ Each element of $\by$ can be approximated with a linear Taylor series.

Let $\bj^{i}$ be the row vector of partial derivatives of the $i$th function with respect to the $n$ elements of $\bx:$

$$
\bj^{i}(\bx) = \frac{\partial g_i(\bx)}{\partial \bx'} = \frac{\partial y_i}{\partial \bx'}
$$


The linear Taylor expansion at $\bmu$, the mean vector of $\bx$, is:

$$
\bg_i(\bx) \approx g_{i}(\bmu) + \bj^{i}(\mu)(\bx-\bmu) .
$$

From this, we obtain

$$
\begin{aligned}
\E[\bg_i(\bx)] &\approx g_{i}(\bmu)  \\
\var[\bg_i(\bx)] &\approx \bj^i(\bmu)\var(\bx)\bj^i(\bmu)'
\end{aligned}
$$

and 

$$
\cov(\bg_i(\bx), \bg_j(\bx)) \approx \bj^i(\bmu)\var(\bx)\bj^j(\bmu)'
$$

Then

$$
\begin{aligned}
\E[\bg(\bx)] &\approx \bg(\bmu)  \\
\E[\bg(\bx)] &\approx \bJ(\bmu)\var(\bx)\bJ(\bmu)'
\end{aligned}
$$

$\bJ(\bmu)$ is obtained by collecting the row vectors $\bj^i(\bmu)$ in a matrix:

$$
\bJ(\bmu) = \left. \frac{\partial \by}{\partial \bx'} \right\vert_{\bx=\bmu} \;.
$$














