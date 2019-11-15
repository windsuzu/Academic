# Probability 

該筆記參考 [醫學統計學](https://bookdown.org/ccwang/medical_statistics6)

## Axiom

* $$0 \le P(A) \le 1$$
* $$P(\Omega) = 1 \mid \Omega = \text{total sample space}$$
* $$\text{When }A_1, A_2, \cdots, A_n \text{ are independent}$$
  * $$P(A_1 \cup A_2 \cup \cdots \cup A_n) = P(A_1) +  P(A_2) + \cdots +  P(A_n)$$

## Conditional Probability

* $$P(A \mid S) = \frac{P(A\cap S)}{P(S)}$$
* $$P(A \cap S) = P(A\mid S)P(S)$$

## Independent

* $$P(A \cap B) = P(A)P(B)$$
  * $$P(A\mid B) = P(A)$$
    * B 無法提供任何訊息給 A


# Bayes Theorem

* 用於條件互調
* 已知
  $$
  \begin{aligned}
  P(A \cap S) &= P(A\mid S)P(S) \\
  &= P(S\mid A)P(A)
  \end{aligned}
  $$
* 所以
  $$
  \begin{aligned}
  P(S\mid A)P(A) &= P(A\mid S)P(S) \\
  \Rightarrow P(S\mid A) &= \frac{P(A\mid S)P(S)}{P(A)}
  \end{aligned}
  $$

* 另外已知
  $$
  \begin{aligned}
  P(A) &= P(A \cap S) + P(A \cap \bar{S})\\
  &= P(A\mid S)P(S) + P(A\mid\bar{S})P(\bar{S})
  \end{aligned}
  $$
* 最終的 Bayes theorem formula
  $$
  P(S\mid A) = \frac{P(A\mid S)P(S)}{P(A\mid S)P(S) + P(A\mid\bar{S})P(\bar{S})}
  $$

### Example

* 20% 吸菸 $$P(S) = 0.2$$
* 吸菸有 9% 有氣喘 $$P(A\mid S) = 0.09$$
* 不吸菸有 7% 有氣喘 $$P(A\mid\bar{S}) = 0.07$$
* 有一個氣喘人出現，他有抽菸的機率是多少
  * Find $$P(S\mid A)$$

$$
\begin{aligned}
P(S\mid A) &= \frac{P(A\mid S)P(S)}{P(A\mid S)P(S) + P(A\mid\bar{S})P(\bar{S})} \\
&= \frac{0.09 \cdot 0.2}{0.09 \cdot 0.2 + 0.07 \cdot 0.8}\\
&= 0.24
\end{aligned}
$$

# Expectation and Variance

* Expectation
* 求取一組 **Discrete Random Variables $$X$$** 的期望 (均值)
  * 將所有 X 的值和對應機率相乘後求和，也會用 $$\mu$$ 表示
  * $$E(X) = \sum_x x\cdot P(X=x)$$

* Variance
* 衡量一組數據變化幅度
  * $$Var(X) = E((X-\mu)^2) \mid \mu = E(x)$$
  * 也可以寫成
  * $$Var(X) = E(X^2) - E(X)^2$$
* Variance 有一些性質
  1. $$Var(X+b) = Var(X)$$
  2. $$Var(aX) = a^2Var(X)$$
  3. $$Var(aX+b) = a^2Var(X)$$

# Bernoulli distribution

* 有一個 X = 2 ramdom variables $$\{0, 1\}$$
* 兩個變數是 independent
* 假設取 1 的機率有 P
* X 期望值為
  $$
  \begin{aligned}
  E(X) &= \sum_x x\cdot P(X=x) \\
  &= 1 \cdot P + 0 \cdot (1-P) \\
  &= P
  \end{aligned}
  $$
* X 的 Var 為 $$(x = x^2)$$
  $$
  \begin{aligned}
  Var(X) &= E[X^2] - E[X]^2 \\
  &= E[X] - E[X]^2 \\
  &= P - P^2 \\
  &= P(1-P)
  \end{aligned}
  $$

## 證明 independent X, Y 時兩大公式
* $$E(XY) = E(X)E(Y)$$

$$
\begin{aligned}
E(XY) &= \sum_x \sum_y xyP(X=x, Y=y) \\
&= \sum_x \sum_y xyP(X=x)P(Y=y) \\
&= \sum_x xP(X=x) \sum_y yP(Y=y) \\
&= E(X)E(Y)
\end{aligned}
$$

* $$Var(X+Y) = Var(X) + Var(Y)$$

$$
\begin{aligned}
Var(X+Y) &= E((X+Y)^2) - E(X+Y)^2 \\
&= E(X^2+2XY+Y^2) - (E(X) + E(Y))^2 \\
&= E(X^2) + E(Y^2) + 2E(XY) \\&\,\,\,\,\,\,- E(X)^2 - E(Y)^2 - 2E(X)E(Y) \\
&= E(X^2) -E(X)^2 + E(Y^2) - E(Y)^2 \\
&= Var(X) + Var(Y)
\end{aligned}
$$

# Binomial Distribution

* 通常是 $$n$$ 次成功率 $$P$$ 的實驗，他成功的次數
* success in $$n$$ independent **Bernoulli trials**
* 若 X 符合二項分布，記為 $$X \sim \text{Binomial}(n, P)$$
* 第 x 次實驗的機率寫為
  $$
  P(X=x) =\binom{n}{x}P^x(1-P)^{n-x} \mid \text{for } x = 1, 2, \cdots, n 
  $$

## Expectation and Variance of Binomial Distribution

* 期望值就會等於 X 滿足 $$X \sim \text{Binomial}(n, P)$$
* 用 $$X_i, i = 1, 2, \cdots n$$ 標記每個獨立通過實驗的 $$X$$

$$
\begin{aligned}
E(X) &= E(\sum_{i=1}^n X_i) \\
&= E(X_1 + X_2 + \cdots + X_n) \\
&= E(X_1) + E(X_2) + \cdots + E(X_n) \\
&= \sum_{i=1}^n E(X_i) \\
&= \sum_{i=1}^n P \\
&= nP
\end{aligned}
$$

* 計算 Variance

$$
\begin{aligned}
Var(X) &= Var(\sum_{i=1}^n X_i) \\
&= Var(X_1 + X_2 + \cdots + X_n) \\
&= Var(X_1) + Var(X_2) + \cdots + Var(X_n) \\
&= \sum_{i=1}^n Var(X_i) \\
&= \sum_{i=1}^n P(1-P) \\
&= nP(1-P)
\end{aligned}
$$

# Poisson Distribution

* 事件在時間 $$T$$ 發生 $$\lambda$$ 次
  * 期望在該時間的發生次數是 $$E(X) = \lambda T$$
* 用微分想像 $$T$$ 有 $$n$$ 個時段，$$n \rightarrow \infin$$ 的每個微小時段都發生一次事件
  * 每個微小時段可視為一個 Bernoulli (有發生或沒有發生)
  * 整個 $$T$$ 發生事件可視為 Binomial distribution

* 若 $$X$$ 代表一次事件發生經過的所有時間段
* 當 X 符合泊松分佈時
  $$
  X \sim \text{Poisson}(\mu = \lambda T)
  $$

* the probability function of a Poisson distribution
  $$
  P(X = x) \rightarrow \frac{\mu^x}{x!}e^{-\mu} 
  $$

* Expectation of poisson
  $$
  E(X) = \mu
  $$

* Variance of poisson
  $$
  Var(X) = \mu
  $$

# Normal Distribution

## Probability density function， PDF

![](../.gitbook/assets/normal_distribution_pdf.png)

* 給定範圍 [a, b] 且 a < b，那麼一個隨機連續變量 X 的機率將滿足
  $$
  P(a \le X \le b) = \int_a^b f(x) dx
  $$
  * 這稱為**概率密度方程 (probability density function, PDF)**
  * 在 a ∼ b 區間內的積分，就是這個連續變量在這個區間內取值的概率
* 整個範圍的面積等於 1
  $$
  \int_{-\infty}^\infty f(x) dx = 1
  $$
  * Expectation
    $$
    E(X) = \int_{-\infty}^\infty x\cdot f(x)dx
    $$
  * Variance
    $$
    Var(X) = \int_{-\infty}^\infty(x-\mu)^2f(x)dx
    $$

## Normal Distribution

* 當數據 X 符合 normal distribution，通常會用 exp 和 var 來描述
  $$
  X \sim N(\mu, \sigma^2)
  $$

* 他的 probability density function 可表示為
  $$
  f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{(-\frac{(x-\mu)^2}{2\sigma^2})}
  $$

* Expectation
  $$E(x) = \mu$$

* Variance
  $$Var(x) = \sigma^2$$

## Standard Normal Distribution

* Normal distribution with $$\mu = 0, \sigma^2 = 1$$ 時稱之
  * 記為 $$Z \sim N(0, 1)$$
* 他的 probability density function 可表示為
  $$
  f(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}}
  $$

* 他有 95% 的面積在 standard deviation -1.96 至 1.96 區間
* 任何 normal distribution 都可以正規化成 standard，利用以下公式
  $$
  Z = \frac{X-\mu}{\sigma}
  $$

# Central Limit Theorem

## Covariance

* 還記得兩個獨立變數的 variance 可以拆開
  $$Var(X+Y) = Var(X) + Var(Y)$$
* 若兩個變數互相會影響時 :
  $$
  \begin{aligned}
  Var(X+Y) &= E[((X+Y) - E(X+Y))^2] \\
  &= E[((X+Y)- (E(X) + E(Y)))^2] \\
  &= E[(X - E(X)) - (Y - E(Y))^2] \\
  &= E[(X-E(X))^2 + (Y - E(Y))^2 + 2(X-E(X))(Y - E(Y))] \\
  &= Var(X) + Var(Y) + 2E[(X-E(X))(Y-E(Y))]
  \end{aligned}$$

* 後面多出來的 $$E[(X-E(X))(Y-E(Y))]$$ 稱為 **Covariance (協方差)**
  $$
  Cov(X, Y) = E[(X-E(X))(Y-E(Y))]
  $$

* 所以當兩變數互相影響、不為獨立時，Variance 的算法如下
  $$
  Var(X+Y) = Var(X) + Var(Y) + 2Cov(X, Y)
  $$

* **注意 : Covariance 只能評價 X, Y 之間的 *linear assoication***

* 以下有一些 covariance 的 properties
  * $$Cov(X, X) = Var(X)$$
  * $$Cov(X, Y) = Cov(Y, X)$$
  * $$Cov(aX, bY) = ab Cov(X, Y)$$
  * $$Cov(X+Y, X-Y) = Var(X) - Var(Y)$$
  * $$X, Y \text{ independent} \rightarrow Cov(X, Y) = 0 \text{  (no vice versa)}$$

## Correlation

* Covariance 的大小波動不穩定，會被各自數值、單位影響
* 可以除以各自標準差 (standardization)，得到相關係數 Corr (-1 to 1)
  $$
  Corr(X, Y) = \frac{Cov(X, Y)}{SD(X)SD(Y)} = \frac{Cov(X, Y)}{\sqrt{Var(X)Var(Y)}}
  $$

## the Central Limit Theorem

* 當你有數量為 $$n$$ 的樣本，其 sampling distribution 為 $$\bar{X}_n$$
* 當樣本數增加 $$n \rightarrow \infty$$，會接近 normal distribution

* 可以寫成
  $$
  \bar{X}_n \sim N(\mu, \frac{\sigma^2}{n})
  $$
* 或寫成
  $$
  \sum_{i=1}^n X_i \sim N(n\mu, n\sigma^2)
  $$
* 簡而言之，只要樣本數夠大， Sampling distribution 的分布會服從於 Normal distribution

### Binomial Distribution with Central Limit Theorem

* 二項分布要解決 $$n \rightarrow \infty$$ 得到 $$X \sim \text{Binomial}(n, P)$$
* 因為 n 非常大，計算非常困難
* 所以可以運用 Central Limit Theorem
  $$
  X \sim N(nP, nP(1-P))
  $$
* n 多少算大
  * $$n > 20 \text{ AND } nP > 5 \text{ AND } n(1-P) > 5$$

