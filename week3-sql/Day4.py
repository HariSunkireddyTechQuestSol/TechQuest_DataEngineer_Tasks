import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect('company.db')
cur = conn.cursor()

# Fetch data using pandas
print("Original Employees Table:")
df = pd.read_sql_query("SELECT * FROM employees", conn)
print(df, "\n")

# UPDATE operation
cur.execute("UPDATE employees SET salary = salary + 5000 WHERE emp_name = 'Alice'")
conn.commit()

# DELETE operation
cur.execute("DELETE FROM employees WHERE emp_name = 'Eve'")
conn.commit()

# Fetch updated data using pandas
print("After UPDATE and DELETE:")
df_updated = pd.read_sql_query("SELECT * FROM employees", conn)
print(df_updated, "\n")

# You can also use JOIN with pandas
print("Joined Employee + Department Data:")
query = """
SELECT e.emp_name, e.salary, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
"""
df_joined = pd.read_sql_query(query, conn)
print(df_joined)

# Close connection
conn.close()
