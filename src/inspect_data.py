import pandas as pd


df = pd.read_csv("data/raw/dirty_cafe_sales.csv")

print("First five rows:")
print(df.head())

print("\nDataFrame information:")
df.info()

print("\nDescriptive summary:")
print(df.describe(include="all"))

print("\nColumn data types:")
print(df.dtypes)

print("\nRow count:")
print(len(df))
