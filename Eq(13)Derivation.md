<!--
 * @Author: CTC 2801320287@qq.com
 * @Date: 2023-07-16 16:27:41
 * @LastEditors: CTC_322 2310227@tongji.edu.cn
 * @LastEditTime: 2023-07-20 14:47:44
 * @Description: 
 * 
 * Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
-->
# Deriving Equation (13)

Invariant Flag: An invariant maximal flag for the matrices $\{A_i\}_{i=1}^{m}$ is a set of subspaces $\{ S_{j} \}_{j=1}^{n}$ which follows:

$$
A_{i} S_{j} \subset S_{j}, \text{ while } S_{j} \nsubseteq S_{j + 1}.
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
    &= \sum_{k = 1}^{n} \varepsilon_{k} \mathrm{Re} \left( \vec{v}_{k}^{H} A_{i} \sum_{j_{1}=1}^{n} \left( c_{j_{1}} \vec{v}_{j_{1}} \right) \sum_{j_{2}=1}^{n} \left( c_{j_{2}} \vec{v}_{j_{2}}^{H} \right) \vec{v}_{k} \right) \\
    &= \sum_{k = 1}^{n} \varepsilon_{k} \mathrm{Re} \left( \vec{v}_{k}^{H} A_{i} \sum_{j_{1}=1}^{n} \left( c_{j_{1}} \vec{v}_{j_{1}} \right) c_{k} \vec{v}_{k}^{H} \vec{v}_{k} \right) \qquad (\{ \vec{v}_{k} \} \text{ is an orthonormal basis of } \mathbb{C}^{n}) \\
    &= \sum_{k = 1}^{n} \varepsilon_{k} \mathrm{Re} \left( c_{k} \vec{v}_{k}^{H} A_{i} \sum_{j_{1}=1}^{n} \left( c_{j_{1}} \vec{v}_{j_{1}} \right) \vec{v}_{k}^{H} \vec{v}_{k} \right) \\
\end{aligned}
$$