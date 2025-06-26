import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6, 7])
c = np.array([7, 8, 9])

print("Compatibilty shapes", a.shape == b.shape)

#for rows
original = np.array([[1, 2], [3, 4]])
new_row = np.array([[5, 6]])

with_new_row = np.vstack((original, new_row))
print(original)
print(with_new_row)

#for column
new_col = np.array([[7], [8]])
with_new_col = np.hstack((original, new_col))
print("With new column", with_new_col)
 
#delete opertion
arr = np.array([1, 2, 3, 4, 5])
deleted = np.delete(arr, 2)
print("Array after deletion: ", deleted)
