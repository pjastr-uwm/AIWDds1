import pandas as pd

data = {'Region': ['Północ', 'Południe', 'Wschód', 'Zachód', 'Północ', 'Południe'],
        'Produkt': ['A', 'A', 'A', 'A', 'B', 'B'],
        'Sprzedaż': [150, 200, 130, 180, 220, 170]}
df = pd.DataFrame(data)
sprzedaz = df["Sprzedaż"]
df2 = df[df["Sprzedaż"] > 180]