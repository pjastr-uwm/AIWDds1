import pandas as pd

d = {'klucz1': 50, 'klucz2': 100, 'klucz3': 150}
k = ['klucz0', 'klucz2', 'klucz3', 'klucz4']
series1 = pd.Series(d, index=k)
series1.name = "Wartość"
series1.index.name = "Klucz"
