import pandas as pd

df = pd.read_csv(r"D:\ecommerce-analytics\data\raw_orders.csv")
df.head()

# Convert date column into proper date format
df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")

# Check for missing values
df.isnull().sum()

df["revenue"] = df["quantity"] * df["price"]
total_revenue = df["revenue"].sum()
total_revenue
top_product = df.groupby("product")["quantity"].sum().sort_values(ascending=False)
top_product
total_customers = df["customer_id"].nunique()
total_customers

import matplotlib.pyplot as plt

product_sales = df.groupby("product")["quantity"].sum()

plt.figure(figsize=(8,5))
product_sales.plot(kind="bar")
plt.title("Quantity Sold per Product")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.show()

revenue_per_product = df.groupby("product")["revenue"].sum()

plt.figure(figsize=(8,5))
revenue_per_product.plot(kind="bar")
plt.title("Revenue per Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

daily_revenue = df.groupby("date")["revenue"].sum()

plt.figure(figsize=(8,5))
daily_revenue.plot(kind="line", marker="o")
plt.title("Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.show()

df.to_csv(r"D:\ecommerce-analytics\data\clean_orders.csv", index=False)
