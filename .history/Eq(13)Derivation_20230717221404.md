<!--
 * @Author: CTC 2801320287@qq.com
 * @Date: 2023-07-16 16:27:41
 * @LastEditors: CTC 2801320287@qq.com
 * @LastEditTime: 2023-07-17 22:14:04
 * @Description: 
 * 
 * Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
-->
# Deriving Equation (13)

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
    &=
\end{aligned}
$$

$$
\begin{aligned}
    \vec{x} \vec{x}^{H} &= \left( \sum_{j_{1}=1}^{n} c_{j_{1}} \vec{v}_{j_{1}} \right) \left( \sum_{j_{2}=1}^{n} c_{j_{2}} \vec{v}_{j_{2}}^{H} \right) \\
    &= \sum_{j_{1}=1}^{n} \left( \sum_{j_{2}=1}^{n} c_{j_{1}} c_{j_{2}} \vec{v}_{j_{1}} \vec{v}_{j_{2}}^{H} \right)
\end{aligned}
$$

As we assume that $\{\vec{v}_{j} \} \; (j \in \{ 1,2,\cdots,n \})$ is an orthonormal basis of $\mathbb{C}^{n}$, we can derive that

$$
\vec{v}_{i} \vec{v}_{j}^{H} = 
$$

$$
\begin{aligned}
    \dot{V}(\vec{x}) &= \sum_{k = 1}^{n} \varepsilon_{k} \vec{v}_{k}^{H} \left( A_{i} \vec{x} \vec{x}^{H} + \vec{x} \vec{x}^{H} A_{i}^{H} \right) \vec{v}_{k} \\
    &= \sum_{k = 1}^{n} \varepsilon_{k} \vec{v}_{k}^{H} \left( A_{i} \vec{x} \vec{x}^{H} + \vec{x} \vec{x}^{H} A_{i}^{H} \right) \vec{v}_{k}
\end{aligned}
$$






















