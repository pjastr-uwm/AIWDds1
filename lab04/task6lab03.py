import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([10, 20])
print(A.T * B)
B = B.reshape(2, 1)
print(A * B)
