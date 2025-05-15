import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = ["Fakt", "Super Express", "Gazeta wyborcza", "Rzeczpospolita"]
y = [130000, 78000, 40000, 19000]
c = ["lightcyan", "lightsalmon", "lightsteelblue", "lightpink"]
plt.bar(x, y, color=c)
plt.title("Wyniki sprzedaży dzienników ogólnopolskich za 1Q2023")
plt.xticks(rotation=30)
plt.yticks(np.arange(0, 120001, 20000))
plt.tight_layout()
plt.savefig("zad3.png")
plt.show()
