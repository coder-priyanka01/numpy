import numpy as np
import matplotlib.pyplot as plt

#Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000], #Paradise biryani
    [2, 120000, 140000, 160000, 190000], #beijing bites
    [3, 200000, 230000, 260000, 300000], #pizza hub
    [4, 180000, 210000, 240000, 270000], #burgur point
    [5, 160000, 185000, 205000, 230000]  #chai point
])
cumsum = np.cumsum(sales_data[:, 1:], axis=1)
print(cumsum)

plt.figure(figsize=(10, 6))
plt.plot(np.mean(cumsum, axis=0))   
plt.title("Average cumulative sales across all restaurant")
plt.xlabel("years")
plt.ylabel("sales")
plt.grid(True)
plt.show()