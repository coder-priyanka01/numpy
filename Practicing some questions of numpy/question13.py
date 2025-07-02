import numpy as np

# Replace all odd numbers in a numpy array with -1.
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
array[array % 2 == 1] = -1
print(array)  # Output: [-1  2 -1  4 -1  6 -1  8 -1]