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

以下是 boolean indexing 的方式

``` py
df[df.A > 0]  # 找出 column A 所有大於 0 的 Data frame

df2[df2['E'].isin(['two', 'four'])]  # 找出 column E 的值包含 two 或 four 的 Data frame
```

# Settings

``` py
pd.Series([1, 2, 3], index=pd.date_range('20100101', period=3))  # 可以指派想要的 index

df.at[dates[0], 'A'] = 0  # 利用 label 指派數值

df.iat[0, 1] = 0  # 利用 position 指派數值

df.loc[:, 'D'] = np.array([5] * len(df))  # 指派整個 numpy array

df2[df2 > 0] = -df2  # 修改所有 value
```

# Missing Data

接著有一些處理 missing data (NaN) 的方法

``` py
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
# reindex 可以 change/add/delete 特定 axis 的 index

df1.loc[dates[0]:dates[1], 'E'] = 1

#                   A         B         C  D    F    E
# 013-01-01  0.000000  0.000000 -1.509059  5  NaN  1.0
# 013-01-02  1.212112 -0.173215  0.119209  5  1.0  1.0
# 013-01-03 -0.861849 -2.104569 -0.494929  5  2.0  NaN
# 013-01-04  0.721555 -0.706771 -1.039575  5  3.0  NaN

df1.dropna(how='any')  # 把包含 NaN 的 rows 全刪掉

df1.fillna(value=5)  # 把 NaN 全填成 5

pd.isna(df1)  # 把 table 變成 True/False table (NaN = True) 
```

# Apply function

``` py
df.apply(np.cumsum)

df.apply(lambda x: x.max() - x.min())
```

# Histogramming

``` py
s = pd.Series(np.random.randint(0, 7, size=10))
# 0    4
# 1    2
# 2    1
# 3    2
# 4    6
# 5    4
# 6    4
# 7    6
# 8    4
# 9    4

s.value_counts()
# 4    5
# 6    2
# 2    2
# 1    1
```

# Merge

Concat 可以將 objects 組合起來

``` py
pieces = [df[:3], df[3:7], df[7:]]

pd.concat(pieces)
```

也可以用 SQL-like 的 merge (join) 方法

``` py
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
#    key  lval
# 0  foo     1
# 1  foo     2

right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
#    key  rval
# 0  foo     4
# 1  foo     5

pd.merge(left, right, on='key')
#    key  lval  rval
# 0  foo     1     4
# 1  foo     1     5
# 2  foo     2     4
# 3  foo     2     5
```

另一個 Merge 的 example

``` py
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
#    key  lval
# 0  foo     1
# 1  bar     2

right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
#    key  rval
# 0  foo     4
# 1  bar     5

pd.merge(left, right, on='key')

#    key  lval  rval
# 0  foo     1     4
# 1  bar     2     5
```

最後還有 append

``` py
df.append(s, ignore_index=True)
```

# Grouping

"group by" 可以細分成以下三個 steps

* **Splitting** the data into groups based on some criteria
* **Applying** a function to each group independently
* **Combining** the results into a data structure

``` py
#      A      B         C         D
# 0  foo    one -1.202872 -0.055224
# 1  bar    one -1.814470  2.395985
# 2  foo    two  1.018601  1.552825
# 3  bar  three -0.595447  0.166599
# 4  foo    two  1.395433  0.047609
# 5  bar    two -0.392670 -0.136473
# 6  foo    one  0.007207 -0.561757
# 7  foo  three  1.928123 -1.623033

df.groupby('A').sum()
#             C        D
# A                     
# bar -2.802588  2.42611
# foo  3.146492 -0.63958

df.groupby(['A', 'B']).sum()
#                   C         D
# A   B                        
# bar one   -1.814470  2.395985
#     three -0.595447  0.166599
#     two   -0.392670 -0.136473
# foo one   -1.195665 -0.616981
#     three  1.928123 -1.623033
#     two    2.414034  1.600434
```

# Reshaping

The stack() method “compresses” a level in the DataFrame’s columns.

``` py
#                      A         B
# first second                    
# bar   one     0.029399 -0.542108
#       two     0.282696 -0.087302
# baz   one    -1.575170  1.771208
#       two     0.816482  1.100230

stacked = df.stack()
# first  second   
# bar    one     A    0.029399
#                B   -0.542108
#        two     A    0.282696
#                B   -0.087302
# baz    one     A   -1.575170
#                B    1.771208
#        two     A    0.816482
#                B    1.100230
```

The inverse operation of stack() is unstack(), which by default unstacks the last level:

``` py
stacked.unstack()
#                      A         B
# first second                    
# bar   one     0.029399 -0.542108
#       two     0.282696 -0.087302
# baz   one    -1.575170  1.771208
#       two     0.816482  1.100230

stacked.unstack(1)
# second        one       two
# first                      
# bar   A  0.029399  0.282696
#       B -0.542108 -0.087302
# baz   A -1.575170  0.816482
#       B  1.771208  1.100230
```

# Categoricals

# Plotting

# Getting Data In/Out
