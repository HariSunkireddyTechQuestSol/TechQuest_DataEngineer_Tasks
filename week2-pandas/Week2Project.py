import pandas as pd 
#Loading Sample CSV file
df = pd.read_csv("EmployeeData.csv")

#Dropping Null values
filterdf = df.dropna()
print(filterdf)

#Renaming Column names
new_df = filterdf.rename(columns={"Emp ID":"EID","Email ID":"Email","Salary($)":"Salary"})
print(new_df)

#Performing Agrregrations 
gdf = new_df.groupby("Dept")

avg_salary = gdf["Salary"].mean()
print(avg_salary)

#Exporting Cleaned data to new file 

filterdf.to_csv("Cleaned_EmployeeData.csv")