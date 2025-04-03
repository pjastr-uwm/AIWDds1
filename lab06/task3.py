import pandas as pd

dane = pd.read_csv("date_temp.csv", parse_dates=["Reading_Date"], date_format="%Y/%m/%d")