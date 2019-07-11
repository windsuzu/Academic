# More determinant depth

### Determinant when row multiplied by scalar

* https://youtu.be/32rdijPB-rA

我們將矩陣某一列全部乘以 k 會發生什麼事呢
$$
\left\lvert\begin{matrix} a&b\\kc&kd \end{matrix}\right\rvert =
kad - kbc = 
k(ad-bc) =
k\left\lvert\begin{matrix} a&b\\c&d \end{matrix}\right\rvert
$$
新的 determinant 會等於原本的 determinant 乘上 k



那如果兩列都乘以 k 會怎麼樣呢
$$
\left\lvert\begin{matrix} ka&kb\\kc&kd \end{matrix}\right\rvert =
k^2(ad)-k^2(bc) = 
k^2(ad-bc) =
k^2\left\lvert\begin{matrix} a&b\\c&d \end{matrix}\right\rvert
$$
會變成 k 的 2 次方 ( 2 列 ) 再乘以 determinant



假設今天有一個 3 × 3 矩陣 A
$$
\mathbf{A} = \begin{bmatrix} a&b&c\\d&e&f\\g&h&i\end{bmatrix}
$$
我們從他的第二列展開 determinant 會得到
$$
\lvert \mathbf{A} \rvert = 
- d\left\lvert\begin{matrix} b&c\\h&i \end{matrix}\right\rvert
+e\left\lvert\begin{matrix} a&c\\g&i \end{matrix}\right\rvert
-f\left\lvert\begin{matrix} a&b \\ g&h\end{matrix}\right\rvert
$$
現在我們將第二列元素都乘上 k 得到 A'， A' 的 determinant 會等於
$$
\begin{align}
\lvert \mathbf{A'} \rvert &= 
-kd\left\lvert\begin{matrix} b&c\\h&i \end{matrix}\right\rvert
+ke\left\lvert\begin{matrix} a&c\\g&i \end{matrix}\right\rvert
-kf\left\lvert\begin{matrix} a&b \\ g&h\end{matrix}\right\rvert \\
&=k\left(-d\left\lvert\begin{matrix} b&c\\h&i \end{matrix}\right\rvert
+e\left\lvert\begin{matrix} a&c\\g&i \end{matrix}\right\rvert
-f\left\lvert\begin{matrix} a&b \\ g&h\end{matrix}\right\rvert\right) \\
&= k \lvert \mathbf{A}\rvert
\end{align}
$$
我們試著將他 generalize 成 n × n 矩陣
$$
\mathbf{A}_{n\times n} = \begin{bmatrix} 
a_{11} & a_{12} & \cdots &a_{1n}\\
\vdots\\
\color{red}{a_{i1}} & \color{red}{a_{i2}} & \cdots &\color{red}{a_{in}}\\
\vdots\\
a_{n1} & a_{n2} & \cdots &a_{nn}
\end{bmatrix}
$$
假設我們從第 i 列展開，可以得到
$$
\begin{align}
\det(\mathbf{A}) &= 
(-1)^{i+1}a_{i1}\det(\mathbf{A}_{i1}) +
(-1)^{i+2}a_{i2}\det(\mathbf{A}_{i2}) +
\cdots +
(-1)^{i+n}a_{in}\det(\mathbf{A}_{in}) \\
&= \sum_{j=1}^{j=n}\left((-1)^{i+j}a_{ij}\det(\mathbf{A}_{ij}\right)
\end{align}
$$
現在第 i 列全部乘以 k 了，新的 A' 的 determinant 等於
$$
\begin{align}
\det(\mathbf{A'}) &= 
(-1)^{i+1}\color{red}{k}a_{i1}\det(\mathbf{A}_{i1}) +
(-1)^{i+2}\color{red}{k}a_{i2}\det(\mathbf{A}_{i2}) +
\cdots +
(-1)^{i+n}\color{red}{k}a_{in}\det(\mathbf{A}_{in}) \\
&= \sum_{j=1}^{j=n}\left((-1)^{i+j}\color{red}{k}a_{ij}\det(\mathbf{A}_{ij}\right) \\
&= \color{red}{k}\sum_{j=1}^{j=n}\left((-1)^{i+j}a_{ij}\det(\mathbf{A}_{ij}\right) \\
&= \color{red}{k}\det(\mathbf{A})
\end{align}
$$
現在我們可以確定，當你對 matrix 的 n row 執行 multiplication by k

你的 determinant 就必須要乘以 k 的 n 次方
$$
\det(k\mathbf{A}) = k^n\det(\mathbf{A})
$$


### Determinant when row is added

* https://youtu.be/VrB3LaSD_uo

什麼時候 determinant 會等於另外兩個 matrix 的 determinant 的相加呢
$$
\mathbf{X} = \begin{bmatrix} a &b \\x_1&x_2\end{bmatrix},
\mathbf{Y} = \begin{bmatrix} a &b \\y_1&y_2\end{bmatrix},
\mathbf{Z} = \begin{bmatrix} a &b \\x_1+y_1&x_2+y_2\end{bmatrix}
$$

$$
\begin{align}
\det(\mathbf{X}) &= ax_2-bx_1 \\
\det(\mathbf{Y}) &= ay_2-by_1 \\
\det(\mathbf{Z}) &= a(x_2+y_2)-b(x_1+y_1) \\
&=ax_2+ay_2-bx_1-by_1 \\
&= (ax_2-bx_1)+(ay_2-by_1)\\
&= \det(\mathbf{X}) + \det(\mathbf{Y})
\end{align}
$$

看起來是只有某一列不同，其他列完全相同的時候，他們的 determinant 才會有所關聯

我們換成 n × n 矩陣觀察
$$
\mathbf{X} = \begin{bmatrix} 
a_{11} &a_{12} & \cdots & a_{1n}\\
\vdots \\
x_1&x_2&\cdots&x_n\\
\vdots\\
a_{n1} &a_{n2} &\cdots& a_{nn}
\end{bmatrix},
\mathbf{Y} = \begin{bmatrix} 
a_{11} &a_{12} & \cdots & a_{1n}\\
\vdots \\
y_1&y_2&\cdots&y_n\\
\vdots\\
a_{n1} &a_{n2} &\cdots& a_{nn}
\end{bmatrix},
\mathbf{Z} = \begin{bmatrix} 
a_{11} &a_{12} & \cdots & a_{1n}\\
\vdots \\
x_1+y_1&x_2+y_2&\cdots&x_n +y_n \\
\vdots\\
a_{n1} &a_{n2} &\cdots& a_{nn}
\end{bmatrix}
$$
各別求出他們的 determinants
$$
\begin{align}
\det(\mathbf{X}) = \sum_{j=1}^n(-1)^{i+j}x_j\det(\mathbf{A}_{ij}) \\
\det(\mathbf{Y}) = \sum_{j=1}^n(-1)^{i+j}y_j\det(\mathbf{A}_{ij}) \\
\det(\mathbf{Z}) = \sum_{j=1}^n(-1)^{i+j}(x_j +y_j)\det(\mathbf{A}_{ij}) 

\end{align}
$$
我們得知此時
$$
\det(\mathbf{X}) + \det(\mathbf{Y}) = \det(\mathbf{Z})
$$


但我們要注意，只有在這個非常特殊的情況下 (所有元素相同，單獨一列不同) 才會發生

一般的相加是不會讓 determinant 也相加的 !
$$
\mathbf{Z} = \mathbf{X} +\mathbf{Y} \not \Rightarrow
\det(\mathbf{Z}) = \det(\mathbf{X}) + \det(\mathbf{Y})
$$


### Duplicate row determinant

* https://youtu.be/gYv8sttBIqs

我們先了解，當 matrix 交換任意兩列時，新產生的 matrix 的 determinant 將加上負號
$$
\begin{align}
\mathbf{A} &= \begin{bmatrix} a&b\\c&d\end{bmatrix}, \det(\mathbf{A}) = x \\ 
\mathbf{A'} &= \begin{bmatrix} c&d\\a&b\end{bmatrix}, \det(\mathbf{A'}) = -x \\
\end{align}
$$


現在我們來看當 matrix 擁有相同兩列時會發生什麼

我們先用 **Row vector** 的方式來呈現整個 matrix
$$
\mathbf{A} = \begin{bmatrix} \vec{r_1}\\  \vec{r_2}\\\vdots \\ \vec{r_i} \\ \vec{r_j}\\\vdots\\\vec{r_n}\end{bmatrix},
\text{where } \vec{r_i} = \begin{bmatrix} a_{i1} & a_{i2}&\cdots&a_{in} \end{bmatrix}
$$
接著我們將 matrix A 的第 i 列和第 j 列互換，得到了 matrix S 
$$
\mathbf{S} = \begin{bmatrix} \vec{r_1}\\  \vec{r_2}\\\vdots \\ \vec{r_j} \\\vec{r_i}\\\vdots\\\vec{r_n}\end{bmatrix}
$$
此時，S 的 determinant 應該為 A 的 determinant 加上負號
$$
\det(\mathbf{S}) = -\det(\mathbf{A})
$$
但我們想知道，若 i 和 j 列的元素是完全一樣的話會發生什麼

兩列一樣，那代表交換後， S 還是等於 A 矩陣，determinant 應該要一模一樣才對

但我們又不能違背交換兩列要加上負號的規則

所以 S determinant 等於 A determinant 又等於負的 A determinant
$$
\begin{align}
&\text{if row }i = \text{row }j \\ 
& \mathbf{S} = \mathbf{A} \Rightarrow 
\det(\mathbf{S}) = \det(\mathbf{A}) = -\det(\mathbf{A})
\end{align}
$$
什麼時候才會滿足負正相等，只有 0 的時候
$$
\mathbf{A} \text{ has Duplicate Rows} \Rightarrow \det(\mathbf{A}) = 0
$$


我們可以統整一下
$$
\text{matrix invertible} \iff \text{rref is } \mathbf{I_n} \\
\begin{align}
\text{duplicate rows }&\Rightarrow \text{never get rref to } \mathbf{I_n} \\
&\Rightarrow \text{not invertible} \\
&\Rightarrow \det = 0
\end{align}
$$


### Determinant after row operations

- https://youtu.be/kpG7xySkivg

接著來看一下，若把某一個 row 加上另一個 row 乘以任意 scalar 的結果

也就是執行完一次 row operation 後，determinant 會有所改變嗎 ?

> 像在簡化至 rref 時，將任一列乘以 c 加到另一列來做消除的動作，我們稱之為 row operation



我們假設 A 把第 j 列減掉 c 乘上第 i 列得到 B
$$
\mathbf{A} = \begin{bmatrix} \vec{r_1}\\  \vec{r_2}\\\vdots \\ \vec{r_i} \\\vec{r_j}\\\vdots\\\vec{r_n}\end{bmatrix},
\mathbf{B} = \begin{bmatrix} \vec{r_1}\\  \vec{r_2}\\\vdots \\ \vec{r_i} \\\vec{r_j} - c\vec{r_i}\\\vdots\\\vec{r_n}\end{bmatrix}
$$
這時候 B 的 determinant 等於
$$
\det(\mathbf{B}) =
\det\left(\begin{bmatrix} \vec{r_1}\\  \vec{r_2}\\\vdots \\ \vec{r_i} \\\vec{r_j}\\\vdots\\\vec{r_n}\end{bmatrix}\right) + 
\det\left(\begin{bmatrix} \vec{r_1}\\  \vec{r_2}\\\vdots \\ \vec{r_i} \\ - c\vec{r_i}\\\vdots\\\vec{r_n}\end{bmatrix}\right)
$$

> 這是根據我們學過的 Determinant when row is added

然後我們又可以將第二個的 -c 拆出來
$$
\det(\mathbf{B}) =
\det\left(\begin{bmatrix} \vec{r_1}\\  \vec{r_2}\\\vdots \\ \vec{r_i} \\\vec{r_j}\\\vdots\\\vec{r_n}\end{bmatrix}\right) - c
\det\left(\begin{bmatrix} \vec{r_1}\\  \vec{r_2}\\\vdots \\ \vec{r_i} \\\vec{r_i}\\\vdots\\\vec{r_n}\end{bmatrix}\right)
$$
結果得到兩個 row 相同，兩個 row 相同意味著 det = 0
$$
\begin{align}
\det(\mathbf{B}) &=
\det\left(\begin{bmatrix} \vec{r_1}\\  \vec{r_2}\\\vdots \\ \vec{r_i} \\\vec{r_j}\\\vdots\\\vec{r_n}\end{bmatrix}\right) - 0\\
&= \det(\mathbf{A})
\end{align}
$$
所以，當 matrix 做了任意的 row operation 時，他的 determinant 是不變的 !



