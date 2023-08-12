<!--
 * @Author: CTC 2801320287@qq.com
 * @Date: 2023-08-05 16:16:25
 * @LastEditors: CTC 2801320287@qq.com
 * @LastEditTime: 2023-08-09 20:10:21
 * @Description: Koopman Common Control Lyapunov Function
 * 
 * Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
-->
# What's NEW?

Mugisho's work provided a novel framework to construct a common Lyapunov function for nonlinear systems by introducing **Koopman Operator Theory** to traditional Lie-algebraic sufficient condition of uniform stability of switched systems. However, the choice of lifting functions, as well as basis of tangental space(for the construction of CLF) are neglected.

Like common approximations of infinite-dimensional Koopman operators, data-driven methods should be applied when obtaining linear mapping of the higher-dimensional dynamics. Moreover, such process enables us improve the construction of measurement space(or lifting space), providing better linear mapping approximation in a sparser form, as is illustrated later.

## 1. Autonomous Systems

For autonomous systems, we can derive and improve a linear approximation of Koopman operator as follows:

1. We assume the lifting function to be $\vec{y}_{N \times 1} = g(\vec{x}_{n \times 1})$. The lifted dynamics follows:

   $$
   \vec{y}'_{N \times 1} = A_{N \times N} \vec{y}_{N \times 1}
   $$

2. Arrange snapshot data of $\vec{y}$ into two data matrixes $Y$ and $Y'$:

   $$
   Y = \begin{bmatrix}
    \vert & \vert & & \vert \\
    \vec{y}_{0} & \vec{y}_{1} & \cdots & \vec{y}_{m - 1} \\
    \vert & \vert & & \vert \\
   \end{bmatrix}, \quad
   Y' = \begin{bmatrix}
    \vert & \vert & & \vert \\
    \vec{y}_{1} & \vec{y}_{2} & \cdots & \vec{y}_{m} \\
    \vert & \vert & & \vert \\
   \end{bmatrix}.
   $$

   $Y$ and $Y'$ have the following relationship:

   $$
   \begin{aligned}
    Y'_{N \times m} &= A_{N \times N} Y_{N \times m} \\
    A_{N \times N} &= \argmin_{A}{\lVert Y'_{N \times m} - A_{N \times N} Y_{N \times m} \rVert_{F}} \\
    &= Y'_{N \times m} Y_{N \times m}^{\dagger},
   \end{aligned}
   $$

   where $\lVert \cdot \rVert_{F}$ is the Frobenius norm and $\dagger$ denotes pseudo-inverse.
3. Compute the singular value decomposition of $Y$, truncate to $r$th rank.

   $$
   \begin{aligned}
   Y_{N \times m}&=U_{N \times m} \Sigma_{m \times m} (V_{m \times m})^{H}\\
   &\approx \tilde{U}_{N \times r} \tilde{\Sigma}_{r \times r} (\tilde{V}_{m \times r})^{H},
   \end{aligned}
   $$

   where $H$ denotes the conjugate transpose, $r$ is the rank of truncation. The left singular vectors $U$ are known as POD modes. $U$, $\tilde{U}$, $V$ and $\tilde{V}$ are orthonormal, they satisfy:

   $$
   U^{H} U = I_{N \times N}, \quad \tilde{U}^{H} \tilde{U} = I_{N \times N}, \\
   V^{H} V = I_{m \times m}, \quad \tilde{V}^{H} \tilde{V} = I_{m \times m}.
   $$

4. Matrix $A$ may be obtained with the pseudo-inverse of $X$ obtained via the SVD:

   $$
   \begin{aligned}
      A_{N \times N}&=X'_{N \times m} (X_{N \times m})^{\dagger}\\
      &=X'_{N \times m} \tilde{V}_{m \times r} (\tilde{\Sigma}_{r \times r})^{-1} (\tilde{U}_{N \times r})^{H}
   \end{aligned}
   $$

5. As we only focus on the leading $r$ eigen-pairs of $A$(in other words, the leading $r$ features of the autonomous dynamical system), we may thus project $A$ onto the POD modes in $U$, so as to lower the rank of our approximation model:

   $$
   \begin{aligned}
   \tilde{A}_{r \times r}&=(\tilde{U}_{N \times r})^{H} A_{N \times N} \tilde{U}_{N \times r}\\
   &=(\tilde{U}_{N \times r})^{H} X'_{N \times m} \tilde{V}_{m \times r} (\tilde{\Sigma}_{r \times r})^{-1} (\tilde{U}_{N \times r})^{H} \tilde{U}_{N \times r}\\
   &=(\tilde{U}_{N \times r})^{H} X'_{N \times m} \tilde{V}_{m \times r} (\tilde{\Sigma}_{r \times r})^{-1}
   \end{aligned}
   $$

   In our lower-rank approximation, the discrete-time mapping is defined with the reduced-order $\tilde{A}$ for the dynamics of $\vec{x}$ projected on POD modes:

   $$
   (\tilde{\vec{y}}_{k+1})_{r \times 1}=\tilde{A}_{r \times r} (\tilde{\vec{y}}_{k})_{r \times 1}
   $$

   Matrix $\tilde{U}$ provides a linear mapping to reconstruct the full state $\vec{y}$:

   $$
   \vec{y}=\tilde{U}\tilde{\vec{y}}
   $$

6. Compute the spectral decomposition of $\tilde{A}$:

   $$
   \tilde{A}_{r \times r} W_{r \times r}=W_{r \times r} \Lambda_{r \times r},
   $$

   where $W$'s columns are $\tilde{A}$'s eigenvectors, $\Lambda$ is a diagonal matrix composed of $\tilde{A}$'s eigenvalues.

7. Reconstruct the high-dimensional DMD modes $\Phi$ according to:

   $$
   \Phi_{n \times r} = X'_{n \times m} \tilde{V}_{m \times r} (\tilde{\Sigma}_{r \times r})^{-1} W_{r \times r},
   $$

   We can verify that these DMD modes are eigenvectors of the high-dimensional $A$ matrix corresponding to the eigenvalues in $\Lambda$:

   $$
   \begin{aligned}
   A \Phi & = (X' \tilde{V} \tilde{\Sigma}^{-1} \tilde{U}^{H})(X' \tilde{V} \tilde{\Sigma}^{-1} W)\\
   & = X' \tilde{V} \tilde{\Sigma}^{-1} \tilde{A} W\\
   & = X' \tilde{V} \tilde{\Sigma}^{-1} W \Lambda\\
   & = \Phi \Lambda
   \end{aligned}
   $$
8. We can obtain a sparser higher-dimensional dynamics by improving our lifting function with DMD mode $\Phi$.

   $$
   \begin{aligned}
      \vec{y}' &= A \vec{y} \\
      \vec{y}' &= \Phi \Lambda \Phi^{\dagger} \vec{y} \\
      (\Phi^{\dagger} \vec{y}') &= \Lambda (\Phi^{\dagger} \vec{y})
   \end{aligned}
   $$

   Define $\vec{z} = \Phi^{\dagger} \vec{y}$. $\vec{z} = \vec{z}(\vec{x})$ is our enhanced lifting function. $\vec{z}$ provides better sparity as they should satisfy:

   $$
   \vec{z}'_{r \times 1} = \Lambda_{r \times r} \vec{z}_{r \times 1}.
   $$

9. Our identification and approximation is based on discrete-time snapshots. We can obtain a higher-dimensional linear continuous-time system:

   $$
   \begin{aligned}
      e^{\mathcal{A} \Delta t} \vec{z} &= \Lambda \vec{z} \\
      e^{\mathcal{A} \Delta t} &= \mathrm{diag} (\Lambda_{1}, \Lambda_{2}, \cdots, \Lambda_{r}) \\
      \Rightarrow \mathcal{A} &= \frac{1}{\Delta t} \mathrm{diag} \bigg(\ln(\Lambda_{1}), \ln(\Lambda_{2}), \cdots, \ln(\Lambda_{r}) \bigg)
   \end{aligned}
   $$

   Linear continuous-time system is

   $$
   \dot{\vec{z}} = \mathcal{A} \vec{z}
   $$

## 2. Systems with Input

Koopman control system is a realization of DMDc(Dynamic Mode Decomposition with control) with Koopman operator theory. DMDc is an identification method, as is shown as follows:

$$
\begin{aligned}
   \vec{x}' &= A \vec{x} + B \vec{u} \\
   X' &= A X + B Y \\
   X' &= \begin{bmatrix}
      A & B
   \end{bmatrix} \begin{bmatrix}
      X \\ Y
   \end{bmatrix}.
\end{aligned}
$$

Koopman control system theory assumes that the original state vector $\vec{x}$ can be linearly expressed by its lifting function $\vec{z}$, as lifting function is a set of orthonormal functions. Such relationship is written as $\vec{x} = C \vec{z}$. Milan Korda managed to identify $A$,$B$ and $C$ simultaneously:

$$
\begin{aligned}
   \left \{\begin{aligned}
      & \vec{z}' = A \vec{z} + B \vec{u}, \\
      & \vec{x} = C \vec{z}.
   \end{aligned} \right. \\
   \Rightarrow \left \{\begin{aligned}
      & Z' = A Z + B Y, \\
      & X = C Z.
   \end{aligned} \right. \\
   \Rightarrow \begin{bmatrix}
      Z' \\ X
   \end{bmatrix} = \begin{bmatrix}
      A & B \\
      C & \mathbf{0}
   \end{bmatrix} \begin{bmatrix}
      Z \\ Y
   \end{bmatrix}.
\end{aligned}
$$

The concatenated matrix $\begin{bmatrix}
   A & B \\
   C & \mathbf{0}
\end{bmatrix}$ includes vital information of desired higher-dimensional control system.

$$
\begin{aligned}
   \vec{z}'_{N \times 1} &= A_{N \times N} \vec{z}_{N \times 1} + B_{N \times M} \vec{u}_{M \times 1} \\
   \begin{pmatrix}
      \vec{z}_{k + 1} \\
      \vec{z}_{k + 2} \\
      \vdots \\
      \vec{z}_{k + n_{future}} \\
      \vec{u}_{k} \\
      \vdots \\
      \vec{u}_{k + n_{future} - 1}
   \end{pmatrix} &= \left[ \begin{array}{cccccc:c}
      \mathbf{0} & I & \mathbf{0} & \mathbf{0} & \cdots & \mathbf{0} & \mathbf{0} & \mathbf{0} & \cdots & \mathbf{0} \\
      \mathbf{0} & \mathbf{0} & I & \mathbf{0} & \cdots & \mathbf{0} & \mathbf{0} & \mathbf{0} & \cdots & \mathbf{0} \\
      \vdots & \vdots & \ddots & \vdots & \cdots & \vdots & \mathbf{0} & \mathbf{0} & \cdots & \mathbf{0} \\
      \mathbf{0} & \mathbf{0} & \cdots & \mathbf{0} & \mathbf{0} & I & \mathbf{0} & \mathbf{0} & \cdots & \mathbf{0} \\
      \mathbf{0} & \mathbf{0} & \cdots & \mathbf{0} & \mathbf{0} & I & \mathbf{0} & \mathbf{0} & \cdots & K_{1} \\ \hdashline
      \mathbf{0} & \mathbf{0} & \cdots & \cdots & \cdots & \mathbf{0} & \mathbf{0} & I & \cdots & \mathbf{0} \\
      \mathbf{0} & \mathbf{0} & \cdots & \cdots & \cdots & \mathbf{0} & \vdots & \vdots & \ddots & \vdots \\
      \mathbf{0} & \mathbf{0} & \cdots & \cdots & \cdots & \mathbf{0} & \mathbf{0} & \mathbf{0} & \cdots & I \\
      K_{2} & \mathbf{0} & \cdots & \cdots & \cdots & \mathbf{0} & \mathbf{0} & \mathbf{0} & \cdots & \mathbf{0}
   \end{array} \right] \begin{pmatrix}
      \vec{z}_{k} \\
      \vec{z}_{k + 1} \\
      \vdots \\
      \vec{z}_{k + n_{future} - 1} \\
      \vec{u}_{k - 1} \\
      \vdots \\
      \vec{u}_{k + n_{future} - 2}
   \end{pmatrix}
\end{aligned}
$$

This is VERY VERY VERY UGLY. Eigenvalue of this disgusting matrix is meaningless. I wanted to write a general mapping for MPC cases, but failed.
