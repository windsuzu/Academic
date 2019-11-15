# Setting and Estimator

* 在訓練前，必須確保 data 的格式為 (n_samples, n_features)
* 例如以下為 iris dataset 的格式
  * 共 150 筆訓練資料，每筆含 4 個 features

``` python
from sklearn import datasets
iris = datasets.load_iris()
data = iris.data
print(data.shape)  # (150, 4)
```

* 不是這個格式的話就要轉成該格式
* 例如 digits dataset 的格式不符合訓練格式
  * 共 1797 筆訓練資料，每筆是個 8x8 圖案
  * 試著把他轉成 (1797, 64)

``` python
digits = datasets.load_digits()
print(digits.images.shape)  # (1797, 8, 8)

# =========補充 : 可以用以下方式來查看圖片=========
import matplotlib.pyplot as plt 
plt.imshow(digits.images[0], cmap=plt.cm.gray_r) 
plt.show()
# ===============================================

data = digits.images.reshape(digits.images.shape[0], -1)  
print(data.shape)  # (1797, 64)
```

# Estimators

* scikit-learn 最關鍵的物件就是 Estimator
* 例如在 introduction 的 SVC
* 每種 estimator 都要有 `fit` method 來訓練 data
  * 或是給定 transformer 來從 raw data 中 extract/filter 一些 useful features  
* 每種 estimator 都可以在定義時給予 hyperparameters

``` python
estimator = Estimator(param1=1, param2=2)
print(estimator.param1)  # 1

estimator.fit(data)
```

# Supervised learning

## k-Nearest neighbors classifier

訓練資料採用 iris dataset

首先將 iris 的 training data 分成 train 和 test 兩組

``` python
np.random.seed(0)
indices = np.random.permutation(len(iris_X))

iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]
```

再來 import knn 的套件訓練 training data

``` python
knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train)
predicts = knn.predict(iris_X_test)

print(predicts)     # [1 2 1 0 0 0 2 1 2 0]
print(iris_y_test)  # [1 1 1 0 0 0 2 1 2 0]
```

* 更多的 Nearest Neighbors Documentation 可以查看官方文檔
  * https://scikit-learn.org/stable/modules/neighbors.html#neighbors

## Linear Regression

這裡用 diabetes dataset 實作 linear regression

該 dataset 共有 442 筆病人資料，每筆含 10 種 features

``` python
diabetes = datasets.load_diabetes()
diabetes_X_train = diabetes.data[:-20]
diabetes_X_test  = diabetes.data[-20:]
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test  = diabetes.target[-20:]
```

用 linear regrssion 方式學習

``` python
from sklearn import linear_model
regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)

print(regr.coef_)  # 可以觀察訓練好的參數
# [   0.30349955 -237.63931533  510.53060544  327.73698041 -814.13170937
#   ​492.81458798  102.84845219  184.60648906  743.51961675   76.09517222]

# 計算預測值和真實資料的 mean square error
np.mean((regr.predict(diabetes_X_test) - diabetes_y_test)**2)
# 2004.56760268...

# 1 = perfect prediction
# 0 = no linear relationship between X and y
regr.score(diabetes_X_test, diabetes_y_test)
# 0.5850753022690..
```

## Classification

classification 比 linear regression 更適合用於 iris dataset

``` python
from sklearn import linear_model
log = linear_model.LogisticRegression(solver='lbfgs', C=1e5, multi_class='multinomial')
log.fit(iris_X_train, iris_y_train)
# LogisticRegression(C=100000.0, class_weight=None, dual=False,
#    fit_intercept=True, intercept_scaling=1, l1_ratio=None, max_iter=100,
#    multi_class='multinomial', n_jobs=None, penalty='l2', random_state=None,
#    solver='lbfgs', tol=0.0001, verbose=0, warm_start=False)
```

### Exercise

* 用 digits dataset 的前 90 % 作為 training data
* 其餘作為 test data
* 然後用 kNN 和 classification 來試著 train & predict

``` python
digits = datasets.load_digits()
X_digits = digits.data / digits.data.max()
y_digits = digits.target

n_samples = len(X_digits)

X_train = X_digits[:int(.9 * n_samples)]
y_train = y_digits[:int(.9 * n_samples)]
X_test = X_digits[int(.9 * n_samples):]
y_test = y_digits[int(.9 * n_samples):]

knn = neighbors.KNeighborsClassifier()
logistic = linear_model.LogisticRegression(solver='lbfgs', max_iter=1000,
                                           multi_class='multinomial')

print('KNN score: %f' % knn.fit(X_train, y_train).score(X_test, y_test))
print('LogisticRegression score: %f'
      % logistic.fit(X_train, y_train).score(X_test, y_test))

# KNN score: 0.961111
# LogisticRegression score: 0.933333
```

## SVM

* SVM 提供了兩種算法
  * SVR (Support Vector Regression)
  * SVC (Support Vector Classification)
* 也能更改 kernel 類別
  * linear
    * ```svc = svm.SVC(kernel='linear')```
  * poly (polynomial)
    * ```svc = svm.SVC(kernel='poly', degree=3)```
  * rbf (radial basis function)
    * ```svc = svm.SVC(kernel='rbf')```
    * gamma: inverse of size of radial kernel

``` python
from sklearn import svm
svc = svm.SVC(kernel='linear')
svc.fit(iris_X_train, iris_y_train)

# SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#    decision_function_shape='ovr', degree=3, gamma='auto_deprecated',
#    kernel='linear', max_iter=-1, probability=False, random_state=None,
#    shrinking=True, tol=0.001, verbose=False)
```

# Scores

* 每個 estimator 都有一個 score 屬性能使用
* 越高代表 fit 的成果越好

``` python
svc.fit(X_digits[:-100], y_digits[:-100])
   .score(X_digits[-100:], y_digits[-100:])

# 0.98
```

# Cross-Validation

* Scikit-learn 提供了 k-fold cross validation 來讓評分更精準

``` python
X = ["a", "a", "a", "b", "b", "c", "c", "c", "c", "c"]
k_fold = KFold(n_splits=5)
for train_indices, test_indices in k_fold.split(X):
    print('Train: %s | test: %s' % (train_indices, test_indices))

# 意思就是將 data 拆成以下的組合

# Train: [2 3 4 5 6 7 8 9] | test: [0 1]
# Train: [0 1 4 5 6 7 8 9] | test: [2 3]
# Train: [0 1 2 3 6 7 8 9] | test: [4 5]
# Train: [0 1 2 3 4 5 8 9] | test: [6 7]
# Train: [0 1 2 3 4 5 6 7] | test: [8 9]
```

* 實際應用時如下，就可以得到 n 組不同的評分

``` python
digits = datasets.load_digits()
X_digits = digits.data
y_digits = digits.target
svc = svm.SVC(C=1, kernel='linear')

res = [svc.fit(X_digits[train], y_digits[train])
          .score(X_digits[test], y_digits[test]) for train, test in k_fold.split(X_digits)]

# [0.9638888888888889, 0.9222222222222223, 0.9637883008356546, 0.9637883008356546, 0.9303621169916435]
```

# Unsupervised Learning

## K-means Clustering

``` python
from sklearn import cluster, datasets
iris = datasets.load_iris()
X_iris = iris.data
y_iris = iris.target

k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X_iris)

print(k_means.labels_[::10])
# [0 0 0 0 0 1 1 1 1 1 2 2 2 2 2]

print(y_iris[::10])
# [0 0 0 0 0 1 1 1 1 1 2 2 2 2 2]
```