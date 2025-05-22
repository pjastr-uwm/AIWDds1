import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(2, 5, 100)
y1 = x + 4
y2 = np.sin(2 * x)

fig, ax1 = plt.subplots()

ax1.plot(x, y1, "red", linestyle=":", label=r"$x+4$")
ax1.set_title("Wykresy - kilka")
ax1.set_ylim(-12, 12)
ax1.legend(loc=2)
ax1.set_xlabel("oś pozioma")
ax1.set_ylabel("oś pionowa po lewej stronie", color="green")
ax2 = ax1.twinx()

ax2.plot(x, y2, "violet", linestyle=":", label=r"$\sin(2x)$")
ax2.set_ylim(-2, 2)
ax2.set_ylabel("oś pionowa po prawej stronie")
ax2.legend(loc=8)

fig.tight_layout()
plt.show()
