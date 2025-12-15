import pandas as pd

df = pd.read_csv("Sample.CSV")
print("DataFrame: \n",df)

filtered_df = df[df["age"]>25]
print("Filtered DataFrame based on age: \n",filtered_df)

sorted_df = df.sort_values('age')
print("DataFrame sorted by age: \n",sorted_df)

avg_age_by_designation = df.groupby('Designation')['age'].mean()
print("Average age for each Designation: \n ",avg_age_by_designation)
