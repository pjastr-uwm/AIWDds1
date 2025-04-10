import pandas as pd

dane_lewostronne = pd.Series([90, 85, 82, 81, 80, 79, 75, 70, 65, 50])
dane_symetryczne = pd.Series([50, 60, 65, 70, 75, 80, 85, 90, 95, 100])
dane_prawostronne = pd.Series([50, 55, 60, 65, 70, 75, 76, 78, 85, 95])
print(dane_symetryczne.skew())
print(dane_symetryczne.kurt())
print(dane_lewostronne.skew())
print(dane_lewostronne.kurt())
print(dane_prawostronne.skew())
print(dane_prawostronne.kurt())