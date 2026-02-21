import pandas as pd

# CSV file read
data = pd.read_csv("sales_data.csv")

print("Full Dataset:")
print(data)

# Total Sales calculate
total_sales = data["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Sales by Product
product_sales = data.groupby("Product")["Sales"].sum()

print("\nSales by Product:")
print(product_sales)

# Best Selling Product
best_product = product_sales.idxmax()
print("\nBest Selling Product:", best_product)

# Convert Date column to datetime
data["Date"] = pd.to_datetime(data["Date"])

# Extract Month
data["Month"] = data["Date"].dt.month

# Monthly Sales
monthly_sales = data.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)


import matplotlib.pyplot as plt

# Bar Chart for Monthly Sales
monthly_sales.plot(kind="bar")

plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()