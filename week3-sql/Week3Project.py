import sqlite3

conn = sqlite3.connect("NewEmp_db.db")
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Department (
    dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dept_name TEXT NOT NULL
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Employee (
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    emp_name TEXT NOT NULL,
    salary REAL,
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
)
''')

cur.executemany("INSERT INTO Department (dept_name) VALUES (?)", [
    ('HR',),
    ('Engineering',),
    ('Finance',)
])

cur.executemany("""
INSERT INTO Employee (emp_name, salary, dept_id)
VALUES (?, ?, ?)
""", [
    ('Alice', 65000, 1),
    ('Bob', 85000, 2),
    ('Charlie', 72000, 3),
    ('David', 90000, 2)
])
conn.commit()

cur.execute("UPDATE Employee SET salary = salary + 5000 WHERE emp_name = 'Alice'")
conn.commit()

print("All Employees:")
for row in cur.execute("SELECT * FROM Employee"):
    print(row)

print("\nEmployees with salary > 70000:")
for row in cur.execute("SELECT emp_name, salary FROM Employee WHERE salary > 70000"):
    print(row)

print("\nEmployee details with Department names:")
for row in cur.execute("""
SELECT e.emp_name, e.salary, d.dept_name
FROM Employee e
INNER JOIN Department d ON e.dept_id = d.dept_id
"""):
    print(row)

conn.close()
