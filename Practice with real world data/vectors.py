import numpy as np
import matplotlib.pyplot as plt

vector1 = np.array([1, 2, 3, 4, 5])
vector2 = np.array([6, 7, 8, 9, 10])
print("vector addition: ", vector1 + vector2)

print("\n Multiplication vector", vector1 * vector2)

print("\n Dot Product", np.dot(vector1, vector2))

angle = np.arccos(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))
print(angle)

