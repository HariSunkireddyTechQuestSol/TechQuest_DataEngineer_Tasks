import sqlite3

# 1. Connect to database (creates file if it doesn’t exist)
conn = sqlite3.connect("sample.db")

# 2. Create a cursor object (used to execute SQL commands)
cursor = conn.cursor()

# 3. Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT,
    salary REAL
)
""")

# 4. Insert sample records
cursor.executemany("""
INSERT INTO employees (name, department, salary)
VALUES (?, ?, ?)
""", [
    ("Alice", "HR", 60000),
    ("Bob", "Engineering", 85000),
    ("Charlie", "Marketing", 70000)
])

# 5. Commit the changes (saves data)
conn.commit()

# 6. Fetch and display data using SELECT
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

print("Employee Records:")
for row in rows:
    print(row)

# 7. Close the connection
conn.close()
