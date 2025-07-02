import numpy as np

# find the indices of non-zero elements in a numpy array
array = np.array([0, 1, 2, 0, 3, 4, 0])
non_zero_indices = np.nonzero(array)
print(non_zero_indices)  # Output: (array([1, 2, 4, 5]),)