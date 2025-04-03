import pandas as pd

data = {
'Region': ['North', 'South', 'East', 'West', 'North', 'South'],
'Product': ['Electronics', 'Furniture', 'Clothing',
'Electronics', 'Furniture', 'Clothing'],
'Sales_Channel': ['Online', 'Retail', 'Online', 'Wholesale', 'Retail', 'Online'],
'Units_Sold': [120, 80, 200, 150, 90, 300],
'Revenue': [60.5, 45.0, 35.0, 70.0, 50.5, 55.0],
'Profit': [15.2, 12.0, 8.5, 20.5, 13.2, 10.0]
}
sales_df = pd.DataFrame(data)
print(sales_df["Revenue"])
profit15 = sales_df[sales_df["Profit"] > 15]
