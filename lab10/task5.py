import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

center = pd.read_csv("footfall_shopping_centers.csv", parse_dates=["date"])
center2 = center.melt(id_vars="date", value_vars=["mall_A", "mall_B", "mall_C"],
                      var_name="Center name", value_name="Value")
mall_A = center2[center2["Center name"]=="mall_A"]
mall_B = center2[center2["Center name"]=="mall_B"]
mall_C = center2[center2["Center name"]=="mall_C"]
x = mall_A["date"]
y = mall_A["Value"]
y2 = mall_B["Value"]
y3 = mall_C["Value"]
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
plt.savefig("zad5.png")
plt.show()