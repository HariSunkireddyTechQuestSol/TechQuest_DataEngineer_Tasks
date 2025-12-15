import sqlite3

# Connect (or create) database
conn = sqlite3.connect('company.db')
cur = conn.cursor()

# Create first table - Departments
cur.execute('''
CREATE TABLE IF NOT EXISTS departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT
)
''')

# Create second table - Employees
cur.execute('''
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT,
    salary REAL,
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
)
''')

# Insert data into departments
cur.executemany("INSERT INTO departments (dept_name) VALUES (?)", [
    ("HR",),
    ("Engineering",),
    ("Marketing",)
])

# Insert data into employees
cur.executemany("""
INSERT INTO employees (emp_name, salary, dept_id)
VALUES (?, ?, ?)
""", [
    ("Alice", 60000, 1),
    ("Bob", 85000, 2),
    ("Charlie", 70000, 3),
    ("David", 90000, 2),
    ("Eve", 55000, 1)
])

conn.commit()

# ------------------------------
# Fetch specific records using WHERE
print("\nEmployees with salary > 60000:")
for row in cur.execute("SELECT emp_name, salary FROM employees WHERE salary > 60000"):
    print(row)

# ORDER BY
print("\nEmployees ordered by salary descending:")
for row in cur.execute("SELECT emp_name, salary FROM employees ORDER BY salary DESC"):
    print(row)

# LIMIT
print("\nTop 3 highest paid employees:")
for row in cur.execute("SELECT emp_name, salary FROM employees ORDER BY salary DESC LIMIT 3"):
    print(row)

# ------------------------------
# INNER JOIN between employees and departments
print("\nEmployee details with department names:")
for row in cur.execute("""
SELECT e.emp_name, e.salary, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
"""):
    print(row)

# Close connection
conn.close()
