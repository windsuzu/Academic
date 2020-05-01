
5
Graph optimization 在二維空間
座標更新，查看錯誤

6
解 optimal poses (F) 的方式，他的大約會等於底下式子

7
用 Gauss-Newton 來解剛剛的 approximation function
可轉成矩陣

8
一連串時間點的算法

9
如果沒辦法取量測值 (x, y, theta) 呢 => scan-to-scan

10
可以計算時間點之間改變的 transformation
用每個時間點的所有點集合，和下個時間點的點集合，來求出轉換關係

11
開始最佳化，並把 p 和 q 改成 p', q'
將最佳化拆成兩個階段，先求 R 再求 t

12
求 R 的方法，簡化

13
求 R 的方法 by H

15
因為可能不知道 p 和 q 的絕對對應關係，所以要用 ICP
ICP 也像一種最佳化，不斷 init 看是否最好，或是更新

因為 q, p 分別對應兩個時間的 scan 所以稱為 scan2scan

16
多考慮 landmarks，變成 bipartite
讓 pose 之間，landmark 之間沒有關係
這方法叫 bundle adjustment
得到觀測模型 h ，和實際量測的，一起最小化

17
加入 landmark 之後的 J 和 H，因為 J sparse 所以得到 H 如右下 (較快)
用高斯牛頓求解最佳化左下

18
landmakr 用 grid map 形式有兩種做法
kartoslam, Cartographer

19
robot pose (x, y, psi), landmark 為激光打到的 (sx, sy) 要轉成 world coor
最大化 grid 是 1 (被佔)的機率 = 最小化 grid 0 (沒有被佔) 機率

20
用高斯牛頓法求解

21
因為要用到 M 所以要怎麼求 M

# Feature Descriptor & Multi-view Geometry

23
loop detection 機制

24
一種 SLAM 定義方式是由抓點方式定義
ICP 時要抓點，所以有幾種方法可以抓點

25
另一種 SLAM 定義方式為 direct, indirect
indirect: 跟對應點的投影結果比較，越像越好
direct: 畫面點都已定義好，所以可以直接比較

2627
SLAM 歷史

28
ORB SLAM DEMO (sparse + indirect)

29
LSD SLAM DEMO (semi-dense + direct)

30
Kinet Fusion (depth sensor addition)

31
Visual SLAM 有兩大部分

## Computer Vision

33 
SLAM 跟圖學的 SfM 十分相似，只是 SLAM 是 realtime

343536
SfM 流程
1. 找 feature points (SIFT: NN 以外最好)
2. 預測 points 對應到真實 3D 場景會變怎樣 (geometry)
3. 優化預測
4. 找出 rotation 或 translation 是否合理

37
Feature Points Detection/Description

39
Popular Feature Extractors

40
找出 SIFT features

41
SIFT 應用1 找兩張圖 matching 地點

42
SIFT 應用2 找多張圖 overlap 並拼接

43
SIFT 應用3 photosynth

44
SIFT 優點

45
SIFT 4步驟

46-52
SIFT 1: Scale-space Extrema Detection
找出圖片變化較大的點
用 Gaussian pyramid 方式

53
SIFT 2: Key point localization
在產生的 pyramid 找極值
1. 跟鄰居比較
2. 用 taylor 找出更精確的預測
3. check 是否為平坦區域或 edge 並 reject

56
上述步驟的展示 

57
SIFT 3: Orientation assignment
為 key point 找出描述 (任意方向都是在描述同一點)

58
計算 magnitude 和 orientation theta

59
SIFT 4: Keypoint Descriptors
用現有 feature 做出一致性的 feature descriptor

60-61
做法 Lowe's keypoint descriptor

62 
總結 SIFT 做法

63
RCA-SIFT

64
SURF

66
RANSAC

67
為了更了解 8 matches 要先講到 camera calibration
Camera calibration 就是求出 intrinsics 和 extrinsics 所有參數

68
Pinhole Camera Projection Model
利用 image coor 和 world coor 的對應
來找出沒有做任何 rotate, translate 的 intrinsic, extrinsic matrix

69
x0, y0 是 principle point 和原點的 offset

70
a, s 可以校正 distortion

71
一組 x, y, z 可以和 u 或 v 分別產生兩個對應的方程式
假設 extrinsic 有 8 個要解，只需要 4 組對應點

72
傳統是利用 marker 來解

73
但可能沒有 marker

74
假設有一連串 frame (sx1, sx2, ...)
KMP = intrinsic * extrinsic * 3d coor
來求解 M

75
KMP 圖解

76
epipolar plane 會通過兩個 camera 中心 c0, c1 形成三角形平面
從 p0 投影來的 p1 這幾個點會連成一直線，為 epipolar line
可以得到兩個畫面對同一點所產生的投影關係方程

