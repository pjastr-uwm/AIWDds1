import numpy as np

values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mask = values % 2 == 0
np.putmask(values, mask, [0])
np.put(values, [0, 4, 8], [100, 200, 300])
