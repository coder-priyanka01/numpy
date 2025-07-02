import numpy as np

# create a 5x5 array with 1s on the border and 0s inside
array_5x5 = np.ones((5, 5)) 
array_5x5[1:-1] = 0
print(array_5x5)
# Output:
# [[1. 1. 1. 1. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 0. 0. 0. 1.]]    