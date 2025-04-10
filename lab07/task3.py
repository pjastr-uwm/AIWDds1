import pandas as pd

pomiary = pd.DataFrame({
    'Próbka': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],
    'Wynik1': [45, 47, 49, 51, 46, 48, 50, 52],
    'Wynik2': [120, 150, 110, 190, 200, 115, 140, 180]
})
wynik1 = pomiary["Wynik1"]
print(wynik1.max() - wynik1.min())
print(wynik1.mean())
print(wynik1.var())
print(wynik1.std())