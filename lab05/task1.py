import pandas as pd

series1 = pd.Series([15, 28, 33, 47, 52, 61])
tab1 = series1.to_numpy()
print(tab1.dtype)
print(series1[series1 > 40])

