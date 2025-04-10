import pandas as pd

ceny_produktow = pd.DataFrame({
    'Produkt': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Cena': [25, 35, 40, 45, 50, 55, 60, 75, 90, 120]
})
print(ceny_produktow["Cena"].quantile(0.25))
print(ceny_produktow["Cena"].quantile(0.5))
print(ceny_produktow["Cena"].quantile(0.75))
