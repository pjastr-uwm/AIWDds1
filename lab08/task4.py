import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ceny = pd.read_csv("ceny23.csv", sep=";", decimal=",")
pomarancze = ceny[ceny["Rodzaje towarów i usług"] =="pomarańcze - za 1kg"]
x = pomarancze["Miesiące"]
y = pomarancze["Wartosc"]
plt.plot(x,y, label="Pomarańcze")
plt.xticks(x, rotation=30)
plt.grid(True, alpha=0.7)
plt.legend()
plt.title("Wykres cen za rok 2017")
plt.ylabel("[zł]")
plt.xlabel("Miesiące")
plt.tight_layout()
plt.savefig("task4.webp")
plt.show()

