import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x= ['Piłka nożna', 'Koszykówka', 'Tenis', 'Siatkówka', 'Hokej']
y1 = np.array([10,25,34,24, 54])
y2 = np.array([20,25,16, 27, 20])
y3 = np.array([24, 20, 30,22, 11])
plt.bar(x,y1)
plt.bar(x,y2, bottom=y1)
plt.bar(x,y3, bottom =y1+y2)
plt.grid(axis='y', alpha=0.6)
plt.show()