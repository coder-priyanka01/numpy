import numpy as np
import time

py_list = [1,2,3]
print("Python list multiplication", py_list * 2)

np_array = np.array([1,2,3])#element wise multiplicstion
print("Python list multiplication", np_array * 2)

start = time.time()
py_list = [i*2 for i in range(100000)]
print("\n list operation time: ", time.time() - start)

start = time.time()
np_array = np.arange(1000000) * 2
print("\n numpy operation time: ", time.time() - start)
