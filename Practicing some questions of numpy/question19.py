import numpy as np

# sort a numpy array by the second column
array_2d = np.array([[1, 3], [4, 1], [2, 2]])
sorted_array = array_2d[array_2d[:, 1].argsort()]
print(sorted_array)