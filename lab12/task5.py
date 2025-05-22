import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.DataFrame({
'Punkty (%)': [65, 78, 90, 55, 82, 74, 88, 91, 67, 59]
})

plt.hist(df1["Punkty (%)"], bins=3, edgecolor="black")
plt.show()