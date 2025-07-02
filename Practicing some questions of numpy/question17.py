import numpy as np

# create a checkerboard pattern using numpy 8x8 grid
checkerboard = np.zeros((8, 8))
checkerboard[1::2, ::2] = 1
checkerboard[::2, 1::2] = 1
print(checkerboard)