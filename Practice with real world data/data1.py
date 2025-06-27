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

print("=== Zomato sales analysis ===")
print("\n sales data shape", sales_data.shape)
print("\n sample data for 1st 3 restau: ", sales_data[:3])
print("\n sample data for 1st 3 restau: ", sales_data[:, 1:])

#total sales per year
print(np.sum(sales_data, axis = 0))
yeary_total = np.sum(sales_data[:, 1:], axis=0)
print(yeary_total)

#Minimum sales per restaurant
min_sales = np.min(sales_data[:, 1:], axis=0)
print(min_sales)
