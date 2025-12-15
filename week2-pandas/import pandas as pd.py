import pandas as pd 
from tabulate import tabulate

df = pd.read_csv("Sample.csv")

print(df)

cleaned_df = df.dropna()
print(tabulate(cleaned_df,headers='Keys',tablefmt='psql'))

print(df[df["age"]>30])

agg_df = df.groupby("Designation")["age"].mean()
print(agg_df)


