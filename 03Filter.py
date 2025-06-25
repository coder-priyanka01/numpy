import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even_number = numbers[numbers % 2 == 0]
print("Even numbers", even_number)