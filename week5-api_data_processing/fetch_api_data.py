import pandas as pd 

df = pd.read_csv("EmployeeData copy.csv")

df.to_json("EmployeeData.json", orient="records", lines=True)
df = pd.read_json("EmployeeData.json", lines=True)
print(df)
