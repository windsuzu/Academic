# Introduction to Motion Planning

Motion planning 志在找出一連串動作序列，讓車子移動到終點

動作序列必須要滿足一些要求:

* 避免撞到障礙物
* 動作限制 (e.g., maximum speed)
* 移動路徑需要平滑
* 最短路徑

Motion planning 可以分成三部分:

* Path planning
* Curve interpolation
* Trajectory planning

## Path Planning

![](../.gitbook/assets/path_planning.png)

地圖可以被轉換成以上兩種格式:

1. 交叉點口做為節點
2. 產生離散網格，每一點做為節點

這些節點稱為 weight points，用來做為 shortest path algorithm 的單位

![](../.gitbook/assets/path_planning2.png)

問題有三:

1. 節點分配不均
2. 形成路徑不夠平滑
3. 節點資訊不夠 (一階、二階微分資訊)

## Curve Interpolation

![](../.gitbook/assets/curve_interpolation.png)

用一個 curve function 來連接 weight points 使得路徑變得平滑

並讓路徑點獲得微分資訊

## Trajectory Planning

在動態中可能有移動的物體成為障礙物

![](../.gitbook/assets/dynamic_environment_problem.png)

Trajectory planning 除了規劃路徑外，還要計算出每個時間點的運動資訊

根據預測 obstacle 的未來行動來規劃每個時間點的動作

![](../.gitbook/assets/trajectory_planning.png)

* y-axis 為車子的位移
* x-axis 為時間

所以會在離散時間點，進行路徑的採樣，找出當中 cost 最小的當作合適的軌跡

## Motion Planning Flow

![](../.gitbook/assets/motion_planning_flow.png)

整個 motion planning 的流程如圖所示

1. 路徑規劃: 得到空間節點
2. 內插: 得到較平滑的曲線、微分資訊
3. 軌跡規劃: 得到運動狀態、時間規劃
4. 運用前一章所講的 feedback control 來移動車子

## Path vs. Trajectory

Motion planning = Path planning + Trajectory planning

* Path planning (只考慮空間資訊)

$$
\begin{aligned}
&\text{Input: Start/End Position} \left\{\left[x_{s}, y_{s}\right],\left[x_{e}, y_{e}\right]\right\} \\
&\text{Output: Way Points} \left\{\left[x_{s}, y_{s}\right],\left[x_{1}, y_{1}\right],\left[x_{2}, y_{2}\right], \ldots,\left[x_{e}, y_{e}\right]\right\}  
\end{aligned}
$$

* Trajectory planning (考慮空間及時間資訊)

$$
\begin{aligned}
\text{Inputs: } &\text{Start/End Position} \left\{\left[x_{s}, y_{s}\right],\left[x_{e}, y_{e}\right]\right\} \\
&\text{Curve Function} f(x).  \\
&\text{Time Density} \Delta t \\\\
\text{Outputs: } &\text{Motion information with time} \\ 
&\left\{\left[x_{0}, y_{0}, v_{0}, a_{0}, t_{0}\right],\left[x_{1}, y_{1}, v_{1}, a_{1}, t_{1}\right],\left[x_{2}, y_{2}, v_{2}, a_{2}, t_{2}\right], \ldots,\left[x_{N}, y_{N}, v_{N}, a_{N}, t_{N}\right]\right\}
\end{aligned}
$$

# Path Planning

在 Path planning 要先把地圖轉換成 graph G

* G = (V, E)
* V: a set of **Vertices**
* E: a set of **Edges**

在 edges 上可能有 weights，我們就可以求解 **single-source** shortest path (給定起點的最短路徑)

* Dijkstra: 用來求 non-negative weights graph
* Best-First Search (BFS): 是一種 heuristic greedy search
* A*: BFS + Dijkstra

## Dijkstra's Algorithm

Dijkstra 可以找到最佳路徑，但不能有負的 weights

* 從一個 start point (v)
  * 找出距離最短且還沒結束的 vertex (u)
  * 更新其他沒結束的 vertex (v')
  * d(v, v’) = min(d(v, u) + <u, v’>, d(v, v’))

* Pseudo code

``` python
def Dijkstra(G, weight, v_start): 

    for each vertex v in G.vertices: 
        v.distance = INF 
        v.predecessor = None
    v_start.distance = 0

    Q = set(G.vertices)

    while Q is not empty:
        u = extract_min(Q)
        for each vertex v in G.Adj[u]:
            if v.distance > u.distance + weight[u][v]:
                v.distance = u.distance + weight[u][v]
                v.redecessor = u
```

![](../.gitbook/assets/path_planning_dijkstra.png)

* Time complexity
  * Original algorithm: $$O(V^2)$$
  * Optimized (Fibonacci-Heap): $$O(E+V\log V)$$

Dijkstra 好處是一定能找到最佳解，壞處是當節點變多效率會變很差

## Best-First Search (BFS)

BFS 會對每個 point (v) 使用 heuristic function (f(v)) 來預估 v 和終點的最小 cost 路徑

這個 heuristic function 可能是:

* Euclidean Distance
* Manhattan Distance

![](../.gitbook/assets/path_planning_bfs.png)

BFS 優點是很快，但缺點是 heuristic 的預測不一定是最佳解

## A* Algorithm

A* 則是把 Dijkstra 和 BFS 的優點結合起來，圖中會有兩種參數 (考慮歷史和未來)

![](../.gitbook/assets/path_planning_astar.png)

* g(v) 計算從起點到 v 的 cost
* h(v) 計算從 v 到終點的預測 cost

![](../.gitbook/assets/path_planning_astar2.png)

``` python
A -> B (2+10)  *
  -> C (7+8)

B -> C (4+8)   *
  -> D (3+12)
  -> E (8+9)

C -> F (3+7)   *

F -> G (1+3)   *
  -> H (5+0)

G -> H (2+0)   *
```

* 當 h(v) 接近 0 時，則 A* 就會像 Dijkstra 一樣
* 當 g(v) 接近 0 時 (或 h(v) 遠大於 g(v) 時)，則 A* 就會像 BFS 一樣

總而言之，決定好的 heuristic function 是最重要的

### Heuristic Function

在 mobile robot 中，我們可以將 2D 平面轉化為 grid space，然後就可以依此定義幾種 distance

![](../.gitbook/assets/path_planning_heuristic.png)

## Comparison

* Easy Case

![](../.gitbook/assets/path_planning_comparison_easy.png)

* Hard Case

![](../.gitbook/assets/path_planning_comparison_hard.png)

## Sampling Based Planning Methods

因為 A* 依然會搜尋路徑的所有可能 (resolution complete)，所以有人提出了 Sampling based planning methods

利用 sampling 方式來挑選最佳路徑，雖然會找 sub-optimal solution 但能減少搜尋時間 (probabilistic completeness)

### PRM

Probabilistic Road-Map (PRM) 是第一種 sampling based planning

PRM 會利用隨機採樣的方式來將 graph 建立成 2D space

1. 從 free area 隨機採樣，移除在 occupied area 的點

![](../.gitbook/assets/prm_1.png)

2. 連接 k-nearest neighbor points
3. 移除穿過 occupied area 的 edges

![](../.gitbook/assets/prm_2.png)

4. 連接 connected components

![](../.gitbook/assets/prm_3.png)

5. 就可以從產生的 graph 進行 path planning

![](../.gitbook/assets/prm_4.png)

### RRT

PRM 建立 graph 還是太慢了，所以又出現了 rapidly exploring random tree (RRT)

RRT 動態建立 tree branch 並且檢查是否有 collision

![](../.gitbook/assets/rrt_algorithm.png)

挑選隨機點的機率是 P，挑選到終點機率是 (1-P)

![](../.gitbook/assets/rrt_1.png)

從已建立的 graph 找出離隨機點最近的一點

![](../.gitbook/assets/rrt_2.png)

延伸兩者之間的距離

![](../.gitbook/assets/rrt_3.png)

反覆進行一樣的事，但不使用會 cross obstacle 的路徑

![](../.gitbook/assets/rrt_4.png)

直到要延伸的路徑 < 到終點的路徑，就可以結束了

![](../.gitbook/assets/rrt_5.png)

### RRT*

RRT* 是 RRT 的改良版本，現在被廣泛用在 mobile robot 的路徑規劃 

RRT* 基於 RRT 加入了 re-parent 和 re-wire 的步驟，增加了路徑平滑度

![](../.gitbook/assets/rrt_star_algorithm.png)

紅色部分是新加入的 re-parent 和 re-wire

#### Re-parents

從新的節點周圍找出接近的節點，然後計算是否有比原本 parent cost 還要更低的，做為新的 parent

![](../.gitbook/assets/rrt_star_reparent.png)

#### Re-wire

將新節點再做為 parent 連到周圍接近的節點，改變其他節點的 parent (若新節點比他的 parent 的 cost 還要低)

![](../.gitbook/assets/rrt_star_rewire.png)

### Comparison

![](../.gitbook/assets/rrt_rrt_star.png)

# Curve Interpolation

## Representation of Curves

$$y = f(x) \text{ or } x = g(y)$$

* Explicit
  * 用函式來表達 curve 上每個點 (x, y) 的關係
  * 有的垂直線、圓形可能無法表達

$$
\begin{aligned}
&f(x, y) = 0\\
\text{Line: }&ax+by+c=0\\
\text{Circle: }&x^2+y^2-r^2=0
\end{aligned}
$$

* Implicit
  * 用 f(x, y) 來表示，每個 curve 上的點 (x, y) 需滿足 f(x, y) = 0
  * 需要把所有點都帶進 f(x, y) 去看是否等於 0

$$
p(u) = \begin{bmatrix}
x(u) & y(u)
\end{bmatrix}^T
$$

* Parametric
  * 用 u 來表示 curve 上的每個點 (x, y)
  * 方便產生、控制 curve
  * 每個點對 u 做偏微分，可以得到該點切線方向 (trace 時每個點的速度)

## Parametric Cubic Polynomial Curves

我們可以用 polynomial (degree = n+1) 來表示 parametric curves

$$\mathbf{p}(u)=c_{0}+c_{1} u+c_{2} u^{2}+\cdots c_{n} u^{n}$$

實作上只需要到 **cubic polynomial curve** 即可

$$
\begin{aligned}
\mathbf{p}(u)=c_{0}+c_{1} u+c_{2} u^{2}+c_{3} u^{3}=\mathbf{u}^{T} \mathbf{c} &&(0 \le u \le 1)
\end{aligned}
$$

我們會用 **least square curve fitting** 來解出所有的 $$c_i$$

給定一個點得到 (x, y) 分別兩個方程式，所以會有 8 個未知數，需要至少 4 個點才能解出 (底下聯立式 * 4)

$$\begin{aligned}
&x(u)=c_{x 0}+c_{x 1} u+c_{x 2} u^{2}+c_{x 3} u^{3}\\
&y(u)=c_{y 0}+c_{y 1} u+c_{y 2} u^{2}+c_{y 3} u^{3}
\end{aligned}$$

### Least Square Curve Fitting

給定四個座標點 (control points, weight points)，四個點給定的 u 值平均分布在 curve 上

於是就可以得到以下公式 (從 cubic polynomial curve 推得)

$$\begin{aligned}
&\mathbf{p}_{0}=\mathbf{p}(0)=\mathbf{c}_{0} \\
&\mathbf{p}_{1}=\mathbf{p}\left(\frac{1}{3}\right)=\mathbf{c}_{0}+\frac{1}{3} \mathbf{c}_{1}+\left(\frac{1}{3}\right)^{2} \mathbf{c}_{2}+\left(\frac{1}{3}\right)^{3} \mathbf{c}_{3}\\
&\mathbf{p}_{2}=\mathbf{p}\left(\frac{2}{3}\right)=\mathbf{c}_{0}+\frac{2}{3} \mathbf{c}_{1}+\left(\frac{2}{3}\right)^{2} \mathbf{c}_{2}+\left(\frac{2}{3}\right)^{3} \mathbf{c}_{3}\\
&\mathbf{p}_{3}=\mathbf{p}(\mathbf{1})=\mathbf{c}_{0}+\mathbf{c}_{1}+\mathbf{c}_{2}+\mathbf{c}_{3}
\end{aligned}$$

可以寫成 $$\mathbf{P}=\mathbf{A c}$$ 的格式，其中 
$$\mathbf{P}=\left[\begin{array}{c}
\mathbf{p}_{0} \\
\mathbf{p}_{1} \\
\mathbf{p}_{2} \\
\mathbf{p}_{3}
\end{array}\right] \quad \mathbf{c}=\left[\begin{array}{c}
\mathbf{c}_{0} \\
\mathbf{c}_{1} \\
\mathbf{c}_{2} \\
\mathbf{c}_{3}
\end{array}\right]\quad
\mathbf{A}=\left[\begin{array}{cccc}
1 & 0 & 0 & 0 \\
1 & \frac{1}{3} & \left(\frac{1}{3}\right)^{2} & \left(\frac{1}{3}\right)^{3} \\
1 & \frac{2}{3} & \left(\frac{2}{3}\right)^{2} & \left(\frac{2}{3}\right)^{3} \\
1 & 1 & 1 & 1
\end{array}\right]$$

接著把 $$\mathbf{P}=\mathbf{A c}$$ 兩邊都乘上 $$\mathbf{A}^{-1}$$ 就可以得到 $$\mathbf{c}$$

$$
\begin{aligned}
&\mathbf{A}^{-1} = \mathbf{M}_{\mathbf{I}}\\
&\mathbf{c}=\mathbf{M}_{\mathbf{I}} \mathbf{P}\\
&\mathbf{p}(u)=\mathbf{u}^{T} \mathbf{c}=\mathbf{u}^{T} \mathbf{M}_{\mathbf{I}} \mathbf{P}
\end{aligned}
$$

注意，因為要滿足 4 維的矩陣乘法，所以把 x, y 對應的 coefficient 拆成兩半表示

$$\mathbf{c}_{k}=\left[\begin{array}{l}
c_{k x} \\
c_{k y}
\end{array}\right]$$

## Cubic Interpolating Curves

當有很多點的時候，則是四個點一組，依序拼出 curves

但不同區段接起來的 curves 可能不夠平滑，所以要考慮「當前區段第一個點」和「前一個區段最後一個點」的**微分連續性**

所以需要列出一些限制式:

* 每個 control points 都在 curve 上
* 每個 curve 和前個 curve 的一階、二階微分要連續
* 頭尾端點的 curvature (曲率) 為 0

最終就可以根據限制式列出 n * n 的矩陣方程來解出這個 curve (n 為 control points 的數量)

## Hermite Curves

Hermite curves 是另一種使用 control points 產生出 curve 的方式

特別的是，只需透過頭和尾兩個點的**位置**及**一階微分資訊**來求得

![](../.gitbook/assets/hermite_curves.png)

* 我們先知道 P 的一階微分長怎樣

$$\begin{aligned}
&\mathbf{p}(u)=c_{0}+c_{1} u+c_{2} u^{2}+c_{3} u^{3}\\
&\mathbf{p}^{\prime}(u)=\mathbf{c}_{1}+2 u \mathbf{c}_{2}+3 u^{2} \mathbf{c}_{3}
\end{aligned}$$

* 位置

$$\begin{aligned}
&\mathbf{p}_{0}=\mathbf{p}(0)=\mathbf{c}_{0}\\
&\mathbf{p}_{3}=\mathbf{p}(\mathbf{1})=\mathbf{c}_{0}+\mathbf{c}_{1}+\mathbf{c}_{2}+\mathbf{c}_{3}
\end{aligned}$$

* 一階微分

$$\begin{aligned}
&\mathbf{p}_{0}^{\prime}=\mathbf{p}^{\prime}(0)=\mathbf{c}_{1}\\
&\mathbf{p}_{3}^{\prime}=\mathbf{p}^{\prime}(\mathbf{1})=\mathbf{c}_{1}+2 \mathbf{c}_{2}+3 \mathbf{c}_{3}
\end{aligned}$$

我們一樣可以得到 $$\mathbf{Q}=\mathbf{A c}$$，其中的 $$\mathbf{A}^{-1}$$ 可以記為 $$\mathbf{M}_{\mathbf{H}}$$ (Hermite Geometry Matrix)

$$\mathbf{Q}=\left[\begin{array}{l}
\mathbf{p}_{0} \\
\mathbf{p}_{3} \\
\mathbf{p}_{0}^{\prime} \\
\mathbf{p}_{3}^{\prime}
\end{array}\right]=\left[\begin{array}{llll}
1 & 0 & 0 & 0 \\
1 & 1 & 1 & 1 \\
0 & 1 & 0 & 0 \\
0 & 1 & 2 & 3
\end{array}\right] \mathbf{c}, \quad \mathbf{M}_{\mathbf{H}}=\left[\begin{array}{llll}
1 & 0 & 0 & 0 \\
1 & 1 & 1 & 1 \\
0 & 1 & 0 & 0 \\
0 & 1 & 2 & 3
\end{array}\right]^{-1}=\left[\begin{array}{cccc}
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
-3 & 3 & -2 & -1 \\
2 & 2 & 1 & 1
\end{array}\right]$$

再來就可以算出 $$\mathbf{c}$$ 矩陣，進而得到 $$\mathbf{p}(u)$$

$$\begin{aligned}
&\mathbf{c}=\mathbf{M}_{\mathbf{H}} \mathbf{Q}\\
&\mathbf{p}(u)=\mathbf{u}^{T} \mathbf{c}=\mathbf{u}^{T} \mathbf{M}_{H} \mathbf{Q}
\end{aligned}$$

## Bezier Curves

當我們只知道四個 control points 而**不知道任何的一階微分資訊**時，就可以使用 bezier curves

Bezier curves 利用 p1, p2 的位置，來預估頭尾 p0, p3 的一階微分

![](../.gitbook/assets/bezier_curves.png)

> * 1/3 是兩點的間距

所以 Bezier 跟 Hermite 只差在一階微分的值，是用**近似**的方法求得

$$
\begin{aligned}
&P(0)=P_{0}=c_{0}\\
&P(1)=P_{3}=c_{0}+c_{1}+c_{2}+c_{3}\\\\
&P^{\prime}(0)=3\left(P_{1}-P_{0}\right)=c_{1}\\
&P^{\prime}(1)=3\left(P_{3}-P_{2}\right)=c_{1}+2 c_{2}+3 c_{3}\\\\
&\mathbf{c}=\mathbf{M}_{\mathrm{B}} \mathbf{P}, \quad \mathbf{M}_{\mathrm{B}}=\left[\begin{array}{cccc}1 & 0 & 0 & 0 \\ -3 & 3 & 0 & 0 \\ 3 & -6 & 3 & 0 \\ -1 & 3 & -3 & 1\end{array}\right]\\
&\mathbf{p}(u)=\mathbf{u}^{T} \mathbf{c}=\mathbf{u}^{T} \mathbf{M}_{\mathrm{B}} \mathbf{P}
\end{aligned}
$$

所以從以下五個 bezier curves 可以看到，中間點皆是為了預測頭尾微分，而非真正要連接的點

![](../.gitbook/assets/bezier_curves_example.png)

## Cubic B-spline Curves

上述所產生的 local curves 在連接時，依然會有一階微分不同導致不平滑的問題

方法是透過 B-spline curves

* 讓 curves 不一定要通過頭尾的 control points
* 但卻可以讓兩個區段在接點處，一階微分的值是相同的
* 事實上 B-spline 還能滿足接點處的二階微分相同

![](../.gitbook/assets/b_spline_curves.png)

在推導時，一樣是每四個 control points 來求得一個 curve

![](../.gitbook/assets/b_spline_curves_continuity.png)

* $$q(u)$$ 由 $$\mathbf{p}_{i-3}, \mathbf{p}_{i-2}, \mathbf{p}_{i-1}, \mathbf{p}_{i}$$ 推導而出
* $$p(u)$$ 由 $$\mathbf{p}_{i-2}, \mathbf{p}_{i-1}, \mathbf{p}_{i}, \mathbf{p}_{i+1},$$ 推導而出

我們希望這兩個區段的 $$q(1)$$ 和 $$p(0)$$ 的位置相同、一階微分也相同

所以要滿足以下式子

$$\begin{aligned}
&\mathbf{p}(0)=\mathbf{q}(1)= \color{red}{\frac{1}{6}\left(\mathbf{p}_{i-2}+4 \mathbf{p}_{i-1}+\mathbf{p}_{i}\right)}\\
&\mathbf{p}^{\prime}(0)=\mathbf{q}^{\prime}(1)= \color{red}{\frac{1}{2}\left(\mathbf{p}_{i}-\mathbf{p}_{i-2}\right)}
\end{aligned}$$

後方求值的設定 (紅色處) 不是固定的，以上只是列出常用的做法

* 位置使用鄰近的三個 points 來預估
* 一階微分則用鄰近的兩個 points 來預估
* 要注意鄰近的點需要從兩個區段都有用到的點才能拿來使用

$$
\begin{aligned}
\text{Since } &\mathbf{p}(u)=\mathbf{c}_{0}+\mathbf{c}_{1} u+\mathbf{c}_{2} u^{2}+\mathbf{c}_{3} u^{3}=u^{T} \mathbf{c}\\
&\mathbf{p}(0)=\mathbf{c}_{0}=\frac{1}{6}\left(\mathbf{p}_{i-2}+4 \mathbf{p}_{i-1}+\mathbf{p}_{i}\right) \\
&\mathbf{p}^{\prime}(0)=\mathbf{c}_{1}=\frac{1}{2}\left(\mathbf{p}_{i}-\mathbf{p}_{i-2}\right) \\
&\mathbf{p}(1)=\mathbf{c}_{0}+\mathbf{c}_{1}+\mathbf{c}_{2}+\mathbf{c}_{3}=\frac{1}{6}\left(\mathbf{p}_{i-1}+4 \mathbf{p}_{i}+\mathbf{p}_{i+1}\right) \\
&\mathbf{p}^{\prime}(1)=\mathbf{c}_{1}+2 \mathbf{c}_{2}+3 \mathbf{c}_{3}=\frac{1}{2}\left(\mathbf{p}_{i+1}-\mathbf{p}_{i-1}\right)
\end{aligned}
$$

最後我們就可以像其他兩種 curves 一樣推導出 $$\mathbf{c}$$ 和 $$\mathbf{p}(u)$$

$$\begin{aligned}
&\mathbf{P}=\mathbf{A c}\\
&\mathbf{M}_{\mathrm{S}}=\mathbf{A}^{-1}=\frac{1}{6}\left[\begin{array}{cccc}
1 & 4 & 1 & 0 \\
-3 & 0 & 3 & 0 \\
3 & -6 & 3 & 0 \\
-1 & 3 & -3 & 1
\end{array}\right] &&\Rightarrow \mathbf{c}=\mathbf{M}_{\mathrm{S}} \mathbf{P}\\
& \quad&&\Rightarrow \mathbf{p}(u)=u^{T} \mathbf{c} = u^T\mathbf{M}_{\mathrm{S}} \mathbf{P}
\end{aligned}$$

# Trajectory Planning

## State Lattices Planning

一般的自走車，不需要考慮環境變化，只需要預測障礙與終點規劃，所以可以使用 nontemporal state lattice 來規劃曲線

![](../.gitbook/assets/lattices_planning.png)

自駕車則需要考慮的周遭動態的變化，所以有人發明了結合 temporal 和 spatial 的規劃方法

![](../.gitbook/assets/state_lattices_planning.png)

這就是 State lattice planning

1. 在結合的**空間**及**時間**中，採樣軌跡
2. 計算每條軌跡的代價
   * 代價可以有很多種
     * Objective achievement cost (目標與終點距離)
     * Lateral offset cost (遵守交通規則)
     * Collision cost (避免碰撞)
     * Longitude jerk cost (舒服)
     * Lateral acceleration cost (舒服)
3. 確認軌跡是否能夠使用 (有無避障)，並選擇最低代價的那條軌跡

下圖是一個一維道路的 spatiotemporal state lattice

![](../.gitbook/assets/spatiotemporal_state_lattices.png)

* $$l$$: 代表空間
* $$t$$: 代表時間 
* $$\Delta l, \Delta t$$: 代表空間和時間的 resolution
* $$\Delta l_{\text{max}}, \Delta t_{\text{max}}$$: 代表空間和時間的 constraints

其中線段的斜率代表了縱向的速度

* 例如 $$v_0$$ 線段的速度為 2
* 而 $$v_1$$ 線段的速度為 1

右上的藍色限制區塊，展示了套用平滑的規劃曲線結果

### Example

假設紅色車子想要超越藍色車子，我們可以將所有條件投射到 spatiotemporal state lattice

![](../.gitbook/assets/spatiotemporal_state_lattices1.png)

讓我們可以直接在 lattice 上進行規劃

* 平形四邊形的寬度: 紅色車子長度
* 平形四邊形的斜率: 紅色車子速度

藍色車子可以選擇加速或減速，所以代表在 lattice 上的某個**時間點**，可以有好幾種不同的**速度選擇**

![](../.gitbook/assets/spatiotemporal_state_lattices2.png)

我們對這些採樣進行平滑計算並處理，得到了加速或減速各別最佳 (最小 cost) 的結果

![](../.gitbook/assets/spatiotemporal_state_lattices3.png)

所以藍色線段會選擇超車，而黃色線段會選擇跟車

## Frenet Coordinate

看完一維空間後，再來要考慮蜿蜒的二維空間

![](../.gitbook/assets/frenet_coordinate.png)

Frenet coordinate 將車子位置投影到二維路徑中

* $$l$$: 代表路徑方向的位移
* $$r$$: 代表與路徑的橫向誤差

我們的目標是從路徑點和參數，計算出該參數之下的座標點

* 路徑點: $$\left(X_{s}(l), Y_{s}(l)\right)$$
* 參數: $$(l, r)$$
* 目標座標: $$(x(t), y(t))$$

![](../.gitbook/assets/frenet_coordinate2.png)

從圖形中可以推出以下公式 (轉換方程: Frenet to standard coordinate)

$$
\begin{aligned}
&x(t)=X(l)-r Y^{\prime}(l)\\
&y(t)=Y(l)+r X^{\prime}(l)
\end{aligned}
$$

我們可以進一步對轉換方程，求取其一階、二階微分

$$
\begin{aligned}
&\dot{x}(t)=\dot{l} X^{\prime}(l)-\dot{r} Y(l)-r \dot{l} Y^{\prime}(l)\\
&\dot{y}(t)=\dot{l} Y^{\prime}(l)+\dot{r} X(l)+r \dot{l} X^{\prime}(l)\\\\

&\ddot{x}(t)=\ddot{l} X^{\prime}+\ddot{l}^{2} X^{\prime \prime}-\ddot{r} Y-(2 \dot{r} \dot{l}+r \ddot{l}) Y^{\prime}-\dot{r} \dot{l}^{2} Y^{\prime \prime} \\
&\ddot{y}(t)=\ddot{l} Y^{\prime}+\ddot{l}^{2} Y^{\prime \prime}-\ddot{r} \mathrm{X}-(2 \dot{r} \dot{l}+r \ddot{l}) \mathrm{X}^{\prime}-\dot{r} \dot{l}^{2} \mathrm{X}^{\prime \prime}
\end{aligned}
$$

## Trajectory Generation

現在我們來生成二維的軌跡，定義車子狀態、縱向狀態、橫向狀態

* Vehicle States
  * $$[x, y, \theta, v, a]$$

* Longitude States
  * $$l$$: longitude distance
  * $$\dot{l}$$: longitude speed
  * $$\ddot{l}$$: longitude acceleration

* Lateral States
  * $$r$$: lateral offset
  * $$\dot{r}$$: lateral speed
  * $$\ddot{r}$$: lateral acceleration

![](../.gitbook/assets/trajectory_generation1.png)

分別定義起始時 (t0) 的狀態，還有終點時 (t1) 的狀態

$$
\begin{aligned}
\text{State at time } t_0:
\left\{\left(r_{0}, \dot{r}_{0}, \ddot{r}_{0}\right),\left(l_{0}, \dot{l}_{0}, \ddot{l}_{0}\right)\right\}
\\
\text{State at time } t_1:
\left\{\left(r_{1}, \dot{r}_{1}, \ddot{r}_{1}\right),\left(l_{1}, \dot{l}_{1}, \ddot{l}_{1}\right)\right\}
\end{aligned}
$$

![](../.gitbook/assets/trajectory_generation2.png)

將開始與結束作為 curve function 的 boundary condition

* 符合 longitude trajectory ($$l(t)$$) 的 boundary condition

$$\begin{aligned}
&l\left(t_{0}\right)=l_{0}, l\left(t_{1}\right)=l_{1}\\
&\dot{l}\left(t_{0}\right)=\dot{l}_{0}, \dot{l}\left(t_{1}\right)=\dot{l}_{1}\\
&\ddot{l}\left(t_{0}\right)=\ddot{l}_{0}, \ddot{l}\left(t_{1}\right)=\ddot{l}_{1}
\end{aligned}$$

* 符合 lateral trajectory ($$r(t)$$) 的 boundary condition

$$\begin{aligned}
&r\left(t_{0}\right)=r_{0}, r\left(t_{1}\right)=r_{1}\\
&\dot{r}\left(t_{0}\right)=\dot{r}_{0}, \dot{r}\left(t_{1}\right)=\dot{r}_{1}\\
&\ddot{r}\left(t_{0}\right)=\ddot{r}_{0}, \ddot{r}\left(t_{1}\right)=\ddot{r}_{1}
\end{aligned}$$

最終我們就可以將任意時間點 $$t$$ 帶入 curve function 求得 longitude 和 lateral 的值

$$l=l(t), r=r(t)$$

接著就可以用剛剛在 Frenet 推導的公式，將這些在 Frenet 的狀態轉換到標準座標系上

![](../.gitbook/assets/frenet_to_standard.png)

就可以得到目標軌跡了 !

## Trajectory Planning Example

以下是一個在二維情況下，進行軌跡規劃的結果

![](../.gitbook/assets/trajectory_planning_example.png)
