filter 即時 (用前一刻來修正目前) incremental 誤差累積

graph (batch) 參考更多先前記錄

===

particle filter => fast slam

之前
ekf pose, landmark = gaussian => drawback
1. 無法很好表達 robot's pose
2. 算 pose, landmarks 的 covariance 的 cost 很大

Particle
解決上面兩個問題

===

先學 Sampling
PX 無法算
採樣 f(x) normalize Z 得到 PX (但當採樣多時 Z 很難求)

===

Basic sampling
更公平

===

Importance sampling
用簡單分布來近似目標分布
px/pix 是 weight (px >>> pix 代表跟目標還差很多，就可以調整)

變大的就會比較容易被二次採樣，從而改變 pix 為近似 px

若 weight 都一樣 (大小) 那就會很像 px

===

SIS 定位

目標 p 
proposal pi (為了逼近 p)
就可以得到 weight

可以拆成 1:t-1 * t 時間點的機率

再用 bayes theorem

把此刻 t 未知的 p 近似於 pi 所以又可以消掉

因為每個時間點都做 importance sampling 所以是 sequential

===

SIS 問題: 權重退化、不見、過大

SIR: resampling => weight 都一樣，但原本較大的採樣比較多次

===

FAST SLAM

把 pose, map 拆開來 (rao black wellization)
降低原本 slam 問題

把每個 landmark 都獨立 (因 particle filter likelihood 可以任意)

改良 : resampling 不用每次都做
NEFF 所有粒子分布情況
越平均 = N (個粒子)
若不平均 => 小於一個 threshold => resampling

改良2: balance binary tree 存 map

===

Grid based Fast slam

更新粒子的 occupancy grid map
odd(s)
用 bayes 算出 odd(s|z) 等於 odd(s) 乘上觀察結果
用 log 可以簡化計算


更新粒子的 importance weight
laser beam model

===

Graph based
