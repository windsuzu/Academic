# Numpy

Here are some tutorials and examples :

* [Quickstart tutorial - Numpy Official documentation](https://numpy.org/devdocs/user/quickstart.html)
* [Learn Numpy in 5 minutes - Best Python Library](https://www.youtube.com/watch?v=xECXZ3tyONo)

Before you start, It's important to import `numpy` in your code.

``` py
import numpy as np
```

## Numpy arrays

``` py
a = np.zeros(3)
# [0. 0. 0]  ndarray with floats

a.shape
# (3,)

a.shape = (3, 1)
# [[0.
#   0.
#   0.]]

a = np.ones(5)
# [1. 1. 1. 1. 1.]

a = np.empty(3)
# [0. 0. 0]

a = np.linspace(2, 10, 5)  # from 2 to 10, with 5 elements
# [2. 4. 6. 8. 10.]

a = np.array([1, 2, 3])
# [1, 2, 3]  ndarray

a_list = [[10, 20, 30], [40, 50]]
a = np.array(a_list)
# [[10, 20, 30], [40, 50]]  ndarray

np.random.seed(0)
a = np.random.randint(10, size=5)
# [5 0 3 3 7]

a[0:2]
# [5, 0]

a[-1]
# 7
```

## Statistical functions

``` py
np.sum(arr)  # sum
np.prod(arr)  # product
np.mean(arr)  # mean
np.std(arr)  # standard deviation
np.var(arr)  # variance
np.min(arr)  # minimum
np.max(arr)  # maximum
np.argmin(arr)  # indices of min
np.argmax(arr)  # indices of max
```

## Filters on arrays

``` py
a = np.array([1, 2, 3, 4, 5])

a < 3
# [True, True, False, False, False]

a > 3
# [False, False, False, True, True]

a[a < 3]
# [1, 2]
```

## Array Operations

``` py
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

a + b
# [7, 9, 11, 13, 15]

a + 30
# [31, 32, 33, 34, 35]

a * b
# [6, 14, 24, 36, 50]

a @ b  # dot product
# 130

a = np.array([[1, 2, 3], [4, 5, 6]])
a.T  # transpose
# [[1, 4],
#  [2, 5],
#  [3, 6]]

a = np.array([1, 4, 2, 6, 0])
np.sort(a)
# [0, 1, 2, 4, 6]
```