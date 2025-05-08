import matplotlib.pyplot as plt

x = [1000, 1500, 2000, 2500, 3000]
y1 = [50, 70, 90, 120, 150]
x2 = [750, 1200, 1600, 2000, 2400]
y2 = [40, 60, 80, 100, 130]
plt.scatter(x, y1, s=45, color="blue", label="A")
plt.scatter(x2, y2, s=45, color="red", label="B", marker="^")
plt.legend()
plt.title("Sprzedaż vs budżet reklamowy")
plt.xlabel("Budżet reklamowy [PLN]")
plt.ylabel("Sprzedaż [sztuki]")
plt.savefig("zad1.jpg")
plt.show()
