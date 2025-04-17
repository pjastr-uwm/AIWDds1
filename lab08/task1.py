import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.arange(-3,1,0.1)
y1 = np.exp(4*x)
y2 = 2*np.cos(3*x)
y3 = x**2+4
plt.plot(x,y1, "red", linestyle="dotted", label=r"$y=e^{4x}$")
plt.plot(x,y2, "blue", linestyle="solid", label=r"$y=2\cos (3x)$")
plt.plot(x,y3, "green", linestyle="dashed", label=r"$y=x^2+4$")
plt.legend()
plt.title("Wykres trzech funkcji")
plt.grid(True)
plt.show()