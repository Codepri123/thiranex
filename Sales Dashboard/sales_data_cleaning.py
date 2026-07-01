import pandas as pd
df=pd.read_csv("Sales Dashboard/sales_data_sample.csv",encoding="cp1252")
print(df)
df=df.dropna()
df=df.drop_duplicates()
print(df)
df["Total_Sales"]=df["PRICEEACH"]*df["QUANTITYORDERED"]
print(df)
df["Average_Sales"]=df["SALES"].mean()
print(df)
df["Total_orders"]=df["QUANTITYORDERED"].nunique()
print(df)
df["Revenue"] = df.groupby("PRODUCTLINE")["SALES"].transform("sum")
print(df)
df.to_csv("sales_data.csv")

