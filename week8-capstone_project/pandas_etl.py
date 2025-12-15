import pandas as pd
import sqlite3


# CAPSTONE ETL PIPELINE

# Extract  → Transform  → Load using Pandas & SQLite

def etl_process(csv_file, db_file, table_name):
    """
    Capstone ETL Function
    ---------------------
    Extracts employee data from a CSV file, performs
    transformations using Pandas, and loads the final
    dataset into a SQLite database.
    """

   
    # 1. EXTRACT 
   
    # Read source CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file)

    print("=== Extracted Raw Data ===")
    print(df, "\n")

   
    # 2. TRANSFORM 

    # Step 1: Remove rows with missing values
    # Ensures data consistency and quality
    cleaned_df = df.dropna()

    print("=== After Removing Missing Values ===")
    print(cleaned_df, "\n")

    # Step 2: Rename columns for clarity and standard naming
    transformed_df = cleaned_df.rename(columns={
        "Name": "Employee Name",
        "Salary($)": "Salary"
    })

    print("=== After Renaming Columns ===")
    print(transformed_df, "\n")

    # Step 3: Drop columns that are not required for analysis
    # This reduces table size and removes unnecessary personal data
    transformed_df = transformed_df.drop(
        columns=["Email ID", "Joining Date", "Phone No"]
    )

    print("=== After Dropping Unnecessary Columns ===")
    print(transformed_df, "\n")

    # Step 4: Create a derived column using business logic
    # Calculate a 10% salary hike
    transformed_df["Salary Hike"] = transformed_df["Salary"] * 0.10

    print("=== After Adding Salary Hike Column ===")
    print(transformed_df, "\n")


    # 3. LOAD 
   
    # Connect to SQLite database (creates DB file if not exists)
    conn = sqlite3.connect(db_file)

    # Load transformed data into SQLite table
    # Replaces the table if it already exists
    transformed_df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    # Close database connection
    conn.close()

    print(
        f"Data successfully loaded into database '{db_file}' "
        f"inside table '{table_name}'"
    )

    # Return final DataFrame (useful for validation/testing)
    return transformed_df



# 4. CAPSTONE PIPELINE EXECUTION 


if __name__ == "__main__":
    try:
        etl_process(
            csv_file="employee_data.csv",
            db_file="EmployeeData.db",
            table_name="EmployeeData"
        )
    except Exception as e:
        print(f"Capstone ETL Pipeline Failed: {e}")
