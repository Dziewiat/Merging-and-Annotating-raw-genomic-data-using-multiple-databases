import pandas as pd


df = pd.read_csv("C:/Users/patap/Desktop/Python projects/Merging and Annotating raw genomic data using multiple"
                 " databases/results/variants-cleaned.csv")
df.drop(df.columns[0], axis=1)
df

# Data analysis
# Determining the variant type


def variant_type(row):
    if len(row["REF_x"]) == len(row["ALT_x"]):
        # Checking for Multi-Nucleotide Variations
        var_count = 0
        for i, j in zip(row["REF_x"], row["ALT_x"]):
            if i != j:
                var_count += 1
        if var_count == 1:
            return "SNV"
        else:
            return "MNV"  # In case of Multi-Nucleotide Variations
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
# The goal is to assign gene names to specific SNVs
# This is done by merging based on if the mutation position is between the gene start and end position
hg19_df = pd.read_csv("C:/Users/patap/Desktop/Python projects/Merging and Annotating raw genomic data using multiple"
                      " databases/raw_gene_data/hg19-genes.csv")
sorted_snv_df = snv_df.sort_values(by="POS_x")
sorted_hg19_df = hg19_df.sort_values(by="Start")  # Sorting dataframes for the merge_asof function
merged_df = pd.merge_asof(sorted_snv_df, sorted_hg19_df, left_on="POS_x", right_on="Start", direction="backward")
print(merged_df)
merged_df.to_excel("C:/Users/patap/Desktop/Python projects/Merging and Annotating raw genomic data using multiple"
                   " databases/results/merged-dataframe.xlsx")

# Deleting rows in which the chromosomes do not match
merged_df = merged_df.loc[merged_df["CHROM_x"] == merged_df["chrom"]]
print(merged_df)
merged_df.to_excel("C:/Users/patap/Desktop/Python projects/Merging and Annotating raw genomic data using multiple"
                   " databases/results/merged-dataframe-cleaned.xlsx")
