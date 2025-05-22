import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.DataFrame({
    'Sklep': ['Sklep A'] * 5 + ['Sklep B'] * 5 + ['Sklep C'] * 5,
    'Cena (zł/kg)': [3.5, 3.6, 3.7, 3.4, 3.8,
                     3.9, 4.0, 3.8, 4.1, 3.7,
                     4.2, 4.1, 4.3, 4.0, 4.2]
})

shopA = df1[df1["Sklep"] == "Sklep A"]
shopB = df1[df1["Sklep"] == "Sklep B"]
shopC = df1[df1["Sklep"] == "Sklep C"]
priceA = shopA["Cena (zł/kg)"]
priceB = shopB["Cena (zł/kg)"]
priceC = shopC["Cena (zł/kg)"]

plt.boxplot([priceA, priceB, priceC])
plt.title("Wykres pudełkowy cen w różnych sklepach")
plt.xticks([1, 2, 3], ["Sklep A", "Sklep B", "Sklep C"])

plt.show()
