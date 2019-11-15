# Introduction

* Probability theory
  * The probability of an event is the limit of its relative frequency in a large number of trials.
* Baye's theory
  * Probability is a measure of the degree of belief about an event.
* 概率論主要應用在能重複觀察的實驗來定義出概率
  * 用多次投擲硬幣來預測出 probability
* 貝葉斯概率則是用類似常識、自己的信仰來定義概率
  * 珠寶店遭小偷，剛好有一個人破窗而出，他是小偷的機率 ?

* Baye's theory 認為所有的機率都是**條件機率 (conditional probability)**
  * 根據已知的信息得出
  * 大家都接受的某種假設所得出

# Quantifying plausibility

* Bayesian probability 需要符合以下條件
  * $$\text{Plausibility(A)} \in \mathbb{R} \text{ with boundary}$$
  * Transitivity
    * $$\text{plaus(A)} \rightarrow \text{plaus(B)} \text{ and}$$
    * $$\text{plaus(B)} \rightarrow \text{plaus(C)} \text{ then}$$
    * $$\text{plaus(A)} \rightarrow \text{plaus(C)}$$
  * Consistency
    * Event A 發生只跟所有與 A 直接相關資訊有關，不包括其他推理到 A 之前的資訊
* 根據條件，可以計算以下的條件機率
  $$
  \begin{aligned}
  Pr(A\mid B) &= \frac{Pr(B\mid A)Pr(A)}{Pr(B)} \\
  &\propto Pr(B\mid A)Pr(A)
  \end{aligned}
  $$
  * 寫成文字 : `posterior odds ∝ likelihood × prior odds`
    * **posterior probability** : B 發生情況下 A 發生機率
    * **likelihood** : A 發生情況下 B 發生機率
    * **prior probability** : A 發生機率
 
 * 以珠寶店為例
   * $$A$$ : 珠寶店被偷
   * $$B$$ : 有一個人破窗而出
   * $$Pr(A)$$ = 珠寶店被偷機率 (prior)
   * $$Pr(B\mid A)$$ = 珠寶店被偷的同時，剛好有一個人破窗而出的機率 (likelihood)
   * $$Pr(A\mid B)$$ = 用有人破窗而出來推測珠寶店被偷的機率 (posterior)

* Bayes 對整個世界的理解源於我們每個人自己認為的**事件發生概率 (personalisitic probability)**，或者叫**信念度 (degree of belief)**

# Example

* Mr. Smith 有 2 個小孩，一個小孩是男生，另一個是女生的機率為何 ?
  * 男女比例為 50-50 
* 先看所有可能性

| 第一個小孩 | 第二個小孩 |
| ---------- | ---------- |
| 男         | 男         |
| 男         | 女         |
| 女         | 男         |
| 女         | 女         |

* 因為第四個不可能，所以機率是 2/3
* 現在用 Baye's theorem 來計算 $$Pr(\text{1 girl}\mid \text{no 2 girls})$$

$$
\begin{aligned}
&= \frac{Pr(\text{no 2 girls}\mid \text{1 girl}) \times Pr(\text{1 girl})}{\sum_{j=0}^2Pr(\text{no 2 girls}\mid \text{j girls}) \times Pr(\text{j girls})}\\
&=\frac{1\times\frac{1}{2}}{1\times\frac{1}{4} + 1 \times \frac{1}{2} + 0\times \frac{1}{4}} \\
&= \frac{\frac{1}{2}}{\frac{3}{4}} = \frac{2}{3}
\end{aligned}
$$