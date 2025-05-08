import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

football = pd.read_csv("footfall_shopping_centers.csv", parse_dates=["date"])
x = football["date"]
y = football["mall_A"]
y2 = football["mall_B"]
y3 = football["mall_C"]
plt.scatter(x,y, s=60, label="A")
plt.scatter(x,y2, s=60, label="B")
plt.scatter(x,y3, s=60, label="C")
plt.xticks(rotation=30)
plt.title("Dane o centrach handlowych")
plt.grid(True, alpha=0.3)
plt.legend()
plt.xlabel("Dni")
plt.ylabel("Wartość")
plt.tight_layout()
plt.savefig("zad4.eps")
plt.show()