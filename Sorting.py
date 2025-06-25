import numpy as np 

unsorted = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print("Sorted Array", np.sort(unsorted))

arr_2d_unsorted = np.array([[3, 1], [1, 2], [2, 3]])
print("Sorted 2D array by column", np.sort(arr_2d_unsorted, axis=0))
