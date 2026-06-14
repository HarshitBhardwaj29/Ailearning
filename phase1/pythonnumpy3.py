import numpy as np
import matplotlib.pyplot as plt
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]   # Chai Point
])

print("=== Zomoto sales analysis")
print("\n Sales data shapes",sales_data.shape)
print("\n Sample data for 1st 3 ",sales_data[0:3])
print(sales_data[:,1:])
#first one is row and second one is column

# total sales per year
print(np.sum(sales_data[:,1:],axis=0))


#max sales
max_sales = np.max(sales_data[:,1:],axis=0)
avg_sales = np.mean(sales_data[:,1:],axis=1)

cumsum = np.cumsum(sales_data[:,1:],axis=1)
plt.figure(figsize=(10,6))
plt.plot(np.mean(cumsum,axis=0))
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

vector1 = np.array([1,2,3,4,5,6])
