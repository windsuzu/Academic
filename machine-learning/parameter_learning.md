# Gradient Descent
梯度下降 (Gradient descent) 是一種可以把 cost function 最小化的算法

甚至可以拿來解決 Linear Regression 以外的機器學習問題

我們首先定義 cost function 問題為 :
![](../.gitbook/assets/machine_learning/week_one/cost_function_problem.png)

> Gradient descent 可以解決超過 2 個以上的 theta 值

而 gradient descent 是這樣解決問題的 :
![](../.gitbook/assets/machine_learning/week_one/gradient_descent_outline.png)

所以假設我們在一個 theta 0 和 theta 1 所生成的 cost function 圖表上

我們將他看成地形圖，而最高點的就是山頂
![](../.gitbook/assets/machine_learning/week_one/gradient_descent_graph.png)

假設我們起始點設在在山頂上

那我們就環繞四周，看哪個方向可以通往最低點

然後我們就往那個方向走幾步路下山

重複這個步驟，直到到達最低點

所以根據我們起始點的不同，會造成下山方向的不同，然後找到不同的最低點

---

要達成上面這個方法，需要使用到微分技巧

而 gradient descent 的 algorithm 是這樣的 :

$$
\begin{aligned}
\text{repeat } &\text{until convergence } :\\
&\theta_j := \theta_j - \alpha \frac{d}{d\theta_j}J(\theta_0, \theta_1, ..., \theta_n)
\end{aligned}
$$

我們將公式拆解開來 :
$$
\begin{aligned}
:= &: 代表的是 \text{ assignment operator 例如 } a := a+1\\
\theta_j&: \text{代表的是第 j 個 } \theta \text{ 值}  \\
\alpha&: \text{代表的是下山的步伐大小} \\
\frac{d}{d\theta_j}J(\theta_0,\theta_1,...\theta_n)&: \text{是一個微分方程，用第 j 個 }\theta \\&\,\,\,\text{ 來微分每個回合的 cost function}
\end{aligned}
$$
---

要注意的是，在 gradient descent algorithm 中

所有的 theta 值必須被同時更新

![](../.gitbook/assets/machine_learning/week_one/gradient_descent_caveats.png)

# Gradient Descent Intuiton
