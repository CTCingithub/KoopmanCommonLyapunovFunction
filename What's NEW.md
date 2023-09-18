<!--
 * @Author: CTC 2801320287@qq.com
 * @Date: 2023-08-05 16:16:25
 * @LastEditors: CTC 2801320287@qq.com
 * @LastEditTime: 2023-09-18 23:36:58
 * @Description: Koopman Common Control Lyapunov Function
 * 
 * Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
-->
# What's NEW?

Mugisho's work provided a novel framework to construct a common Lyapunov function for nonlinear systems by introducing **Koopman Operator Theory** to traditional Lie-algebraic sufficient condition of uniform stability of switched systems. However, the choice of lifting functions, as well as basis of tangental space(for the construction of CLF) are neglected.

Like common approximations of infinite-dimensional Koopman operators, data-driven methods should be applied when obtaining linear mapping of the higher-dimensional dynamics. Moreover, such process enables us improve the construction of measurement space(or lifting space), providing better linear mapping approximation in a sparser form, as is illustrated later.

## 1. Autonomous Systems

For autonomous systems, a common approach to derive and improve a linear approximation of Koopman operator is shown as follows:

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
   \Phi_{N \times r} = X'_{N \times m} \tilde{V}_{m \times r} (\tilde{\Sigma}_{r \times r})^{-1} W_{r \times r},
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

   Define $\vec{\varphi} = \Phi^{\dagger} \vec{y}$. Elements of $\vec{\varphi} = \vec{\varphi}(\vec{x})$ are the Koopman eigenfuctions. $\vec{\varphi}$ provides better sparity as they should satisfy:

   $$
   \vec{\varphi}'_{r \times 1} = \Lambda_{r \times r} \vec{\varphi}_{r \times 1}.
   $$

<!--
9. Our identification and approximation is based on discrete-time snapshots. We can obtain a higher-dimensional linear continuous-time system if all diagonal elements of $\Lambda$ is positive(This is a very rare case, and not desired as the system is unstable):

   $$
   \begin{aligned}
      e^{\mathcal{A} \Delta t} \vec{\varphi} &= \Lambda \vec{\varphi} \\
      e^{\mathcal{A} \Delta t} &= \mathrm{diag} (\Lambda_{1}, \Lambda_{2}, \cdots, \Lambda_{r}) \\
      \Rightarrow \mathcal{A} &= \frac{1}{\Delta t} \mathrm{diag} \bigg(\ln(\Lambda_{1}), \ln(\Lambda_{2}), \cdots, \ln(\Lambda_{r}) \bigg)
   \end{aligned}
   $$

   Linear continuous-time system is

   $$
   \dot{\vec{\varphi}} = \mathcal{A} \vec{\varphi}
   $$
-->

We managed to exact a enhanced set of measurement functions with snapshot data, and derived a linear discrete system. However, we desire a continuous-time form approximation for further discussion. Suppose $\vec{y} (\vec{x})$ follows:

$$
\dot{\vec{y}} = \mathcal{A} \vec{y}.
$$

With DMD mode $\Phi$, we're still able to enhance our lifting fuction for sparser dynamical behavior in measurement space:

$$
\begin{aligned}
   \Phi^{\dagger} \dot{\vec{y}} &= \Phi^{\dagger} \mathcal{A} \vec{y} \\
   \frac{d (\Phi^{\dagger} \vec{y})}{d t} &= \left( \Phi^{\dagger} \mathcal{A} \Phi \right) (\Phi^{\dagger} \vec{y}) \\
   \dot{\vec{\varphi}} &= \left( \Phi^{\dagger} \mathcal{A} \Phi \right) \vec{\varphi}.
\end{aligned}
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

Koopman control system theory assumes that the original state vector $\vec{x}$ can be linearly expressed by its lifting function $\vec{\varphi}$, as lifting function is a set of orthonormal functions. Such relationship is written as $\vec{x} = C \vec{\varphi}$. Milan Korda managed to identify $A$,$B$ and $C$ simultaneously:

$$
\begin{aligned}
   \left \{\begin{aligned}
      & \vec{z}' = A \vec{z} + B \vec{u}, \\
      & \vec{x} = C \vec{\varphi}.
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

<!--
$$
\begin{aligned}
   \vec{\varphi}'_{N \times 1} &= A_{N \times N} \vec{\varphi}_{N \times 1} + B_{N \times M} \vec{u}_{M \times 1} \\
   \begin{pmatrix}
      \vec{\varphi}_{k + 1} \\
      \vec{\varphi}_{k + 2} \\
      \vdots \\
      \vec{\varphi}_{k + n_{future}} \\
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
      \vec{\varphi}_{k} \\
      \vec{\varphi}_{k + 1} \\
      \vdots \\
      \vec{\varphi}_{k + n_{future} - 1} \\
      \vec{u}_{k - 1} \\
      \vdots \\
      \vec{u}_{k + n_{future} - 2}
   \end{pmatrix}
\end{aligned}
$$
-->

It's impossible to convert a state-space function to an autonomous system directly. However, it's still possible to convert a system under switched control to a switched autonomous system, given the relationship between feedback $\vec{u}$ and states $\vec{x}$. Suppose they follows a nonlinear feedback design $\{ \vec{u}_{i} = f_{i} (\vec{x}) \}$. Moreover, as the lifting function set $\{ z_{j} (\vec{x}) \}$ fulfils orthogonality and constructs a Hibert space, usually refered as measurement space or lifting space, we're able to expand elements of the control input $\vec{u}$ in terms of our measurement functions, written as

$$
u_{i} = f_{i} (\vec{x}) = K_{i1} z_{1} (\vec{x}) + K_{i2} z_{x} (\vec{x}) + \cdots + K_{ir} z_{r} (\vec{x}) \\
\Rightarrow \vec{u}_{m \times 1} (\vec{x}) = \begin{bmatrix}
   K_{11} & K_{12} & \cdots & K_{1r} \\
   K_{21} & K_{22} & \cdots & K_{2r} \\
   \vdots & \vdots & \ddots & \vdots \\
   K_{m1} & K_{m2} & \cdots & K_{mr}
\end{bmatrix}_{m \times r} \begin{pmatrix}
   z_{1} (\vec{x}) \\ z_{2} (\vec{x}) \\ \vdots \\ z_{r} (\vec{x})
\end{pmatrix}_{r \times 1} = K_{m \times r} \vec{\varphi}_{r \times 1}.
$$

Then we're able to transform subsystems with control to autonomous subsystems:

$$
{}^{i} \! \vec{z}' = {}^{i} \! A {}^{i} \! \vec{z} + {}^{i} \! B {}^{i} \! \vec{u} = ({}^{i} \!A + {}^{i} \! B {}^{i} \! K) {}^{i} \! \vec{z} = {}^{i} \! \bar{A} {}^{i} \! \vec{z}.
$$

The equation above gives a discrete mapping of system's state variables' measurement before and after a specific constant time step. In a digital sampling system, this time step should be the sampling interval $\tau$. Then we're able to apply conclusions of autonomous systems to systems with input.

<!--
Therefore, if all discrete subsystems following ${}^{i} \! \vec{z}' = {}^{i} \! \bar{A} {}^{i} \! \vec{z}$ where ${}^{i} \! \bar{A}$ is logable, we can convert all these systems to continuous autonomous divergent systems, it's impossible to realize GUAS with switching.

In a two-subsystem case, measurement $\vec{\varphi}$ may be the following form at a certain switching moment:

$$
\vec{\varphi} = {}^{1} \! \bar{A} {}^{2} \! \bar{A} {}^{1} \! \bar{A} {}^{1} \! \bar{A} {}^{2} \! \bar{A} {}^{2} \! \bar{A} \vec{\varphi}_{0}
$$
-->

## 3. Construction of Common Measurement Space

For a switched system $\{{}^{i} \!  \dot{\vec{x}} = {}^{i} \! f ({}^{i} \!  \vec{x})\} (i=1,2, \cdots)$ , we suppose the initial choice of measurement fuction is $\vec{y}_{N \times 1} = g(\vec{x})$, corresponding DMD mode matrix , eigenvalue matrix and eigenfuctions are ${}^{i} \! \Phi_{N \times r}$ , ${}^{i} \! \Lambda_{r \times r}$ and ${}^{i} \! \vec{\varphi}_{r \times 1}$.

The dominanting problem is, the invariant subspaces may not be able to linearly transformed to each other, even though they may share a same rank (if we truncated to the same rank $r$ in former steps). In other words, it's possible that ${}^{1} \! \vec{\varphi}$ cannot be expanded with elements in ${}^{2} \! \vec{\varphi}$ for example.

<!--
We'll demonstrate how we managed to construct a common measurement space with the following 2-subsystem example.

$$
\vec{y} = g(\vec{x}) = \begin{pmatrix}
   1 \\ x \\ x^{2} \\ x^{3}
\end{pmatrix}, \\
{}^{1} \! \Phi^{\dagger} = \begin{bmatrix}
   1 & 0 & 2 & 0\\
   0 & -4 & -1 & 2 \\
   0 & 0 & 0 & -3
\end{bmatrix}, \qquad
{}^{2} \! \Phi^{\dagger} = \begin{bmatrix}
   1 & 3 & 4 & 0\\
   0 & 2 & -5 & 2 \\
   0 & 0 & 0 & 3
\end{bmatrix}.
$$
-->

Our latter discussion is written in tensor form for simplicity, taking advantage of Einstein's summation convention. Koopman operator is defined through the following composition in discrete-time autonomous systems.

$$
K \circ g (\boldsymbol{x}) = K \circ g_{j} (\boldsymbol{x}) \boldsymbol{e}^{j} = g_{j} (F(\boldsymbol{x})) \boldsymbol{e}^{j}.
$$

With the introduction of tensor-style expression, we obtain a relatively simplier and concise equation, which the linear infinite-dimensional operator $K$'s finite-dimensional matric form approximation $A$ follows.

$$
\begin{aligned}
   A_{ij} g_{j} (\boldsymbol{x}) \boldsymbol{e}^{j} &= g_{j} (F(\boldsymbol{x})) \boldsymbol{e}^{j} \\
   \Rightarrow A_{ij} g_{j} (\boldsymbol{x}) &= g_{j} (F(\boldsymbol{x})).
\end{aligned}
$$

Suppose there's a vector-shaped set of functions $\hat{g}$ defined in the initial measurement space $\{ g_{j} \}$. This function set can be utilized to define a new measurement space. The transformation between two coordinates is

$$
\hat{g} = \hat{g}_{j} \boldsymbol{e}^{j} = T_{ij} g_{j} \boldsymbol{e}^{j}.
$$

Where $T$ is the transformation matrix, which is $\Phi^{\dagger}$ in the first section.

We have

$$
\begin{aligned}
   K \circ \hat{g} &= K \circ \left( T_{ij} g_{j} \boldsymbol{e}^{j} \right) \\
   &= T_{ij} \left( K \circ g_{j} \boldsymbol{e}^{j} \right) \\
   &= T_{ij} A_{ij} g_{j} \boldsymbol{e}^{j}.
\end{aligned}
$$

The new measurement space works if there exists a matrix $S$ satisfying $S T = I$.

In a 2-subsystem case, we have

$$
{}^{1} \! S {}^{1} \! T = I, \qquad {}^{2} \! S {}^{2} \! T = I.
$$

Our target is to find a bilinear function $\Gamma ({}^{1} \! T, {}^{2} \! T)$, which satisfies

$$
\forall {}^{1} \! T, {}^{2} \! T \in M(r), \quad \Gamma ({}^{1} \! T, {}^{2} \! T) \in M(r'),
$$

Where

$$
M (i) = \{T \vert T \in \mathbb{R}^{i \times N}, \quad \exist S, \quad S T = I_{N \times N} \}, \qquad r \leq r' \leq N.
$$

For a simple example, in which
$$
g (\vec{x}) = \begin{pmatrix}
   1 \\ x_{1} \\ x_{2} \\ x_{1}^{2} \\ x_{1} x_{2} \\ x_{2}^{2}
\end{pmatrix}, \quad
{}^{1} \! \varphi (\vec{x}) = \begin{pmatrix}
   x_{1} \\
   x_{2} + x_{2}^{2} \\
   x_{1} + x_{1} x_{2}
\end{pmatrix}, \quad
{}^{2} \! \varphi (\vec{x}) = \begin{pmatrix}
   x_{2} \\
   x_{1} + x_{1} x_{2} \\
   3 + x_{1}^{2}
\end{pmatrix}.
$$

${}^{1} \! \varphi (\vec{x})$ and ${}^{2} \! \varphi (\vec{x})$ are 3-dimensional embedding of the 6-dimensional manifold $g (\vec{x})$, our new flow map should have a dimension bigger than 3 in order not to lose evolution on ${}^{1} \! \varphi (\vec{x})$ and ${}^{2} \! \varphi (\vec{x})$. Moreover, as we focus more on subsystems' Koopman eigenfunctions for latter construction of a common measurement space, the tangental space is obtained with our new measurement functions and ODEs the subsystems follow. Sparity doesn't play a vital role in the selection of new measurement functions.

<!--
Not finished!!!
-->

We designed a special procedure to obtain a common measurement space:

1. For eigenfunctions ${}^{k} \! \varphi (\vec{x}) = {}^{k} \! T_{r \times N} g_{N \times 1} (\vec{x})$, we obtain the reduced row-echelon form of ${}^{k} \! T$ with Gaussian elimination, and call them ${}^{k} \! T'$.
2. We define a $N \times N$ square matrix $G$. If the $i$-th column of a certain ${}^{k} \! T'$ is a $0$ vector, we delete the $i$-th row of $G$.

Then we define $G g(\vec{x})$ to be our common measurement space.

## 4. Sparse Identification of Koopman Eigenfunctions

Researchers have been developing a variety of data-driven methods to identify Koopman eigenfunctions. Neural networks might be able to fit Koopman invariant subspaces, but lack explicit expressions. Therefore, we identify Koopman eigenfunctions with SINDy. We choose lifting function $g(\vec{x})$ as candidate functions $\Theta (\vec{x} $. Elements of Koopman eigenfunction $\varphi$, denoted as $\varphi_{j}$, follows

$$
\varphi_{j} (\vec{x}) = \vec{\xi}_{j}^{\top} \Theta (\vec{x}).
$$

Then we have

$$
\begin{aligned}
   \frac{d \varphi_{j}}{d t} &= \lambda_{j} \varphi_{j} \\
   \nabla_{\vec{x}} \varphi_{j} \frac{d \vec{x}}{d t} &= \lambda_{j} \varphi_{j} \\
   \nabla_{\vec{x}} \left( \vec{\xi}_{j}^{\top} \Theta \right) f &= \lambda_{j} \vec{\xi}_{j}^{\top} \Theta \\
   \Rightarrow \bigg( \left( \nabla_{\vec{x}} \Theta \right) f\bigg)^{\top} \vec{\xi}_{j} &= \lambda_{j} \Theta^{\top} \vec{\xi}_{j}.
\end{aligned}
$$

We define

$$
\gamma_{1} (\vec{x}) = \Bigg( \bigg( \nabla_{\vec{x}} \Theta (\vec{x}) \bigg) f(\vec{x}) \Bigg), \qquad
\gamma_{2} (\vec{x}) = \bigg( \Theta (\vec{x}) \bigg)^{\top}. \\
\Gamma_{1} = [\underbrace{\gamma_{1} (\vec{x}_{1}), \quad \gamma_{1} (\vec{x}_{2}), \quad \cdots, \quad \gamma_{1} (\vec{x}_{m})}_{\text{Snapshot of } m \text{ moments}}], \\
\Gamma_{2} = [\underbrace{\gamma_{2} (\vec{x}_{1}), \quad \gamma_{2} (\vec{x}_{2}), \quad \cdots, \quad \gamma_{2} (\vec{x}_{m})}_{\text{Snapshot of } m \text{ moments}}].
$$

The equation is simplified:

$$
\gamma_{1} (\vec{x}) \vec{\xi}_{j} = \gamma_{2} (\vec{x}) \lambda_{j} \vec{\xi}_{j}. \\
\Downarrow \\
\Gamma_{1} \vec{\xi}_{j} = \Gamma_{2} \lambda_{j} \vec{\xi}_{j}.
$$

Eigenpairs $\left( \lambda_{j}, \vec{\xi}_{j} \right)$ forms the eigen system of $\Gamma_{2}^{\dagger} \Gamma_{1}$. Eigenfunctions $\varphi (\vec{x})$ is

$$
\varphi (\vec{x}) = \begin{pmatrix}
   \varphi_{1} (\vec{x}) \\ \vdots \\ \varphi_{j} (\vec{x}) \\ \vdots \\ \varphi_{r} (\vec{x})
\end{pmatrix} = \begin{bmatrix}
   \vec{\xi}_{1}^{\top} \\ \vdots \\ \vec{\xi}_{j}^{\top} \\ \vdots \\ \vec{\xi}_{r}^{\top}
\end{bmatrix} \Theta (\vec{x}).
$$
