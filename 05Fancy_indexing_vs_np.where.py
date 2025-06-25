import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
indices = [0, 2, 4]
print(numbers[indices])

Where_result =  np.where(numbers > 5)
print("Np where", numbers[Where_result])

condition_array = np.where(numbers > 5)
print(condition_array)