# Vectors and spaces

## Vectors

賦予任意坐標方向性，並且可以從任意起點開始

* Scalar multiplication
  * 視覺上就像一個向量，被直直的拉長 10 倍

$$
\vec{v} = (2,3) 
\\10\vec{v} = (20, 30)
$$

![](../.gitbook/assets/scalar_multiplication.jpg)

* Unit vector
  * A unit vector has a magnitude \(or length\) of 1.

$$
\begin{align}
&\vec{v} = \left(2,3\right)
\\ &\text{unit vector of } \vec{v} = \left(\frac{2}{\sqrt{13}},\:\frac{3}{\sqrt{13}}\right)\\
\\ &\text{check: }\sqrt{\left(\frac{2}{\sqrt{13}}\right)^2+\left(\frac{3}{\sqrt{13}}\right)^2} = 1
\end{align}
$$

* Add & subtract vectors
  * 視覺上就像先往第一個向量前進後，再往第二個向量的 \(正或反\) 向前進

$$
\begin{align}
\vec{u} &= (-5, 3)\\
\vec{w} &= (-12, -4)\\
\vec{w} - \vec{u} &= (-7, -7)
\end{align}
$$

![](../.gitbook/assets/add_vectors.jpg)

## Linear Combination and Span

* [https://youtu.be/Qm\_OS-8COwU](https://youtu.be/Qm_OS-8COwU)

向量加上任意 **實數 scalar** 後，並且透過加法組合在一起時，產生一個 **線性** 的組合即為 _**Linear combination**_

$$
a_1\vec{v_1} + a_2\vec{v_2}+ \cdots + a_n\vec{v_n}. | a_n \in \mathbb{R}
$$

舉個例子，以下兩個向量經過與 scalar 相乘後，可以組合並且表示一個新的向量

$$
3 \begin{bmatrix} 1\\ 2\end{bmatrix}
+2 \begin{bmatrix} 0\\ 3\end{bmatrix}=
\begin{bmatrix} 3\\ 12\end{bmatrix}
$$

因為 Vectors 可以與**任意**實數相乘，產生的 linear combination 就可以任意表示其他向量，這個現象叫作 _**Span**_

例如以下兩個向量不管 a1 和 a2 為何，在 combine 之後只能 span 這兩條向量原本的那條線

$$
\begin{align}
a_1 \begin{bmatrix} 1\\ 2\end{bmatrix}+
a_2\begin{bmatrix} 2\\ 4\end{bmatrix}&=\\
a_1 \begin{bmatrix} 1\\ 2\end{bmatrix}+
2a_2\begin{bmatrix} 1\\2\end{bmatrix}&=\\
a_1 +2a_2 \begin{bmatrix} 1\\ 2\end{bmatrix}&=
a\begin{bmatrix} 1\\ 2\end{bmatrix}
\end{align}
$$

![](../.gitbook/assets/linear_combination1.jpg)

而底下兩個向量卻可以 **span** 整個二維平面的任意兩點，我們可以這樣表示

$$
\begin{align}
&\vec{v_1} = (1,0), \vec{v_2} = (0,1)\\
&a_1\vec{v_1} + a_2\vec{v_2} = \mathbb{R}^2
\end{align}
$$

## Linear Dependence & Linear Independence

* [https://youtu.be/CrV1xCWdY-g](https://youtu.be/CrV1xCWdY-g)

有了 linear combination 和 span 的知識後，很簡單就可以了解 Linear dependence / independence 的意義，

當你想要 span 某個東西時，使用不多不少剛剛好的向量來表示即為 _**Linear Independence**_

> 例如使用 \(1, 0\) 和 \(0, 1\) 來 span 整個 R2 平面時，這兩個向量即為線性獨立

而在 span 時，使用了 **多餘** 的向量，這個向量和本來就足夠的向量，形成了 _**Linear Dependence**_

> 例如本來只用 \(1, 0\) 和 \(0, 1\) 已經可以 span R2 ，
>
> 但我又加了向量 \(1, 3\) 來形成 R2 平面， \(1, 3\) 和另外兩個向量即為線性依賴



* [https://youtu.be/Alhcv5d\_XOs](https://youtu.be/Alhcv5d_XOs)
* 正式一點的定義為
  * 當 linear combination 中有任意一個向量可以被表示為其他向量的加總時
  * 或是某個向量的 scalar 不為 0 卻可以讓整個 linear combination 變為 0 時
  * 即為 **Linear dependence**

$$
\begin{align}
\text{Linear dependent} &\iff a_1\vec{v_1} + a_2\vec{v_2}+\cdots+a_n\vec{v_n} = 0 = \begin{bmatrix} 0\\\vdots\\0 \end{bmatrix}\\
&\iff \text{for some }a_i \text{ , not all are zero, at least one non-zero}\\
v_1 = a_2v_2 + a_3v_3+\cdots+a_nv_n&\iff 
\end{align}
$$

上面的定義可以很好的用來檢驗向量間為 linear dependence or linear independence

例如要檢測下面兩個向量是否有 linear dependence

$$
\begin{align}
\vec{v_1} &= (2,1)\\ \vec{v_2} &= (3,2) \\
a_1\vec{v_1}+a_2\vec{v_2} &= 0 = \begin{bmatrix} 0\\0 \end{bmatrix}\\
a_1 \begin{bmatrix}2\\1\end{bmatrix} + a_2 \begin{bmatrix}3\\2\end{bmatrix}&=\begin{bmatrix}0\\0\end{bmatrix}
\end{align}
$$

再將其拆開驗證即可

$$
\left\{\begin{matrix}
2a_1 + 3a_2 &= 0\\
a_1 + 2a_2 &= 0\\
\end{matrix}\right.\\
a_1 = 0
\\a_2 =0
$$

可以得到結果， v1 和 v2 為 linear independence !

> 3 demension example: [https://youtu.be/9kW6zFK5E5c](https://youtu.be/9kW6zFK5E5c)

## Subspaces and basis for a subspace

