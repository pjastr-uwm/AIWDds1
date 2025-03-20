import numpy as np

matrix = np.array([[5, 12, 8], [3, 7, 9], [15, 4, 2]])
cond = [matrix < 5, (5 <= matrix) & (matrix < 10), matrix >= 10]
values = [0, 50, 100]
print(np.select(cond, values, default=100))
