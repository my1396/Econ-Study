---
layout: post
title: Taylor Series
tag: study
update: 2024-03-10
---

Taylor Polynomial at $x=a$

- Constant: $f(x) \approx f(a)$
- Linear: $f(x) \approx f(a) + f'(a)(x-a)$
- Quadratic $f(x) \approx f(a) + f'(a)(x-a) + \frac{1}{2}f''(a)(x-a)^2$ 

We write $f^{(n)}(x)$ to mean the $n$th derivative of $f(x)$, and $T_n(x)$ to mean the $n$th degree Taylor polynomial of $f(x)$.

$$
\begin{aligned}
T_n(x) &= f(a) + f'(a)(x-a) + \frac{1}{2}f''(a)(x-a)^2 + \cdots + \frac{1}{n!}f^{(n)}(a)(x-a)^n \\
&= \sum_{i=0}^n \frac{f^{(i)}(a)}{i!} (x-a)^i
\end{aligned}
$$

If $a=0$, we call the function a **Maclaurin polynomial**.

$$
\begin{aligned}
T_n(x) &= f(0) + f'(0)x + \frac{1}{2}f''(0)x^2 + \cdots + \frac{1}{n!}f^{(n)}(0)x^n \\
&= \sum_{i=0}^n \frac{f^{(i)}(0)}{i!} x^i
\end{aligned}
$$

Tayloar and Maclaurin series are expansions of infinite degrees.

- Taylor series: $f(x) = \sum_{i=0}^{\infty} \frac{f^{(i)}(a)}{i!} (x-a)^i$
- Maclaurin series: $f(x) = \sum_{i=0}^\infty \frac{f^{(i)}(0)}{i!} x^i$

Note that the derivatives are taken at $x=a$.

Important Taylor Series Expansions

| Function and Series                    | First Few Terms                            | Interval of Convergence |
| -------------------------------------- | ------------------------------------------ | ----------------------- |
| $e^x=\sum_{n=0}^\infty \frac{x^n}{n!}$ | $1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots$ | $(-\infty, \infty)$     |
| $\frac{1}{1-x}=\sum_{n=0}^\infty x^n$  | $1+x+x^2+x^3+\cdots$                       | $(-1,1)$                |



**Algebra of Power Series**

Let $f(x)=\sum_{n=0}^\infty a_nx^n$ and $g(x)=\sum_{n=0}^\infty b_nx^n$ converge absolutely for $\vert x\vert<R$, and let $h(x)$ be continuous.

1. $f(x)\pm g(x) = \sum_{n=0}^\infty (a_n\pm b_n)x^n\quad$ for $\vert x\vert<R$.
2. $f(x)\, g(x) = (\sum_{n=0}^\infty a_nx^n)(\sum_{n=0}^\infty b_nx^n) = \sum_{n=0}^\infty (a_0b_n + a_1b_{n-1} + \ldots + a_nb_0)x^n\quad$ for $\vert x\vert<R$. 
3. $f(h(x)) = \sum_{n=0}^\infty a_n (h(x))^n \quad$  for $\vert h(x)\vert <R$.  We simply substitute $h(x)$ for $x$ in the series.















