import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.1)
y = x ** 2 + 5 * x - (1 - x ** 2) / (1 + x ** 2)
plt.plot(x, y)
plt.show()
