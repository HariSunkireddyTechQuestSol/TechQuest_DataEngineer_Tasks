import pandas as pd

df = pd.read_csv("Sample.csv")

print("Original DataFrame: \n", df)

print("Printing first five rows of the dataframe: \n",df.head(5))

dropped_df = df.dropna()
print("Dataframe after dropping rows with having null values: \n",dropped_df)

fill_df =df.fillna("Unknown")
print("Dataframe after filling null values: \n", fill_df)

df.rename(columns= {'name':'Person_Name','age':'Person_Age'}, inplace=True)
print(df)