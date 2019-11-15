* 本篇完全參考 scikit-learn 的官方 documentation
  * https://scikit-learn.org/stable/tutorial/basic/tutorial.html

# Loading Dataset

* scikit-learn 提供很多內建的 dataset 作為測試

``` python
from sklearn import datasets

iris = datasets.load_iris()     # 辨識花朵
digits = datasets.load_digits() # 辨識手寫數字
```

* 載入的物件有幾個屬性
  * **data** : training data X
  * **target** : label y

``` python
print(digits.data)
# [[ 0.   0.   5. ...   0.   0.   0.]
#  [ 0.   0.   0. ...  10.   0.   0.]
#  [ 0.   0.   0. ...  16.   9.   0.]
#  ...
#  [ 0.   0.   1. ...   6.   0.   0.]
#  [ 0.   0.   2. ...  12.   0.   0.]
#  [ 0.   0.  10. ...  12.   1.   0.]]

print(digits.target)
# [0, 1, 2, ..., 8, 9, 8]
```

# Learning and Predicting

* scikit-learn 提供多種傳統 Machine learning 套件
* 可以呼叫這些套件，並修改其 hyperparameters 便可開始訓練
* 以下用內建的 SVM 套件來示範

``` python
from sklearn import svm

X, y = digits.data, digits.target

clf = svm.SVC(gamma=0.001, C=100.)  # 利用 SVM 提供的 support vector classification
clf.fit(X, y)  # clf 即為訓練好的 model (hypothesis)

print(clf)
# SVC(C=100, cache_size=200, class_weight=None, coef0=0.0,
#    decision_function_shape='ovr', degree=3, gamma=0.001, kernel='rbf',
#    max_iter=-1, probability=False, random_state=None, shrinking=True,
#    tol=0.001, verbose=False)
```

* 接著就可以拿訓練好的 model 進行預測
  * predict 需要傳遞一個 list 作為 param
  * 所以這邊使用 `X[-1:]`

``` python
ans = clf.predict(X[-1:])  # 試著預測最後一個 data

print(ans)
# [8]
```

# Save Model

* Python 內建的 pickle 以及 joblib 都可以將 model 存起來下次使用
* 以下是 pickle 範例

``` python
import pickle

s = pickle.dumps(clf)  # save

clf2 = pickle.loads(s)
clf2.predict(X[-1:])  # 8
```

* joblib 可以存更大更複雜的 model，但需要存至 disk 上

``` python
from joblib import dump, load

dump(clf, 'myModel.joblib')
clf3 = load('myModel.joblib')
clf3.predict(X[-1:])  # 8
```

# Refitting and Updating Hyperparameters

* 建立好的 model 可以隨時修改或 overwrite 他的 hyperparameters
* 以下先使用 kernel 為 linear 的 SVC
* 接著再改回 kernel 為 rbf 的 SVC

``` python
clf = svm.SVC()

clf.set_params(kernel='linear').fit(X, y)
clf.predict(X[:1])

clf.set_params(kernel='rbf', gamma='scale').fit(X, y)
clf.predict(X[:1])
```