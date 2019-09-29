# Matrices for solving systems by elimination

## Solve Linear System with matrix row-echelon form

我們可以利用矩陣之力，將 Linear system 轉為矩陣快速解出答案

$$
\left\{\begin{matrix}
x_1+2x_2+x_3+x_4=7\\
x_1+2x_2+2x_3-x_4=12\\ 
2x_1+4x_2+6x_4=4
\end{matrix}\right.
$$

可以轉為 Augmented matrix

$$
A=\begin{bmatrix} 
\begin{array}{cccc|c} 
1&2&1&1&7\\
1&2&2&-1&12\\
2&4&0&6&4\\
\end{array}\end{bmatrix}
$$

將矩陣運算至 Reduced Row-echelon form

* 紅色的為 Leading 1s 只在該列有他一個 1 存在，該元素又稱為 pivot value
* 而藍色的為 free variables

$$
\begin{bmatrix} 
\begin{array}{cccc|c} 
\color{red}1&\color{blue}2&0&\color{blue}3&2\\
0&0&\color{red}1&\color{blue}-2&5\\
0&0&0&0&0\\
\end{array}\end{bmatrix} = \text{rref}(A)
$$

我們可以將結果轉回 equations

$$
\begin{aligned}
&\left\{\begin{matrix}
x_1+2x_2+3x_4=2\\
x_3-2x_4=5
\end{matrix}\right.\\\\
\Rightarrow\,& 
\left\{\begin{matrix}
x_1 = 2-2x_2-3x_4\\
x_3 = 5 + 2x_4
\end{matrix}\right.\\
\end{aligned}
$$

並且可以表示成像 linear combination 的形式

$$
\begin{bmatrix}x_1\\x_2\\x_3\\x_4\end{bmatrix} =
\begin{bmatrix}2\\0\\5\\0\end{bmatrix} +
x_2\begin{bmatrix}-2\\1\\0\\0\end{bmatrix}+
x_4\begin{bmatrix}-3\\0\\2\\1\end{bmatrix}
$$

在圖形上看起來像是這樣

![](../../.gitbook/assets/linear_system.jpg)

## linear systems

若你的 reduced-row echelon form 算到變成這樣時

$$
\begin{bmatrix} 
\begin{array}{cccc|c} 
1&2&0&3&4\\
0&0&1&-2&4\\
\color{red}0&\color{red}0&\color{red}0&\color{red}0&\color{red}-4\\
\end{array}\end{bmatrix}
$$

表示你的三個 R4 向量在空間內是沒有交集的，所以是**無解 \(no solution\)**

而每一個 leading ones 都可以對應一個值，這樣子代表**唯一解 \(uniqle solution\)**

$$
\begin{bmatrix} 
\begin{array}{cccc|c} 
1&x&x&x&a\\
0&1&x&x&b\\
0&0&1&x&c\\
0&0&0&1&d\\
\end{array}\end{bmatrix}
$$

而上面的例題中，含有 free variables 的，代表沒有唯一解，也就是**無限多解**

$$
\begin{bmatrix} 
\begin{array}{cccc|c} 
\color{red}1&\color{blue}2&0&\color{blue}3&2\\
0&0&\color{red}1&\color{blue}-2&5\\
0&0&0&0&0\\
\end{array}\end{bmatrix}
$$

