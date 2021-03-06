# Control Theory

* Control system
  * 能夠影響整個系統未來 state 的機制
* Control theory
  * 因應 output 來改變 input

## Open Loop Control

![](../.gitbook/assets/open_loop_control.png)

例如汽車油門要根據汽車的速度變化 (e.g. 上下坡) 而改變

![](../.gitbook/assets/open_loop_control_example.png)

## Close Loop Control

只有 input-output 很難去做修正，所以需要透過前一次 output 來修正

![](../.gitbook/assets/close_loop_control.png)

* Sensor
  * 量測上一次的 output 結果，用來和 reference 比對
* Reference
  * 用來比對和 output 的結果，計算出 error
* Controller
  * 根據 error 改變 input

例如根據汽車當前的速度，來調整要加速或減速

![](../.gitbook/assets/close_loop_control_example.png)

## Linear Time Invariant System

我們可以將 time domain 轉置成 frequency domain 重整一下 loop control

![](../.gitbook/assets/linear_time_loop_control.png)

所有的運算和參數都以頻率來表達

* G = Input 運算結果
* H = Sensor 運算結果
* D = Controller 運算結果
* r = reference
* e = error
* y = output

我們可以得到 $$e = r - yH$$ (誤差等於 reference 減去 sensor 所算的結果)

![](../.gitbook/assets/linear_time_loop_control_combine.png)

頻率中 D 到 G 的運算可以視為相乘，我們可以得到 y 等於 e 經過 D 和 G 兩個運算

$$
y = e \cdot D \cdot G
$$

接著經過一連串的運算

$$
\begin{aligned}
e &= \frac{y}{DG} \\
r - yH &= \frac{y}{DG}\\
(DG)(r-yH) &= y\\
DGr -DGyH &= y\\
DGr &= y + DGyh = y(1+DGH)\\
y &= \frac{DGr}{1+DGH}
\end{aligned}
$$

於是我們可以將 output (y) 看成是 reference (r) 經過 $$\frac{DG}{1+DGH}$$ 運算而來

![](../.gitbook/assets/linear_time_loop_control_open.png)

變成一個 open loop control

# Control Methods

## PID Control

* PID 分別為三個詞的縮寫
  * Proportional gain
  * Integral gain
  * Differential gain

### Proportional gain

Controller 設定一個值來與前一個 error 相乘，得到下一次修改的 input，這個值就叫做 proportional gain

在下圖，老皮根據終點距離來得到 error 並和 0.1 (proportional gain) 相乘

![](../.gitbook/assets/proportional_gain.png)

* 當距離 100 時，走 10 m/s (100*0.1)
* 當距離 90 時，走 9 m/s (90*0.1)
* 當距離 0 時，就停止了 (0*0.1)

![](../.gitbook/assets/proportional_gain_result.png)

#### Problem

老皮若想往天空飛，那只用 proportional gain 勢必是無法完美達成的，因為最終會停止掉下來，又往上升上去

假設老皮的螺旋槳轉速 200 rpm 可以對抗重力維持在空中

$$
\begin{aligned}
\text{Error} \times \text{Gain} &= \text{Propeller speed}\\
100 \times 2 &= 200 \text{rpm}\\
40 \times 5 &= 200 \text{rpm}\\
20 \times 10 &= 200 \text{rpm}\\
2 \times 100 &= 200 \text{rpm}\\
\end{aligned}
$$

不管設計多少的 gain (2, 5, 10, 100, ...) 都無法讓老皮到達並停留在天空上的終點

這個情況稱為 **steady state error** (y 會隨時間接近 r，但永遠存在 error)

![](../.gitbook/assets/steady_state_error.png)

### Integral gain

我們可以加入一個 integrator 來解決 steady state error 造成的問題

![](../.gitbook/assets/integral_gain.png)

新增的 integrator 會累積 error 的資訊來補充 proportional gain 不足的量

例如 error 變成 0 時，integrator 就提供 200 rpm 來讓老皮維持在高空

#### Problem

Integrator 若沒有良好設計，會超過 200 rpm 讓老皮繼續往上飛

![](../.gitbook/assets/integral_gain_problem.png)

而超過 reference 又產生了 negative error，讓 proportional gain 變負，老皮往下降

### Differential gain

若能預測 error 變化量，就能預防 integral gain 忽高忽低的問題

![](../.gitbook/assets/differential_gain.png)

我們在 controller 加上第三個 derivative 元件

因為 error 是往下變小的，變化量就是 error 的斜率 (紅線)

因為斜率是負的，所以 derivative 也產生一個負值，來和 integrator 抗衡

### Summary

![](../.gitbook/assets/pid_control.png)

PID control 可以寫成 discrete form

$$
K_pe(t) + K_i\sum_0^te_t + K_d(e(t)-e(t-1))
$$

其中的 $$K_p, K_i, K_d$$ 分別就代表了 proportional, integral, differential gain 的參數

通常就是調整這三個參數，來完成一個好的 controller

# Basic Kinematic Model

若我們想讓車子移動到路徑上到達終點，可以用前後和左右兩種 control 方式

![](../.gitbook/assets/car_pid_control.png)

若只使用 PID control 來完成，需要調整太多的參數

所以我們必須要引入一些車輛的特性，來減輕 control system 的負擔

* 在低速時
  * 可以用簡單的幾何模型來描述 car state
* 在高速時
  * 因會產生側向滑動，所以需要套入更難的動力學模型

我們用 x, y 代表車子的二維座標，$$\theta$$ 代表車子的轉向，合起來為車子的狀態

$$
\text{state: } \xi_1 = \begin{bmatrix}x\\y\\\theta\end{bmatrix}
$$

因為座標有分車子當前的座標，還有世界座標，我們有一個 rotation matrix 可以轉換兩個座標系統

$$
R(\theta) = \begin{bmatrix}
\cos\theta & \sin\theta & 0 \\
-\sin\theta & \cos\theta & 0 \\
0& 0& 1
\end{bmatrix}
$$

基本的模型 (basic kinematic model) 指的就是狀態 (state) 的變化 (derivative)

> 我們會在符號上加上一點代表微分後的變化

![](../.gitbook/assets/basic_kinematic_model.png)

State 變化可以從車子的當前狀態，乘上 rotation matrix 的反矩陣得到

* $$\dot{x_R}$$ 是 $$x_R$$ 的變化，也就是前進速度 ($$v$$)
* 而側向是沒有速度的，所以 $$\dot{y_R} = 0$$
* $$\dot{\theta}$$ 是 $$\theta$$ 的變化，也就是角速度 ($$\omega$$)

$$
\begin{aligned}
\text{Kinematic Model:} \\
\begin{bmatrix}\dot{x} \\ \dot{y} \\ \dot{\theta}\end{bmatrix} &= 
R(\theta)^{-1}\begin{bmatrix}\dot{x_R}\\\dot{y_R}\\\dot{\theta}\end{bmatrix} \\
&= \begin{bmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0& 0& 1\end{bmatrix}
\begin{bmatrix}v\\0\\\omega\end{bmatrix} \\
&= \begin{bmatrix}v\cos(\theta) \\ v\sin(\theta) \\\omega\end{bmatrix}
\end{aligned}
$$

----

## Differential Drive Vehicle

![](../.gitbook/assets/differential_drive_vehicle.png)

現在來考慮兩輪的自走車活動模型

* P: 原點
* l: 原點分別到兩輪的距離
* r: 輪子的半徑
* 座標依然是 $$x_R, y_R$$

![](../.gitbook/assets/differential_drive_vehicle2.png)

兩輪的轉速分別是 $$\phi_1$$ 和 $$\phi_2$$

* 右輪 (左輪) 速度 = 半徑 * 角速度
  * $$\text{right: } r \times \dot{\phi_1}$$
  * $$\text{left: } r \times \dot{\phi_2}$$
* 原點的速度就是右輪 (左輪) 速度的一半
  * $$\dot{x_{R1}} = \frac{r\dot{\phi_1}}{2}$$
  * $$\dot{x_{R2}} = \frac{r\dot{\phi_2}}{2}$$
* 原點的角速度 = 速度 / 到輪子的距離 
  * $$\omega_1 = \frac{r\dot{\phi_1}}{2l}$$
  * $$\omega_2 = \frac{-r\dot{\phi_2}}{2l}$$
  * 要注意左輪旋轉半徑是 $$-l$$

而原點的運動就是左右兩輪相加

$$
\begin{aligned}
\text{Kinematic Model:} \\
\begin{bmatrix}\dot{x} \\ \dot{y} \\ \dot{\theta}\end{bmatrix} &= 
R(\theta)^{-1}\begin{bmatrix}\dot{x_R}\\\dot{y_R}\\\dot{\theta}\end{bmatrix} \\
&= \begin{bmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0& 0& 1\end{bmatrix}
\begin{bmatrix} 
\frac{r\dot{\phi_1}}{2}+\frac{r\dot{\phi_2}}{2}\\
0\\
\frac{r\dot{\phi_1}}{2l}-\frac{r\dot{\phi_2}}{2l}
 \end{bmatrix} \\
\end{aligned}
$$

左右輪的馬達轉速通常不會設成參數，而是用 $$v, \omega$$ 來推導

![](../.gitbook/assets/rpm_inference.png)

* 直線前進，相同轉速，相同方向 ($$\frac{v}{r}$$) 
* 原地旋轉，相同轉速，相反方向 (正負 $$\omega$$)

## Pure Pursuit Control

Pure pursuit control 將根據速度與角速度來畫圓弧移動到前方某個點的位置

![](../.gitbook/assets/pure_pursuit_control.png)

* $$L_d$$ 是車子與目標點的距離
* $$R$$ 是畫圓產生的半徑
* $$\alpha$$ 是車子直線方向和 $$L_d$$ 的夾角
  * $$\alpha = \arctan\left(\frac{y-y_g}{x-x_g}\right) - \theta$$
  * 因為圓心角 = 兩倍的弦切角
  * 所以圓心角就是 $$2 alpha$$
* 因為是等腰三角形
  * 所以其他兩個角是 $$\frac{\pi}{2} - \alpha$$

根據正弦定理可以得到

$$
\begin{aligned}
\frac{L_d}{\sin(2\alpha)} &= \frac{R}{\sin(\frac{\pi}{2}-\alpha)} \\\\
R &= \frac{L_d\sin(\frac{\pi}{2}-\alpha)}{\sin(2\alpha)} 
&= \frac{L_d\cos(\alpha)}{2\sin(\alpha)\cos(\alpha)} 
&= \frac{L_d}{2\sin(\alpha)} \\\\
\omega &= \frac{v}{R} = \frac{2v\sin(\alpha)}{L_d} 
\end{aligned}$$

也就是說，若速度 v 透過 PID 為已知的值，那就可以推出對應的角速度 ($$\omega$$)

> Ld 通常用速度來決定，速度越快就越遠
> - e.g., $$L_d = kv + L_{fc}$$
> - 其中的 $$k, L_{fc}$$ 是可調參數

# Kinematic Bicycle Model

上面講的模型可以自由移動旋轉，但真正的車子是有一定的幾何限制 (**nonholonomic constraints**)

而生活中最常見的移動機構設計是 bicycle model (汽車可以把前後的兩個輪子各別簡化為一個)

* 前輪控制方向 (方向盤)
* 後輪控制速度 (引擎)

![](../.gitbook/assets/kinematic_bicycle_model.png)

* 後輪為車輛原點 (x, y)
* 車輛轉向 (車軸方向) $$\theta$$
* 方向盤轉角 $$\delta$$
* 車軸長度 $$L$$

![](../.gitbook/assets/kinematic_bicycle_model2.png)

將前輪放大可以得到一些細節

* 車子以 v 的速度向前
* 有兩個世界座標的軸分量 (weight) 為 $$\dot{x_f}$$ 和 $$\dot{y_f}$$

計算兩個 weight 對車子垂直方向的 weight

* $$\dot{x_f}\sin(\theta+\delta)$$
* $$\dot{y_f}\cos(\theta+\delta)$$

考慮在低速下，兩個 weight 相加會抵消，就可以得到前後輪的 equation (**Nonholonomic constraint equations**)

$$
\begin{aligned}
(1) && \dot{x_f}\sin(\theta+\delta) - \dot{y_f}\cos(\theta+\delta) = 0 && \text{(front wheel)}\\
(2) && \dot{x}\sin(\theta) - \dot{y}\cos(\theta) = 0 && \text{(rear wheel)}
\end{aligned}
$$

我們的目標是算出車輛**原點的運動**，可以從後輪座標推得前輪座標 (**Front wheel position**)

$$
\begin{aligned}
x_f = x + L\cos(\theta) \\
y_f = y + L\sin(\theta)
\end{aligned}
$$

將前輪座標帶回 (1) 就可以得到**基於車輛原點的限制方程式**

$$
\begin{aligned}
(3) && \dot{x}\sin(\theta+\delta) - \dot{y}\cos(\theta+\delta) - \dot{\theta}L\cos(\delta) = 0
\end{aligned}
$$
  
由 (2) 和 (3) 可以得到一組解，代表原點的變化 

$$
\begin{aligned}
(4) && \dot{x} = v\cos(\theta)\\
(5) && \dot{y} = v\sin(\theta)
\end{aligned}
$$

將 (4) 和 (5) 再帶回 (3) 就可以得到角速度 ($$\dot{\theta}$$)

$$
\dot{\theta} = \frac{v\tan(\delta)}{L}
$$

**於是我們就可以得到完整的 kinematic bicycle model (基於方向盤轉角 $$\delta$$)**

$$
\begin{bmatrix}
\dot{x}\\\dot{y}\\\dot{\theta}
\end{bmatrix} =
\begin{bmatrix}
\cos(\theta) \\ \sin(\theta) \\ \frac{\tan(\delta)}{L}
\end{bmatrix} v
$$

以及一些相關的 properties

$$
\begin{aligned}
&\bullet R\dot{\theta} = v \\
&\bullet \frac{v\tan(\delta)}{L} = \frac{v}{R} \\
&\bullet \tan(\delta) = \frac{L}{R} 
\end{aligned}
$$

## Pure Pursuit Control for Bicycle Model

![](../.gitbook/assets/bicycle_model_pure_pursuit_control.png)

我們可以將 bicycle model 應用於 pure pursuit control

* $$\alpha$$ 和 $$R$$ 和原本的 pure pursuit control 一樣
* 我們可以用上面的 bicycle model properties 來求得方向盤轉角 ($$\delta$$)

$$
\begin{aligned}
&\tan(\delta) = \frac{L}{R} \\
&\delta = \arctan\left(\frac{L}{R}\right) = \arctan\left(\frac{2L\sin(\alpha)}{L_d}\right)
\end{aligned}
$$

# Stanley Control

Pure pursuit control 雖然好用但不夠穩定，而 Stanley control 提供了漸進穩定的效果

![](../.gitbook/assets/stanley_control.png)

在 stanley control 會根據當前最近目標點，找到**切線、法線**做為新的座標系

* $$v$$: 前輪方向
* $$\delta$$: 方向盤方向
* $$\theta_e$$: 路徑上的法線方向
* $$\delta - \theta_e$$: 速度方向與路徑方向夾角

而法線狀態 (微分) 就是以下式子，可以當作追蹤的誤差

$$
\dot{e} = v\sin(\delta - \theta_e)
$$

加入誤差對時間變化的假設，希望誤差隨時間變化漸進到 0

$$
\begin{aligned}
\dot{e} &= -ke, \text{ where } k > 0  \\
 -ke &= v\sin(\delta - \theta_e) \\
\delta &= \arcsin\left(-\frac{ke}{v}\right) + \theta_e
\end{aligned}
$$

最終可以得到方向盤控制量 $$\delta$$ (其中 k 是調整漸進程度的參數)

因為當 $$\lvert -ke/vf \rvert > 1$$ 時為 undefined，所以可以改成近似的 local exponential stability (LES)

$$
\delta = \arctan\left(-\frac{ke}{v}\right) + \theta_e
$$

改成 arctan 可避免 undefined 但在角度很大時，可能會造成誤差變大

# LQR Control

因為太難的運動模型無法直接分析 error function，所以 LQR control 運用 cost function 概念

* 運動模型是 linear form
* Cost function 是 quadratic form

$$
\text{cost function } c = \underbrace{x^TQx}_{\text{state error}} + \underbrace{u^TRu}_{\text{minimum control}}
$$

其中 **Q, R 矩陣**分別代表 state, control 在不同維度的重要性

而最終就是要將以下的 total objective function 最小化

$$
\text{minimize } J = \int_0^T \left[x(t)^TQx(t) + u(t)^TRu(t)\right]dt + x^T(T) Sx(T)
$$

若以下狀態從現在到終點 (terminal state) $$\left[ u_t^\ast ,u_{t+1}^\ast , u_{t+2}^\ast , \cdots , u_T^\ast  \right]$$ 是最佳解

那麼 $$\left[ u_{t+1}^\ast , u_{t+2}^\ast , \cdots , u_T^\ast  \right]$$ 也會是最佳解

所以我們可以應用 **dynamic programming** 從最佳解的最終狀態，遞迴解回現在狀態

## Value function

通常我們並不知道 terminal state，或者是 terminal state 需要無限時間

這時候我們就會用 value function $$V(x)$$

$$
V(x_t) = \min_u \left( x_t^TQx_t + u_tRu_t + V(x_{t+1}) \right)
$$

* $$V(x)$$ 代表最佳情況下，未來所有代價的總和
* 當前 V = 當下最佳控制的代價 + 下一刻 V

我們可以假設 $$V(X)$$ 是 quadratic form (寫成以下，其中 P 是對稱矩陣)

$$
V(x_t) = x_t^T P_t x_t
$$

再將 linear motion model ($$Ax_t+Bu_t$$) 帶入當中得到

$$
\begin{aligned}
V\left(x_{t}\right)&
=\min _{\mathbf{u}}\left\{x_{t}^{T} Q x_{t}+u_{t} R u_{t}+x_{t+1}^{T} P_{t+1} x_{t+1}\right\}
\\
&=\min _{\mathbf{u}}\left\{x_{t}^{T} Q x_{t}+u_{t} R u_{t}+\left(A x_{t}+B u_{t}\right)^{T} P_{t+1}\left(A x_{t}+B u_{t}\right)\right\}
\\
&=\min _{\mathbf{u}}\left\{x_{t}^{T}\left(Q+A^{T} P_{t+1} A\right) x_{t}+2 x^{T} A^{T} P B u+u_{t}^{T}\left(R+B^{T} P_{t+1} B\right) u_{t}\right\}
\end{aligned}
$$

因為我們假設的 value function 是 quadratic 形式，所以可以用微分來求最佳控制 ($$u^\ast$$)

$$
\begin{aligned}
&V\left(x_{t}\right)=x_{t}^{T} P_{t} x_{t}=\min _{u}\left\{x_{t}^{T}\left(Q+A^{T} P_{t+1} A\right) x_{t}+2 x^{T} A^{T} P B u+u_{t}^{T}\left(R+B^{T} P_{t+1} B\right) u_{t}\right\}
\\
&\frac{\partial}{\partial u}\left[x_{t}^{T}\left(Q+A^{T} P_{t+1} A\right) x_{t}+2 x^{T} A^{T} P B u_{t}^{*}+u_{t}^{* T}\left(R+B^{T} P_{t+1} B\right) u_{t}^{*}\right]=0
\\
&2\left(x^{T} A^{T} P_{t+1} B\right)^{T}+2\left(R+B^{T} P_{t+1} B\right) u_{t}^{*}=0
\\
&u_{t}^{*}=-\left(R+B^{T} P_{t+1} B\right)^{-1} B^{T} P_{t+1} A x_{t}
\end{aligned}
$$

得到的 $$u^\ast$$ 就可以帶回 $$V(x) = x_t^TP_tx_t$$

$$x_{t}^{T} P_{t} x_{t}=x_{t}^{T}\left(Q+A^{T} P_{t+1} A-A^{T} P_{t+1} B\left(R+B^{T} P_{t+1} B\right)^{-1} B^{T} P_{t+1} A\right) x_{t}$$

把兩側的 $$x$$ 都拿掉就可以得到 $$P$$，這個 P 矩陣是 **discrete algebraic Riccati equations (DARE)**

$$
P_{t}=Q+A^{T} P_{t+1} A-A^{T} P_{t+1} B\left(R+B^{T} P_{t+1} B\right)^{-1} B^{T} P_{t+1} A
$$

P 代表了前後時刻的轉換方程

> * 順帶一提，在連續的情況下是 continuous algebraic Riccati equations (CARE)
> $$\dot{P}=-P A-A^{T} P+P B R^{-1} P-Q$$


因為 P 不會隨時間變化，所以式子中等式左右的 P 可以改成相同的形式

$$
P=Q+A^{T} P A-A^{T} P_{t+1} B\left(R+B^{T} P B\right)^{-1} B^{T} P A
$$

在實作時還可以更簡化，使用 iterative 的方式來求 P 直到收斂

![](../.gitbook/assets/iteratively_find_riccati_equation.png)

## LQR Control for Kinematic Model

$$
\begin{aligned}
\text{Define: } \\
&\text{State }x = \left[ e, \dot{e}, \theta, \dot{\theta}\right]\\
&\text{Matrix } Q, R
\end{aligned}
$$

* $$e$$: 橫向的最近距離 (誤差)
  * $$\dot{e}$$: 橫向距離 (誤差) 的改變量
* $$\theta$$: 方向誤差
  * $$\dot{\theta}$$: 方向誤差的改變量

兩個改變量存在是為了限制 state 誤差改變量不要太大

接著需要 linear kinematic motion model:

$$\frac{d}{d t}\left[\begin{array}{l}
e \\
\dot{e} \\
\theta \\
\dot{\theta}
\end{array}\right]=\left[\begin{array}{llll}
1 & d t & 0 & 0 \\
0 & 0 & v & 0 \\
0 & 0 & 1 & d t \\
0 & 0 & 0 & 0
\end{array}\right]\left[\begin{array}{l}
e \\
\dot{e} \\
\theta \\
\dot{\theta}
\end{array}\right]+\left[\begin{array}{c}
0 \\
0 \\
0 \\
\frac{v \tan (\delta)}{L}
\end{array}\right]$$

* 橫向距離 = 上個時間點距離 (1) + 橫向速度 (dt)
* 角度 = 上個時間點角度 (1) + 角速度 (dt)
* 最後加的方向盤控制量 ($$\delta$$) 並不是線性的
  * 所以可以用 $$\delta$$ 來近似取代 $$\tan(\delta)$$

$$\approx\left[\begin{array}{cccc}
1 & d t & 0 & 0 \\
0 & 0 & v & 0 \\
0 & 0 & 1 & d t \\
0 & 0 & 0 & 0
\end{array}\right]\left[\begin{array}{c}
e \\
\dot{e} \\
\theta \\
\dot{\theta}
\end{array}\right]+\left[\begin{array}{l}
0 \\
0 \\
0 \\
\frac{v}{L}
\end{array}\right] \delta=A x+B u$$

於是就可以得到 LQR 可解的線性模型 ($$Ax + Bu$$)

然後用 DARE 求出 P matrix

$$P=Q+A^{T} P A-A^{T} P B\left(R+B^{T} P B\right)^{-1} B^{T} P A$$

再求出最佳的控制量

$$u_{t}^{*}=-\left(R+B^{T} P_{t+1} B\right)^{-1} B^{T} P_{t+1} A x_{t}$$

# Summary

* Basic Kinematic Model

$$
\begin{aligned}
\begin{bmatrix}\dot{x} \\ \dot{y} \\ \dot{\theta}\end{bmatrix} &= 
R(\theta)^{-1}\begin{bmatrix}\dot{x_R}\\\dot{y_R}\\\dot{\theta}\end{bmatrix} \\
&= \begin{bmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0& 0& 1\end{bmatrix}
\begin{bmatrix}v\\0\\\omega\end{bmatrix} \\
&= \begin{bmatrix}v\cos(\theta) \\ v\sin(\theta) \\\omega\end{bmatrix}
\end{aligned}
$$

* Differential Drive Vehicle

$$
\begin{aligned}
\text{Kinematic Model:} \\
\begin{bmatrix}\dot{x} \\ \dot{y} \\ \dot{\theta}\end{bmatrix} &= 
R(\theta)^{-1}\begin{bmatrix}\dot{x_R}\\\dot{y_R}\\\dot{\theta}\end{bmatrix} \\
&= \begin{bmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0& 0& 1\end{bmatrix}
\begin{bmatrix} 
\frac{r\dot{\phi_1}}{2}+\frac{r\dot{\phi_2}}{2}\\
0\\
\frac{r\dot{\phi_1}}{2l}-\frac{r\dot{\phi_2}}{2l}
 \end{bmatrix} \\
\end{aligned}
$$

* Kinematic Bicycle Model

$$
\begin{aligned}
&\begin{bmatrix}
\dot{x}\\\dot{y}\\\dot{\theta}
\end{bmatrix} =
\begin{bmatrix}
\cos(\theta) \\ \sin(\theta) \\ \frac{\tan(\delta)}{L}
\end{bmatrix} v
\\\\
&\bullet R\dot{\theta} = v \\
&\bullet \frac{v\tan(\delta)}{L} = \frac{v}{R} \\
&\bullet \tan(\delta) = \frac{L}{R} 
\end{aligned}
$$

* Control Algorithms

![](../.gitbook/assets/control_algorithms.png)