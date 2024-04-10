The goal of this code is to merge two files, one containing mutations data, and the other containing genomic data. It determines mutation types and matches mutations to specific genes.

It cleans an Excel file containing information about gene mutations by:
- Handling missing values
- Removing duplicates
- Checking for inconsistencies

Next it analyzes the data, looking for SNV type mutations and filters out any other mutation types.

Then it merges the Excel file with a .csv file containing some genomic data, like gene locations and names by matching the mutation positions and gene locations.
