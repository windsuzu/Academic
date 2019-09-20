# Local Search Algorithms and Optimization Algorithms
前幾章的 Search algorithm 在找解答時

順便把經過也找了出來 (e.g., path to goal)

但其實很多問題只要求解答而已 (e.g., 8-queens problem)

---
* 這種直接求解的算法稱作 **Local Search** Algorithm
  * 每個 operation 只將 single current node 移動到鄰居
  * low memory
  * 可以在 infinite state spaces 找到 reasonable solutions
  * 他適合利用 **objective function** 來解決 **optimization problems**

![](../.gitbook/assets/ncku_artificial_intelligence/state_space_1d.png)

* Local Search 的目標是找到 Global maximum (也就是 best solution)
* 下面介紹第一個 local search algorithm : hill climbing 

## Hill Climbing Search
* 會在 loop 中不斷找尋可以往上走的方向
  * 直到找到 **peak (no neighbor has a higher value)** 才停止
* 因為只觀察 current state 的鄰居，不會觀察全局
  * 所以只需保存 current node 的 objective function value
    * 不需要用到 search tree structure
* 又稱作 **Greedy local search** (效能還不錯)
* 但演算法會因為一些原因而卡住 :
  * Local maxima
  * Ridges
  * Plateaux or shoulder

![](../.gitbook/assets/ncku_artificial_intelligence/hill_climbing_algorithm.png)

### Example : 8-queens problem
* Successors of a state : 放下 queen 之後的所有的可能性
* Heuristic cost function (h) : 有幾對 queens 會互相攻擊
* 當 best h 有數個時，會隨機選取

![](../.gitbook/assets/ncku_artificial_intelligence/hill_climbing_8_queens.png)

* 8-queens 共有 8^8 states (17 millions)
* 若很 greedy 每次皆選最陡的路往上走
  * 有 86% 會卡住
    * 但只需花 3 步就會卡住
  * 只有 14% 會找到解
    * 但只需花 4 步找到解

* 若是繼續走，希望走到的只是一個 plateau
  * 有 94% 可以找到解
    * 但要花 21 步
  * 而失誤的話要等到 64 步才會知道

### Mutation
* **Stocastic hill climbing**
  * 
* **First-choice hill climbing**
  * 
* **Random-restart hill climbing**
  * 



## Simulated Annealing
accept badness solution at beginning

with temperature T goes down => becomes unlikely to accept badness


## Local Beam Search
k init state
select k from k^2
if best => halt
information can be pass among each others

stochastic beam search

## Genetic Algorithm


