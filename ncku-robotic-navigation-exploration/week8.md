# Multi-view Geometry & Transformation Optimization

2D feature tracking => SIFT, ORB

得到 feature point (SIFT) 如何去預測 3D structure 跟 pose

17
world (x, y, z) 投影到 u, v 可以寫成公式

18
extrinsic = rotation + translation

21
用六組 point pair 把 C 解出來就可以看到 A|AT
但只需三組就能解出 extrinsic (PnP)

25
s (scale) 要猜測，除非用 marker 有固定比例尺

26
c0c1 (t) 可看成 c0 到 c1 的 translation
c1p1 (Rp1) 可看成對 p1 做 rotation
可以列出多組已知 p0, p1 來求 E

27
示範用多組對應來解 E，可以寫成 Ax = 0 來求解
另外找對應點時不用全部 sift point 都找，可用 epipolar line 找

28
得到 E 要拆解回 t 跟 R (用 SVD)

29
因為矩陣拆解可能有正負影響得到多種結果
意思是 p 點到底坐落在 A, B 相機的前方還是後方 (所以有四種可能)
所以必須要都在 A, B 前方的那一個解才行

30
有了 t, R 接著要來猜 p 的 3D structure (叫做 Triangulation, 3D Structure Recovering)

M = Rt 可以回推 P

31
SLAM 總流程

32-42
總流程圖解
1. 共同看到的點來求 E
2. 拆成 Rt
3. 回推共同紅色點 structure
4. 新的 frame 進來，用 feature matching 找出 overlap 的部分
5. 用 PnP 和 Recover 找出紅色點 structure
6. 重複進行

43
不只要猜 Rt 還有 s (因為每個 frame 進來會改變 s)
有一些方法可以校正 scale

44
因為也要討論 loop detection 所以要採用 image matching

45
對 sift point pair 看 similarity
目標是找出 transformation T 可以解釋 similarity

46
要解 transformation T 的六個參數
底下式子代表轉換到相似的照片上

47
越多組 pair (三組以上) 可以越精準的猜出 transformation
但挑的點不好，就不會對

48-52
例如用 linear regression 找點，去除掉 outliers

53
做法是 RANSAC

54
解釋 RANSAC

6162
實際上 match 失敗的會定為 outliers 然後被移除
然後再計算 inliners

# Lee Group & Lee Algebra

70
error function 越小越好

71
R 在 2D 可以用 theta 表示就好
但在 3D 變得非常複雜，且無法簡單求導數

72
R 可以有很多種表達方式

73
假設我們用 Axis-angle，定義旋轉軸 w 跟旋轉角度 theta
r' 是 r 延著旋轉軸 w 進行 theta 度的向量，可拆成平行和垂直 w 的向量
因為水平不會改變，可以沿用舊的
最後可以得到 rodrigues rotation 公式: 在 axis-angle 下用舊的向量來取得新的旋轉向量

74
用 rotation matrix 來表達 R
要跟著 unit basis 來描述向量

75
原本座標跟新座標的轉換描述為 R
把所有合法的 R 集合起來就是 SO(3), R 要有 orthogonal, det = 1
3 代表三維

76
不只描述 rotation 還想描述 translation 就 +t
連續的轉換太麻煩，用更簡潔的方式 T 
T 一樣可以組成 group = SE(3)

77
Group 的基本定義
* closure: 進行 binary operation 還在同空間
* identity
* inverse
* associativity: 結合律

78
來看兩個 rotation matrix 可否符合 group
加法無法為 group，要相乘

79
Lie Group 裡的元素都是連續的
要解 manifold space 的最佳化，就要了解 lie group 和 mapping 對應的 lie algebra

80
Property of Lie Group SO(3)
* R 為 orthogonal (RRT = I)
* R 會跟著時間改變: 寫成 R(t)
* R(t)R(t)T = I

對 t 做導數，再乘上 transpose 會得到反對稱矩陣

上三角: 建構反對稱 (antisymmetric) 矩陣
下三角: 從反對稱矩陣中，推回三維向量矩陣

81
對 t 做導數，得到的反對稱矩陣叫做 phi
可以再推得 R(t) 的一階導數結果

phi(t0) 其實就是 SO3 在原點附近的正切空間

82
因為知道怎麼求 R(t) 微分，就可以求 R(t)
很多個 phi 就可以組成 Lie algebra，這些 phi 可以形成反對稱矩陣

83
Lie algebra 代表的就是 Lie group 的切線空間，也要滿足一些特性
binary operation 為 Lie bracket (外積是一種)

* closure
* bilinearity
* alternativity
* jacobi identity








# ORB SLAM

2
Tracking
Mapping
Loop closing
是非同步處理

3
graph 每個點代表 key frame (藍色區)
edge 代表 frame 關聯性
keyframe 中有很多 keypoints 分別都會對應到 map point (三維空間真實地圖點)


4
共有三種 graph
covisibility: 找出 keyframe 共同的 keypoints 關聯性
spanning tree: 簡化版的 covisibility
essential: 從 sapnning tree 再加上 frame 共同觀察點超過 100

Covisibility Graph 中的每個 node 都是 keyframe，而 edges 的權重代表 keyframe 間共同分享的 points 數量
Essential Graph 則是 covisibility graph 做完 spanning tree 之後所產生，做法是只對有最多共同點的 keyframe 進行連接，最後再連接共同點大於 100 的 keyframe 得到新的 edges


可直接用 essential 進行最佳化

56
演算法1: Tracking
用 constant velocity motion model 來預測相機的 pose
根據上個和現在的 frame 來優化 pose

找附近的 frame 一起最佳化現在的 keyframe，先找 K1 再找 K2

78
演算法1: Mapping
找出潛在的 map points，然後再對他們進行優化

910
時間拉長 error 會累積所以 loop closing 可以穩定下來
