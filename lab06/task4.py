import pandas as pd
from sqlite3 import connect

conn = connect('sales_data3.db')
data = pd.read_sql("SELECT * FROM sales", con=conn)
data["sale_date"] = pd.to_datetime(data["sale_date"])
