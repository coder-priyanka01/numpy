import numpy as np

# normalize a random 5x5 matrix(values between 0 and 1)
matrix = np.random.rand(5, 5)
normalized_matrix = (matrix - np.min(matrix)) / (np.max(matrix) - np.min(matrix))
print(normalized_matrix)
# Output: A 5x5 matrix with values normalized between 0 and 1

