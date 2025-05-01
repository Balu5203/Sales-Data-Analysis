import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Load data
df = pd.read_csv('E:/Document/python/sales_data_analysis/data/sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Total'] = df['Quantity'] * df['Unit Price']

# Title
st.title("📊 Sales Data Dashboard")

# Date filter
start_date = st.date_input("Start Date", df['Date'].min())
end_date = st.date_input("End Date", df['Date'].max())
filtered_df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]

# Key metrics
total_sales = filtered_df['Total'].sum()
average_order = filtered_df['Total'].mean()
top_region = filtered_df.groupby('Region')['Total'].sum().idxmax()

st.metric("Total Sales", f"${total_sales:,.2f}")
st.metric("Average Order Value", f"${average_order:,.2f}")
st.metric("Top Region", top_region)

# Plots
st.subheader("Sales by Region")
region_sales = filtered_df.groupby('Region')['Total'].sum()
fig1, ax1 = plt.subplots()
region_sales.plot(kind='bar', ax=ax1)
ax1.set_ylabel("Sales ($)")
st.pyplot(fig1)

st.subheader("Top Products")
top_products = filtered_df.groupby('Product')['Total'].sum().sort_values(ascending=False)
fig2, ax2 = plt.subplots()
top_products.plot(kind='barh', ax=ax2)
ax2.set_xlabel("Sales ($)")
st.pyplot(fig2)

st.subheader("Sales Over Time")
sales_trend = filtered_df.groupby('Date')['Total'].sum()
fig3, ax3 = plt.subplots()
sales_trend.plot(ax=ax3)
ax3.set_ylabel("Sales ($)")
ax3.set_xlabel("Date")
st.pyplot(fig3)
