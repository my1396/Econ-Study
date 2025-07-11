---
layout: post
title: Econometric Notes
tag: study
update: 2024-10-27
---


<head>
    <style>
      /* Whatever that is inside this <style> tag is all styling for your markup / content structure.
      /* The . with the boxed represents that it is a class */
      /* this is only for proper styling in VS Code Preview */
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


## Geometry

**Quadrant** (plane geometry)

The axes of a two-dimensional Cartesian system divide the plane into four infinite regions, called quadrants, each bounded by two half-axes.

-   the numbering goes counter-clockwise starting from the upper right ("northeast") quadrant.

<img src="{{ site.baseurl}}/images/quadrant geometry.png" alt="quadrant geometry" style="display: block; margin-right: auto; margin-left: auto; zoom:50%;" />

orthographic projection (正射投影): top view, front view, (right) side view.

锐角 acute angel \
钝角 obtuse angel \
直角 right angel

complementary angel 互余角 $\alpha+\beta=\frac{\pi}{2}$.

supplementary angel 互补角 $\alpha+\beta=\pi$.

<img src="{{ site.baseurl}}/images/triangel.png" alt="triangel" style="display: block; margin-right: auto; margin-left: auto; zoom:60%;" />

斜边 hypotenuse  /haɪˈpɑːtənuːs/ \
邻边 adjacent side \
对边 opposite side

<span style='color:#008B45FF'>Pythagoras’ /pəˈθægərəs/ or Pythagorean /pəˌθæɡəˈriən/ theorem</span> 勾股定理

**Law of Cosine**: tells the length of the 3rd side of a triangle if we know 2 sides and the angle between them.

$$
\begin{align*}c^2=a^2+b^2-2ab\cos\theta\end{align*}
$$


circumference /sərˈkʌmfərəns/ 周长

trapezoid 梯形 $A=\frac{(a+b)}{2}\cdot h$. (上底 + 下底) $\times$ 高/2.

parallelogram /ˌpærəˈleləɡræm / 平行四边形

parallelepiped /ˌpærəˌleləˈpaɪˌpɪd / 平行六面体 (倾斜长方体)

tetrahedron /ˌtetrəˈhiːdrən/ 四面体, also called "tiangular pyramid", 三角锥, is a polyhedron composed of four triangular faces.

polyhedron 多面体 \
cube 正方体 \
cuboid 长方体 

sector 扇形  \
已知弧长 $A=\frac{1}{2}l\cdot r$。 $l$ 为扇形弧长，$r$ 为半径。与三角形面积类比，$\frac{1}{2}$底$\times$高，半径可看作底，弧长看作高。

已知圆心角 $A=\frac{n}{360}\pi r^2=\frac{1}{2}\theta\cdot r^2$。$n$单位为度数degree， $\theta$ 为圆心角，单位为弧度radian。

-   度数弧度转换公式：$\frac{n}{180}\pi=\theta$。

-   弧长公式：$l=\theta \cdot r$ (圆心角弧度 $\times$ 半径)。

    圆周长 $C=2\pi r$，弧长 $l=\frac{\theta}{2\pi}\cdot C=\frac{\theta}{2\pi}\cdot 2\pi r=\theta r$。

Volume of a sphere (ball) $V=\frac{4}{3}\pi r^3$, $r$ is radius. Surface $S=4\pi r^2$.

secant line 割线 \
tangent line 切线

**直线方程的各种形式**

<ol>
<li>一般式: $Ax+By+C=0$ <br/>

斜率: $k=-\frac{A}{B}$ <br/>
法向量: $\overrightarrow{\textbf{n}}=(A,B)$ <br/>
方向向量: $\overrightarrow{\textbf{a}}=(B,-A)$ 

</li>


<li>点斜式: $y-y_0=k(x-x_0)$ <br/>

点斜式是由一个定点 $P(x_0,y_0)$ 和斜率 $k$ 确定的直线方程。<br/>

斜率: $k$ <br/>
法向量: $\overrightarrow{\textbf{n}}=(k,-1)$ <br/>
方向向量: $\overrightarrow{\textbf{a}}=(1,k)$ 

</li>

<li> 斜截式: $y=kx+b$ <br/>

斜截式是由斜率 $k$ 和 $y$ 轴上的截距 $b$ 确定的直线方程。<br/>

斜率: $k$ <br/>
法向量: $\overrightarrow{\textbf{n}}=(k,-1)$ <br/>
方向向量: $\overrightarrow{\textbf{a}}=(1,k)$ 

</li>

<li> 两点式: $\displaystyle \frac{y-y_1}{y_2-y_1} = \frac{x-x_1}{x_2-x_1}$ <br/>

两点式是由已知的两个点 $(x_1,y_1)$, $(x_2,y_2)$ 确定的直线方程。<br/>

斜率: $k = \frac{y_2-y_1}{x_2-x_1}$ <br/>
法向量: $\overrightarrow{\textbf{n}}=(y_2-y_1,x_1-x_2)$ <br/>
方向向量: $\overrightarrow{\textbf{a}}=(x_2-x_1,y_2-y_1)$ 

</li>

<li> 点向式: $\displaystyle \frac{y-y_0}{b} = \frac{x-x_0}{a}$ <br/>

点向式是由已知的定点 $P(x_0,y_0)$ 和方向向量 $\overrightarrow{\textbf{a}}=(a,b)$ 所确定的直线方程。<br/>

斜率: $k = \frac{b}{a}$ <br/>
法向量: $\overrightarrow{\textbf{n}}=(b,-a)$ <br/>
方向向量: $\overrightarrow{\textbf{a}}=(a,b)$ 

</li>

<li> 参数式: $\left\{\begin{aligned}&x=x_0+at & \\ &y = y_0+bt & \end{aligned}\right.$ <br/>

这里的参数是$t$，是点向式的变式，也是由定点 $P(x_0,y_0)$ 和方向向量 $\overrightarrow{\textbf{a}}=(a,b)$ 所确定的直线方程。<br/>

斜率: $k = \frac{b}{a}$ <br/>
法向量: $\overrightarrow{\textbf{n}}=(b,-a)$ <br/>
方向向量: $\overrightarrow{\textbf{a}}=(a,b)$ 

</li>

<li> 特别参数式: $\left\{\begin{aligned}&x=x_0+t\cos \alpha & \\ &y = y_0+t\sin \alpha & \end{aligned}\right.$ <br/>

这里的参数是 $t$，是参数式的特例，即以直线的倾角。<br/>

斜率: $k = \tan \alpha$ <br/>
法向量: $\overrightarrow{\textbf{n}}=(\sin \alpha, -\cos \alpha)$ <br/>
方向向量: $\overrightarrow{\textbf{a}}=(\cos \alpha, \sin \alpha)$ 

</li>

<li> 点法式: $A(x-x_0)+B(y-y_0)=0$ <br/>

点向式是由已知的定点 $P(x_0,y_0)$ 和法向量 $\overrightarrow{\textbf{a}}=(a,b)$ 所确定的直线方程。<br/>

斜率: $k = -\frac{A}{B}$ <br/>
法向量: $\overrightarrow{\textbf{n}}=(A,B)$ <br/>
方向向量: $\overrightarrow{\textbf{a}}=(B,-A)$ 

</li>

</ol>
Reference: <https://zhuanlan.zhihu.com/p/26263309>

**dot product** vs. **cross product**

- dot product is a scalar, used to calculate projection along a direction ($\vec{A}\cdot \hat{u}$ is the component of $\vec{A}$ along $\hat{u}$, ^ indicates a unit vector); determine if two vectors are <span style='color:#008B45FF'>orthogonal</span> (if $\vec{A}\cdot\vec{B}=0$, then $\vec{A}\perp\vec{B}$);

  - The magnitude of the dot product is the same as the magnitude of one of them, multiplied by the component of one vector that is parallel to the other. 

  $$
  \begin{align*}
  \vec{A}\cdot\vec{B} &= \sum_i a_ib_i \\
  \vec{A}\cdot\vec{B} &= \vert\vec{A}\vert\vert\vec{B}\vert \cos\theta \\
  \vec{A}\cdot\vec{A} &= \vert A\vert^2 \quad (\cos0=1)
  \end{align*}
  $$

  

- cross product is a vector, used to 1) calculate area of parallelogram formed by two vectors; 2) get the normal vector; if $\vec{A}\times\vec{B}=0$, then $\vec{A}\parallel\vec{B}$ (<span style='color:#008B45FF'>parallel</span>);

  - The magnitude of the cross product is the same as the magnitude of one of them, multiplied by the component of one vector that is perpendicular to the other. 
  - If $\vec{A}\parallel\vec{B}$, no component is perpendicular to the other vector. Hence, the cross product is 0 although you can still find a perpendicular vector to both of these. 

  $$
  \begin{align*}
  \vec{A}\times\vec{B} &=\vert\vec{A}\vert\vert\vec{B}\vert \sin\theta\cdot\vec{n},\; \vec{n} \textrm{ decided by right-hand rule.} \\
  \vec{A}\times\vec{A}&=0 \quad (\sin0=0\textrm{, area of a line is 0})
  \end{align*}
  $$

Geometric illustration: \
<https://math.stackexchange.com/a/1730547>


## Inner and Outer Product

If $X$ and $Y$ are random variables, then the inner product is given by 

$$
\langle X, Y\rangle = \E[XY]
$$

and norm is given by $\Vert Y \Vert^2 = \langle Y, Y\rangle = \E Y^2.$

A random variable $S'$ is called a **projection** (or $L_2$-projection) of $Y$ onto $\Scal$ if $S'\in \Scal$ and 

$$
\E(Y-S')^2 \le \E(Y-S)^2 \quad \forall S\in \Scal.
$$

In words, $S'$ is the projection of $Y$ onto $\Scal$ if its the best approximation of $Y$ in $\Scal$ in terms of mean squared error (MSE).

$\E[Y\mid X]$ is the function of $X$ that has the smallest possible MSE for predicting $Y.$ Thus $\E[Y\mid X]$ is the projection of $Y$ onto the set of random variables $\\{h(X)\mid h \text{ is any real-valued function}\\}.$

___

If $\boldsymbol{u}$ and $\boldsymbol{v}$ are column vectors with the same size, then $\boldsymbol{u}^T \boldsymbol{v}$ is the inner product; if $\boldsymbol{u}$ and $\boldsymbol{v}$ are column vectors of any size, then $\boldsymbol{u} \boldsymbol{v}^T$ is the outer product.

- Inner product is a *number*;
- Outer product is a *matrix*. Let $\boldsymbol{u}$ be $n\times 1$ and $\boldsymbol{v}$ be $m\times 1$, then $\boldsymbol{u} \boldsymbol{v}^T$ is $n\times m$.


___


**Change of Variable Formula**

Given the distribution of $X$, we can obtain the distribution of a continuous function of $X$, e.g. $Y=g(X)$.


$$
\begin{align*}
F_Y(y)&=P(Y\le y)=P\left(g(X)\le y\right) \\
&=\left\{
	\begin{array}{ll}
	P\left(X\le g^{-1}(y)\right) = F_X(g^{-1}(y)) & \text{when $g(x)$ is $\uparrow$} \\
	P\left(X\ge g^{-1}(y)\right) = 1- F_X(g^{-1}(y))  & \text{when $g(x)$ is $\downarrow$}
	\end{array} \right. \\
f_Y(y) &= f_X(g^{-1}(y)) \cdot \left\vert \frac{\partial }{\partial y} g^{-1}(y) \right\vert
\end{align*}
$$


Change of Variable for a **Double Integral**

Let $X$ and $Y$ be two jointly continuous random variables. Let $(Z, W) = g(X,Y) = (g_1(X,Y), g_2(X,Y))$, where $g$: $\mathbb{R}^2 \mapsto \mathbb{R}^2$ is a continuous one-to-one (invertiable) funtion with continuous partial derivatives.

Let $h=g^{-1}$, i.e., the inverse function that takes $(Z,W)$ and returns $(X,Y)$, $(X,Y)=h(Z,W)=(h_1(Z,W),h_2(Z,W))$. 

Then $Z$ and $W$ are jointly continuous and their joint PDF, $f_{ZW}(z,w)$, for $(z,w)\in R_{ZW}$ is given by

$$
f_{ZW}(z,w)=f_{XY}(h_1(z,w),h_2(z,w)) \cdot \vert \boldsymbol{J}\vert,
$$

where $\boldsymbol{J}$ is the Jacobian of $h$, defined by 

$$
\boldsymbol{J} =
\text{det} \begin{bmatrix}
\frac{\partial h_1}{\partial z} & \frac{\partial h_1}{\partial w} \\
\frac{\partial h_2}{\partial z} & \frac{\partial h_2}{\partial w}
\end{bmatrix} =
\frac{\partial h_1}{\partial z} \cdot \frac{\partial h_2}{\partial w} - \frac{\partial h_1}{\partial w} \cdot \frac{\partial h_2}{\partial z}
$$

Let $X$ and $Y$ be two random variables with joint PDF $f_{XY}(x,y)$. Let $Z=X+Y$. Find $f_Z(z)$.

To apply the change of variable, we need two random variables $Z$ and $W$. Define

$$
\begin{align*}
\left\{ 
	\begin{array}{ll}
	z = x+y & \text{i.e., }g_1(x,y)\\
	w = x & \text{i.e., }g_2(x,y)
	\end{array}
\right.
\end{align*}
$$

Then we can find the inverse transform:

$$
\begin{align*}
\left\{ 
	\begin{array}{ll}
	x = w & \text{i.e., }h_1(x,y)\\
	y = z-w & \text{i.e., }h_2(x,y)
	\end{array}
\right.
\end{align*}
$$

Then, we have absolute value of the Jacobian

$$
\vert \boldsymbol{J} \vert = 
\vert \text{det} \begin{bmatrix}
0 & 1 \\
1 & -1
\end{bmatrix} \vert 
=
\vert 
0-1
\vert =
1
$$

Thus,

$$
f_{ZW}(z,w)=f_{XY}(w,z−w).
$$

But since we are interested in the marginal PDF, $f_Z(z)$, we have

$$
f_Z(z)=\int_{-\infty}^{\infty}f_{XY}(w,z−w)dw.
$$

Note that, if $X$ and $Y$ are independent, then $f_{XY}(x,y)=f_X(x)fY(y)$ and we conclude that
$$
f_Z(z)=\int_{-\infty}^{\infty}f_X(w)f_Y(z−w)dw.
$$

The above integral is called the *convolution* of $f_X$ and $f_Y$, and we write

$$
f_Z(z)=f_X(z)*f_Y(z) = \int_{-\infty}^{\infty}f_X(w)f_Y(z−w)dw = \int_{-\infty}^{\infty}f_Y(w)f_X(z−w)dw.
$$

<div class = "boxed">
<strong>Theorem</strong>  If X and Y are two jointly continuous random variables and $Z=X+Y$, then

$$
f_Z(z)=\int_{-\infty}^{\infty}f_{XY}(w,z−w)dw.
$$

If X and Y are also independent, then

$$
f_Z(z) = \int_{-\infty}^{\infty}f_Y(w)f_X(z−w)dw.
$$
</div>

Let  $X$ and  $Y$ be two independent discrete random variables. Denote their respective pmfs (probability mass function) by  $p_X(x)$ and  $p_Y(y)$, and their supports by  $R_X$ and  $R_{Y}$. Let

$$
Z=X+Y
$$

and denote the pmf of $Z$ by  $p_Z(z)$. Then,

$$
\begin{align*}
p_Z(z) &= \sum_{k=-\infty}^{\infty} p_X(x=k)\cdot p_Y(y=z-k) \\
&= \sum_{x\in R_X} p_X(x=k)\cdot p_Y(y=z-k)
\end{align*}
$$

or

$$
p_Z(z) = \sum_{y\in R_y} p_X(x=z-k)\cdot p_Y(y=k).
$$


___


**Expectation**

Expectation are denoted by $\mathbb{E}(X)$ or $\mathbb{E}_X(X)$ to denote the expectation is taken over the RV $X.$

$$
\mathbb{E}(X) = 
\begin{cases}
\displaystyle \sum_{x}x f(x) & \text{for discrete } X \\
\displaystyle \int_{-\infty}^{\infty} x f(x)\, \mathrm dx & \text{for continuous } X \\
\end{cases}
$$


**Conditional Expectations**

The conditional expectation for $Y$, given that $X$ has a prescribed value, is defined as follows:

$$
\mathbb E(Y|X=x) = \sum_j y_j P(Y=y_j|X=x) = \sum_j y_j f_{Y|X}(x,y_i) \, ,
$$

which is <span style='color:#337ab7'>a function of $X.$</span> 


The conditional expectation for $X$ given $Y$, $\mathbb E(X\vert Y=y)$, is defined as follows:

$$
\mathbb E(X\vert Y=y) = \sum_i x_i P(X=x_i\vert Y=y) = \sum_i x_i f_{X\vert Y}(x_i,y) \, ,
$$

which is <span style='color:#337ab7'>a function of $Y.$</span> 


We denote the conditional expectation for $Y$ given $X$ as follows:

$$
\varphi_X(x) = \mathbb E(Y|X=x) \, .
$$

Technically, this is termed the *regression function* of $Y$ on $X$.

The expectation of the regression function is:

$$
\begin{aligned}
\mathbb E(\varphi_X(x)) &= \sum_i \varphi_X(x_i) f_X(x_i) \\
&= \sum_i \left\lbrace \sum_j y_j \, \frac{f_{XY}(x_i,y_j)}{f_X(x_i)} \right\rbrace f_X(x_i) \\
&= \sum_j y_j \sum_i f_{XY}(x_i,y_j) \\
&= \sum_j y_j f_Y(y_j) \\
&= \mathbb E(Y) \,.
\end{aligned}
$$

___


## Law of Iterated Expectations (LIE)

Fora any random variable $X\in \mathcal X$ and $Y\in \mathcal Y \subset \mathbb R$,

$$
\begin{align*}
\mathbb{E}_Y(Y) = \mathbb{E}_X\left[\mathbb{E}_{Y\vert X}\right(Y\vert X=x\left)\right] = \sum_{x\in\mathcal X} \mathbb{E}[Y\vert X=x]\, \mathbb{P}(X=x) .
\end{align*}
$$

(the subscript in $\mathbb{E}_Y$ and $\mathbb{E}_X$ indicate on which variable the expectation is taken)
or more succinctly  

$$
\begin{align*}
\mathbb{E}[Y] = \mathbb{E}\left[\mathbb{E}\right(Y\vert X\left)\right].
\end{align*}
$$

It repsents a transformation from condictional to unconditional expectaion.
The expected value (this expectation is with respect to  $X$) of the conditional expectation of $Y$ given $X$ is the expected value of $Y$.

LIE is also calld the *law of total expectation*, which can be derived from the *law of total probability*. We will see this in what follows. LIE is also referred to as "Adam’s Law."

___

Suppose $\mathbb{E}(Y\vert X)=0$, then   

$$
\begin{align*}
1. \quad & \mathbb{E}[Y] = \mathbb{E}\left[\mathbb{E}\right(Y\vert X=x\left)\right] = 0 \\
2. \quad & \mathbb{E}[g(X)\cdot Y] = \mathbb{E}\left[\mathbb{E}[g(X)\cdot Y\vert X]\right] = \mathbb{E}\left[g(X)\cdot \mathbb{E}[Y\vert X]\right] = \mathbb{E}[g(X)\cdot0]=0
\end{align*}
$$

Note that we start from the conditional expectation being $0$, and conclude that unconditional expectation and its product with a function of $X$ are $0$'s too.\
Conditional expectation is a *stronger* condition than unconditional expectation.

In other words, although conditional expectations can vary arbitrarily for different values of $X$, if you know what the conditional expectations are, the overall expected value of $Y$ is fully determined.

A simple example is one where $X$ takes only two values.  Suppose we are interested in mean birthweight ($Y$) for children of mother's who either drank alcohol during their pregnancy ($X=1$) or who didn't drink alcohol during their pregnancy ($X=0$).  

Suppose the following numbers:

$$
\begin{aligned}
  \mathbb{E}[Y|X=1] &= 7, \;\;\;  \mathbb{P}(X=1) = 0.1\\
  \mathbb{E}[Y|X=0] &= 8, \;\;\;  \mathbb{P}(X=0) = 0.9 \\
\end{aligned}
$$

The law of iterated expectation says that

$$
\begin{aligned}
  \mathbb{E}[Y] &= \mathbb{E}_X \big[ \mathbb{E}[Y|X] \big] \\
  &= \sum_{x \in \mathcal{X}} \mathbb{E}[Y|X=x] \cdot \mathbb{P}(X=x) \\
  &= \mathbb{E}[Y|X=0] \cdot \mathbb{P}(X=0) + \mathbb{E}[Y|X=1] \cdot \mathbb{P}(X=1) \\
  &= (8) \times (0.9) + (7) \times (0.1) \\
  &= 7.9
\end{aligned}
$$


Expressing mathematically, suppose we have a sample space, $X=\{A, A^c\}$, then 

$$
\mathbb E (Y) = \mathbb E (Y|A)\, P(A) + \mathbb E (Y|A^c)\, P(A^c)
$$

___

**Identities for conditional expectations**

- LIE (Adam's Law) $\mathbb{E}[Y] = \mathbb{E}\left[\mathbb{E}\right(Y\mid X\left)\right].$
- Generalized Adam’s Law 

    $$
    \E\left[ \E[Y \mid g(X)] \mid f(g(X)) \right] = \E[Y\mid f(g(X))]
    $$

    for any $f$ and $g$ with compatible domains and ranges. We also have that 

    $$
    \E\left[ \E[Y \mid g(X)] \mid f(g(X)=z) \right] = \E[Y\mid f(g(X))=z]
    $$

- Independence: $\E[Y\mid X] = \E[Y]$ if $X$ and $Y$ are independent.

- Taking out what is known: $\E[h(X)Z\mid X]=h(X)\E[Z\mid X]$

- Linearity: $\E[aX+bY\mid Z] = a\E[X\mid Z] + b\E[Y\mid Z],$ for any $a, b\in \R.$

- Projection interpretation: $\E\left[\left(Y-\E[Y\mid X]\right)h(X)\right] = 0$ for any function $h: \Xcal \to \R.$

- Keeping just what is needed: $\E[XY] = \E[X\E[Y\mid X]]$ for $X, Y\in \R.$

More about LIE: <https://davidrosenberg.github.io/ttml2021fall/background/conditional-expectation-notes.pdf>

___


### Partitioning and Conditioning

In the general case, consider a <span style='color:#337ab7'>partition</span> of the sample space: $\{X_1, X_2, \ldots, X_n\}$, each event has a corresponding probability: $P(X_1), P(X_2), \ldots, P(X_n)$.

Given another event $Y$, then according to the *partition rule* we have:

$$
\begin{aligned}
P(Y) &= \sum_i^n P(Y \cap X_i) \\
&= \sum_i^n P(Y \vert X_i)\, P (X_i)\\
&= P(Y|X_1)P(X_1) + P(Y|X_2)P(X_2) + \cdots + P(Y|X_n)P(X_n) .
\end{aligned}
$$

This is called the "<span style='color:#008B45FF'>**law of total probability**</span>".

Then it follows that:

$$
\begin{aligned}
\mathbb{E}(Y) &= \sum_j y_j P(Y=y_j)  \\
&= \sum_j y_j \left[P(Y=y_j|X_1)P(X_1) + P(Y=y_j|X_2)P(X_2) + \cdots + P(Y=y_j|X_n)P(X_n) \right] \\
&= \sum_j y_jP(Y=y_j|X_1)\,P(X_1) + \sum_j y_jP(Y=y_j|X_2)\,P(X_2) + \cdots + \sum_j y_jP(Y=y_j|X_n)\,P(X_n) \\
&= \mathbb{E}(Y|X_1)\,P(X_1) + \mathbb{E}(Y|X_2)\,P(X_2) + \cdots + \mathbb{E}(Y|X_n)\,P(X_n) \\
&= \mathbb{E}\left[\mathbb{E}(Y|X)\right]
\end{aligned}
$$


A reverse proof starting from $\mathbb{E}\left[\mathbb{E}(Y\vert X)\right]$.

$$
\begin{align*}
\mathbb{E}\left[\mathbb{E}(Y|X)\right] 
&= \sum_{x\in\mathcal X} p(x)\, \mathbb{E}(Y|X=x) \\
&= \sum_{x\in\mathcal X} \left[p(x) \sum_{y\in\mathcal Y} y\, p(y|x) \right] \\
&= \sum_{y\in\mathcal Y} \left[ y \sum_{x\in\mathcal X} p(x,y) \right] \\
&= \sum_{y\in\mathcal Y} y\,p(y) \\
&= \mathbb E(Y) \tag*{\(\square\)}
\end{align*} 
$$


In case of continuous variables, we have

$$
\begin{align}
\mathsf E(Y) &= \int_\Bbb R y\,f_Y(y)\,\mathrm d y && \text{by definition of expectation} \\[1ex]
&= \int_\Bbb R y\int_\Bbb R f_{Y\mid X}(y\mid x)~f_X(x)\,\mathrm d x\,\mathrm d y &&\text{Law of Total Probability} \\[1ex]
&= \int_\Bbb R f_X(x)\int_\Bbb R y~f_{Y\mid X}(y\mid x)\,\mathrm d y\,\mathrm d x &&\text{Fubini's Theorem } \\[1ex]
&= \int_\Bbb R f_X(x)\,\mathsf E(Y\mid X{\,=\,}x)\,\mathrm d x && \text{by definition of conditional expectation} \\[1ex]
&= \mathsf E\left[\mathsf E(Y\mid X)\right] && \text{by definition of expectation} 
\end{align}
$$


___

**Generalization of LIE in time series**

$$
\mathbb{E}\big[\mathbb{E}(y_{t+2}|x_{t+1}) |x_t \big] = \mathbb{E}[y_{t+2} |x_t]
$$

as $x_{t} \subset x_{t+1}$.


More generally, for any random variable $z$ and two information sets $\mathcal{J}$ and $\mathcal{I}$ with $\mathcal{J} \subset \mathcal{I}$, then

$$
\mathbb{E}\big[\mathbb{E}(x|\mathcal{I}) |\mathcal{J} \big] = \mathbb{E}[x |\mathcal{J}]
$$


___

**Intuition behind the LIE**

Think of $\mathbf{x}$ as a discrete vector taking on possible values $\mathbf{c}_1, \mathbf{c}_2, \ldots, \mathbf{c}_M$ with probabilities $p_1, p_2, \ldots, p_M$. Then LIE says:

$$
\mathbb{E}(y) = p_1 \mathbb{E}(y\vert \mathbf{x}=\mathbf{c}_1) + p_2 \mathbb{E}(y\vert \mathbf{x}=\mathbf{c}_2) + \cdots + p_M \mathbb{E}(y\vert \mathbf{x}=\mathbf{c}_M).
$$

Ths is, $\mathbb{E}(y)$ is simply a weighted average of the $\mathbb{E}(y\vert \mathbf{x}=\mathbf{c}_i)$, where the weight $p_i$ is the probability that $\mathbf{x}$ takes on the value of $\mathbf{c}_i$. In other words, a weighted average of averages.

E.g., suppose we are intrested in average IQ generally, but we have measures of average IQ by gender. We could figure out the quantity of interest by weighting average IQ by the relative proportions of men and women.


Bayes' Theorem 贝叶斯定理

Partition Theorem (total expectation theorem, law of total probability) Ituition

$$
\mathbb{P}(\text{eventual goal}) = \sum_{\text{options}} \mathbb{P}(\text{eventual goal}|\text{option})\, \mathbb{P}(\text{option})
$$

___

**Decomposition of variance**

Or sometimes called **Law of Total Variance**.

$$
\text{Var}(Y) = \text{Var}_\mathbf{x}[\mathbb{E}(y\vert \mathbf{x})]
 + \mathbb{E}_\mathbf{x}[\text{Var}(y\vert \mathbf{x})]
$$

In plain language, the variance of $Y$ deceomposes into the variance of the conditional mean plus the expected variance around the conditional mean.

**Population and Sample**

Population quantities need to know the DGP. Any thing you observe is for samples.

Expectation operator is a linear operator, meaning that we have

$$
\begin{align*}
\mathbb{E}(a+bX)=a+b\,\mathbb{E}(X)
\end{align*}
$$

More generally, let $a_1, \ldots, a_n$ and $b_1, \ldots, b_n$ be sequences of non-random variables and let $X_1, \ldots, X_n$ be a sequence of random variables. Then,  

$$
\begin{align*}
\mathbb{E}\left[\sum_{i=1}^n(a_i+b_iX_i)\right] = \sum_{i=1}^n \mathbb{E}(a_i+b_iX_i) = \sum_{i=1}^n\left(a_i+b_i\mathbb{E}[X_i]\right).
\end{align*}
$$


Linear Transformations of a Random Vector

Let $Y=A+BX$, $X$ is $p\times 1$ random vector, $A$ is $q \times 1$ non-random vector, $B$ is $p\times q$ non-random matrix.

The expected value of this transformation is given by

$$
\mathbb{E}(Y) = A + B\, \mathbb{E}(X)
$$

The variance of this transformation is given by

$$
\text{Var}(Y) = B\, \text{Var}(X)\, B'
$$


A $q \times q$ square matrix $\Sigma$ is called non-negative definite (or *positive semi-definite*) if for any non-zero $q \times 1$ vector $\boldsymbol{a}$ it holds that

$$
\boldsymbol{a}'\Sigma\, \boldsymbol{a} \ge 0
$$

If the square matrix $\Sigma$ is non-negative definite, we write $\Sigma \ge 0$.

Note that all covariance matrix of a random vector is positive semi-definite.

___

**Expectations of Functions of RVs**

If $X$ is a RV, then expected value of $g(X)$ is given by 

$$
\begin{align*}
\mathbb{E}[g(X)] = \left\{
	\begin{array}{ll}
	\int g(x)f(x)dx & \text{for continuous $X$} \\
	\sum_xg(x)f(x) & \text{for discrete $X$}
	\end{array} \right.
\end{align*}
$$

where $f(x)$ is the probability density (mass) function of continuous (discrete) $X$.

Variance is also an expectation by setting $g(X) = \left[X-\mathbb{E}(X)\right]^2$. In other words, $\text{Var}(X) = \mathbb{E}\left[(X-\mathbb{E}(X))^2\right]$.

$$
\begin{align*}
\text{Var}(X) = \mathbb{E}[(X-\mathbb{E}(X))^2] = \left\{
	\begin{array}{ll}
	\int [x-\mathbb{E}(X)]^2 f(x)dx & \text{for continuous $X$} \\
	\sum_x [x-\mathbb{E}(X)]^2 f(x) & \text{for discrete $X$}
	\end{array} \right.
\end{align*}
$$


Example: **Bernoulli**

Let $X \sim \textrm{Bernoulli}(\theta)$, and recall that we have $\mathbb{E}(X)=\theta$. Then

$$
\begin{align*}
\text{Var}(X) &= \mathbb{E}(X-E[X])^2 \\ 
			 &= \sum_x \left(x-\mathbb{E}[X]\right)^2 f(x) \\
			 &= (0-\theta)^2 \times f(0) + (1-\theta)^2\times f(1) \\
			 &= \theta^2(1-\theta) + (1-\theta)^2\theta \\
			 &= \theta (1-\theta).
\end{align*}
$$

Alternative derivation: Since $0^2=0$ and $1^2=1$, we have $X^2=X$ implying that $\mathbb{E}(X^2)=\mathbb{E}(X)=\theta$. Therefore,

$$
\begin{align*}
\text{Var}(X)=\mathbb{E}[X^2]-(\mathbb{E}[X])^2 = \theta-\theta^2
\end{align*}
$$



**Sample mean** Let $X_1, \ldots, X_n$ denote $n$ observations on a variable $X$, the sample mean is

$$
\begin{align*}
\overline{X}=\frac{1}{n}\sum_{i=1}^nX_i
\end{align*}
$$

Sometimes, you add a subscript $n$ to denote the sample size, $\overline{X}_n .$

$\overline{X}$ is a random variable, as it is the average of random variables.
This is in sharp contrast to $\mathbb{E}[X]$ which is non-random.  

$\overline{X}$ varies with each sample.
If we could repeatedly collect new samples of size $n$ from the same population and each time were able to estimate $\overline{X}$, these estimates would be different from each other.
The distribution of a statistic, like $\overline{X}$, is called its **sampling distribution**.  

One useful feature is  $\mathbb{E}[\overline{X}] = \mathbb{E}[X]$.
This doesn't mean that $\overline{X}$ itself is equal to $\mathbb{E}[X]$.  Rather, it means that, if we could repeatedly obtain (a huge number of times) new samples of size $n$ and compute $\overline{X}$ each time, the average of $\overline{X}$ across repeated samples would be equal to $\mathbb{E}[X].$

Proof:

$$
\begin{aligned}
  \mathbb{E}[\overline{X}] &= \mathbb{E}\left[ \frac{1}{n} \sum_{i=1}^n X_i \right] \\
  &= \frac{1}{n} \mathbb{E}\left[ \sum_{i=1}^n X_i \right] \\
  &= \frac{1}{n} \sum_{i=1}^n \mathbb{E}[X_i] \\
  &= \frac{1}{n} \sum_{i=1}^n \mathbb{E}[X]  \;\;\;\; (X_i\text{ are iid with mean } \mathbb{E}[X]) \\
  &= \frac{1}{n}\, n\, \mathbb{E}[X] \\
  &= \mathbb{E}[X]
\end{aligned}
$$


Two ways to compute the **Sample variance** 

- unadjusted sample variance, also called biased sample variance:
$$
\begin{align*}
S_n^2 = \frac{1}{n}\sum_{i=1}^n(X_i-\overline X)^2
\end{align*}
$$

- adjusted sample variance, also called unbiased sample variance 

$$
\begin{align*}
S_n^2 = \frac{1}{n-1}\sum_{i=1}^n(X_i-\overline X)^2
\end{align*}
$$

The latter subtracts 1 from $n$ in the denominator, which is known as a *degrees of freedom correction*.
See proof [here](https://www.statlect.com/fundamentals-of-statistics/variance-estimation).


Distinguish the sample variance $(S^2_n)$ from the variance of sample mean $(\text{Var}(\overline{X}))$. 

**Covariance and Correlation**

*Covariance and correlation* measure the linear association btw two RVs $X$ and $Y$

$$
\begin{aligned}
\gamma &\equiv \text{Cov}(X, Y) = \mathbb{E}\big\{[X-\mathbb{E}(X)][Y-\mathbb{E}(Y)]\big\} \\
\rho &\equiv \frac{\text{Cov}(X, Y)}{\sqrt{\text{Var}(X)\text{Var}(Y)}}
\end{aligned}
$$

where the expected value $\mathbb{E}[\cdot]$ is taken over the joint distribution of $(X,Y)$.

More formally

$$
\begin{aligned}
\textrm{Cov}(X, Y) = \begin{cases}
\sum_y\sum_x[X-\mathbb{E}(X)][Y-\mathbb{E}(Y)]f(x,y) & \textrm{for } X, Y \textrm{ discrete}  \\
\iint[X-\mathbb{E}(X)][Y-\mathbb{E}(Y)]f(x,y) dxdy   & \textrm{for } X, Y \textrm{ continuous}  \\
\end{cases}
\end{aligned}
$$

where the sum and integral are over the supports of $X$ and $Y$.

For linear transformations, we have

$$
\text{Cov}(a+bX, c+dY) = bd\,\text{Cov}(X,Y)
$$

for known constants $a,b,c,d$.

The additive law of covariance holds that the covariance of a random variable with a sum of random variables
is just the sum of the covariances with each of the random variables.

$$
\text{Cov}(X+Y, Z) = \text{Cov}(X,Z) + \text{Cov}(Y,Z)
$$


More generally,

$$
\color{#008B45}\text{Cov}\left(\sum_{i=1}^m a_iX_i, \sum_{j=1}^n b_iY_i\right) =
\sum_{i=1}^m\sum_{j=1}^n a_ib_j\text{Cov}(X_i, Y_j).
$$

One of the applications of covariance is finding the variance of a <span style='color:#008B45'>**sum of several random variables**</span>.
In particular, if $Z=X+Y$, then

$$
\begin{aligned}
\text{Var}(Z) &= \text{Cov}(Z,Z) \\
&= \text{Cov}(X+Y, X+Y) \\
&= \text{Cov}(X,X) + \text{Cov}(X,Y) + \text{Cov}(Y,X) + \text{Cov}(Y,Y) \\
&= \color{#008B45}\text{Var}(X) + \text{Var}(X) + 2\text{Cov}(X,Y).
\end{aligned}
$$

More generally, for $a_i\in \mathbb{R}, i=1,\ldots,n$, we conclude:

$$
\color{#008B45} \text{Var}\left(\sum_{i=1}^n a_iX_i \right) = 
\sum_{i=1}^n a_i^2 \text{Var}(X_i) + \sum_{i=1}^n\sum_{j=1}^n a_ia_j \text{Cov}(X_i, X_j).
$$

Or equivalently, 

$$
\color{#008B45} \text{Var}\left(\sum_{i=1}^n a_iX_i \right) = 
\sum_{i=1}^n a_i^2 \text{Var}(X_i) + 2\sum_{i=2}^n\sum_{j=1}^{i-1} a_ia_j \text{Cov}(X_i, X_j).
$$

If we have either $\mathbb{E}(X)=0$ or $\mathbb{E}(Y)=0$ or both

$$
\text{Cov}(X, Y) = \mathbb{E}{(XY)} - \mathbb{E}{(X)}\mathbb{E}{(Y)} = \mathbb{E}{(XY)}
$$

The *sample covariance*, $\hat{\gamma}$, in a sample of $n$ observations on $(X_i,Y_i)$ is

$$
\hat{\gamma} = \frac{1}{n-1}\sum_{i=1}^n (X_i-\overline{X})(Y_i-\overline{Y})
$$

Division by $n-1$ rather than $n$ is called a degrees of freedom correction.

Correlation is a scaled measure of covariance:

$$
\textrm{Corr}(X,Y)=\frac{\textrm{Cov}(X, Y)}{\sqrt{\text{Var}(X)\text{Var}(Y)}}
$$

If $\textrm{Corr}(X,Y)=0$, we say that $X$ and $Y$ are <span style='color:#008B45FF'>uncorrelated</span> or orthogonal, denoted by $X {\color{#008B45FF}\perp} Y$ (perpendicular symbol).


$X {\color{#008B45FF}\indep} Y$ (double perpendicular symbol) denotes $X$ and $Y$ are <span style='color:#008B45FF'>independent</span>.

$X \indep Y \Rightarrow X \perp Y$,  in plain language, independence implies zero correlation. 

Dependent but uncorrelated example

Let $X\sim U(-1,1)$ (任何定义域centered on zero is ok), $Y=f(X)=X^2$. Then $E[X]=0$. 

$$
\begin{aligned}
\text{Cov}(X, Y) &= E[Xf(X)] - E[X]E[f(X)] \\
&= E[Xf(X)] \quad (E[X]=0) \\
&= \int_{-1}^1 x\,f(x)\,p(x)\, dx
\end{aligned}
$$

where $p(x)$ is the pdf of $X$. 

$$
p(x) = \left\{
\begin{array}{ll}
\frac{1}{2} & x\in [-1,1] \\
0 & \text{otherwise}
\end{array}
\right.
$$

Now we have $X$ as an odd funcction and $[-1,1]$ is a symmetric domain. That means as long as $f(x)$ is an even function, we have $xf(x)p(x)$ as on odd function. It then follows that

$$
\int_{-a}^a x\,f(x)\,p(x)\, dx = 0,
$$

and so $\text{Cov}(X, f(X))=0$. 

$f(X)=X^2$ is an even function, which satisfies the condition.


___

**Properties of covariance**

1. The covariance of a variable with itself is the variance of the random variable.

    $$
    \cov(X, X) = \var(X)
    $$
2. The covariance of a random variable, $X$, with a constant, $c$ is zero.
  
    $$
    \cov(c, X) = 0 
    $$
3. The covariance is commutative.
  
    $$
    \cov(X, Y) = \cov(Y,X)
    $$
4. If $X$ and $Y$ are independent then 

    $$\cov(X,Y)=0$$
5. Adding a constant to either or both random variables does not change their covariances.

    $$
    \cov(X+c, Y+k) = \cov(X,Y)
    $$
6. Multiplying a random variable by a constant multiplies the covariance by that constant.

    $$
    \cov(cX, kY) = ck\times\cov(X,Y)
    $$
7. The covariance of a random variable with a sum of random variables is the sum of the covariances with each of the random variables.

    $$
    \cov(X+Y, Z) = \cov(X,Z) + \cov(Y,Z)
    $$
8. More generally, covariance of sum of random variables:

    $$
    \cov\left(\sum_{i=1}^ma_iX_i, \sum_{j=1}^nb_jY_j\right)= \sum_{i=1}^m\sum_{j=1}^na_ib_j\cov(X_i,Y_j)
    $$

___

Properties for correlation coefficients

1. Adding a constant to a random variable does not change their correlation coefficient.

    $$
    \cor(X+c, Y+k) = \cor(X,Y)
    $$
2. Multiplying a random variable by a constant does not change their correlation coefficient.

    $$
    \cor(cX, dY) = \cor(X,Y)
    $$

___

## Joint Distributions and Independence

**Joint Distribution Function (Joint CDF)**

$$
\begin{aligned}
F(x_1, x_2) &= P(X_1\le x_1, X_2\le x_2) \\
&= \left\{
	\begin{array}{ll}
	\displaystyle \int_{-\infty}^{x_1}\int_{-\infty}^{x_2} f(a, b)\, \mathrm da\, \mathrm db & \text{continuous} \\
	\displaystyle  \sum_{a\le x_1} \sum_{b\le x_2} f(a,b) & \text{discrete}
	\end{array} \right.
\end{aligned}
$$



**Joint Density Function (Joint PDF)**

$$
f\,(x_1, x_2) =  \left\{
	\begin{array}{ll}
	\displaystyle \frac{\partial^2F(x_1, x_2)}{\partial x_1\, \partial x_2} & \text{continuous} \\ 
	\displaystyle  P(X_1=x_1, X_2=x_2) & \text{discrete}
	\end{array} \right.
$$

In other words, for the continuous case, $f(x_1,x_2)$ is the function that satisfies

$$
F(x_1, x_2) = \int_{\infty}^{x_2}\int_{\infty}^{x_1} f(a,b)\, \mathrm da\mathrm db
$$

**Marginals**

Consider a discrete random vector, when one of these entries is taken in isolation, its distribution can be characterized in terms of its probability mass function. This is called *marginal probability mass function*, in order to distinguish it from the *joint probability mass function* (PMF), which is instead used to characterize the joint distribution of all the entries of the random vector considered together.


**Formal Definition** Let $X_1, \ldots, X_K$ be $K$ discrete random variable forming a $K\times 1$ random vector. Then, for each $i=1,\ldots,K,$ the probability mass function of the random variable $X_i$, denoted by $p_{X_i}(x_i)\, ,$ is called <span style='color:#008B45FF'>**marginal probability mass function**</span>. 

$p_{X_i}(x_i)$ is a function: $\mathbb R \mapsto [0,1]$ such that 

$$
p_{X_i}(x_i) = P(X_i=x_i)
$$

where $p_{X_i}(x_i)$ is the probability that $X_i$ will be equal to $x_i$.

By contrast, the <span style='color:#008B45FF'>**joint probability mass function**</span> of the vector $X$ is a function $p_X: \mathbb R^K \mapsto [0,1]$ such that

$$
p_{X}(x) = p_{X_1,\ldots,X_K}(x_1, \ldots, x_K) = P(X_1=x_1, \ldots, X_K=x_k)
$$

where $P(X_1=x_1, \ldots, X_K=x_k)$ is the probability that $X_i$ will be equal to $x_i$, simultaneously for all $i=1,\ldots, K\,.$


**Marginal PMFs**

The marginal PMF of $X$ is given by

$$
\begin{align*}
P_X(x) &= P(X=s) \\
&= \sum_{y_j\in R_Y} P(X=x, Y=y_j) \quad \text{(Law of total probability)} \\
&= \sum_{y_j\in R_Y} P_{XY}(x, y_j)
\end{align*}
$$

where $R_Y=\{y_1,y_2,\ldots\}$ is the range of $Y$.


Similarly, the marginal PMF of $Y$ is given by

$$
P_Y(y) = \sum_{x_i\in R_X} P_{XY}(x_i, y)
$$

where $R_X=\{x_1,x_2,\ldots\}$ is the range of $X$.

We can define the *joint range* for $X$ and $Y$ as

$$
R_{XY} = \{(x,y) | P_{XY}(x,y) >0 \} \, .
$$

Equivalently, we can also write

$$
\begin{aligned}
R_{XY} &\subset R_X \times R_Y \\
&= \{(x_i,y_j) | x_i\in R_X, y_j\in R_Y \} \, .
\end{aligned}
$$


Note that 

- The event $X=x$ can be written as $\{(x_i,y_j): x_i=x, y_j \in R_Y \}\, .$
- Also, the event $Y=y$ can be written as $\{(x_i,y_j): x_i\in R_X, y_j=y\}\, .$

___

It is called *marginalization* or *integrating out* $X_2$ to get the marginal of $X_1$. \
The marginal of one variable can be obtained by integrating the other variable. This applies to $n$-dimension.

$$
f_{X_1}(k) =  \left\{
	\begin{array}{ll}
	\displaystyle \int_{-\infty}^\infty f(k, x_2) \, \mathrm dx_2 & \text{continuous} \\
	\displaystyle \sum_{x_2} f(X_1=k,X_2=x_2) & \text{discrete}
	\end{array} \right.  
$$

Marginalizaing the joint density w.r.t. $X_1$ to get the marginal of $X_2$.

$$
f_{X_2}(k) =  \left\{
	\begin{array}{ll}
	\displaystyle \int_{-\infty}^\infty f(x_1,k) \, \mathrm dx_1 & \text{continuous} \\
	\displaystyle \sum_{x_1} f(X_1=x_1,X_2=k) & \text{discrete}
	\end{array} \right. 
$$


where $\sum_{x_1}$ and $\sum_{x_2}$ mean sum over all values of $x_1$ and $x_2$, respectively.


**Marginal CDFs**

If we know the joint CDF of $X_1$ and $X_2$, we can find the marginal CDFs, $F_{X_1}(x_1)$ and $F_{X_2}(x_2)$. Specifically, for any $x \in \mathbb{R}$, we have

$$
F_{X_1}(x_1) = P(X_1\le x_1) = P(X_1\le x_1, X_2\le \infty) 
= F_{X_1X_2}(x_1,\infty) 
= \lim_{x_2\to\infty} F_{X_1X_2}(x_1,x_2) \, .
$$

Similarly,

$$
F_{X_2}(x_2) = P(X_2\le x_2) = P(X_1\le \infty, X_2\le x_2) 
= F_{X_1X_2}(\infty,x_2)
= \lim_{x_1\to\infty} F_{X_1X_2}(x_1,x_2) \, .
$$

___


**Example**

Suppose we have a pair of discrete random variable $\{(X, Y )\}$, with an associated joint probability tabulated mass, $f_{XY} (x,y)$, as tabulated below.

<table class="table-sm" style="max-width: 70%; margin-left: auto;margin-right: auto;"><thead>
  <tr>
    <th></th>
    <th></th>
    <th colspan="3" style="text-align: center; border-bottom: 1pt solid gray; border-left: 1pt solid gray; ">$X$</th>
  </tr></thead>
<tbody>
  <tr >
    <td></td>
    <td></td>
    <td style="border-bottom: 1pt solid gray; border-left: 1pt solid gray; text-align: center;">1</td>
    <td style="border-bottom: 1pt solid gray; text-align: center;">2</td>
    <td style="border-bottom: 1pt solid gray; text-align: center;">3</td>
  </tr>
  <tr>
    <td rowspan="3" style="border-top: 1pt solid gray; font-weight:bold; text-align: right; border-right: 1pt solid gray; width: 10%;">$Y$</td>
    <td style="border-right: 1pt solid gray; border-top: 1pt solid gray; width: 15%; text-align: center; ">-1</td>
    <td style="text-align: center;">0.1</td>
    <td style="text-align: center;">0.1</td>
    <td style="text-align: center;">0.0</td>
  </tr>
  <tr>
    <td style="border-right: 1pt solid gray; text-align: center; ">0</td>
    <td style="text-align: center;">0.2</td>
    <td style="text-align: center;">0.0</td>
    <td style="text-align: center;">0.3</td>
  </tr>
  <tr>
    <td style="border-right: 1pt solid gray; text-align: center; ">2</td>
    <td style="text-align: center;">0.1</td>
    <td style="text-align: center;">0.2</td>
    <td style="text-align: center;">0.0</td>
  </tr>
</tbody>
</table>


The sum of all probabilities should be equal to 1.

$$
\sum_{i}\sum_{j} f_{X,Y} (x_i, y_j) = 1
$$

To calculate the *marginal masses*, we sum along either the rows or the columns, respectively. 

Summing along the rows ($X$) gives us the marginal probability of $Y$.

$$
\begin{aligned}
f_Y(Y=-1) &= \sum_{i=1}^3 f_{X,Y}(x_i, -1) = 0.1+0.1+0 = 0.2 \\
f_Y(Y=0) &= \sum_{i=1}^3 f_{X,Y}(x_i, 0) = 0.2+0+0.3 = 0.5 \\
f_Y(Y=2) &= \sum_{i=1}^3 f_{X,Y}(x_i, 2) = 0.1+0.2+0 = 0.3
\end{aligned}
$$

While summing along the columns ($Y$) gives us the marginal probability of $X$.

$$
\begin{aligned}
f_X(X=1) &= \sum_{j=1}^3 f_{X,Y}(1, y_j) = 0.1+0.2+0.1 = 0.4 \\
f_X(X=2) &= \sum_{j=1}^3 f_{X,Y}(2, y_j) = 0.1+0+0.2 = 0.3 \\
f_X(X=3) &= \sum_{j=1}^3 f_{X,Y}(3, y_j) = 0+0.3+0 = 0.3
\end{aligned}
$$

Then the calculation of expectations is straightforward:

$$
\begin{aligned}
\mathbb E(X) &= \sum_i x_i f_X(x_i) = 1\times 0.4 + 2\times 0.3 + 3\times 0.3 = 1.9 \\
\mathbb E(Y) &= \sum_i y_i f_Y(y_i) = -1\times 0.2 + 0\times 0.5 + 2\times 0.3 = 0.4 
\end{aligned}
$$

so that, $\mathbb E (X)\, \mathbb E (Y)= 0.76\,.$ 

After some calculation, summing over the entire table:

$$
\mathbb E(XY) = \sum_{i,j}x_i y_j f_{X,Y}(x_i, y_j) =0.7 \,.
$$

Since $\mathbb E(XY)=0.7\neq \mathbb E(X)\mathbb E(Y)$, thus $X$ and $Y$ are correlated.


___

### Independence

Two random variables $X_1$ and $X_2$ are independent if and only if

$$
F_{X_1X_2}(x_1, x_2) = F_{X_1}(x_1) F_{X_2}(x_2)
$$

where $F_{X_1X_2}(x_1, x_2)$ is their joint distribution function and $F_{X_1}(x_1)$ and $F_{X_2}(x_2)$ are their marginal distribution function.

The joint probability density function, $f_{X_1X_2}(x_1, x_2),$ is also the product of their marginal probability density functions.

$$
f_{X_1X_2}(x_1, x_2) = f_{X_1}(x_1) f_{X_2}(x_2)
$$


___

### Conditioning

Conditional density:

$$
\begin{aligned}
f_{X_1\vert X_2}(X_1=x_1\vert X_2=x_2) &= \frac{f_{X_1 X_2}(X_1=x_1, X_2=x_2)}{f_{X_2}(X_2=x_2)} \\
f_{X_2\vert X_1}(X_2=x_2\vert X_1=x_1) &= \frac{f_{X_1 X_2}(X_1=x_1, X_2=x_2)}{f_{X_1}(X_1=x_1)} 
\end{aligned}
$$

Note that nominator is the <span style='color:#337ab7'>joint density</span>, denominator is the <span style='color:#337ab7'>marginal density</span>.\
Conditinal pdf could be written more succinctly as

$$
\begin{aligned}
f_{X_1\vert X_2}(x_1\vert x_2) &= \frac{f_{X_1 X_2}(x_1, x_2)}{f_{X_2}(x_2)} \\
f_{X_2\vert X_1}(x_2\vert x_1) &= \frac{f_{X_1 X_2}(x_1, x_2)}{f_{X_1}(x_1)} ,
\end{aligned}
$$

or we can drop the subscripts all together

$$
\begin{aligned}
f(x_1\vert x_2) &= \frac{f(x_1, x_2)}{f(x_2)} \\
f(x_2\vert x_1) &= \frac{f(x_1, x_2)}{f(x_1)} .
\end{aligned}
$$

Here, we use the lower case letters to denote the actual values the RV's take.


Multiplication Rule

$$
\begin{aligned}
f(x_1, x_2) &= f(x_1\vert x_2)\, f(x_2) \\
&= f(x_2\vert x_1)\, f(x_1)
\end{aligned}
$$

Conditional cdf is integrated based on conditional pdf:

$$
\begin{aligned}
F_{X_1\vert X_2}(x_1\vert X_2=x_2) &=  P(X_1\le x_1 \vert X_2=x_2) \\
&= \left\{
\begin{array}{ll}
	\int_{-\infty}^{x_1} f_{X_1\vert X_2}(s {\color{#008B45FF}\vert X_2=x_2}) \, \mathrm ds & \text{continuous} \\
	\sum_{s\le x_1} f_{X_1\vert X_2}(X_1=s {\color{#008B45FF}\vert X_2=x_2})  &\text{discrete}
\end{array} \right. 
\end{aligned}
$$

or could be written more succinctly as

$$
\begin{aligned}
F(x_1\vert x_2)  &=  P(X_1\le x_1 \vert X_2=x_2) \\
&=  \left\{
\begin{array}{ll}
	\int_{-\infty}^{x_1} f(s{\color{#008B45FF}\vert x_2})\, \mathrm ds & \text{continuous} \\
	\sum_{s\le x_1} f(X_1=s {\color{#008B45FF}\vert X_2=x_2})  &\text{discrete}
\end{array} \right. 
\end{aligned}
$$

Expectation 

$$
\mathbb{E}[h(X,Y)] = \int_{-\infty}^\infty\int_{-\infty}^\infty h(x,y)\, f_{XY}(x,y) \, \mathrm dx \mathrm dy
$$

Conditional expectation on $X$ is indicated using a subscript in $\mathbb{E}_X$, e.g.,

$$
\mathbb{E}_X[h(X, Y)] = \mathbb{E}[h(X, Y)|X] =  \int_{-\infty}^\infty h(x,y) f_{h(X,Y)|X} (h(x,y)|x) \mathrm dy
$$

Here, we "integrate out" the $Y$ variable, and we are left with a function of $X$.

It is also possible the subscript indicates marginal density.

$$
\mathbb{E}_X[h(X, Y)] = \int_{-\infty}^\infty h(x,y) f_X(x) \mathrm dx
$$

Here, we "average over" the $X$ variable, and we are left with a function of $Y$.


___

### **Conditional expectation for several variables**

We extend to three variables.

We have the following probability mass function:

$$
P(X=x, Y=y, Z=z) = P(x,y,z) \, ,
$$

where we use some shorthand, $P(X=x_i, Y=y_j \vert Z=z_k) = P(x,y\vert z)$.

Joint marginal mass is given by

$$
\begin{aligned}
P(x,y) &= \sum_z P(x,y,z) \\
P(x,z) &= \sum_y P(x,y,z) \\
P(y,z) &= \sum_x P(x,y,z) 
\end{aligned} .
$$


The joint conditional probability is given by

$$
P(x,y|z) = \frac{P(x,y,z)}{P(z)} \, ,
$$

and the conditional probability.

$$
P(x|y,z) = \frac{P(x,y,z)}{P(y,z)} \, .
$$


We have the following useful lemmas.

- <span style='color:#337ab7'>**Linearity**</span>: 

$$
\mathbb E(aX+bY\vert Z) = a \mathbb E(X\vert Z) + b \mathbb E(Y\vert Z)
$$

- <span style='color:#337ab7'>**Pull-through rule**</span>: 

  $$
  \mathbb E\left[g(X)\,h(Y)\vert Y\right] = h(Y)\, \mathbb E\left[g(X)\vert Y\right]
  $$

  Proof:

  $$
  \begin{align*}
    E\left[g(X)h(Y)\vert Y\right] &= \sum_x g(x) h(y) P(x|y) \\
    &= h(y) \sum_x g(x) P(x|y) \\
    &= h(y)\, \mathbb E[g(X)|Y=y] \tag*{\(\square\)}
  \end{align*} 
  $$

- <span style='color:#337ab7'>**Tower rule**</span>: 

  $$
  \mathbb E\left[ \mathbb E\left(Z\vert X,Y\right) \vert Y\right] = \mathbb E \left[ \mathbb E(Z\vert Y) \vert Y, X\right ]= \mathbb E[Z\vert Y]
  $$

  This is a generalization of the conditional expectation theorem.

  Proof:

  $$
  \begin{align*}
  E\left[ \mathbb E\left(Z\vert X,Y\right) \vert Y\right] 
  &= \sum_x \mathbb E\left(Z\vert X,Y\right) P(x|y) \\
  &= \sum_x \left[\sum_z z P(z|x,y)\right] P(x|y) \\
  &= \sum_x \sum_z z \, \frac{P(x,y,z)}{P(x,y)} \times \frac{P(x,y)}{P(y)} \\
  &= \sum_x\sum_z z\, \frac{P(x,y,z)}{P(y)}  \\
  &= \sum_x\sum_z z\, P(x,z|y)  \\
  &= \sum_z z\, P(z|y) \\
  &= \mathbb E(Z|Y)
  \end{align*} 
  $$


___


## Moments


We often summarise properties of distributions using their moments.


The $r^{\text{th}}$ order moment is defined by

$$
\begin{aligned}
\mathbb{E}(X^r) = \left\{
\begin{array}{ll}
	\int_{-\infty}^\infty x^r f(x)dx & \text{continuous} \\
	\sum_x x^r f(x) &\text{discrete}
\end{array} \right.
\end{aligned}
$$


### First order moment

The first moment is called the expected value or expectation, which is given by 

$$
\begin{aligned}
\mathbb{E}(X) = \left\{
\begin{array}{ll}
	\int_{-\infty}^\infty x f(x)dx & \text{continuous} \\
	\sum_x x f(x)  &\text{discrete}
\end{array} \right. 
\end{aligned}
$$

### Second moment about the mean

Also called second central moment.
The variance is obtained by setting $g(X)=\left[X-\mathbb{E}(X)\right]^2.$

$$
\begin{aligned}
\text{Var}(X) = \mathbb{E}[\left(X-\mathbb{E}(X)\right)^2] = \left\{
\begin{array}{ll}
	\int_{-\infty}^\infty \left[X-\mathbb{E}(X)\right]^2 f(x)dx & \text{continuous} \\
	\sum_x \left[X-\mathbb{E}(X)\right]^2 f(x) &\text{discrete}
\end{array} \right. 
\end{aligned}
$$

Unconditional expectation of functions of RVs

$$
\begin{aligned}
\mathbb{E}[g(x)] = \left\{
\begin{array}{ll}
	\int_{-\infty}^\infty g(x){\color{red}f(x)}dx & \text{continuous} \\
	\sum_x g(x){\color{red}f(x)} &\text{discrete}
\end{array} \right.  
\end{aligned}
$$

Conditional expectation of functions of RVs

$$
\begin{aligned}
\mathbb{E}(g(x) \vert Y=y) = \left\{
\begin{array}{ll}
	\int_{-\infty}^\infty g(x){\color{#008B45FF}f(x\vert Y=y)}dx & \text{continuous} \\
	\sum_x g(x){\color{#008B45FF}f(x\vert Y=y)} &\text{discrete}
\end{array} \right.  
\end{aligned}
$$

Note: 
- For <span style='color:red'>unconditional</span> moments, use the appropriate <span style='color:red'>unconditional</span> density.
- For <span style='color:#008B45FF'>conditional</span> moments, use the appropriate <span style='color:#008B45FF'>conditional</span> density.
- Expectation or expected value is a population quantity because it requires knowledge of the density function.
- The sample analogue of the expected value is the sample mean or sample average.


Conditional and Unconditional Variance

Unconditional 

$$
\begin{aligned}
\text{Var}(X) &= \mathbb{E} [(X-\mathbb{E}(X))^2] \\
&= \left\{
\begin{array}{ll}
	\int_{-\infty}^{\infty} \left(x-\mathbb{E}(X) \right)^2 f(x) dx & \text{continuous} \\
	\sum_{x} \left(x-\mathbb{E}(X) \right)^2 f(x)  &\text{discrete}
	\end{array} \right. 
\end{aligned}
$$

Conditional variance use conditional expectations

$$
\begin{aligned}
\text{Var}(X{\color{#008B45FF}\vert Y}) &= \mathbb{E} [(X-\mathbb{E}(X{\color{#008B45FF}\vert Y}))^2 {\color{#008B45FF}\vert Y}] \\
&= \left\{
\begin{array}{ll}
	\int_{-\infty}^{\infty} [x-\mathbb{E}(X{\color{#008B45FF}\vert Y=y})]^2 f(x{\color{#008B45FF}\vert y}) dx & \text{continuous} \\
	\sum_{x} [x-\mathbb{E}(X{\color{#008B45FF}\vert Y=y})]^2 f(x{\color{#008B45FF}\vert y})  &\text{discrete}
	\end{array} \right. 
\end{aligned}
$$

Alternatively, the conditional variance can be written as 

$$
\text{Var}(X{\color{#008B45FF}\vert Y}) = \mathbb{E}[X^2{\color{#008B45FF}\vert Y}] - \left(\mathbb{E}[X{\color{#008B45FF}\vert Y} ]\right )^2
$$

Independence conditional on other variables

$X_1$ and $X_2$ are said to be independent conditional on $X_3$ if 

$$
f(x_1, x_2 \vert x_3) = f(x_1\vert x_3) f(x_2\vert x_3)
$$

The left-hand-side (LHS) represents the joint behavior of $X_1$ and $X_2$ conditional on $X_3$, the RHS represents the individual behavior conditional on $X_3$.

This is denoted as 

$$
X_1 \indep X_2 \vert X_3
$$

Note that this <span style='color:#008B45FF'>does not imply</span> $X_1 \indep X_2$! \
E.g., $X_1$ and $X_2$ can be returns on two equities where $X_3$ is some global macroeconomic factor affecting multiple variables at once (e.g. federal reserve interest rate). \
Another example for $X_1, X_2$ would be wages and level of education, whereas $X_3$ is level of intelligence.

For three or more RVs, the joint PDF, joint PMF, and joint CDF are defined in a similar way to what we have seen for the case of two random variables. \
Let $X_1, X_2, \ldots, X_n$ be $n$ discrete RVs. The joint PMF is defined as 

$$
P_{X_1, X_2, \ldots, X_n} (x_1, x_2, \ldots, x_n) = P(X_1=x_1, X_2=x_2, \ldots, X_n=x_n).
$$

For $n$ jointly continuous RVs $X_1, X_2, \cdots, X_n$, the joint PDF is defined to be the function $f_{X_1, X_2, \cdots, X_n}(x_1, x_2, \cdots, x_n)$ such that the probability of any set $A\in \mathbb{R}^n$ is given by the integral of the PDF over the set $A$. In particular, we can write

$$
P\big((X_1, X_2, \cdots, X_n)\in A\big) = \int \cdots \underset{A}{\int} \cdots \int f_{X_1, X_2, \cdots, X_n}(x_1, x_2, \cdots, x_n) dx_1dx_2\cdots dx_n.
$$

<div class = "boxed">
<strong>Definition</strong>  $X_1, X_2, \cdots, X_n$ are said to be independent and identically distributed (iid) if they are independent, and they have the same marginal distributions:

$$
F_{X_1}(x) = F_{X_2}(x) = \cdots = F_{X_n}(x), \text{for all } x\in\mathbb{R}.
$$

</div>



The *moment-generating function* (MGF) of a random variable $X$ is

$$
M_X(t) = E(e^{tX}) = \begin{cases}
\displaystyle \int_{-\infty}^{\infty} e^{tx} f_X(x) \mathrm ds  & \text{continuous } X \\
\displaystyle \sum_{i=0}^\infty e^{tx_i} P(X=x_i) & \text{discrete } X 
\end{cases}
$$

- The MGF of X gives us all moments of X. That is why it is called the moment generating function. 

    We can obtain all moments of $X$:

    $$
    \mu_n = E[X^n] = M_X^{(n)} (0) = \left. \frac{\mathrm d^n M_X}{\mathrm dt^n} \right\vert_{t=0} \,.
    $$

    That is, the $n$th moment about zero is the <span style='color:#337ab7'>$n$th derivative of the moment generating function</span>, evaluated at $t=0.$

- The MGF (if it exists) uniquely determines the distribution.



Linear Algebra \
<https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab>



___

**Convergence**
- Formal definition of convergence is: \
  Let $X_n=c+\frac{1}{n}$ for $n=1,2, \ldots$ and some constant $c$. $X_n$ converges to $c$ iff for $\forall \delta>0$, there exists some values $n^{\ast}$ such that for all $n>n^*$ we have $\vert X_n-c \vert < \delta$.

- Convergence in Probabiliy, $\lim_{n\to\infty}P(\vert X_n-c\vert < \varepsilon) =1$, denoted as $\text{plim}_{n\to\infty}X_n=c$, or $X_n \xrightarrow{p} c$.

- Almost Sure Convergence, $P(\lim_{n\to\infty}\vert X_n-c\vert =0)=1$, denoted as $X_n \xrightarrow{a.s.} c$.

- Convergence in Mean Square, $\lim_{n\to\infty}\mathbb{E}[(X_n-c)^2]=0$,  denoted as $X_n \xrightarrow{m.s.} c$.

- Convergence in Distribution, $P(X_n\le x) \rightarrow P(X\le x)$ as $n\rightarrow \infty$, $X_n\xrightarrow{d}X$. If $X\sim N(\mu, \sigma^2)$, then $X_n \xrightarrow{d} N(\mu, \sigma^2)$.

Note: 
- Convergence in probability is weaker than both a.s. and m.s. convergence. Obtaining any type of convergence is sufficient. In certain cases, proving one type can be easier than another type.
- Convergence in probability implies convergence in distribution. Convergence in probability means that two objects converge to each other. Convergence in distribution means that the distributions of two different objects become the same.

**Consistent estimator**

$\hat{\theta}$ is a consistent estimator of $\theta$ if 

$$
  \hat{\theta} \xrightarrow{p} \theta.
$$


## Law of Large Numbers (LLN)

- Chebyshev's (week) LLN\
  Let $X_1, \ldots, X_n$ be an iid sequence with mean $\mathbb{E}(X_i)=\mu$ and $\text{Var}(X_i)=\sigma^2$. Then,

  $$
  \begin{align*}
  \frac{1}{n}\sum_{i=1}^nX_i &\xrightarrow{p} \mathbb{E}(X_i). \\
  (\text{i.e., } \overline{X}_n &\xrightarrow{p} \mu )
  \end{align*}
  $$

  LLN tells us that the sample mean is a consistent estimator of the expected value. \
  Note that 3 assumptions need to be satisfied: 
  1. $X_1, \ldots, X_n$ are an iid distributed;
  2. exist finite mean $\mu$; and
  3. exist finite variance $\sigma^2$.


- Kolmogorov's (strong) LLN \
  Let $X_1, \ldots, X_n$ be an iid sequence with mean $\mathbb{E}(X_i)=\mu$. Then

  $$
  \frac{1}{n}\sum_{i=1}^nX_i \xrightarrow{a.s.} \mathbb{E}(X_i).
  $$

  Note that the strong LLN requires *only finite mean*.

  Kolmogorov's LLN is very hard to prove. Weak LLN can be easily proved by showing m.s. convergence, which implies convergence in probability.

  Proof of weak LLN:

  Let $$\overline{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$$ be the sample average. 
  To prove weak LLN, we can show $\lim_{n\to\infty}\mathbb{E}(\overline{X}_n-\mu)^2=0$.

  $$
  \begin{align*}
  \lim_{n\to\infty}\mathbb{E}(\overline{X}_n-\mu)^2 &=
  \lim_{n\to\infty} \text{Var}[\overline{X}_n] \\
  &= \lim_{n\to\infty} \frac{\sigma^2}{n} \\
  &= 0
  \end{align*}
  $$
  
  This shows $\overline{X}_n \xrightarrow{m.s} \mu$, which implies $\overline{X}_n \xrightarrow{p} \mu$.

- LLN for random vectors \
  For $\boldsymbol{y}\in \mathbb{R}^m$, if $\boldsymbol{y}_i$ are independent and identically distributed and $E\,\vert\vert \boldsymbol{y} \vert\vert <\infty$, then as $n\to\infty$,

  $$
  \overline{\boldsymbol{y}} = \frac{1}{n}\sum_{i=1}^n\boldsymbol{y}_i \xrightarrow{p} E\,[\boldsymbol{y}].
  $$

  Note: convergence in probability of a vector can be defined as convergence in probability of all elements in the vector.

  $E\,\vert\vert \boldsymbol{y} \vert\vert <\infty \Leftrightarrow E\,\vert y_j \vert <\infty $. Saying that the expected value of Euclidean norm is finite is equivalent to say that the expected value of each element is finite.

  $$
  \overline{\boldsymbol{y}} = \frac{1}{n}\sum_{i=1}^n\boldsymbol{y}_i = \begin{pmatrix} 
  \overline{y}_1 \\
  \overline{y}_2 \\
  \vdots         \\
  \overline{y}_m \\
  \end{pmatrix}
  $$

  - <span style='color:#797D7F'> $E\,\vert\vert \boldsymbol{y} \vert\vert <\infty$ indicates 1st moment finite; </span>
  - <span style='color:#797D7F'> $E\,\vert\vert \boldsymbol{y} \vert\vert^2 <\infty$ indicates 2nd moment finite.  </span>
  

  **Ergodic Theorem**

  If $\boldsymbol{y}_t$ is strictly stationary, ergodic, and $E\,\vert\vert \boldsymbol{y} \vert\vert <\infty $, then as $n\to\infty$,

  $$
  E\vert\vert \overline{\boldsymbol{y}}-\boldsymbol{\mu} \vert\vert \to 0
  $$

  and

  $$
  \overline{\boldsymbol{y}} \xrightarrow{p} \boldsymbol{\mu}
  $$

  where $\boldsymbol{\mu}=E[\boldsymbol{y}_t]$.

  The ergodic theorem shows that ergodicity is sufficient for consistent estimation.

  Note that instead of requireing iid, ergodicity imposes a weaker assumption which requires only stationarity and ergodicity. That is, serial dependence is allowed for in the time series.



**Unbiasedness vs Consistency**

- Unbiasedness, $\mathbb{E}(\hat{\theta})=\theta$, is a finite sample property, that holds for any sample size.
- Consistency, $\hat{\theta}\xrightarrow{p}\theta$, is a asymptotic property, that holds in the limit as $n\to \infty$.
- Note: neither property implies the other. 
  + If we are interested in bias, we take the **expectation** on both sides of the equation.
  + When we are interested in consistency we take the **probability limit**.


___

## Central Limit Theorem (CLT)

Suppose that $X_1, \ldots, X_n$ is an iid sequence with mean $\mathbb{E}(X_i)=\mu$ and $\text{Var}(X_i)=\sigma^2$. Let $\overline{X}=\sum_{i=1}^n X_i.$ Then,

$$
\frac{\overline{X}-\mathbb{E}[\overline{X}]}{\sqrt{\text{Var}[\overline{X}]}} 
= \frac{\overline{X}-\mu}{\sqrt{\sigma^2/n}} 
= {\color{#008B45FF} \sqrt{n}} \cdot \frac{\overline{X}-\mu}{\sigma} 
\xrightarrow{d} N(0,1)
$$

equivalently, we can write 

$$
\sqrt{n}\cdot\frac{\overline{X}-\mu}{\sigma} 
\overset{a}{\sim} N(0,1)
$$

$\overset{\rm a}{\sim}$ means "*approximately distributed with*". \
Or we can also write as

$$
\begin{align*}

\begin{array}{rlrl}
	\sqrt{n} (\overline{X}-\mu)  &\xrightarrow{d} N(0,\sigma^2),  &
  \sqrt{n} (\overline{X}-\mu)  &\overset{a}{\sim} N(0,\sigma^2) \\
  
  \overline{X} -\mu  &\xrightarrow{d} N(0,\sigma^2/n), &
  \overline{X} -\mu  &\overset{a}{\sim} N(0,\sigma^2/n) \\

  \overline{X} &\xrightarrow{d} N(\mu,\sigma^2/n), &
  {\color{#008B45FF} \overline{X}} & {\color{#008B45FF} \overset{a}{\sim} N(\mu,\sigma^2/n) }.
\end{array} 

\end{align*}
$$

Note: The CLT is a very powerful result. $X_1, \ldots, X_n$ can be from any possible distribution (*iid* with *finite mean and variance*), and still their normalized sample mean will be standard normal.

- In practice, we replace $\sigma$ with $\widehat{\sigma}$ because we do not observe $\sigma$ but we do observe $\widehat{\sigma}$.
- Population variance estimators, $\widehat{\sigma}^2$. Two versions: 
  - biased sample variance: $$s_1^2 = \frac{1}{n} \sum_{i=1}^n [(X_i-\overline{X})^2]$$ and 
  - unbiased sample variance: $$s_2^2 = \frac{1}{n-1} \sum_{i=1}^n [(X_i-\overline{X})^2]$$
  - Both options are consistent; using either is fine.

Define the *partial sum* $S_n := \sum_{i=1}^n X_i = n\overline{X}_n$. By LLN, we have

$$
\frac{\overline{X}-\mu}{\sigma/\sqrt{n}} \xrightarrow{d} N(0,1) 
$$

Multiply the denominator and numerator by $n$, we have

$$
\begin{align*}
\frac{n\overline{X}-n\mu}{n\cdot\sigma/\sqrt{n}}  = \frac{S_n-n\mu}{\sigma\sqrt{n}} 
\end{align*}
$$

which converges in distribution to

$$
\frac{S_n-n\mu}{\sigma \sqrt{n}} \xrightarrow{d} N(0,1) .
$$


### MDS CLT

CLT for martingale differences


We are interested in an asymptotic approximation for the distribution of standardized sample means such as

$$
\boldsymbol{S}_n = \frac{1}{\sqrt{n}} \sum_{t=1}^n \boldsymbol{u}_t
$$

where $\boldsymbol{u}_t$ is mean zero with finite variance $E[\boldsymbol{u}_t\boldsymbol{u}_t']=\boldsymbol{\Sigma}<\infty$.

The MDS CLT theorem says if $\boldsymbol{u}_t$ is a strictly stationary and ergodic martingale difference sequence and $E[\boldsymbol{u}_t\boldsymbol{u}_t']=\boldsymbol{\Sigma}<\infty$, then as $n\to\infty,$

$$
\boldsymbol{S}_n = \frac{1}{\sqrt{n}} \sum_{t=1}^n \boldsymbol{u}_t \overset{d}{\to} N(\boldsymbol{0}, \boldsymbol{\Sigma}).
$$

The conditions for the theorem are similar to the Lindeberg-Lévy CLT. The only difference is that the i.i.d. assumption has been replaced by the assumption of a strictly stationarity and ergodic MDS.


___


## Big-O Little-o Notation

Consider a sequence of random variables $X_n$ and a sequence of constants $a_n$ for $n = 1, 2, . . .$\
If $X_n/a_n \xrightarrow{p} 0$, we say $(X_n/a_n)=o_p(1)$ or $X_n=o_p(a_n)$.\
Consequently:
1. If $X_n\xrightarrow{p}0$, we say $X_n=o_p(1)$.
2. If $n^\alpha X_n\xrightarrow{p}0$ for some $\alpha$, we say $X_n/n^{-\alpha}=o_p(1)$ or $X_n=o_p(n^{-\alpha})$.

E.g., For $X_1, X_2, \ldots, X_n$ iid with mean $\mu$ and variance $\sigma^2$, by the LLN we have $\overline{X}\xrightarrow{p}\mu$. Then, $\overline{X}-\mu\xrightarrow{p}0$ and so $\overline{X}-\mu = o_p(1)$.

Big-O notation relaxes the convergence to a finite limit (zero or non-zero). \
If $X_n/a_n \xrightarrow{d} X$ or $X_n/a_n \xrightarrow{p} X$, we say $(X_n/a_n)=O_p(1)$ or $X_n=O_p(a_n)$.\
Consequently:
1. If $X_n\xrightarrow{d}X$ or $X_n\xrightarrow{p}X$, we say $X_n=O_p(1)$.
2. If $n^\alpha X_n\xrightarrow{d}X$ or $n^\alpha X_n\xrightarrow{p}X$ for some $\alpha$, we say $X_n/n^{-\alpha}=O_p(1)$ or $X_n=O_p(n^{-\alpha})$.

E.g., For $X_1, X_2, \ldots, X_n$ iid with mean $\mu$ and variance $\sigma^2$, define $Z=\frac{\overline{X}-\mu}{\sigma}$. Then, by the CLT we have $\sqrt{n}Z\xrightarrow{d}N(0,1)$ and so $\sqrt{n}Z = O_p(1)$ or equivalently $Z=O_p(n^{-1/2})$.


___

## Type I and II Errors

Type I error: rejecting a true $H_0$. Corresponds to the *level of significance*, $\alpha$, 

$$
\alpha = P(\text{reject } H_0 \vert H_0 \text{ is true})\,.
$$

Type II error: failing to reject a false $H_0$. The probability of committing a Type II error is called $\beta\,.$

$$\beta=P(\text{fail to reject} H_0\vert H_0 \text{ is false})\,.$$

$\beta$ is related to the *Power of a test*.
$\beta = 1-\text{Power of a test} = 1-P(\text{reject } H_0\vert H_0 \text{ is false})\,.$

In hypothesis testing, the <span style='color:#008B45'>*size of a test*</span> is the (maximum) probability of committing a Type I error, that is, of incorrectly rejecting the null hypothesis when it is true.

The <span style='color:#008B45'>*power of a test*</span> refers to the probability of correctly rejecting $H_0$ when $H_1$ is true.




<img src="https://drive.google.com/thumbnail?id=1U8Hk_KJfWT5fL6eUgEcPNiiSrueLSfC3&sz=w1000" alt="type-i-and-type-ii-error" style="display: block; margin-right: auto; margin-left: auto; zoom:50%;" />


Note:
- If $\alpha$ increases that means the chances of making a type I error will increase. It is more likely that a type I error will occur. It makes sense that you are less likely to make type II errors, only because you will be rejecting $H_0$ more often. You will be failing to reject $H_0$ less, and therefore, the chance of making a type II error will decrease. Thus, as $\alpha$ increases, $\beta$ will decrease, and vice versa. That makes them seem like complements, but they are not complements.
- For a constant sample size, $n$, if  $\alpha$  increases, $\beta$ decreases. \
For a constant significance level,  $\alpha$ , if $n$ increases, $\beta$ decreases.

**Confusion matrix**

<img src="https://drive.google.com/thumbnail?id=11N5Zr3pnTKJiTAlStrvt3hervdmG3XNj&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

**Precision** is the proportion of all the model's positive classifications that are actually positive.

$$
\text{Precision} = 
\frac{\text{correctly classified actual positives}}
{\text{everything classified as positive}} 
= \frac{TP}{TP+FP}
$$


The **True Positive Rate** (TPR), or the proportion of all actual positives that were classified correctly as positives, is also known as **recall**.

A hypothetical perfect model would have zero false negatives and therefore a recall (TPR) of 1.0, which is to say, a 100% **detection rate**.

In an imbalanced dataset where the number of actual positives is very low, recall is a more meaningful metric than accuracy because it measures the ability of the model to correctly identify all positive instances. For applications like disease prediction, <u>correctly identifying the positive cases is crucial</u>. A false negative typically has more serious consequences than a false positive. 

$$
\text{Recall (or True Positive Rate, TPR)} = 
\frac{\text{correctly classified actual positives}}
{\text{all actual positives}} 
= \frac{TP}{TP+FN}
$$


The **False Positive Rate** (FPR) is the proportion of all actual negatives that were classified incorrectly as positives, also known as the **probability of false alarm**. 

$$
\text{FPR} =
\frac{\text{incorrectly classified actual negatives}}
{\text{all actual negatives}}
= \frac{FP}{FP+TN}
$$

Precision improves as false positives decrease, while recall improves when false negatives decrease.


**Receiver-operating characteristic curve** (ROC)

The ROC curve is a visual representation of model performance across all thresholds.


The ROC curve is drawn by calculating the true positive rate (TPR) and false positive rate (FPR) at every possible threshold (in practice, at selected intervals), then graphing TPR over FPR. 


A perfect model, which at some threshold has a TPR of 1.0 and a FPR of 0.0, can be represented by either a point at (0, 1) if all other thresholds are ignored, or by the following:

<figure style="text-align: center;">
<img src="https://developers.google.com/static/machine-learning/crash-course/images/auc_1-0.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:60%;" />
<figcaption>ROC and AUC of a hypothetical perfect model. Source: <a href="https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc#:~:text=The%20ROC%20curve%20is%20a,holdover%20from%20WWII%20radar%20detection.">Machine Learning, Google for Developers.</a> </figcaption>
</figure>

Toggle thresholds and see how metrics and ROC curve change:
<https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc#auc_and_roc_for_choosing_model_and_threshold>


The area under the ROC curve (AUC) represents the probability that the model, if given a randomly chosen positive and negative example, will rank the positive higher than the negative.

<figure style="text-align: center;">
<img src="https://developers.google.com/static/machine-learning/crash-course/images/auc_0-5.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:100%;" />
<figcaption>ROC and AUC of completely random guesses.</figcaption>
</figure>


For a binary classifier, a model that does exactly as well as random guesses or coin flips has a ROC that is a diagonal line from (0,0) to (1,1). The AUC is 0.5, representing a 50% probability of correctly ranking a random positive and negative example.

The points on a ROC curve closest to (0,1) represent a range of the best-performing thresholds for the given model.

<figure style="text-align: center;">
<img src="https://developers.google.com/static/machine-learning/crash-course/images/auc_abc.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:100%;" />
<figcaption>Three labeled points representing thresholds.</figcaption>
</figure>

If false positives (false alarms) are highly costly, it may make sense to choose a threshold that gives a lower FPR, like the one at point A, even if TPR is reduced. Conversely, if false positives are cheap and false negatives (missed true positives) highly costly, the threshold for point C, which maximizes TPR, may be preferable. If the costs are roughly equivalent, point B may offer the best balance between TPR and FPR.

A concrete example: Imagine a situation where it's better to allow some spam to reach the inbox than to send a business-critical email to the spam folder. You've trained a spam classifier for this situation where the positive class is spam and the negative class is not-spam. In this use case, it's better to minimize false positives, even if true positives also decrease. Choose point A.


___

Q: When should we use one-tailed hypothesis testing? \
A: Authors should explain why they are more interested in an effect in one direction not the other.

Ex1: we compare the mean strength of parts from a supplier (102) to a target value (100). We are considering a new supplier only if the mean strength of their parts is greater than our target value. There is no need for us to distinguish between whether their parts are equally strong or less strong than the target value — either way we'd just stick with our current supplier.

$H_0$: new supplier = target value \
$H_1$: new supplier > target value 


Ex1: We want to know if the battery life is greathn than the orignal after a manufacturing change.

$H_0$: new battery life = original life \
$H_1$: new battery life > original life

- One-tailed test improve the power of a test, that is correctly reject $H_0$ if the null hypothesis is truly false.

___


**log-transformed Models**

1.  **Only the dependent/response variable is log-transformed**. Exponentiate the coefficient. This gives the multiplicative factor for every one-unit increase in the independent variable. Example: the coefficient is 0.198. exp(0.198) = 1.218962. For every one-unit increase in the independent variable, our dependent variable increases by a factor of about 1.22, or 22%. Recall that multiplying a number by 1.22 is the same as increasing the number by 22%. Likewise, multiplying a number by, say 0.84, is the same as decreasing the number by 1 – 0.84 = 0.16, or 16%. 
2.  **Only independent/predictor variable(s) is log-transformed**. Divide the coefficient by 100. This tells us that a 1% increase in the independent variable increases (or decreases) the dependent variable by (coefficient/100) units. Example: the coefficient is 0.198. 0.198/100 = 0.00198. For every 1% increase in the independent variable, our dependent variable increases by about 0.002. For x percent increase, multiply the coefficient by log(1.x). Example: For every 10% increase in the independent variable, our dependent variable increases by about 0.198 * log(1.10) = 0.02.
3.  **Both dependent/response variable and independent/predictor variable(s) are log-transformed**. Interpret the coefficient as the percent increase in the dependent variable for every 1% increase in the independent variable. Example: the coefficient is 0.198. For every 1% increase in the independent variable, our dependent variable increases by about 0.20%. For x percent increase, calculate 1.x to the power of the coefficient, subtract 1, and multiply by 100. Example: For every 20% increase in the independent variable, our dependent variable increases by about (1.20 0.198 – 1) * 100 = 3.7 percent.







___

Semi-parametric models

-   Method of Moments
-   quantile regression


___

**Textbooks**

-   **Econometric Analysis** , 5th Edition, by William H. Greene, Prentice Hall, 2003. \
    **Time Series Analysis**, by J. D. Hamilton, Princeton University Press, 1994. \
    **Estimation and Inference in Econometrics**, by R. Davidon and J. MacKinnon, Oxford University Press, 1993. \
    **Econometric Analysis of Cross Section and Panel Data**, by J. Wooldridge, MIT Press, 1999. \
    **Microeconometrics: Methods and Applications**, Cameron, A. C. and Trivedi, P. K., Cambridge University Press, 2005.

-   **Core Metrics textbooks**

    - Casella, G. and Berger, R.L. (2002) ***Statistical Inference***. 2nd ed. Duxbury.
    - Hendry, D.F. and Nielsen, B. (2007) ***Econometric Modeling***. Princeton.
    - Hoel, P.G., Port, S.C. and Stone, C.J. (1971) ***Introduction to Probability***. Boston: Houghton-Mifflin.

