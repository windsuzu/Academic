# Computing Parameters Analytically

## Normal Equation

有另一個方法可以不用經過 iteration 找到 minimize cost function 的 result \(parameters\)

這個方法叫做 **Normal equation**

只要將 training sets 的 features 和 results 轉換為 matrix

就可以套用 normal equation 的公式來直接得到 optimal solution

$$
\theta = (X^TX)^{-1}X^Ty \mid \theta \in \mathbb{R}^{n+1}
$$

* 用 house pricing 作為範例 :
  * Features 將會加上 x0 組成 matrix X
  * 而已知的 results 將會組成 vector y

![](../../.gitbook/assets/normal_equation_example.png)

* 在 Octave 中要實作 normal equation 的語法如下

  ```text
  pinv(X'*X)*X'*y
  ```

  * pinv = 求反矩陣
  * X' = 求 transpose

* Normal equation **不需要** Feature scaling
* Gradient descent 和 Normal equation 的差異如下 :

| Gradient Descent | Normal Equation |
| :--- | :--- |
| Alpha | No alpha |
| Iteration | No iteration |
| O\(kn^2\) | O\(n^3\) |
| n 可以很大 | n 很大會變慢 |

通常 normal equation 的 n \(features\) 不能很大

當 n 超過 10,000 時，最好使用 gradient descent 取代 normal equation

## Normal Equation Noninvertibility

* 在計算 normal equation 時，若 X^TX 不是 invertible 的話怎麼辦 ?
  * 事實上，Octave 中要計算反矩陣有兩種方法 : **inv** and **pinv**
  * 而 pinv 不管有沒有 invertible 都會返回一個反矩陣
* 但若 X^TX 不是 invertible 的話，可能有以下問題 :
  * 使用了 Redundent features
  * features 數量太多了，已經超過了 training sets 的數量 \(m &lt; n\)

所以可以從這兩點先來修改，應該可以優化計算

