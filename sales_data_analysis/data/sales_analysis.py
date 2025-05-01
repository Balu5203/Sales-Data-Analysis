import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('E:/Document/python/sales_data_analysis/data/sales_data.csv')

# Clean data
df['Date'] = pd.to_datetime(df['Date'])
df['Total'] = df['Quantity'] * df['Unit Price']

# Sales by region
region_sales = df.groupby('Region')['Total'].sum()

# Plot and save
region_sales.plot(kind='bar', title='Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales ($)')
plt.tight_layout()
plt.savefig('../output/region_sales.png')
plt.show()
