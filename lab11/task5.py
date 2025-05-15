import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

handel = pd.read_excel("handel13.xlsx")
stacje = handel[handel["Wyszczególnienie"]=="stacje paliw"]

rok = stacje["Rok"]
wartosc = stacje["Wartosc"]
plt.bar(rok, wartosc)
plt.xticks(rok)
plt.show()