import matplotlib.pyplot as plt
from Merging import df


# Grouping chromosomes with specific variant type quantities
grouped_df = df.groupby(["CHROM_x", "Var_type"]).size().unstack().fillna(0)
print(grouped_df)

# Plotting a stacked bar plot for distribution of variant types across chromosomes
grouped_df[["SNV", "deletion", "insertion"]].plot(kind="bar", stacked=True, color=["red", "blue", "green"])
plt.xlabel("Chromosomes")
plt.ylabel("Variant types")
plt.title("Distribution of variant types across chromosomes")
plt.show()
