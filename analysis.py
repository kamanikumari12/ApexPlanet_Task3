import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_excel("Cleaned_Data.xlsx")

# Create Month column
df["Month"] = pd.to_datetime(df["Order_Date"]).dt.to_period("M").astype(str)

# KPI
print("Total Sales:", df["Total_Sales"].sum())
print("Total Orders:", len(df))
print("Unique Customers:", df["Customer_ID"].nunique())

# Graph 1
top_products = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False).head()

plt.figure(figsize=(8,5))
top_products.plot(kind="bar")
plt.title("Top Products by Sales")
plt.tight_layout()
plt.savefig("graphs/top_products.png")
plt.show()

# Graph 2
city_sales = df.groupby("City")["Total_Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(8,5))
city_sales.plot(kind="bar")
plt.title("Top Cities by Sales")
plt.tight_layout()
plt.savefig("graphs/city_sales.png")
plt.show()

# Graph 3
monthly = df.groupby("Month")["Total_Sales"].sum()

plt.figure(figsize=(10,5))
monthly.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.grid(True)
plt.tight_layout()
plt.savefig("graphs/monthly_sales.png")
plt.show()

# Graph 4
category = df.groupby("Category")["Total_Sales"].sum()

plt.figure(figsize=(6,6))
category.plot(kind="pie",autopct="%1.1f%%")
plt.ylabel("")
plt.title("Category Distribution")
plt.savefig("graphs/category.png")
plt.show()
