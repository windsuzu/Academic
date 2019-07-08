# Finding inverses and determinants

### Deriving a method for determining inverses

- https://youtu.be/6DpzCKJBsz0

我們在做 matrix 轉為 reduced row echelon form 的過程中
$$
\mathbf{A} = 
\begin{bmatrix} 1&-1&-1\\-1&2&3\\1&1&4\end{bmatrix} \rightarrow
\begin{bmatrix} 1&-1&-1\\0&1&2\\0&2&5\end{bmatrix}
$$
其實每個轉換，都是一個 transformation

例如上面消去 row 2 和 row 3 的第一個 element，可以表示成以下的 transformation
$$
T \begin{bmatrix} a_1 \\ a_2\\ a_3\end{bmatrix} \rightarrow
\begin{bmatrix} a_1 \\ a_2+a_1\\ a_3-a_1\end{bmatrix}
$$
而這個 transformation 又可以表示成 matrix，我們知道可以用 identity matrix 當基底來建立
$$
T(\vec{x}) = \mathbf{S_1} \vec{x} \\
\mathbf{S_1} = \begin{bmatrix} 1&0&0\\0&1&0\\0&0&1\end{bmatrix}
\rightarrow
\begin{bmatrix} 1&0&0\\1&1&0\\-1&0&1\end{bmatrix}
$$
也就是說，剛剛 A 在消去 row 2 和 row 3 的動作，其實就是
$$
\begin{align} 
&\begin{bmatrix} 
\mathbf{S}\begin{bmatrix} 1\\-1\\1\end{bmatrix}&
\mathbf{S}\begin{bmatrix} -1\\2\\1\end{bmatrix}&
\mathbf{S}\begin{bmatrix} -1\\3\\4\end{bmatrix}
\end{bmatrix}\\
=\,\, &\mathbf{S_1}\mathbf{A} \\
= &\begin{bmatrix} 1&0&0\\1&1&0\\-1&0&1\end{bmatrix}
\begin{bmatrix} 1&-1&-1\\-1&2&3\\1&1&4\end{bmatrix}
=\,\,\begin{bmatrix} 1&-1&-1\\0&1&2\\0&2&5\end{bmatrix}
\end{align}
$$


我們可以繼續對未完成 reduced row echelon form 的 matrix 進行簡化
$$
\begin{bmatrix} 1&-1&-1\\0&1&2\\0&2&5\end{bmatrix}
\rightarrow
\begin{bmatrix} 1&0&1\\0&1&2\\0&0&1\end{bmatrix}
$$
這次的簡化等於
$$
T \begin{bmatrix} a_1 \\ a_2\\ a_3\end{bmatrix} \rightarrow
\begin{bmatrix} a_1+a_2 \\ a_2\\ a_3-2a_2\end{bmatrix} \Rightarrow
\mathbf{S_2} = 
\begin{bmatrix} 1&1&0\\0&1&0\\0&-2&1\end{bmatrix}
$$
而這個 S2 apply 在 S1*A 上
$$
\mathbf{S_2}(\mathbf{S_1}\mathbf{A}) = 
\begin{bmatrix} 1&1&0\\0&1&0\\0&-2&1\end{bmatrix}
\begin{bmatrix} 1&-1&-1\\0&1&2\\0&2&5\end{bmatrix}
=\begin{bmatrix} 1&0&1\\0&1&2\\0&0&1\end{bmatrix}
$$


還是可以繼續化簡第三行
$$
\begin{bmatrix} 1&0&1\\0&1&2\\0&0&1\end{bmatrix} \rightarrow
\begin{bmatrix} 1&0&0\\0&1&0\\0&0&1\end{bmatrix}
$$

$$
T \begin{bmatrix} a_1 \\ a_2\\ a_3\end{bmatrix} \rightarrow
\begin{bmatrix} a_1-a_3 \\ a_2-2a_3\\ a_3\end{bmatrix} \Rightarrow
\mathbf{S_3} = 
\begin{bmatrix} 1&0&-1\\0&1&-2\\0&0&1\end{bmatrix}
$$

$$
\mathbf{S_3}(\mathbf{S_2}(\mathbf{S_1}\mathbf{A})) = 
\begin{bmatrix} 1&0&-1\\0&1&-2\\0&0&1\end{bmatrix}
\begin{bmatrix} 1&0&1\\0&1&2\\0&0&1\end{bmatrix}
=\begin{bmatrix} 1&0&0\\0&1&0\\0&0&1\end{bmatrix}
$$

可以發現原來 S3 × S2 × S1 的 Product 就是 A 的 inverse matrix
$$
\begin{align}
\mathbf{S_3S_2S_1A} &= \mathbf{I}\\
\mathbf{A^{-1}A}&= \mathbf{I}
\end{align}
$$


但其實不用每次找 inverse function / inverse matrix 都搞的這麼麻煩

上面這樣做只是為了了解尋找 inverse matrix 的原理而已
$$
\begin{align}
&\mathbf{A}&&\mathbf{I}\\
&\mathbf{S_1A}&&\mathbf{S_1I}\\
&\mathbf{S_2S_1A}&&\mathbf{S_2S_1I}\\
&\mathbf{S_3S_2S_1A}&&\mathbf{S_3S_2S_1I}\\
\Rightarrow\,\, &\mathbf{I}&&\mathbf{A^{-1}}\\
\end{align}
$$
我們同時對 matrix A 和 identity matrix 做同樣的 row operation transformation

發現當 A 為 invertible 時 (可以變成 Identity matrix)，對 I 做相同的簡化運算，可以得到 inverse matrix
$$
\begin{bmatrix} \mathbf{A} \mid \mathbf{I}\end{bmatrix}
\rightarrow
\cdots
\rightarrow
\begin{bmatrix} \mathbf{I} \mid \mathbf{A^{-1}}\end{bmatrix}
$$


### Example of finding matrix inverse

* https://youtu.be/r9aTLTN16V4

我們實際來運用剛剛發現的方式，尋找 inverse matrix
$$
\mathbf{A} = \begin{bmatrix} 1&-1&-1\\-1&2&3\\1&1&4\end{bmatrix}
$$
首先將 A 和 I 畫在一起
$$
\begin{bmatrix} \mathbf{A} \mid \mathbf{I}\end{bmatrix} =
\begin{bmatrix} 
\begin{array}{ccc|ccc} 
1&-1&-1&1&0&0\\-1&2&3&0&1&0\\1&1&4&0&0&1 
\end{array}
\end{bmatrix}
$$
先對 A 清空第一行，同樣的運算一樣 apply 到隔壁的 identity matrix
$$
\begin{bmatrix} \mathbf{S_1A} \mid \mathbf{S_1}\end{bmatrix} =
\begin{bmatrix} 
\begin{array}{ccc|ccc} 
1&-1&-1&1&0&0\\0&1&2&1&1&0\\0&2&5&-1&0&1 
\end{array}
\end{bmatrix}
$$
再來清空第二行
$$
\begin{bmatrix} \mathbf{S_2S_1A} \mid \mathbf{S_2S_1}\end{bmatrix} =
\begin{bmatrix} 
\begin{array}{ccc|ccc} 
1&0&1&2&1&0\\0&1&2&1&1&0\\0&0&1&-3&-2&1 
\end{array}
\end{bmatrix}
$$
最後是第三行
$$
\begin{bmatrix} \mathbf{S_3S_2S_1A} \mid \mathbf{S_3S_2S_1}\end{bmatrix} =
\begin{bmatrix} \mathbf{I} \mid \mathbf{A^{-1}}\end{bmatrix} =
\begin{bmatrix} 
\begin{array}{ccc|ccc} 
1&0&0&5&3&-1\\0&1&0&7&5&-2\\0&0&1&-3&-2&1 
\end{array}
\end{bmatrix}
$$
如此一來我們就找到 A 的 inverse matrix
$$
\mathbf{A^{-1}} =
\begin{bmatrix} 
5&3&-1\\7&5&-2\\-3&-2&1 
\end{bmatrix}
$$


### Formula for 2x2 inverse

* https://youtu.be/eEUK_ThrHuQ

我們來找出所有 2 × 2 matrix 的 inverse matrix
$$
\mathbf{A} = \begin{bmatrix} a&b\\c&d\end{bmatrix} \Rightarrow
\begin{bmatrix} \begin{array}{cc|cc} a&b&1&0\\c&d&0&1\end{array}\end{bmatrix}
$$
首先我們要讓 c 變為 0，等於要對 row vectors 執行底下這個 transformation
$$
T_1\left(\begin{bmatrix} c_1 \\ c_2 \end{bmatrix}\right) =
\begin{bmatrix} c_1 \\ ac_2 - cc_1 \end{bmatrix}
$$
第一列保留不變，第二列試著將 c 消為 0
$$
\begin{bmatrix} \begin{array}{cc|cc} a&b&1&0\\c&d&0&1\end{array}\end{bmatrix}
\rightarrow
\begin{bmatrix} \begin{array}{cc|cc} a&b&1&0\\0&ad-bc&-c&a\end{array}\end{bmatrix}
$$


接著我們要讓 b 變為 0
$$
T_2\left(\begin{bmatrix} c_1 \\ c_2 \end{bmatrix}\right) =
\begin{bmatrix} c_1(ad-bc)-c_2(b) \\ c_2 \end{bmatrix}
$$
第二列保留不變，第一列試著將 b 消為 0
$$
\begin{align}
\begin{bmatrix} \begin{array}{cc|cc} a&b&1&0\\0&ad-bc&-c&a\end{array}\end{bmatrix}
&\rightarrow
\begin{bmatrix} \begin{array}{cc|cc} a(ad-bc)&(b)(ad-bc)-(ad-bc)(b)&ad-bc+bc&-ab\\0&ad-bc&-c&a\end{array}\end{bmatrix}\\
&\rightarrow
\begin{bmatrix} \begin{array}{cc|cc} a(ad-bc)&0&ad&-ab\\0&ad-bc&-c&a\end{array}\end{bmatrix}
\end{align}
$$


最後我們要讓 A 變為  identity matrix 完成 reduced row echelon form
$$
T_3\left(\begin{bmatrix} c_1 \\ c_2 \end{bmatrix}\right) =
\begin{bmatrix} \frac{c_1}{a(ad-bc)} \\ \frac{c_2}{ad-bc} \end{bmatrix}
$$
於是我們得到
$$
\begin{align}
\begin{bmatrix} \begin{array}{cc|cc} a(ad-bc)&0&ad&-ab\\0&ad-bc&-c&a\end{array}\end{bmatrix}
&\rightarrow
\begin{bmatrix} \begin{array}{cc|cc} 1&0&\frac{ad}{a(ad-bc)}&\frac{-ab}{a(ad-bc)}\\0&1&-\frac{c}{ad-bc}&\frac{a}{ad-bc}\end{array}\end{bmatrix} \\
&\rightarrow
\begin{bmatrix} \begin{array}{cc|cc} 1&0&\frac{d}{ad-bc}&\frac{-b}{ad-bc}\\0&1&-\frac{c}{ad-bc}&\frac{a}{ad-bc}\end{array}\end{bmatrix} = 
\begin{bmatrix} \mathbf{I} \mid \mathbf{A^{-1}} \end{bmatrix}
\end{align}
$$
我們可以將 inverse matrix 進一步化簡，每個分母都是 ad - bc ，我們將他提出
$$
\mathbf{A^{-1}} = \begin{bmatrix}
\frac{d}{ad-bc}&\frac{-b}{ad-bc}\\-\frac{c}{ad-bc}&\frac{a}{ad-bc}
\end{bmatrix}
= \frac{1}{ad-bc}
\begin{bmatrix}
d&-b\\-c&a
\end{bmatrix}
$$
而這個就是所有 2 × 2 matrix 的 inverse matrix 

> 可以記成 d 和 a 互換， b 和 c 變負



但我們知道，只有 matrix 為 invertible 才會有 inverse function

這個公式剛好可以看出 matrix 是否為 invertible

只要公式得出的結果為 undefined ，則 matrix 即為 non-invertible

而關鍵就在於 ad - bc 等於 0 的時候，公式結果即為 undefined
$$
ad -bc \neq 0 \iff \mathbf{A} \text{ is invertible}
$$
而這個 ad - bc 有一個名稱，叫作 determinant
$$
\det(\mathbf{A}) = 
\left\lvert \mathbf{A} \right\rvert =
\left\lvert \begin{bmatrix} a&b\\c&d\end{bmatrix} \right\rvert =
\left\lvert \begin{matrix} a&b\\c&d\end{matrix} \right\rvert =
ad - bc
$$
所以公式可以再一次簡化
$$
\mathbf{A^{-1}} = \frac{1}{\det(\mathbf{A})}
\begin{bmatrix} d&-b\\-c&a\end{bmatrix}
$$

* 舉個可以 invertible 的例子

$$
\det(\mathbf{B}) =
\left\lvert \begin{matrix} 1&2\\3&4\end{matrix} \right\rvert = 1 \times4-3\times2 = 4-6=-2 \text{ (invertible)} \\
\mathbf{B^{-1}} = \frac{1}{-2}\begin{bmatrix} 4&-2\\-3&1\end{bmatrix} =
\begin{bmatrix} -2&1\\\frac{3}{2}&\frac{1}{-2}\end{bmatrix}
$$



* 舉個不可以 invertible 的例子

$$
\det(\mathbf{C}) =
\left\lvert \begin{matrix} 1&2\\3&6\end{matrix} \right\rvert =
1 \times 6 - 3 \times 2 = 6- 6 = 0 \text{ (non-invertible)}
$$

的確，column 2 可以表示為 column 1 * 2

代表他們是 linear dependence，沒辦法 one-to-one，所以為 non invertible，沒有 inverse matrix



### 3 x 3 determinant

* https://youtu.be/0c7dt2SQfLw

在 generalize determinant 公式前，我們先來試算 3 by 3 matrix 的 determinant

因為我們知道 determinant 很重要，可以快速看出一個 matrix 是否為 invertible
$$
\mathbf{A} = \begin{bmatrix} a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{bmatrix}
$$

$$
\det(\mathbf{A}) = 
a_{11}\left\lvert\begin{matrix}a_{22}&a_{23}\\a_{32}&a_{33}\end{matrix}\right\rvert -
a_{12}\left\lvert\begin{matrix}a_{21}&a_{23}\\a_{31}&a_{33}\end{matrix}\right\rvert +
a_{13}\left\lvert\begin{matrix}a_{21}&a_{22}\\a_{31}&a_{32}\end{matrix}\right\rvert
$$

看起來很抽象，我們實際操作一個 matrix 看看
$$
\mathbf{C} = \begin{bmatrix} 1&2&4\\2&-1&3\\4&0&1\end{bmatrix}
$$

$$
\begin{align}
\det(\mathbf{C}) &= 
1\left\lvert\begin{matrix}-1&-3\\0&1\end{matrix}\right\rvert -
2\left\lvert\begin{matrix}2&3\\4&1\end{matrix}\right\rvert +
4\left\lvert\begin{matrix}2&-1\\4&0\end{matrix}\right\rvert \\
&= 1 \cdot (-1) - 2\cdot(-10)+4\cdot(4) \\
&= -1 +20 + 16 \\
&= 35
\end{align}
$$

所以 C = invertible