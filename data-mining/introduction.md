# Introduction

## Examples
1. Data-Result : Titanic@Kaggle (預測船員存活率)
2. Data-only : Google maps (預測路徑, 塞車警告, 結合各種應用)
3. IoT makes data increasing (Surveillance, healthcare, ...)


## Definition of data mining
* 跨學科的 computer science
* 從 **AI, ML, statistics, DB** 結合出的 large data sets 找出 unknown patterns
* 如何有效的從資料之間找出關聯
* Auto/Semi-automatic
* **Knowledge discovery in databases (KDD)**
  * Data record => Cluster analysis
  * Unusual record => Anomaly detection
  * Dependencies => Association rule mining
* 不只是 retrive 而是 detect/find association

## Applications
* **Market** analysis and management
  * 透過客戶行為找到與公司的關係, 銀行判斷信用
* **Risk** analysis and management
* **Fraud** detection and detection of **unusual** patterns (**outliers**)
  * Whoscall

# Knowledge Discovery from Databases (KDD)
* Nontrivial process of extraction
  * valid (可以用)
  * novel (別人有興趣, 沒有人知道)
  * potential useful
  * understandable (講得出原因)
    * linear regression hypothesis 難以解釋
  * patterns from big data (助於未來分析)

* Pattern
  * expression in languages
  * model applicable

* Example : Uber control drivers

## KDD process
![](../.gitbook/assets/data_mining/introduction/kdd_process.png)

### Databases to work on
* Relational
* Transactional (交易)
* Spatial (空間)
* Time series data (Sensor 等 sequential data)
* Multimedia (照片, 影片)
* Unstructured data (語音)
* Graph (點跟邊資料 => 方便 implement algorithms)

### Knowledge to be mined
* Association rules (買什麼就會順便買什麼)
* Classification
* Clustering
* Time series data analysis
* Semantics


# Data mining tasks
* Predict methods : 用已有變數來 predict 未知變數
  * Classification
  * Regression
  * Deviation detection
* Description methods : 把資料的 label 起來, 解釋 data
  * Clustering
  * Association rule discovery
  * Sequential pattern discovery

## Classification
用已經**分類**過的 data 來學習分類，再丟進從未看過的 data 來**測試**是哪一種分類
* Training sets (each class has features/attributes)
* Find a model for class attribute
* test previously unseen records (test set)

$$
\text{Training set} \rightarrow \text{learn classifier} \rightarrow \text{model} \leftarrow \text{test set}
$$

* Supervised classification
* 建立符合邏輯的模型 (例如樹) 來解釋 data
* Relate to machine learning

### Application
1. Direct marketing (廣告投放)
   * Buy / Don't Buy
2. Fraud detection (避免詐騙)
   * Fair / Fraud
3. Customer Attrition/Churn (使用者忠誠度預測)
   * Loyal / Disloyal
   * feature engineering
4. Sky suvery cataloging (預測銀河狀態)



## Clustering
有點像 unsupervised classification，
把相似度高的 data points (has some attributes) 分類在一起
* 目標是 data 在同一群都很像，跟別群都不像 (maybe tradeoffs)
* 並且該怎麼表示及定義每一群的名字

### Application
1. Market Segmentation (客戶分群)
   * 高, 中, 低消費群
2. Document Clustering (新聞分類)
   * 蔡英文, 柯文哲, 韓國瑜
   * [記者快抄](http://news.ptt.cc/)
3. Stock Clustering
   * 與熱門公司的關聯度, 蘋果關聯股等等


> Classification 跟 Clustering 是可以合作使用的



## Association Rule Discovery

### Definition

## Application

## Sequential Pattern Discovery

### Definition

### Application


## Regression


## Deviation / Anomaly Detection

## Time Series Analysis

## Graph mining



# Summary
