import pandas as pd
df=pd.read_csv("Data Cleaning & Reporting Automation/netflix_titles.csv")
#duplicate data is removed
df=df.drop_duplicates()
print(df)
#remove empty row
df=df.dropna()
print(df)
df=df.dropna()
print(df)
df.to_csv("Data Cleaning & Reporting Automation/netflix_titles.csv")