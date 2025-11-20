import pandas as pd
import sqlite3

def etl_process(csv_file, db_file, table_name):

    # -------- Extract --------
    df = pd.read_csv(csv_file)
    print("Original df:\n", df, "\n")

    # -------- Transform --------
    cleaned_df = df.dropna()
    print("Filtered df:\n", cleaned_df, "\n")

    transformed_df = cleaned_df.rename(columns={
        'Name': 'Employee Name',
        'Salary($)': 'Salary'
    })
    print("Renamed df:\n", transformed_df, "\n")

    transformed_df = transformed_df.drop(columns=['Email ID', 'Joining Date', 'Phone No'])
    print("Dropped columns df:\n", transformed_df, "\n")

    transformed_df['Salary Hike'] = transformed_df['Salary'] * 0.10
    print("Added calculated column df:\n", transformed_df, "\n")

    # -------- Load --------
    conn = sqlite3.connect(db_file)
    transformed_df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

    print(f"Data successfully loaded into DB: {db_file}, table: {table_name}")

    return transformed_df

# Calling the ETL function 

try: etl_process(
        csv_file="EmployeeData copy.csv",
        db_file="EmployeeData.db",
        table_name="EmployeeData"
        )
except Exception as e:
    print(f"An error occurred: {e}")