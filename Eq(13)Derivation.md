<!--
 * @Author: CTC 2801320287@qq.com
 * @Date: 2023-07-16 16:27:41
 * @LastEditors: CTC 2801320287@qq.com
 * @LastEditTime: 2023-07-23 17:44:34
 * @Description: 
 * 
 * Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
-->
# Deriving Equation (13)

Invariant Flag: An invariant maximal flag for the matrices $\{A_i\}_{i=1}^{m}$ is a set of subspaces $\{ S_{j} \}_{j=1}^{n}$ which follows:

$$
A_{i} S_{j} \subset S_{j}, \text{ while } S_{j} \subsetneq S_{j + 1}.
$$

By setting $S_{j} = \mathrm{span} \{ \vec{v}_{1}, \vec{v}_{2}, \cdots, \vec{v}_{j} \}$, one can clearify the invariant flag's physical meaning. Deriving $\{ S_{j} \}_{j=1}^{n}$ is the process of obtaining a set of basis $(\vec{v}_{1}, \vec{v}_{2}, \cdots, \vec{v}_{j})$ which triangularizes all $A_{i}$ matrixes(each corresponds to a linear subsystem) simultaneously.

The Lyapunov function $V(\vec{x})$ is defined as

$$
\begin{aligned}
    V(\vec{x}) &= \sum_{k = 1}^{n} \varepsilon_{k} |\vec{v}_{k}^{H} \vec{x}|^{2} \\
    &= \sum_{k = 1}^{n} \varepsilon_{k} \vec{x}^{H} \vec{v}_{k} \vec{v}_{k}^{H} \vec{x}
\end{aligned}
$$

Where $\varepsilon_{k}>0,k=0,1,\cdots,n$. $\vec{v}_{k}^{H}$ denotes the conjugate transpose of $\vec{v}_{k}$.

Then, we can obtain

$$
\begin{aligned}
    \dot{V}(\vec{x}) &= \sum_{k = 1}^{n} \varepsilon_{k} \frac{d}{dt} \left(\vec{v}_{k}^{H} \vec{x} \vec{x}^{H} \vec{v}_{k} \right) \\
    &= \sum_{k = 1}^{n} \varepsilon_{k} \left( \vec{v}_{k}^{H} \frac{d \vec{x}}{dt} \vec{x}^{H} \vec{v}_{k} + \vec{v}_{k}^{H} \vec{x} \frac{d \vec{x}^{H}}{dt} \vec{v}_{k} \right) \\
    &= \sum_{k = 1}^{n} \varepsilon_{k} \left( \vec{v}_{k}^{H} A_{i} \vec{x} \vec{x}^{H} \vec{v}_{k} + \vec{v}_{k}^{H} \vec{x} \vec{x}^{H} A_{i}^{H} \vec{v}_{k} \right) \\
    &= \sum_{k = 1}^{n} \varepsilon_{k} \vec{v}_{k}^{H} \left( A_{i} \vec{x} \vec{x}^{H} + \vec{x} \vec{x}^{H} A_{i}^{H} \right) \vec{v}_{k} \\
    &= 2 \sum_{k = 1}^{n} \varepsilon_{k} \mathrm{Re} \left( \vec{v}_{k}^{H} A_{i} \vec{x} \vec{x}^{H} \vec{v}_{k} \right)
\end{aligned}
$$

For $\vec{x} = \sum_{j=1}^{n} c_{j} \vec{v}_{j}$, it follows that

$$
\begin{aligned}
    \sum_{k = 1}^{n} \varepsilon_{k} \mathrm{Re} \left( \vec{v}_{k}^{H} A_{i} \vec{x} \vec{x}^{H} \vec{v}_{k} \right) &= \sum_{k = 1}^{n} \varepsilon_{k} \mathrm{Re} \left( \vec{v}_{k}^{H} A_{i} \sum_{j=1}^{n} \left( c_{j} \vec{v}_{j} \right) \vec{x}^{H} \vec{v}_{k} \right) \\
    &= \sum_{k = 1}^{n} \varepsilon_{k} \mathrm{Re} \left( \vec{v}_{k}^{H} A_{i} \sum_{j_{1}=1}^{n} \left( c_{j_{1}} \vec{v}_{j_{1}} \right) \sum_{j_{2}=1}^{n} \left( c_{j_{2}}^{H} \vec{v}_{j_{2}}^{H} \right) \vec{v}_{k} \right) \\
    &= \sum_{k = 1}^{n} \varepsilon_{k} \mathrm{Re} \left( \vec{v}_{k}^{H} A_{i} \sum_{j_{1}=1}^{n} \left( c_{j_{1}} \vec{v}_{j_{1}} \right) c_{k}^{H} \vec{v}_{k}^{H} \vec{v}_{k} \right) \qquad (\{ \vec{v}_{k} \} \text{ is an orthonormal basis of } \mathbb{C}^{n}) \\
    &= \sum_{k = 1}^{n} \varepsilon_{k} \mathrm{Re} \left( c_{k}^{H} \vec{v}_{k}^{H} A_{i} \sum_{j_{1}=1}^{n} \left( c_{j_{1}} \vec{v}_{j_{1}} \right) \vec{v}_{k}^{H} \vec{v}_{k} \right) \\
\end{aligned}
$$

Assume that $\Vert \vec{v}_{j} \Vert=1$ (MENTIONED LATER IN SOURCE PAPER). Then,

$$
\begin{aligned}
    \sum_{k = 1}^{n} \varepsilon_{k} \mathrm{Re} \left( \vec{v}_{k}^{H} A_{i} \vec{x} \vec{x}^{H} \vec{v}_{k} \right)
    &= \sum_{k = 1}^{n} \varepsilon_{k} \mathrm{Re} \left( c_{k}^{H} \vec{v}_{k}^{H} A_{i} \sum_{j_{1}=1}^{n} \left( c_{j_{1}} \vec{v}_{j_{1}} \right) \vec{v}_{k}^{H} \vec{v}_{k} \right) \\
    &= \sum_{k = 1}^{n} \varepsilon_{k} \mathrm{Re} \left( c_{k}^{H} \vec{v}_{k}^{H} A_{i} \sum_{j_{1}=1}^{n} \left( c_{j_{1}} \vec{v}_{j_{1}} \right) \right) \\
    &= \sum_{k = 1}^{n} \varepsilon_{k} \mathrm{Re} \left( c_{k}^{H} \vec{v}_{k}^{H} A_{i} \sum_{j = 1}^{n} \left( c_{j} \vec{v}_{j} \right) \right) \\
    &= \sum_{j = 1}^{n} \sum_{k = 1}^{n} \varepsilon_{k} \mathrm{Re} \left( c_{j} c_{k}^{H} \vec{v}_{k}^{H} A_{i} \vec{v}_{j} \right)
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
    \dot{V}(\vec{x})
    &= 2 \sum_{k = 1}^{n} \varepsilon_{k} \mathrm{Re} \left( \vec{v}_{k}^{H} A_{i} \vec{x} \vec{x}^{H} \vec{v}_{k} \right) \\
    &= 2 \sum_{j = 1}^{n} \sum_{k = 1}^{n} \varepsilon_{k} \mathrm{Re} \left( c_{j} c_{k}^{H} \vec{v}_{k}^{H} A_{i} \vec{v}_{j} \right)
\end{aligned}
$$

From the definition of invariant maximal flag, we're able to obtain that

$$
\forall \vec{v_{j}} \in S_{k}, \quad A_{i} \vec{v}_{j} \in S_{k + 1}. \\
\Rightarrow \text{If} \quad j < k, \quad \vec{v}_{k}^{H} A_{i} \vec{v}_{j} =0.
$$

Since all elements of $S_{j - 1}$ can be expressed with elements in $S_{j}$, but not vice versa, we can rewrite all elements of $S_{j}$ with two parts:

$$
\vec{v}_{j} = \vec{v}_{i,j} + \vec{w}.
$$

Where

$$
\vec{v}_{i,j} \in S_{j}, \qquad \vec{w} \in S_{j - 1}.
$$

The author mentioned that $\vec{v}_{i,j}$ is an eigenvector of $A_{i}$. If $\vec{v}_{i,j}$ isn't an eigenvector of $A_{i}$, then

$$
\underbrace{A_{i} \vec{w}}_{\in S_{j - 1} \subsetneq S_{j}} + \underbrace{A_{i} \vec{v}_{i,j}}_{\notin S_{j}} = A_{i} \vec{v}_{j} \notin S_{j}.
$$

Therefore $\vec{v}_{i,j}$ is an eigenvector of $A_{i}$.

We have that

$$
\begin{aligned}
    \vec{v}_{j}^{H} A_{i} \vec{v}_{j} &= \vec{v}_{k}^{H} A_{i} ( \vec{v}_{i,j} + \vec{w} ) \\
    &= \vec{v}_{j}^{H} (A_{i} \vec{v}_{i,j}) \\
    &= \vec{v}_{j}^{H} \lambda_{i,j} \vec{v}_{i,j} \\
    &= \lambda_{i,j}
\end{aligned}
$$

We're able to rewrite $\dot{V}(\vec{x})$ now:

$$
\begin{aligned}
    \dot{V}(\vec{x}) &= 2 \sum_{j = 1}^{n} \sum_{k = 1}^{n} \varepsilon_{k} \mathrm{Re} \left( c_{j} c_{k}^{H} \vec{v}_{k}^{H} A_{i} \vec{v}_{j} \right) \\
    &= 2 \sum_{j = 1}^{n} \sum_{k = 1}^{j} \varepsilon_{k} \mathrm{Re} \left( c_{j} c_{k}^{H} \vec{v}_{k}^{H} A_{i} \vec{v}_{j} \right) \\
    &= 2 \sum_{j = 1}^{n} \varepsilon_{j} \mathrm{Re} \left( \Vert c_{j} \Vert^{2} \vec{v}_{j}^{H} A_{i} \vec{v}_{j} \right) + 2 \sum_{j = 2}^{n} \sum_{k = 1}^{j - 1} \varepsilon_{k} \mathrm{Re} \left( c_{j} c_{k}^{H} \vec{v}_{k}^{H} A_{i} \vec{v}_{j} \right) \\
    &= 2 \sum_{j = 1}^{n} \varepsilon_{j} \Vert c_{j} \Vert^{2} \mathrm{Re} \left( \lambda_{i,j} \right) + 2 \sum_{j = 2}^{n} \sum_{k = 1}^{j - 1} \varepsilon_{k} \mathrm{Re} \left( c_{j} c_{k}^{H} \vec{v}_{k}^{H} A_{i} \vec{v}_{j} \right) \\
\end{aligned}
$$

For any function $f(k)$ about $k$, there exists

$$
\begin{aligned}
    \sum_{j = 2}^{n} \sum_{k = 1}^{j - 1} f(k) &= \underbrace{f(1)}_{j = 2} + \underbrace{f(1) + f(2)}_{j = 3} + \cdots + \underbrace{f(1) + f(2) + \cdots + f(n - 1)}_{j = n} \\
    &= (n - 1) f(1) + (n - 2) f(2) + \cdots + \left(n - (n - 1) \right) f(n - 1) + \left(n - n \right) f(n) \\
    &= \sum_{j' = 1}^{n} (n - j') f(n) \\
    &= (n - 1) f(1) + \sum_{j = 1}^{n} (n - j) f(n)
\end{aligned}
$$

We noticed that

$$
\begin{aligned}
    \sum_{j = 2}^{n} \sum_{k = 1}^{j - 1} \frac{\varepsilon_{j} \lVert c_{j} \rVert^{2} \mathrm{Re} \left( \lambda_{i,j} \right) + \varepsilon_{k} \Vert c_{k} \Vert^{2} \mathrm{Re} \left( \lambda_{i,k} \right)}{n - 1}
    &= \sum_{j = 2}^{n} (j - 1) \frac{\varepsilon_{j} \lVert c_{j} \rVert^{2} \mathrm{Re} \left( \lambda_{i,j} \right)}{n - 1} + \sum_{j = 2}^{n} (n - j) \frac{\varepsilon_{j} \lVert c_{j} \rVert^{2} \mathrm{Re} \left( \lambda_{i,j} \right)}{n - 1} + (n - 1) \left. \left[ \frac{\varepsilon_{j} \lVert c_{j} \rVert^{2} \mathrm{Re} \left( \lambda_{i,j} \right)}{n - 1} \right] \right \vert_{j = 1} \\
    &= \sum_{j = 2}^{n} (n - 1) \frac{\varepsilon_{j} \lVert c_{j} \rVert^{2} \mathrm{Re} \left( \lambda_{i,j} \right)}{n - 1} + \left. \left[ \varepsilon_{j} \lVert c_{j} \rVert^{2} \mathrm{Re} \left( \lambda_{i,j} \right) \right] \right \vert_{j = 1} \\
    &= \sum_{j = 2}^{n} \varepsilon_{j} \lVert c_{j} \rVert^{2} \mathrm{Re} \left( \lambda_{i,j} \right) + \left. \left[ \varepsilon_{j} \lVert c_{j} \rVert^{2} \mathrm{Re} \left( \lambda_{i,j} \right) \right] \right \vert_{j = 1} \\
    &= \sum_{j = 1}^{n} \varepsilon_{j} \lVert c_{j} \rVert^{2} \mathrm{Re} \left( \lambda_{i,j} \right)
\end{aligned}
$$

Therefore, $\dot{V}(\vec{x})$ can be written as

$$
\begin{aligned}
    \dot{V}(\vec{x}) &= 2 \sum_{j = 1}^{n} \varepsilon_{j} \Vert c_{j} \Vert^{2} \mathrm{Re} \left( \lambda_{i,j} \right) + 2 \sum_{j = 2}^{n} \sum_{k = 1}^{j - 1} \varepsilon_{k} \mathrm{Re} \left( c_{j} c_{k}^{H} \vec{v}_{k}^{H} A_{i} \vec{v}_{j} \right) \\
    &= 2 \sum_{j = 2}^{n} \sum_{k = 1}^{j - 1} \frac{\varepsilon_{j} \lVert c_{j} \rVert^{2} \mathrm{Re} \left( \lambda_{i,j} \right) + \varepsilon_{k} \Vert c_{k} \Vert^{2} \mathrm{Re} \left( \lambda_{i,k} \right)}{n - 1} + 2 \sum_{j = 2}^{n} \sum_{k = 1}^{j - 1} \varepsilon_{k} \mathrm{Re} \left( c_{j} c_{k}^{H} \vec{v}_{k}^{H} A_{i} \vec{v}_{j} \right) \\
    &= 2 \sum_{j = 2}^{n} \sum_{k = 1}^{j - 1} \left[ \frac{\varepsilon_{j} \lVert c_{j} \rVert^{2} \mathrm{Re} \left( \lambda_{i,j} \right) + \varepsilon_{k} \Vert c_{k} \Vert^{2} \mathrm{Re} \left( \lambda_{i,k} \right)}{n - 1} + \varepsilon_{k} \mathrm{Re} \left( c_{j} c_{k}^{H} \vec{v}_{k}^{H} A_{i} \vec{v}_{j} \right) \right]
\end{aligned}
$$
