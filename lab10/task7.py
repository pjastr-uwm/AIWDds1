import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x1 = np.array([9,10,12,13,14,16])
y1 = np.array([58,55,60,64,63,67])
plt.scatter(x1,y1)
xt = np.arange(8,17,1)
plt.xticks(xt)
yt = np.arange(50,71,5)
plt.yticks(yt)
plt.savefig("zad7.webp")
plt.show()