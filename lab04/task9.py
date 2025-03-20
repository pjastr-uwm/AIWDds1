import numpy as np

M = np.array([[6, 2], [3, 9]])
print(np.linalg.det(M))
M_inv = np.linalg.inv(M)
print(M_inv)
print(M @ M_inv)
print(M_inv @ M)
