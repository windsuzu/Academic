# Pandas

Here are some tutorials and examples :

* [10 minutes to pandas — pandas official documentation](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html)
* [Pandas in about 10 minutes! A great python module for Data Science!](https://www.youtube.com/watch?v=iGFdh6_FePU)

Before you start, It's important to import `numpy` and `pandas` in your code.

``` py
import numpy as np
import pandas as pd
```

# Object creation

Series 是 Pandas 的一種 Data structure 用來呈現 one column 的 elements

``` py
pd.Series([1, 2, np.nan, 3])

# 0    1.0
# 1    2.0
# 2    NaN
# 3    3.0
# dtype: float64
```

DataFrame 則是 Pandas 用來呈現 2D elements 的 Data strucutre

``` py
df = pd.DataFrame(np.random.randn(4, 4), index=list("1234"), columns=list("ABCD"))
#           A         B         C         D
# 1  1.867558 -0.977278  0.950088 -0.151357
# 2 -0.103219  0.410599  0.144044  1.454274
# 3  0.761038  0.121675  0.443863  0.333674
# 4  1.494079 -0.205158  0.313068 -0.854096


df = pd.DataFrame({"A": 1., "B": "foo", "C": pd.Series([1, 2, 3, 4])})
#      A    B  C
# 0  1.0  foo  1
# 1  1.0  foo  2
# 2  1.0  foo  3
# 3  1.0  foo  4
```

# Viewing Data
要讀取 table 的頭尾可以利用 head 和 tail 函式

另外也可以列出所有的 rows 和 columns

``` py
df.head(1)
#      A    B  C
# 0  1.0  foo  1

df.tail(2)
#      A    B  C
# 2  1.0  foo  3
# 3  1.0  foo  4

df.index
# RangeIndex(start=0, stop=4, step=1)

df.columns
# Index(['A', 'B', 'C'], dtype='object')
```

其他的還有查看 table 的 describe (mean, std, min, max, ...)

轉置 table，或是透過特定 axis 或特定 columns 來 sorting table

``` py
df.describe()
#          A         C
# count  4.0  4.000000
# mean   1.0  2.500000
# std    0.0  1.290994
# min    1.0  1.000000
# 25%    1.0  1.750000
# 50%    1.0  2.500000
# 75%    1.0  3.250000
# max    1.0  4.000000

df.T  # Transpose

df.sort_index(axis=1, ascending=false)  # Sort by axis 1

df.sort_values(by='B')  # Sort by column 'B'
```

# Selection

想要只看單一 column 或是一個範圍內的 data :

``` py
df['A']  # 只看 A columns

df[0:3]  # 只看 0, 1, 2 rows

df['0': '2']  # 只看 row 名稱為 0 到 row 名稱為 2 的 rows
```

使用 loc 可以做很多事情

``` py
# 只看單一 row 的內容，會以 Series 顯示
df.loc[1]
# A      1
# B    foo
# C      2


# 只看任意幾個 columns
df.loc[:, ['A', 'C']]
#      A  C
# 0  1.0  1
# 1  1.0  2
# 2  1.0  3
# 3  1.0  4


# 只看任意 rows 和 columns 的組合
df.loc[0:2, ['A', 'C']]


# 只看單 row 的某幾個 columns (Series 顯示)
df.loc[3, ['A', 'C']]


# 鎖定某一個點 (row, column) 會以值顯示
df.loc[0, 'A']
```

iloc 則是 loc 的另一種方式，是使用 int position 作為 parameters

``` py
df.iloc[3]  # 第 3 row

df.iloc[3:5, 0:2]  # 3, 4 rows 的 0, 1 columns

df.iloc[1:3, :]  # 1, 2 rows 的 all columns

df.iloc[[1, 2, 4], [0, 2]]  # 1, 2, 4 rows 的 0, 2 columns

df.iloc[1, 1]  # item at (1, 1)
```

