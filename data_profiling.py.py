import pandas as pd

df = pd.read_csv("customer_data.csv")

# Basic Information
print(df.info())

# Missing Values
print(df.isnull().sum())

# Duplicate Records
print("Duplicates:", df.duplicated().sum())

# Statistical Summary
print(df.describe())

# Check Unique Values
print(df.nunique())