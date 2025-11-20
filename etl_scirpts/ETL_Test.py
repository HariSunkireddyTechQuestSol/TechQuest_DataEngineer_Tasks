import pandas as pd
import sqlite3

""" Data Extraction """ 

# Reading data from CSV file 

df = pd.read_csv("EmployeeData copy.csv")
print(df)


""" Data Transformation """

df = df.dropna()
print(df)
print(df.info())


df = df.rename(columns={'Name': 'Employee Name'})
df = df.rename(columns={'Salary($)': 'Salary'})
print(df)
print(df.info())

df = df.drop(columns=['Email ID', 'Joining Date','Phone No'])
print(df)
print(df.info())

df['Salary Hike'] = df["Salary"]*0.10
print(df)
print(df.info())

""" Data Loading """    

conn = sqlite3.connect("Emp.db")
conn.execute("DROP TABLE IF EXISTS EmployeeData")

conn.execute(""" CREATE TABLE IF NOT EXISTS EmployeeData (
    EmployeeID INTEGER PRIMARY KEY,
    EmployeeName TEXT,
    Department TEXT,
    Salary REAL,
    SalaryHike REAL
)""")

df.to_sql("EmployeeData",conn,if_exists="replace",index=False)  
conn.commit()
conn.close()








