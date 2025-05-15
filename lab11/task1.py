import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = [24.8, 13.0, 6.7, 55.5]
c = ['salmon', 'lightblue', 'lightgreen', 'lavender']
e = [0.1, 0, 0, 0]
l = ['Odzieżowe', 'Spożywcze', 'Meblowe', 'Inne']
plt.pie(x, colors=c, labels=l, explode=e, shadow=True, startangle=15, autopct="%1.1f%%")
plt.title("Wyniki sprzedaży - II-IV 2017")
plt.axis('equal')
plt.savefig('zad1.png')
plt.show()
