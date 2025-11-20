import sqlite3
import pandas as pd 


df = pd.read_csv("EmployeeData copy.csv")

print("Original df: \n",df,"\n")

#Perform transformations like filtering, column renaming

df = df.dropna()
print("filtered df \n",df,"\n")

df = df.rename(columns={'Name': 'Employee Name'})
df = df.rename(columns={'Salary($)': 'Salary'})
print("renamed df \n",df,"\n")

df = df.drop(columns=['Email ID', 'Joining Date','Phone No'])
print("dropped df \n",df,"\n")


# Adding Calculated field 

df['Salary Hike'] = df["Salary"]*0.10
print("added calculated field df \n",df)


# Loading transformed data into Sqlite3 db 

conn = sqlite3.connect("EmployeeData.db")

df.to_sql("EmployeeData",conn,if_exists="replace",index=False)
print("\n Data Successfully loaded into db")

query = "SELECT * FROM EmployeeData"
loaded_df = pd.read_sql_query(query,conn)
print("\n Loaded Data from db \n",loaded_df,"\n")

conn.close()