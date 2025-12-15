#Creating Database using Sqlite 

import sqlite3

conn = sqlite3.connect("Sample.db")
cur = conn.cursor()

#Insering Data into Emplooyees Table 
  
cur.execute(""" INSERT INTO employees (name, department, salary)
                VALUES ('Alice', 'HR', 60000),
                       ('Bob', 'Engineering', 85000),
                       ('Charlie', 'Marketing', 70000);
""")

#Filtering the data

content = conn.execute("""select * from employees
                       where salary > 50000;""")

for row in content:
    print(row)

conn.close()

