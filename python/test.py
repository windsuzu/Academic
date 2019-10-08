import pandas as pd
import numpy as np
np.random.seed(0)
a = np.random.randint(10, size=5)
print(a)

a = np.array([[1, 2, 3], [4, 5, 6]])

a = np.array([1, 4, 2, 6, 0])

print(np.sort(a))

print(pd.Series([1, 2, np.nan, 3]))

dates = pd.date_range('20191007', periods=10)

df = pd.DataFrame(np.random.randn(4, 4), index=list("1234"), columns=list("ABCD"))

df = pd.DataFrame({"A": 1., "B": "foo", "C": pd.Series([1, 2, 3, 4])})

print(df.loc[:, ['A', 'C']])
