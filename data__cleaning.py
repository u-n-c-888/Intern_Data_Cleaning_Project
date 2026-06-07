import pandas as pd

# Load Dataset
df = pd.read_csv("customer_data.csv")

# Handle Missing Values

df["City"].fillna("Unknown", inplace=True)

df["Email"].fillna(
    "not_provided@email.com",
    inplace=True
)

# Remove Duplicates

df.drop_duplicates(inplace=True)

# Standardize Gender Values

df["Gender"] = df["Gender"].str.lower()

gender_map = {
    "m":"male",
    "male":"male",
    "f":"female",
    "female":"female"
}

df["Gender"] = df["Gender"].replace(gender_map)

# Standardize Date Format

df["Date_of_Birth"] = pd.to_datetime(
    df["Date_of_Birth"]
)

df["Join_Date"] = pd.to_datetime(
    df["Join_Date"]
)

# Feature Engineering
# Create Customer Age

today = pd.Timestamp.today()

df["Customer_Age"] = (
    (today - df["Date_of_Birth"]).dt.days // 365
)

# Categorize Purchase Amount

def category(x):
    if x < 1000:
        return "Low"
    elif x < 5000:
        return "Medium"
    else:
        return "High"

df["Purchase_Category"] = (
    df["Purchase_Amount"].apply(category)
)

# Outlier Removal (IQR Method)

Q1 = df["Purchase_Amount"].quantile(0.25)
Q3 = df["Purchase_Amount"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[
    (df["Purchase_Amount"] >= lower) &
    (df["Purchase_Amount"] <= upper)
]

# Save Cleaned Dataset


df.to_csv(
    "customer_data_cleaned.csv",
    index=False
)

print("Cleaning completed successfully.")
