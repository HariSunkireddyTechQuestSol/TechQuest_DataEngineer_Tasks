# Week 8 Capstone Project

## Design and Implementation of an End-to-End ETL Pipeline

---

## 1. Introduction

This capstone project focuses on the design and implementation of a complete **ETL (Extract, Transform, Load) pipeline** using Python-based data engineering tools.
The project demonstrates how raw data can be systematically ingested, transformed according to business rules, and stored in a relational database for downstream analytics.

To illustrate both foundational and scalable approaches, the ETL pipeline is implemented in **two versions**:

1. **Pandas-based ETL pipeline (Python + Pandas + SQLite)**
2. **PySpark-based ETL pipeline (PySpark + SQLite)**

Both implementations follow the same logical data flow and transformation rules.

---

## 2. Project Objectives

The primary objectives of this capstone project are:

* To understand and implement core ETL concepts
* To design a structured and reusable ETL pipeline
* To perform data cleaning, transformation, and enrichment
* To load processed data into a relational database
* To compare traditional and distributed-style data processing approaches

---

## 3. Dataset Description

* **Source Type:** CSV file
* **Dataset Name:** EmployeeData copy.csv
* **Description:**
  The dataset contains employee-related information such as name, salary, contact details, and joining date.
  The data is used to demonstrate cleaning operations, schema standardization, and business rule implementation.

---

## 4. High-Level Architecture

```
Source CSV File
      ↓
ETL Processing Layer
(Pandas or PySpark)
      ↓
Cleaned & Transformed Dataset
      ↓
SQLite Relational Database
```

---

## 5. Project Structure

```
Week8_Capstone_Project/
│
├── pandas_etl.py          # ETL pipeline using Pandas
├── pyspark_etl.py         # ETL pipeline using PySpark
├── EmployeeData copy.csv  # Input dataset
├── EmployeeData.db        # SQLite database (generated after execution)
└── README.md              # Project documentation
```

---

## 6. ETL Implementation – Pandas Version

### 6.1 Technologies Used

* Python
* Pandas
* SQLite

### 6.2 ETL Workflow

#### Extract

* Reads employee data from a CSV file using Pandas.

#### Transform

* Removes records containing missing values
* Renames columns to ensure consistency and readability
* Drops columns not required for analysis
* Creates a derived column **Salary Hike**, calculated as 10% of the employee salary

#### Load

* Loads the transformed dataset into a SQLite database table

### 6.3 Execution

```bash
python pandas_etl.py
```

### 6.4 Use Case

This implementation is suitable for:

* Learning core ETL concepts
* Small to medium-sized datasets
* Local data processing and prototyping

---

## 7. ETL Implementation – PySpark Version

### 7.1 Technologies Used

* Python
* PySpark
* SQLite

### 7.2 ETL Workflow

#### Extract

* Reads CSV data using the Spark DataFrame API with automatic schema inference

#### Transform

* Filters records with missing values
* Renames columns using Spark transformations
* Drops unnecessary columns
* Applies business logic to compute the **Salary Hike** column

#### Load

* Converts the Spark DataFrame to a Pandas DataFrame
* Loads the final dataset into a SQLite database

### 7.3 Execution

```bash
python pyspark_etl.py
```

### 7.4 Use Case

This implementation demonstrates:

* Scalable ETL design principles
* Distributed-style data processing
* Readiness for enterprise platforms such as Databricks, Airflow, and Snowflake

---

## 8. Week 8 Capstone Alignment

| Week 8 Activity | Implementation Details             |
| --------------- | ---------------------------------- |
| Day 1           | Dataset selection and ETL design   |
| Day 2           | Data extraction from CSV           |
| Day 3           | Data transformation and enrichment |
| Day 4           | Loading data into SQLite database  |
| Day 5           | End-to-end automated ETL pipeline  |

---

## 9. Learning Outcomes

Through this capstone project, the following skills were developed:

* Practical understanding of ETL pipelines
* Data cleaning and transformation using Pandas and PySpark
* Database integration using SQLite
* Writing structured, reusable, and maintainable code
* Understanding the trade-offs between Pandas and PySpark

---

## 10. Conclusion

This capstone project successfully demonstrates the implementation of an end-to-end ETL pipeline using two different processing approaches.
The Pandas-based solution highlights simplicity and ease of use, while the PySpark-based solution introduces scalability and enterprise-level data processing concepts.

Together, these implementations provide a strong foundation in modern data engineering practices.

---
