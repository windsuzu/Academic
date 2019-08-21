# Subspaces and the basis for a subspace

$$
\begin{aligned}
\text{Subspace }\mathbf{V} = span&\left(\vec{v_1}, \vec{v_2}, \cdots \vec{v_n} \right)\\
&\begin{Bmatrix} \vec{v_1}, \vec{v_2}, \cdots \vec{v_n} \end{Bmatrix} \text{ is linear independence} \\\\

\text{then}\\\\

\mathbf{S} &= \begin{Bmatrix} \vec{v_1}, \vec{v_2}, \cdots \vec{v_n} \end{Bmatrix} \\
\mathbf{S} &\text{ is a } \bold{Basis}  \text{ for }\mathbf{V}
\end{aligned}
$$

* 若利用 **Minimum set of vectors** 來 span 該 subspace V
* 也就是 span subspace V 的向量都是 linear independence 時
* 這些向量的集合稱為該 Subspace 的 **Basis**

我們舉個例子 T

$$
\mathbf{T} = \begin{Bmatrix} \begin{bmatrix}1\\0\end{bmatrix}, \begin{bmatrix}0\\1\end{bmatrix} \end{Bmatrix}
$$

首先他可以 span R2 子空間

$$
\begin{aligned}
c_1\begin{bmatrix} 1\\0\end{bmatrix} + c_2\begin{bmatrix} 0\\1\end{bmatrix} &= \begin{bmatrix} x_1\\x_2\end{bmatrix} \\

c_1 + 0 = x_1, c_1 &= x_1\\
0 + c_2 = x_2, c_2 &= x_2\\
\end{aligned}
$$

並且他為 linear independence

$$
\begin{aligned}
c_1\begin{bmatrix} 1\\0\end{bmatrix} + c_2\begin{bmatrix} 0\\1\end{bmatrix} &= \begin{bmatrix} 0\\0\end{bmatrix} \\

c_1 + 0 = 0, c_1 &= 0\\
0 + c_2 = 0, c_2 &= 0\\
\end{aligned}
$$

所以 T 為 R2 的 basis \(而且是 _**standard basis**_\)

而這些 vectors 所生成的任一個向量在 Subspace 中都是獨一無二的 :

$$
\begin{aligned}
\vec{a} &\in \mathbf{V}, \\
\vec{a} &= c_1\vec{v_1} + c_2\vec{v_2} + \cdots + c_n\vec{v_n} \\
\vec{a} &= d_1\vec{v_1} + d_2\vec{v_2} + \cdots + d_n\vec{v_n} \text{ (subtract)} \\

\vec{0} &= (c_1-d_1)\vec{v_1}  + (c_2-d_2)\vec{v_1}  + \cdots + (c_n-d_n)\vec{v_n} 
\end{aligned}
$$

因為相減還是在 subspace 裡面，並且滿足 basis \(linear independent\)，所以 :

$$
\begin{aligned}
c_1 - d_1 &= 0 \\
c_2 - d_2 &= 0 \\
c_n - d_n &= 0 \\
c_n &= d_n
\end{aligned}
$$

證明了生成的向量為唯一

