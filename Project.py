import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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

# Data analysis
# Determining the variant type


def variant_type(row):
    if len(row["REF_x"]) == len(row["ALT_x"]):
        var_count = 0
        for i, j in zip(row["REF_x"], row["ALT_x"]):
            if i != j:
                var_count += 1
        if var_count == 1:
            return "SNV"
        else:
            return "MNV"  # In case of Multi-Nucleotide Polymorphism
    elif len(row["REF_x"]) > len(row["ALT_x"]):
        return "deletion"
    else:
        return "insertion"


df["Var_type"] = df.apply(variant_type, 1)
print(df.head())

# Filtering out all variants except SNVs
snv_df = df.loc[df["Var_type"] == "SNV"]
print(snv_df.head())
print(len(snv_df))

# Merging filtered dataframe with hg19 file based on common columns
hg19_df = pd.read_csv("C:/Users/patap/Desktop/Python projects/Merging and Annotating raw genomic data using multiple"
                      " databases/raw_gene_data/hg19-genes.csv")

