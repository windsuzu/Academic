# Finding inverses and determinants

## Deriving a method for determining inverses

* [https://youtu.be/6DpzCKJBsz0](https://youtu.be/6DpzCKJBsz0)

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
\begin{aligned} 
&\begin{bmatrix} 
\mathbf{S}\begin{bmatrix} 1\\-1\\1\end{bmatrix}&
\mathbf{S}\begin{bmatrix} -1\\2\\1\end{bmatrix}&
\mathbf{S}\begin{bmatrix} -1\\3\\4\end{bmatrix}
\end{bmatrix}\\
=\,\, &\mathbf{S_1}\mathbf{A} \\
= &\begin{bmatrix} 1&0&0\\1&1&0\\-1&0&1\end{bmatrix}
\begin{bmatrix} 1&-1&-1\\-1&2&3\\1&1&4\end{bmatrix}
=\,\,\begin{bmatrix} 1&-1&-1\\0&1&2\\0&2&5\end{bmatrix}
\end{aligned}
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

而這個 S2 apply 在 S1\*A 上

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
\begin{aligned}
\mathbf{S_3S_2S_1A} &= \mathbf{I}\\
\mathbf{A^{-1}A}&= \mathbf{I}
\end{aligned}
$$

但其實不用每次找 inverse function / inverse matrix 都搞的這麼麻煩

上面這樣做只是為了了解尋找 inverse matrix 的原理而已

$$
\begin{aligned}
&\mathbf{A}&&\mathbf{I}\\
&\mathbf{S_1A}&&\mathbf{S_1I}\\
&\mathbf{S_2S_1A}&&\mathbf{S_2S_1I}\\
&\mathbf{S_3S_2S_1A}&&\mathbf{S_3S_2S_1I}\\
\Rightarrow\,\, &\mathbf{I}&&\mathbf{A^{-1}}\\
\end{aligned}
$$

我們同時對 matrix A 和 identity matrix 做同樣的 row operation transformation

發現當 A 為 invertible 時 \(可以變成 Identity matrix\)，對 I 做相同的簡化運算，可以得到 inverse matrix

$$
\begin{bmatrix} \mathbf{A} \mid \mathbf{I}\end{bmatrix}
\rightarrow
\cdots
\rightarrow
\begin{bmatrix} \mathbf{I} \mid \mathbf{A^{-1}}\end{bmatrix}
$$

## Example of finding matrix inverse

* [https://youtu.be/r9aTLTN16V4](https://youtu.be/r9aTLTN16V4)

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

## Formula for 2x2 inverse

* [https://youtu.be/eEUK\_ThrHuQ](https://youtu.be/eEUK_ThrHuQ)

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
\begin{aligned}
\begin{bmatrix} \begin{array}{cc|cc} a&b&1&0\\0&ad-bc&-c&a\end{array}\end{bmatrix}
&\rightarrow
\begin{bmatrix} \begin{array}{cc|cc} a(ad-bc)&(b)(ad-bc)-(ad-bc)(b)&ad-bc+bc&-ab\\0&ad-bc&-c&a\end{array}\end{bmatrix}\\
&\rightarrow
\begin{bmatrix} \begin{array}{cc|cc} a(ad-bc)&0&ad&-ab\\0&ad-bc&-c&a\end{array}\end{bmatrix}
\end{aligned}
$$

最後我們要讓 A 變為 identity matrix 完成 reduced row echelon form

$$
T_3\left(\begin{bmatrix} c_1 \\ c_2 \end{bmatrix}\right) =
\begin{bmatrix} \frac{c_1}{a(ad-bc)} \\ \frac{c_2}{ad-bc} \end{bmatrix}
$$

於是我們得到

$$
\begin{aligned}
\begin{bmatrix} \begin{array}{cc|cc} a(ad-bc)&0&ad&-ab\\0&ad-bc&-c&a\end{array}\end{bmatrix}
&\rightarrow
\begin{bmatrix} \begin{array}{cc|cc} 1&0&\frac{ad}{a(ad-bc)}&\frac{-ab}{a(ad-bc)}\\0&1&-\frac{c}{ad-bc}&\frac{a}{ad-bc}\end{array}\end{bmatrix} \\
&\rightarrow
\begin{bmatrix} \begin{array}{cc|cc} 1&0&\frac{d}{ad-bc}&\frac{-b}{ad-bc}\\0&1&-\frac{c}{ad-bc}&\frac{a}{ad-bc}\end{array}\end{bmatrix} = 
\begin{bmatrix} \mathbf{I} \mid \mathbf{A^{-1}} \end{bmatrix}
\end{aligned}
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

的確，column 2 可以表示為 column 1 \* 2

代表他們是 linear dependence，沒辦法 one-to-one，所以為 non invertible，沒有 inverse matrix

## 3 x 3 determinant

* [https://youtu.be/0c7dt2SQfLw](https://youtu.be/0c7dt2SQfLw)

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
\begin{aligned}
\det(\mathbf{C}) &= 
1\left\lvert\begin{matrix}-1&-3\\0&1\end{matrix}\right\rvert -
2\left\lvert\begin{matrix}2&3\\4&1\end{matrix}\right\rvert +
4\left\lvert\begin{matrix}2&-1\\4&0\end{matrix}\right\rvert \\
&= 1 \cdot (-1) - 2\cdot(-10)+4\cdot(4) \\
&= -1 +20 + 16 \\
&= 35
\end{aligned}
$$

所以 C = invertible

## n x n determinant

* [https://youtu.be/H9BWRYJNIv4](https://youtu.be/H9BWRYJNIv4)

學會 3 × 3 之後，來試試看 n × n 的格式

$$
\mathbf{A}_{n \times n } = 
\begin{bmatrix} a_{11} & a_{12} &\cdots &a_{1n}\\
a_{21}  &\cdots&&a_{2n} \\ \vdots& &\ddots&\vdots \\
a_{n1}&\cdots&\cdots&a_{nn}
\end{bmatrix}
$$

我們定義一個矩陣 Aij 代表 A 去掉 i row 和 j column 時的樣子

$$
\begin{aligned}
\text{Def: }\mathbf{A}_{ij}=  &(n-1) \times (n-1) \text{ matrix you get}\\
& \text{ if you "ignore" the } i^{th} \text{ row and the } j^{th} \text{ column of }\mathbf{A}

\end{aligned}
$$

看起來很抽象所以舉個例子

$$
\begin{aligned}
\mathbf{A} &= \begin{bmatrix} 1&2&4\\2&-1&3\\4&0&1\end{bmatrix} \\

\mathbf{A}_{11}&= \begin{bmatrix} -1 &3\\0&1\end{bmatrix}, 
\mathbf{A}_{12}= \begin{bmatrix} 2&3\\4&1\end{bmatrix},
\mathbf{A}_{13}= \begin{bmatrix} 2&-1\\4&0\end{bmatrix} \\
\det(\mathbf{A}) &=a_{11} \cdot \mathbf{A}_{11} - a_{12} \cdot \mathbf{A}_{12} + a_{13} \cdot \mathbf{A}_{13}
\end{aligned}
$$

接著就可以來定義 n × n 的 determinant:

$$
\det(\mathbf{A}_{n \times n}) = a_{11} \det(\mathbf{A_{11}}) - a_{12} \det(\mathbf{A_{12}})  +  a_{13} \det(\mathbf{A_{13}})  - + \cdots \pm a_{1n}\det(A_{1n})
$$

這個定義就是個 **recursive definition** ，可以一直往下 solve 到 2 × 2 matrix

我們來試個 4 × 4 的例子

$$
\left\lvert \begin{matrix} 1&2&3&4\\1&0&2&0\\0&1&2&3\\2&3&0&0\end{matrix}\right\rvert
= 1\left\lvert \begin{matrix} 0&2&0\\1&2&3\\3&0&0 \end{matrix} \right\rvert
- 2\left\lvert \begin{matrix} 1&2&0\\0&2&3\\2&0&0 \end{matrix} \right\rvert
+ 3\left\lvert \begin{matrix} 1&0&0\\0&1&3\\2&3&0 \end{matrix} \right\rvert
- 4\left\lvert \begin{matrix} 1&0&2\\0&1&2\\2&3&0 \end{matrix} \right\rvert
$$

接著可以往下 solve 3 × 3 的矩陣，等於

$$
\begin{aligned}
1 \left(
0\left\lvert \begin{matrix} 2&3\\0&0 \end{matrix} \right\rvert 
-2 \left\lvert \begin{matrix} 1&3\\3&0 \end{matrix} \right\rvert 
+0 \left\lvert \begin{matrix} 1&2\\3&0 \end{matrix} \right\rvert \right) \\ 

-2 \left(
1\left\lvert \begin{matrix} 2&3\\0&0 \end{matrix} \right\rvert 
-2 \left\lvert \begin{matrix} 0&3\\2&0 \end{matrix} \right\rvert 
+0 \left\lvert \begin{matrix} 0&2\\2&0 \end{matrix} \right\rvert \right) \\

+3 \left(
1\left\lvert \begin{matrix} 1&3\\3&0 \end{matrix} \right\rvert 
-0 \left\lvert \begin{matrix} 0&3\\2&0 \end{matrix} \right\rvert 
+0 \left\lvert \begin{matrix} 0&1\\2&3 \end{matrix} \right\rvert \right) \\

-4 \left(
1\left\lvert \begin{matrix} 1&2\\3&0 \end{matrix} \right\rvert 
-0 \left\lvert \begin{matrix} 0&2\\2&0 \end{matrix} \right\rvert 
+2 \left\lvert \begin{matrix} 0&1\\2&3 \end{matrix} \right\rvert \right)
\end{aligned}
$$

接著就可以解掉 2 × 2 的矩陣了！

$$
\begin{aligned}
1 \left(
0+(-2)\times(-9)+0 \right) \\ 

-2 \left(0+(-2)\times(-6)+0 \right)\\

+3 \left(1\times(-9)-0+0\right) \\

-4 \left(
1 \times(-6) -0 +2 \times(-2) \right)
\end{aligned}
$$

得到答案

$$
\begin{aligned}
&1(18) -2 (12)+3(-9)-4(-6-4)\\
=\,\,&18 -24-27 +40 \\
=\,\,& 7
\end{aligned}
$$

也就是說，這個矩陣是 invertible 的

## Determinants along other rows/cols

* [https://youtu.be/nu87kfmwNfU](https://youtu.be/nu87kfmwNfU)

其實求 determinant 不是只能展開第一列，可以從任何一列或一行來展開

也就是說我們可以選擇很多 0 的那一列 \(行\) 來展開

只是我們要注意展開的正負符號

$$
\left\lvert \begin{matrix}+&-&+&-&\cdots\\-&+&-&+&\cdots\\+&-&+&-&\cdots\\-&+&-&+&\cdots\\\vdots&\vdots&\vdots&\vdots&\ddots\end{matrix}\right\rvert
$$

其實就是在前面加上 row 和 column 判斷

$$
(-1)^{\text{row} + \text{column}}
$$

在第一列第一行的就是正號

$$
(-1)^{1+1} = (-1)^2 = 1
$$

我們以上面的例子來做看看，我們展開第二列，因為有兩個 0

$$
\left\lvert \begin{matrix} 1&2&3&4\\
\color{red}{1}&\color{red}{0}&\color{red}{2}&\color{red}{0}
\\0&1&2&3\\2&3&0&0\end{matrix}\right\rvert = 
-1 \left\lvert \begin{matrix} 2&3&4\\1&2&3\\3&0&0\end{matrix}\right\rvert
-2 \left\lvert \begin{matrix} 1&2&4\\0&1&3\\2&3&0\end{matrix}\right\rvert
$$

再來第一個 3 × 3 當然展開第三列，第二個我們展開第二列好了

$$
= -1\left(3\times \left\lvert \begin{matrix} 3&4\\2&3\end{matrix}\right\rvert\right)
-2 \left(1\left\lvert \begin{matrix} 1&4\\2&0\end{matrix}\right\rvert
-3\left\lvert \begin{matrix} 1&2\\2&3\end{matrix}\right\rvert
\right)
$$

我們比剛剛更快的還要求到 determinant

$$
\begin{aligned}
&= ((-1) \times 3) - (2\times(-8 +3))\\
&= (-3) - (-10) \\
&=7
\end{aligned}
$$

## Rule of Sarrus of determinants

* [https://youtu.be/4xFIi0JF2AM](https://youtu.be/4xFIi0JF2AM)

這邊還有一個方法可以用來求 3 × 3 的 determinant ，叫作 **Rule of Sarrus**

我們先將一般的 3 × 3 determinant 求出

$$
\begin{aligned}
\left\lvert \begin{matrix} a&b&c\\d&e&f\\g&h&i \end{matrix}\right\rvert &= 
a \left\lvert \begin{matrix} e&f\\h&i \end{matrix}\right\rvert -
b \left\lvert \begin{matrix} d&f\\g&i \end{matrix}\right\rvert +
c \left\lvert \begin{matrix} d&e\\g&h \end{matrix}\right\rvert \\
&= a(ei-fh) - b(di-fg) + c(dh-eg)\\
&= aei - afh -bdi + bfg +cdh - ceg \\
&= \color{blue}{(aei+bfg+cdh)} + \color{red}{(-afh-bdi-ceg)}
\end{aligned}
$$

仔細觀察，等於我們將矩陣多畫出兩行，然後將紅色部分 + 藍色部分

![](../../.gitbook/assets/sarrus.jpg)

一樣來舉個例子

$$
\mathbf{A} = \begin{bmatrix} 1&2&4\\2&-1&3\\4&0&-1\end{bmatrix}
$$

$$
\begin{aligned}
\det(\mathbf{A}) &= 
\left\lvert \begin{matrix} 1&2&4\\2&-1&3\\4&0&-1\end{matrix}\right\rvert
\begin{matrix} 1&2\\2&-1\\4&0\end{matrix} \\\\
&= 
\color{red}{(1 \cdot (-1) \cdot(-1)) + (2\cdot3\cdot4) + (4\cdot2\cdot0)} 
\color{blue}{- (4\cdot(-1)\cdot4) - (1\cdot3\cdot0) - (2\cdot2\cdot-1)} \\
&= 1+24+0 +16-0+4 \\
&= 45
\end{aligned}
$$

