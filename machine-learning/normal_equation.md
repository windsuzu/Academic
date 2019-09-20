# Normal Equation
有另一個方法可以不用經過 iteration 找到 minimize cost function 的 result

這個方法叫做 **Normal equation**

只要將 training sets 的 features 和 results 轉換為 matrix

就可以套用 normal equation 的公式來直接得到 optimal solution
$$
\theta = (X^TX)^{-1}X^Ty
$$

* 用 house pricing 作為範例 :
  * Features 將會加上 x0 組成 matrix X
  * 而已知的 results 將會組成 vector y

![](../.gitbook/assets/machine_learning/week_two/normal_equation_example.png)

* Normal equation **不需要** Feature scaling
* Gradient descent 和 Normal equation 的差異如下 :

| Gradient Descent | Normal Equation |
|------------------|-----------------|
| Alpha            | No alpha        |
| Iteration        | No iteration    |
| O(kn^2)          | O(n^3)          |
| n 可以很大       | n 很大會變慢    |

通常 normal equation 的 n (features) 不能很大

當 n 超過 10,000 時，最好使用 gradient descent 取代 normal equation


# Normal Equation Noninvertibility

