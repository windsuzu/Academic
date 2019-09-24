# Octave : Basic Operation
``` matlab
a = pi;
disp(a);  // 3.1416

A = [1 2; 3 4; 5 6];  // matrix

B = 1:2:10;  // matrix [1 3 5 7 9]

C = 1:5;  // matrix [1 2 3 4 5]

D = ones(2, 3);  // 2*3 matrix with all 1s

E = zeros(2, 2);  // 2*2 matrix with all 0s

F = rand(1, 3);  // 1*3 matrix with each random numbers

hist(A);  // show histogram of A

G = eye(6);  // 6*6 identity matrix

help rand;  // get documentation of rand
```

# Octave : Moving Data Around
* size : Find the size of any matrix :
  ``` matlab
  A = [1 2; 3 4; 5 6];
  size(A);  // 3  2
  ```

* length : Find the length of any vector (or matrix's longest side) :
  ``` matlab
  length(A);  // 3
  B = [1 2 3 4];
  length(B);  // 4
  ```

* 可以使用 Linux 相關語法
  * pwd, ls, cd ...

* load : 載入文件
  ``` matlab
  load featuresX.dat
  load('priceY.dat')
  ```

* who : 可以查看目前所有變數
* whos : who + details
  ``` matlab
  Attr Name       Size                     Bytes  Class
  ==== ====       ====                     =====  =====
      A           3x2                         48  double
      B           1x4                         32  double
  ```

* save : 可以將變數另存成新檔 (存放地點可用 pwd 查)
  ``` matlab
  save record.txt A;
  save record.mat B;
  ```

* clear : 清空所有變數

## 矩陣操作
$$
A = \begin{bmatrix}1&2\\3&4\\5&6\end{bmatrix}
$$

* 冒號的用途
  ``` matlab
  A(:,2);  // 把每一列的第二個叫出來
  
  prints :
  2
  4
  6
  
  A([1, 3], :);  // 列出第一跟三列的所有東西
  
  prints:
  1  2
  5  6
  ```

* 可以修改特定行或列
  ``` matlab
  A(:, 2) = [10; 11; 12];  // 修改每一列的第二個
  
  prints:
  1  10
  3  11
  5  12
  ```

* 可以插入特定行或列
  ``` matlab
  A(:, 3) = [100; 101; 102];  // 將 vector 插入第三行
  A = [A, [1000; 1001; 1002]];  // 將 vector append 到最後一行
  ```

* matrix 強制轉成 vector
  ``` matlab
  A(:);
  
  prints:
  1
  3
  5
  10
  11
  12
  100
  101
  102
  1000
  1001
  1002
  ```

* 合併矩陣
  ``` matlab
  A = [1 2; 3 4; 5 6];
  B = [11 12; 13 14; 15 16];
  
  C = [A, B];  // or [A B]
  
  prints:
  1  2  11  12
  3  4  13  14
  5  6  15  16
  
  D = [A; B];
  
  prints:
  1  2
  3  4
  5  6
  11  12
  13  14
  15  16
  ```

# Octave : Computing on Data
假設我們有以下三個矩陣 :
$$
A = \begin{bmatrix}1&2\\3&4\\5&6\end{bmatrix}, B = \begin{bmatrix}11&12\\13&14\\15&16\end{bmatrix}, C = \begin{bmatrix}1&1\\2&2\end{bmatrix}
$$

* 矩陣相乘
  ``` matlab
  A * C
  ```

* Element-wise
  * 相乘
    * 會將矩陣每一個對應的位子相乘
  ``` matlab
  A .* B
  
  prints:
  11  24
  39  56
  75  96
  ```

  * Power
  ``` matlab
  A .^ 2
  
  prints:
  1   4
  9  16
  25  36
  ```

  * Divide
  ``` matlab
  1 ./ A
  
  prints:
  1.00000   0.50000
  0.33333   0.25000
  0.20000   0.16667
  ```

* 幾乎每個數學式都可以直接跟矩陣一起運作
  * abs
  ``` matlab
  abs([-1;2;-3])

  prints:
  1
  2
  3
  ```
  * negative
  ``` matlab
  v = [-1;2;-3]
  -v
  
  prints:
  1
  -2
  3
  ```

  * addition
  ``` matlab
  v + 1
  
  prints:
  2
  3
  4
  ```

  * floor
  ``` matlab
  a = [1, 15, 2, 0.5]
  floor(a)

  prints:
  1  15  2  0
  ```

  * ceil
  ``` matlab
  a = [1, 15, 2, 0.5]
  ceil(a)

  prints:
  1  15  2  1
  ```


* 對矩陣操作
  * sum
  ``` matlab
  a = [1 2; 3 4];
  sum(a)
  sum(a(:))

  prints:
  4  6
  10
  ```

  * sum with row and column
  ``` matlab
  A = [1 2; 1 2];

  sum(A, 1)  // 等於 sum(A) 求出每個 column 相加

  prints: 
  2  4

  sum(A, 2)  // 求出每個 row 相加

  prints:
  3
  3
  ```

  * prod
  ``` matlab
  a = [1 2; 3 4];
  prod(a)
  prod(a(:))

  prints:
  3  8
  24
  ```

  * comparison
  ``` matlab
  a = [1 2 3 4]
  a < 3

  prints:
  1  1  0  0 
  ```

  * max
  ``` matlab
  a = [1 2 3 4]
  max(a)  // prints: 4

  [val, index] = max(a)
  
  prints:
  val = 4
  index = 4
  ```

  * max with n*n matrix
  ``` matlab
  A =
  8  1  6
  3  5  7
  4  9  2

  max(A, [], 1)  // 會 print 出每 column 最大的，跟預設的 max(A) 一樣

  prints:
  8  9  7

  max(A, [], 2)  // 會 print 出每 row 最大的

  prints:
  8
  7
  9
  ```

  * find
  ``` matlab
  find(a < 3)

  prints:
  1  2
  ```

  * find with row & column
  ``` matlab
  A = magic(3)  // magic(n) 可以產生 n*n 的矩陣，row 和 column 和 diagonal 的 sum 都一樣

  prints:
  8   1   6
  3   5   7
  4   9   2

  [r, c] = find(D >= 7)

  prints:
  r =
  1
  3
  2

  c =
  1
  2
  3

  // means (1, 1), (3, 2), (2, 3)
  ```

* 矩陣運算
  * Transpose
  ``` matlab
  A'

  prints:
  1  3  5
  2  4  6
  ```
  
  * Inverse
  ``` matlab
  pinv(A)
  ```

# Octave : Plotting Data
* 以下介紹一些函數來讓 data 視覺化
* 假設我們有以下的 variables
  ``` matlab
  t = [0:0.01:1];
  y1 = sin(2*pi*4*t);
  y2 = cos(2*pi*4*t);
  A = magic(5);
  ```

* plot(x, y) : 可以生成 x-y 圖表
  ``` matlab
  plot(t, y1);
  ```
  * 要同時 show 出兩個圖表在同一張上
  ``` matlab
  plot(t, y1);
  hold on;
  plot(t, y2);
  ```
  * 可以對圖表做一些標記
  ``` matlab
  xlabel("Time");
  ylabel("Value");
  legend("sin", "cos");
  title("My plot");
  ```
  * 將圖表存成 png 檔於當前目錄
  ``` matlab
  print -dpng 'plot.png'
  ```

* figure(n) : 開新視窗來展示圖表
  ``` matlab
  figure(1);
  plot(t, y1);

  figure(2);
  plot(t, y2);
  ```

* subplot(n, m, z) : 生成一個 n*m 的大視窗，然後目前使用第 z 個 plot
  ``` matlab
  subplot(1, 2, 1);  // 生出一個 1*2 的 grid，然後先在第一個實作 plot
  plot(t, y1);

  subplot(1, 2, 2);
  plot(t, y2);

  axis([0.5, 1, -1, 1]);  // 調整該 plot 的 x, y 軸 (x = 0.5 到 1)  (y = -1 到 1)

  clf;  // clear
  ```

* imagesc(A) : 將 matrix 添加顏色展示出來
  ```
  imagesc(A);

  imagesc(A), colorbar, colormap gray;  // 多了一個 colorbar 然後把顏色用黑白呈現
  ```

> 補充一點 : 在 Octave 可以在單行輸入多個 sequential 指令
> ``` matlab
> a = 1, b = 2, c = 3  // 會顯示
> ```
> 或是
> ``` matlab
> a = 1; b = 2; c = 3;  // 不會顯示
> ```

# Octave : Control Statements (if, for, while)

* For loop
  ``` matlab
  v = zeros(5,1);

  for i = 1 : 5
  v(i) = 2^i
  end

  prints:
  2
  4
  8
  16
  32
  ```

* while
  ``` matlab
  i = 1;
  
  while i <= 5
  v(i) = 100
  i += 1
  end

  prints:
  100
  100
  100
  100
  100
  ```

* if
  ``` matlab
  if v(1) == 100
  disp("first element is 100")
  else
  disp("first element is not 100")
  end

  prints:
  first element is 100
  ```

* Octave 可以直接抓到當前目錄下的任何 file 中的 function
* 我們可以透過 **`addpath(path)`** 來讓 Octave 不管在哪個 working directory 都可以抓到該目錄的 function
  ``` matlab
  addpath("C:/src/octave");
  ```

* 文件名稱即為 function 的名稱
  * 假設我有一個 file 叫作 **`addTwoDigits.m`**，內容如下 :
  ``` matlab
  function sum = addTwoDigits(x, y)
  sum = x + y;
  ```

  * 就可以在 Octave 呼叫該函數
  ``` matlab
  addTwoDigits(1, 2)
  prints: 3
  ```

---

* 現在我們就可以用以上所學來計算 cost function
* 定義一個 file : **`costFunctionJ.m`**
  ``` matlab
  function J = costFunctionJ(X, y, theta)
    % X = design matrix of training sets
    % y = class labels
        
    m = size(X, 1);
    predictions = X*theta;
    sqrErrors = (predictions-y).^2;
      
    J = 1/(2*m)*sum(sqrErrors);
  endfunction
  ```

* 接著定義 training data
  ``` matlab
  X = [1 1; 1 2; 1 3];  // x0 都是 1, x1 分別是 1, 2, 3
  y = [1; 2; 3];  // 這是 result
  theta = [0; 1];  // 假設 theta0 不看, 只看 theta1
  ```

* 因為會完美符合 training sets 所以 cost function 應該會是 0
  ``` matlab
  costFunctionJ(X, y, theta)
  prints: 0
  ```

* 假設把 theta1 也改成 0 (代表我全部的 prediction 都是 0)
  * 那麼 cost function 應該會是
    $$
    \begin{aligned}
    &((0-1)^2 + (0-2)^2 + (0-3^2)) / 2 * 3 \text{ (m 值)} \\
    &= (1 + 4 + 9) / 6 \\
    &= 14 / 6\\
    &= 2.3333
    \end{aligned}
    $$

    ``` matlab
    theta = [0; 0];
    costFunctionJ(X, y, theta)
    prints: 2.3333
    ```

# Octave : Vectorization
* Vectorization 的計算方式將會比 Unvectorization 還要快速
  * Vectorization 在底層是由一些的專家所設計，速度快
  * 所以在實作時，盡量把問題轉換為 vectorization 來解決
  * 在 C++, Java, Python 這類開發工具也應該要這麼解決
  * 計算速度更快、code 行數減少

## 以計算 Cost function 為例
$$
h_\theta(x) = \theta_0x_0 + \theta_1x_1 + \cdots + \theta_nx_n
$$

* 若使用 unvectorization 的方法來計算 :
  ``` matlab
  predication = 0.0;
  
  for j = 1:n+1
  predication += theta(j) * x(j)
  end
  ```
* 而使用 vectorization 來計算 :
  $$
  \begin{aligned}
  h_\theta(x) &= \sum_{j=0}^n \theta_jx_j\\
  &= \theta^Tx
  \end{aligned}
  $$
  ``` matlab
  predication = theta' * x
  ```

## 以計算 Gradient Descent 為例
* 原公式如下 (n = 2) :
$$
\theta_0 := \theta_0 - \alpha \frac{1}{m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})x_0^{(i)}\\
\theta_1 := \theta_1 - \alpha \frac{1}{m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})x_1^{(i)}\\
\theta_2 := \theta_2 - \alpha \frac{1}{m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})x_2^{(i)}
$$

要把他計算成 vectorization 的話，大致上要把公式弄成這樣 :
$$
\theta := \theta - \alpha \delta \mid \theta \in \mathbb{R}^{n+1}, \alpha \in \mathbb{R}, \delta \in \mathbb{R}^{n+1}
$$

其中
$$
\begin{aligned}
\delta_0 &= \frac{1}{m}\sum_{i=1}^m (h_\theta(x^{(i)})- y^{(i)})x_0^{(i)}\\
\delta_1 &= \frac{1}{m}\sum_{i=1}^m (h_\theta(x^{(i)})- y^{(i)})x_1^{(i)} ... \\
\delta &= \begin{bmatrix} \delta_0 \\ \delta_1 \\ ... \end{bmatrix}
\end{aligned}
$$

