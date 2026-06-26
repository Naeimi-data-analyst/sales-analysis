import pandas as pd
import matplotlib.pyplot as plt

# Read Excel file
df = pd.read_excel('sales_data.xlsx')

# Show first 5 rows
print("\n First 5 rows of data:")
print(df.head())

# Descriptive statistics
print("\n Descriptive statistics:")
print(df.describe())

# Total sales
total_sales = df['Sales'].sum()
print(f"\n Total Sales: {total_sales}")

# Best selling product
best_product = df.groupby('Product')['Sales'].sum().idxmax()
best_sales = df.groupby('Product')['Sales'].sum().max()
print(f"\n Best Product: {best_product} with {best_sales} sales")

# ========== Charts ==========

# 1. Bar chart: Sales by product
sales_by_product = df.groupby('Product')['Sales'].sum()
plt.figure(figsize=(8, 5))
sales_by_product.plot(kind='bar', color='skyblue')
plt.title('Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_by_product.png')
plt.show()

# 2. Line chart: Daily sales trend

#df['Date']=pd.to_datetime(df['Date'])
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Sales'], marker='o', linestyle='-', color='green')
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('daily_sales_trend.png')
plt.show()

print("\n Analysis and charts completed successfully!")