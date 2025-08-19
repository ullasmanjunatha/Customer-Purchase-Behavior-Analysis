import pandas as pd
import numpy as np


df = pd.read_excel('Online_Retail.xlsx')


print("\nShape of dataset (rows, columns):")
print(df.shape)

print("\nColumns names and data types:")
print(df.dtypes)

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nSummary  statistics:")
print(df.describe())


print("\nUnique values in categorical columns:")
