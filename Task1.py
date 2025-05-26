import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("D:\Internship\Mall_Customers.csv")

# Inspect the data
print("Initial data:\n", df.head())
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicates:", df.duplicated().sum())

# Drop duplicates
df.drop_duplicates(inplace=True)

# Standardize text
df['Gender'] = df['Gender'].str.lower().str.strip()

# Rename columns
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Export cleaned data
df.to_csv('cleaned_mall_customers.csv', index=False)

print("\nCleaned data saved to 'cleaned_mall_customers.csv'")
