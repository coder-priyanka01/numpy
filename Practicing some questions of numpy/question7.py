import numpy as np

# Multiply two 2D arrays using matrix multiplication.
array1 = np.array([[1, 2],
                [3, 4]])
array2 = np.array([[5, 6],
                [7, 8]])

result = array1 @ array2
print(result)