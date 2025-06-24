import numpy as np
arr = np.arange(12)
print("Original array ", arr)

reshaped = arr.reshape((3, 4))
print("\n Reshaped array ", reshaped)

flattened = reshaped.flatten()
print("\n Flattened array ", flattened)

#ravel (returns view, instead of copy)
raveled = reshaped.ravel()
print("\n raveled array ", raveled)

#Transpose
transpose = reshaped.T
print("\n Transposed array ", transpose)
