import pandas as pd


df = pd.read_excel("C:/Users/patap/Desktop/Python projects/Merging and Annotating raw genomic data using multiple"
                   " databases/raw_gene_data/variants-file.xlsx", sheet_name=0)
print(df.head())
print("Original length:", len(df))

# Data cleaning
# Handling missing values
df = df.dropna(axis=0, how="any")
print("Length without NAs:", len(df))

# Removing duplicates
df = df.drop_duplicates()
print("Length without duplicates:", len(df))

# Correcting inconsistencies
print(df.dtypes)  # All checks out, numbers classified as int 64, rest as objects
print(pd.to_numeric(df["POS_x"], errors='coerce').isnull().value_counts())
print(pd.to_numeric(df["End_x"], errors='coerce').isnull().value_counts())

df.to_csv("C:/Users/patap/Desktop/Python projects/Merging and Annotating raw genomic data using multiple"
          " databases/results/variants-cleaned.csv")
