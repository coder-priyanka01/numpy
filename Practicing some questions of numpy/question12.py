import numpy as np

# Get the 2nd column of a 3X3 array.
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
second_column = array_2d[:, 1]  # Slicing to get the second column
print(second_column)  # Output: [2 5 8]