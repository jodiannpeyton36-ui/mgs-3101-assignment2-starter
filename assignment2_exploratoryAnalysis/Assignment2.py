import pandas as pd
import numpy as np

df = pd.read_csv("Sales-Export_2019-2020.csv")

df = pd.read_csv("Sales-Export_2019-2020.csv")

df.columns = df.columns.str.strip()

for column in ["order_value_EUR", "cost"]:
    if column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")
    else:
        print(f"Warning: column '{column}' not found in the dataset.")

print("\n" + "=" * 60)
print("Exploratory Analysis")
print("=" * 60 + "\n")

print("Shape of Data".center(60, "-"))
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\n" + "-" * 60)
print("Data Types".center(60, "-"))
print(df.dtypes)

print("\n" + "-" * 60)
print("First 5 Rows".center(60, "-"))
print(df.head())

print("\n" + "-" * 60)
print(" Are there any Missing Values?".center(60, "-"))
missing_values = df.isnull().sum()
if missing_values.sum() > 0:
    print(missing_values)
    print(f"Total Missing Values: {missing_values.sum()}")
else:
    print("No missing values found.")

#have these lines calculate using the csv's cost column
column = "cost"
if column in df.columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

print("\n Important statistics")
if len(df[column].dropna()) >= 2:
    values = df[column]
    print(f"\nColumn: {column}")
    print(f"Count: {values.count()}")     
    print(f"Mean: {values.mean():.2f}")       
    print(f"Median: {values.median():.2f}")      
    print(f"Minimum: {values.min():.2f}")     
    print(f"Maximum: {values.max():.2f}")
    print(f"Standard deviation: {values.std():.2f}")
       
else:
    print("Must contain two or more numeric columns for the data")

print("\n" + "-" * 60)
print("Grouping of Sales By Country".center(60, "-"))
Sales_by_country = (df.groupby("country")["order_value_EUR"].sum().sort_values(ascending=False))
print(Sales_by_country)

print("Highest and Lowest Sales by Country".center(60, "-"))
highest_sales_country = Sales_by_country.idxmax()
lowest_sales_country = Sales_by_country.idxmin()
print(f"Highest Sales Country: {highest_sales_country} with sales of {Sales_by_country[highest_sales_country]:,.2f} EUR")
print(f"Lowest Sales Country: {lowest_sales_country} with sales of {Sales_by_country[lowest_sales_country]:,.2f} EUR")