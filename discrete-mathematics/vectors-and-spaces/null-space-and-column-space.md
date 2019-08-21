# Null space and column space

## Matrix vector products

* [https://youtu.be/7Mo4S2wyMg4](https://youtu.be/7Mo4S2wyMg4)

我們接下來可以將 matrix 和 vector 結合運算，我們表達 matrix size 為 m × n 時為

$$
\mathbf{A} = \begin{bmatrix} 
a_{11} & a_{12} & \cdots  & a_{1n}\\
a_{21} & a_{22} & \cdots  & a_{2n}\\
\vdots & &\ddots\\
a_{m1} & & & a_{mn}
\end{bmatrix}
$$

而可以跟他相乘的 vector 的 components 必須要等於 matrix 的 column size

> 例如: m × y matrix 只能跟 y × n 的 vector 相乘，並且會變成 m × n 的 matrix

$$
\begin{bmatrix} 
a_{11} & a_{12} & \cdots  & a_{1n}\\
a_{21} & a_{22} & \cdots  & a_{2n}\\
\vdots & &\ddots\\
a_{m1} & & & a_{mn}
\end{bmatrix}
\cdot
\begin{bmatrix} 
x_{1} \\x_{2}\\\vdots\\x_{n}
\end{bmatrix}
= \mathbf{A}\vec{x}
= \begin{bmatrix} 
a_{11}x_1 + a_{12}x_2+\cdots+a_{1n}x_n\\
a_{21}x_1 + a_{22}x_2+\cdots+a_{2n}x_n\\
\vdots\\
a_{m1}x_1 + a_{m2}x_2+\cdots+a_{mn}x_n\\
\end{bmatrix}=b=
\begin{bmatrix} 
b_{1} \\b_{2}\\\vdots\\b_{n}
\end{bmatrix}
$$

舉個例子

$$
\mathbf{A}\vec{x} = 
\begin{bmatrix} -3 & 0 & 3 & 2 \\1 &7 & -1& 9
\end{bmatrix}
\begin{bmatrix} 2 \\-3\\4\\-1
\end{bmatrix}=
\begin{bmatrix} -6+0+12-2 \\ 2-21-4-9
\end{bmatrix} =\begin{bmatrix} 4\\-32
\end{bmatrix}
$$

我們可以把 matrix A 的兩列視為兩個 row vector ，也就是 column vector 的 **Transpose**

並且把矩陣相乘的結果表示為 Dot Product

$$
\vec{a_1} = \begin{bmatrix} -3\\0\\3\\2\end{bmatrix},
\vec{a_2} = \begin{bmatrix} 1\\7\\-1\\9\end{bmatrix},
\mathbf{A}\vec{x} = \begin{bmatrix} \vec{a_1^T} \\\vec{a_2^T} \end{bmatrix}\vec{x}
= \begin{bmatrix} \vec{a_1}\cdot\vec{x}\\ \vec{a_2}\cdot\vec{x} \end{bmatrix}
$$

我們也可以把矩陣視為一個一個的 column vector

$$
\mathbf{A}\vec{x} = 
\begin{bmatrix} \color{red}-3 & \color{blue}0 & \color{green}3 & \color{orange}2 
\\\color{red}1 &\color{blue}7 & \color{green}-1& \color{orange}9
\end{bmatrix}
\begin{bmatrix} x_1 \\x_2\\x_3\\x_4
\end{bmatrix}
$$

把矩陣相乘的結果表示為每個 vector 和 xi 的乘積相加的 linear combination

$$
\mathbf{A}\vec{x} = \begin{bmatrix}\color{red}\vec{v_1} & \color{blue}\vec{v_2} & \color{green}\vec{v_3} & \color{orange}\vec{v_4}\end{bmatrix} \begin{bmatrix} x_1 \\x_2\\x_3\\x_4
\end{bmatrix} = x_1\vec{v_1} + x_2\vec{v_2} +x_3\vec{v_4} +x_4\vec{v_4}
$$

## Null space of a matrix

* [https://youtu.be/jCwRV1QL\_Xs](https://youtu.be/jCwRV1QL_Xs)

假設有一個 matrix A: m × n，和 vector x 相乘皆為零向量，我們稱之為 **homogeneous equation**

$$
\begin{aligned}
&\mathbf{A}: m\times n \\
&\mathbf{A}\vec{x} = \mathbf{0}\\

\end{aligned}
$$

現在我們想知道所有能夠符合這個 equation 的 x 集合，能不能構成一個 valid 的 subspace ?

$$
\mathbf{N} = \begin{Bmatrix} \vec{x} \in \mathbb{R}^n \mid \mathbf{A}\vec{x} = \mathbf{0}\end{Bmatrix}
$$

答案是可以的，他符合 subspace 的三項條件

* x 包含 0向量
* x 符合加法封閉 \(closure under addition\)
* x 符合乘法封閉 \(closure under scalar multiplication\)

$$
\begin{aligned}
1. \,\,\, &\mathbf{A}\mathbf{0}=\mathbf{0}, \mathbf{0} \in N\\\\
2. \,\,\, &v_1, v_2 \in N, \,\mathbf{A}v_1 = \mathbf{0},\, \mathbf{A}v_2 = \mathbf{0} \\ & \mathbf{A}(v_1+v_2) = \mathbf{A}v_1+\mathbf{A}v_2 = \mathbf{0 + 0 = 0}\\\\
3. \,\,\, &v_1 \in N, c \in \mathbb{R}\\
&\mathbf{A}(cv_1) = c(\mathbf{A}v_1) = c\mathbf{0}= \mathbf{0}
\end{aligned}
$$

我們稱這個 subspace N 為 **A 的 NullSpace**

$$
\mathbf{N} = N(\mathbf{A}) = \text{Nullspace of } \mathbf{A}
$$

## Calculating the null space of a matrix

* [https://youtu.be/qvyboGryeA8](https://youtu.be/qvyboGryeA8)

我們來試著計算隨便一個 matrix A 他的 nullspace 為何

$$
\mathbf{A} = \begin{bmatrix} 1&1&1&1 \\ 1&2&3&4 \\ 4&3&2&1\end{bmatrix} 
\begin{bmatrix} x_1\\x_2\\x_3\\x_4\end{bmatrix} =
\begin{bmatrix} 0\\0\\0\end{bmatrix}
$$

也就是解決 equation

$$
\begin{aligned}
x_1+x_2+x_3+x_4&=0\\
x_1+2x_2+3x_3+4x_4&=0\\
4x_1+3x_2+2x_3+x_4&=0
\end{aligned}
$$

可以利用 Reduced row echelon form 來解

$$
\begin{bmatrix}\begin{array}{cccc|c} 1&1&1&1&0 \\ 1&2&3&4&0 \\ 4&3&2&1&0\end{array}\end{bmatrix}
\Rightarrow
\begin{bmatrix}\begin{array}{cccc|c} 1&1&1&1&0 \\ 0&1&2&3&0 \\ 0&1&2&3&0\end{array}\end{bmatrix}
\Rightarrow
\begin{bmatrix}\begin{array}{cccc|c} 1&0&-1&-2&0 \\ 0&1&2&3&0 \\ 0&0&0&0&0\end{array}\end{bmatrix}
$$

再轉回 equation

$$
\begin{aligned}
x_1 -x_3-2x_4&=0  \Rightarrow \color{red}{x_1=x_3+2x_4}\\
x_2+2x_3+3x_4&=0 \Rightarrow \color{red}{x_2=-2x_3-3x_4}
\end{aligned}
$$

最後得出一個 linear combination，其中 x3 和 x4 可以為任何實數，來拖移兩個向量在 R4 nullspace 移動

$$
\begin{bmatrix} x_1\\x_2\\x_3\\x_4\end{bmatrix}=
x_3\begin{bmatrix} 1\\-2\\1\\0 \end{bmatrix}+
x_4\begin{bmatrix} 2\\-3\\0\\1 \end{bmatrix}
$$

也就是這個 nullspace 是由這兩個向量來 span 而成的

其實也可以發現，要求得 N\(A\) 跟求得 N\(rref\(A\)\) 的 nullspace 是一樣的

$$
N(\mathbf{A}) = span\left(\begin{bmatrix}1\\-2\\1\\0\end{bmatrix}, \begin{bmatrix}2\\-3\\0\\1\end{bmatrix}\right)= N(rref(\mathbf{A}))
$$

#### Null space's relation to linear independence

* [https://youtu.be/-fKh6SNEPr4](https://youtu.be/-fKh6SNEPr4)

當 matrix A 為 m × n 時，其 nullspace 一定為 n 個 components 的 vector

$$
N(\mathbf{A}) = \begin{Bmatrix} \vec{x} \in \mathbb{R}^n \mid \mathbf{A}\vec{x}=\vec{0}\end{Bmatrix}
$$

得出來的 0 矩陣會有 m 個 components

$$
\mathbf{A}_{m \times n} = \begin{bmatrix} \vec{v_1} & \vec{v_2} & \cdots & \vec{v_n} \end{bmatrix}\begin{bmatrix} x_1\\x_2\\\vdots \\ x_n \end{bmatrix} = \begin{bmatrix} 0_1\\0_2\\\vdots \\ 0_m \end{bmatrix}
$$

我們將上面的運算拆出來變成 linear combination 的形式

$$
x_1\vec{v_1} + x_2\vec{v_2} + \cdots + x_n\vec{v_n} = \vec{0}
$$

這時我們思考，若 v1 到 vn 要 linear independence ，那 x1 到 xn 必須都為 0

若 x1 到 xn 都為 0，代表這個 linear combination 只有唯一解

也就是說，A 的 nullspace 在 v1 到 vn 皆為 linear independence 下只有 0 矩陣而已

$$
v_1,v_2,\cdots,v_n \text{ L.I} \iff x_1, x_2,\cdots,x_n =0 \iff N(\mathbf{A}) = \begin{Bmatrix} \vec{0} \end{Bmatrix}
$$

## Column space of a matrix

* [https://youtu.be/st6D5OdFV9M](https://youtu.be/st6D5OdFV9M)

我們已經知道 m × n 代表 Matrix A 有 n 個 column vector，每個都在 Rm 空間

$$
\mathbf{A}_{m \times n} = \begin{bmatrix} \vec{v_1} & \vec{v_2} & \cdots & \vec{v_n} \end{bmatrix}
, \vec{v_1}, \vec{v_2},\cdots, \vec{v_n}\in \mathbb{R}^m
$$

而 Column space 指的就是由這 n 個 column vector 所 span 的空間

$$
C(\mathbf{A}) = span\left( \vec{v_1}, \vec{v_2},\cdots, \vec{v_n} \right)
$$

我們也知道 span 出來的空間符合 subspace 的三大條件

$$
\begin{aligned}
\vec{a} &\in C(\mathbf{A})\\
\vec{a} &= c_1\vec{v_1} + c_2\vec{v_2} + \cdots + c_n\vec{v_n}\\\\
1.\,\, &\vec{a} \text{ contains zero vector}\\
2.\,\, &s\vec{a} = sc_1\vec{v_1} + sc_2\vec{v_2} + \cdots + sc_n\vec{v_n},\,\, s\vec{a} \in C(\mathbf{A})\\
3.\,\, &\vec{b} = b_1\vec{v_1} + b_2\vec{v_2} + \cdots +     b_n\vec{v_n},\,\, \vec{b} \in C(\mathbf{A})\\
&\vec{a}+\vec{b} = (c_1+b_1)\vec{v_1} + (c_2+b_2)\vec{v_2} + \cdots + (c_n+b_n)\vec{v_n} \in C(\mathbf{A})
\end{aligned}
$$

我們可以用下面 Set 的方式來思考 Column space

Column space 就是 matrix A 和任何可以與他相乘的 vector x 所生成的所有向量集合

> vector x 必須要為 n 個 components 這樣才可以相乘

$$
\begin{Bmatrix}\mathbf{A}\vec{x}\mid\vec{x}\in\mathbb{R}^n  \end{Bmatrix} \mid
\mathbf{A}\vec{x}= x_1\vec{v_1} + x_2\vec{v_2} + \cdots + x_n\vec{v_n}
$$

可以表示成

$$
\begin{Bmatrix}x_1\vec{v_1} + x_2\vec{v_2} + \cdots + x_n \mid x_1,x_2,\cdots,x_n \in\mathbb{R}  \end{Bmatrix} 
= span\left( \vec{v_1}, \vec{v_2},\cdots, \vec{v_n} \right)
= C(\mathbf{A})
$$

舉個例子，若向量 b1 不在 A 的 column space 裡，那 Ax = b1 是永遠不會有解的

相反，若向量 b2 他存在於 A 的 column space 裡，那 Ax = b2 將至少會有一個解

$$
\begin{aligned}
\vec{b_1} \notin C(\mathbf{A}) &\mid \mathbf{A}\vec{x} = \vec{b_1} \text{ has no solution}\\

\vec{b_2} \in C(\mathbf{A}) &\mid \mathbf{A}\vec{x} = \vec{b_2} \text{ has a least one solution}\\
\end{aligned}
$$

## Null space and column space basis

* [https://youtu.be/\_uTAdf\_AsfQ](https://youtu.be/_uTAdf_AsfQ)

現在要找出下面 matrix A 的 column space 和 null space

$$
\mathbf{A}= \begin{bmatrix} 1&1&1&1\\2&1&4&3\\ 3&4&1&2\end{bmatrix}
$$

我們可以非常輕鬆求得他的 column space 等於每個 column vector span 而成的空間

但他是否為這個空間的 basis 呢 ? \(要為 basis 必須要 linear independence\)

$$
C(\mathbf{A}) = span\left(
\begin{bmatrix}1\\2\\3\end{bmatrix}, 
\begin{bmatrix}1\\1\\4\end{bmatrix},
\begin{bmatrix}1\\4\\1\end{bmatrix},
\begin{bmatrix}1\\3\\2\end{bmatrix} \right)
$$

要知道 matrix A 有沒有 linear independence 只要看 null space 是否只有包含 0 向量即可

$$
x_1\vec{v_1}+ x_2\vec{v_2} + \cdots + x_n\vec{v_n} = 0 \mid x_1,x_2,\cdots,x_n = 0 \iff \mathbf{A} \text{ is L.I.}\\
A\vec{x}=0, \vec{x} = \begin{Bmatrix}\vec{0} \end{Bmatrix}
$$

要求 A 的 null space 等於求 rref\(A\) 的 null space

$$
rref(\mathbf{A})= \begin{bmatrix} 1&0&3&2\\0&1&-2&-1\\ 0&0&0&0\end{bmatrix}
 \begin{bmatrix} x_1\\x_2\\x_3\\x_4\end{bmatrix} =
  \begin{bmatrix} 0\\0\\0\end{bmatrix}
$$

將矩陣列回 equation

$$
x_1+3x_3+2x_4=0 \Rightarrow \color{red}{x_1=-3x_3-2x_4}\\ 
x_2-2x_3-x_4=0 \Rightarrow \color{red}{x_2 = 2x_3+x_4}\\
$$

並且利用 free variables 來表示 null space 空間

$$
\begin{bmatrix} x_1\\x_2\\x_3\\x_4\end{bmatrix} =
x_3\begin{bmatrix} -3\\2\\1\\0\end{bmatrix} +
x_4\begin{bmatrix} -2\\1\\0\\1\end{bmatrix}
$$

至此，我們可以得到 null space 為下，而且並不是只含有 0 向量

$$
N(\mathbf{A}) = N(rref(\mathbf{A}))=span\left(\begin{bmatrix} -3\\2\\1\\0\end{bmatrix},\begin{bmatrix} -2\\1\\0\\1\end{bmatrix}\right)
$$

所以 A 不為 linear independence，也就是剛剛的 column space 不為 basis

要得到 basis 我們要從剛剛的 column space 刪除多餘的 vectors

$$
\begin{aligned}
x_1 &= -3x_3-2x_4\\
x_2 &= 2x_3+x_4
\end{aligned}
$$

透過剛剛求得的 equation，我們知道 x1 和 x2 都可以由 x3 和 x4 組成，所以 x3 和 x4 是多餘的

$$
\text{basis of } C(\mathbf{A}) = span\left(\vec{x_1},\vec{x_2} \right) = span\left(
\begin{bmatrix}1\\2\\3\end{bmatrix}, 
\begin{bmatrix}1\\1\\4\end{bmatrix}\right)
$$

## Visualizing a column space as a plane in R3

* [https://youtu.be/EGNlXtjYABw](https://youtu.be/EGNlXtjYABw)

從上面的例子我們知道兩個 R3 vector 所 span 出來的為**三維空間**中的一個**平面**

那我們要怎麼找出平面呢 ?

### 方法一

* 先找到 normal vector \(可以由 \(1, 2, 3\) 和 \(1, 1, 4\) 的 Cross product 求得！\)
* 再從任一點向量 \(x, y, z\) 和 \(1, 2, 3\) 或 \(1, 1, 4\) 相減得到一條 **躺在該平面上的向量**
* 最後因為該向量跟 normval vector 會垂直，所以 dot product 為 0
* 以此找到 plane 的 equation

$$
\vec{n} \cdot (\vec{x} - \begin{bmatrix}1\\2\\3\end{bmatrix}) = \vec{0}
$$

來找 normal vector n

$$
\vec{n} =
\begin{bmatrix}1\\2\\3\end{bmatrix}\times
\begin{bmatrix}1\\1\\4\end{bmatrix} = 
\begin{bmatrix}8-3\\-(4-3)\\1-2\end{bmatrix} =
\begin{bmatrix}5\\-1\\-1\end{bmatrix}
$$

接著代回上面式子

$$
\begin{bmatrix}5\\-1\\-1\end{bmatrix} \cdot
\begin{bmatrix}x-1\\y-2\\z-3\end{bmatrix}=0
$$

即可得到平面方程式

$$
\begin{aligned}
&5(x-1)-1(y-2)-1(z-3)=0\\
\Rightarrow\,\,&5x-5-y+2-z+3=0\\
\Rightarrow\,\,&5x-y-z=0 \in C(\mathbf{A})
\end{aligned}
$$

### 方法二

我們知道，Column space 裡的任何一個解 \(vector b\) 都應該在該平面上

$$
C(\mathbf{A}) = 
\begin{Bmatrix} \mathbf{A}\vec{x}\mid\ \vec{x}\in \mathbb{R}^n \end{Bmatrix}=
\begin{Bmatrix} \vec{b}\mid\ \mathbf{A}\vec{x} = \vec{b} \text{ AND } \vec{x} \in \mathbb{R}^n \end{Bmatrix}
$$

我們又知道，要解決 Ax=b 可以轉換為 \[A\|b\] 的矩陣來求 reduced row echelon form

$$
\vec{b} = \begin{bmatrix} x\\y\\z\end{bmatrix},
\mathbf{A}\vec{x}=\vec{b} \Rightarrow
\begin{bmatrix} \begin{array}{cccc|c} 1&1&1&1&x\\2&1&4&3&y\\3&4&1&2&z \end{array} \end{bmatrix} \rightarrow
\begin{bmatrix} \begin{array}{cccc|c} 1&1&1&1&x\\0&1&-2&-1&2x-y\\0&0&0&0&5x-y-z \end{array} \end{bmatrix}
$$

要滿足 Ax=b 的 b 為 valid vector，那最後一行的 5x - y - z 必須要等於 0 才行，所以我們得到

$$
5x-y-z = 0 \in C(\mathbf{A})
$$

## Any subspace basis has same number of elements

* [https://youtu.be/Zn2K8UIT8r4](https://youtu.be/Zn2K8UIT8r4) \(詳細證明\)

下面用矛盾證明 subspace 的 basis 所含的 elements 數量皆相同

$$
\begin{aligned}
\mathbf{A} &= \begin{Bmatrix} a_1,a_2,\cdots,a_n\end{Bmatrix} \text{ is basis of } \mathbf{V}\\
\mathbf{B} &= \begin{Bmatrix} b_1,b_2,\cdots,b_m\end{Bmatrix} \text{ spans } \mathbf{V} \mid m<n\\
\end{aligned}
$$

若把 a1, a2 依序帶入 B set 中取代 b1, b2 ，表面上可以維持 B spans V

而且取代時不可以把原本在 A set 的元素取代掉，因為 A set 的元素之間是 linear independence 的

$$
\begin{aligned}
&\mathbf{B_1} = \begin{Bmatrix} a_1, b_2,b_3, \cdots, b_m\end{Bmatrix} \text{ spans }\mathbf{V}\\
&\mathbf{B_2} = \begin{Bmatrix} a_1, a_2,b_3, \cdots, b_m\end{Bmatrix} \text{ spans }\mathbf{V}\\
&\vdots\\
&\mathbf{B_m} = \begin{Bmatrix} a_1, a_2,a_3, \cdots, a_m\end{Bmatrix} \text{ spans }\mathbf{V}\\

\end{aligned}
$$

但是我們知道 m &lt; n ， A 又可以表示成 Bm 的延伸

$$
\mathbf{A} = \begin{Bmatrix} \color{red}{a_1,a_2,\cdots,a_m}\color{black},\cdots a_n\end{Bmatrix} \text{ is basis of } \mathbf{V}
$$

我們知道 A 已經確定是 span V 的最小組合了，但卻又能用 m 個 a 元素來 span V，產生矛盾

因此，不可能有比 basis 更少的元素組合可以 span subspace

而且，basis 也不能有多餘的元素出現在裡面

**綜合在一起，同一個 subspace 底下的任何 basis 都擁有一個數量的 elements**

> 我們又將這些 basis 共同擁有的元素數量，稱作 dimension
>
> $$
> Dim(\mathbf{A}) = n
> $$

## Dimension of the null space or nullity

* [https://youtu.be/abYAUqs\_n6I](https://youtu.be/abYAUqs_n6I)

假設我們要找出 matrix B 的 nullspace

$$
\mathbf{B} = \begin{bmatrix}1&1&2&3&2\\1&1&3&1&4\end{bmatrix}
$$

我們知道只要將 B 轉為 reduced row echelon form

$$
rref(\mathbf{B})= \begin{bmatrix}1&1&0&7&-2\\0&0&1&-2&2\end{bmatrix} 
\begin{bmatrix} x_1\\x_2\\x_3\\x_4\\x_5\end{bmatrix} = 
 \begin{bmatrix}0\\0\end{bmatrix}
$$

再利用 equation 就可以找出 span null space 的向量集

$$
x_1+x_2+7x_4-2x_5=0 \Rightarrow \color{red}{x_1=-x_2-7x_4+2x_5}\\
x_3-2x_4+2x_5=0 \Rightarrow \color{red}{x_3=2x_4-2x_5}\\
\begin{bmatrix} x_1\\x_2\\x_3\\x_4\\x_5\end{bmatrix} = 
x_2\begin{bmatrix} -1\\1\\0\\0\\0\end{bmatrix}+
x_4\begin{bmatrix} -7\\0\\2\\1\\0\end{bmatrix}+
x_5\begin{bmatrix} 2\\0\\-2\\0\\1\end{bmatrix}
$$

所以 N\(B\) =

$$
N(\mathbf{B}) = N(rref(\mathbf{B})) = span\left(
\begin{bmatrix}-1\\1\\0\\0\\0\end{bmatrix},
\begin{bmatrix}-7\\0\\2\\1\\0\end{bmatrix},
\begin{bmatrix}2\\0\\-2\\0\\1\end{bmatrix}
\right) = span(\vec{v_1},\vec{v_2},\vec{v_3})
$$

而且這三個向量 linear independent，所以為 N\(B\) 的 basis

然後因為找到 basis 了，所以 N\(B\) 的 dimension 為 3，又可以稱作 nullity = 3

> 🤷‍♂️ Nullity = reduced row echelon form 的 non-pivot column 數量

## Dimension of the column space or rank

* [https://youtu.be/JUgrBkPteTg](https://youtu.be/JUgrBkPteTg)

我們可以將 matrix A 的 column 分為五等份，而 column space 即為這五個 column 所 span 而成

$$
\mathbf{A} = \begin{bmatrix}1&0&-1&0&4\\2&1&0&0&9\\-1&2&5&1&-5\\1&-1&-3&-2&9\end{bmatrix},
C(\mathbf{A}) = span\left(
\begin{bmatrix}-1\\2\\-1\\1\end{bmatrix},
\begin{bmatrix}0\\1\\2\\-1\end{bmatrix},
\begin{bmatrix}-1\\0\\5\\-3\end{bmatrix},
\begin{bmatrix}0\\0\\1\\-2\end{bmatrix},
\begin{bmatrix}4\\9\\-5\\9\end{bmatrix}
\right)
$$

但我們並不知道他們五個是否 linear independent，即是否為 basis of column space

這邊提供一個方法找出 column space 的 basis 並且得知他的 dimension 也就是 rank

* 先將 A 化簡為 reduced row echelon form
* 找到 rref 的 pivot columns
* 這些 column 對應回 A ，即是 C\(A\) 的 basis

$$
rref(\mathbf{A}) = \begin{bmatrix}
\color{red}1&\color{blue}0&-1&\color{green}0&4\\
\color{red}0&\color{blue}1&2&\color{green}0&1\\
\color{red}0&\color{blue}0&0&\color{green}1&-3\\
\color{red}0&\color{blue}0&0&\color{green}0&0\end{bmatrix}
$$

因為 1, 2, 4 行為 pivot column ，所以對應回 A 的 1, 2, 4 行即為 C\(A\) 的 basis

$$
C(\mathbf{A})= span\left(
\begin{bmatrix}-1\\2\\-1\\2\end{bmatrix},
\begin{bmatrix}0\\1\\2\\-1\end{bmatrix},
\begin{bmatrix}0\\0\\1\\-2\end{bmatrix}
\right)
$$

> 🤷‍♂️ Dimension = reduced row echelon form 的 pivot column 數量

以下解釋了為何 rref\(A\) 的 pivot column 會等於 C\(A\) 的 basis

> Showing relation between basis cols and pivot cols
>
> * [https://youtu.be/BfVjTOjvI30](https://youtu.be/BfVjTOjvI30)
>
> Showing that the candidate basis does span C\(A\)
>
> * [https://youtu.be/CkQOCnLWPUA](https://youtu.be/CkQOCnLWPUA)

