from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, sum

def main():
    # 1. Create SparkSession
    spark = SparkSession.builder \
        .appName("CSV Processing Job") \
        .getOrCreate()

    # 2. Read CSV
    input_path = "../input/data.csv"
    df = spark.read.csv(input_path, header=True, inferSchema=True)

    # 3. Show schema
    print("=== Schema ===")
    df.printSchema()

    # 4. Select specific columns
    selected_df = df.select("id", "category", "amount", "score")

    # 5. Filter rows (example: amount > 50)
    filtered_df = selected_df.filter(col("amount") > 50)

    # 6. GroupBy + Aggregate
    agg_df = filtered_df.groupBy("category").agg(
        avg("score").alias("avg_score"),
        sum("amount").alias("total_amount")
    )

    print("=== Aggregated Data ===")
    agg_df.show()

    # 7. Save output DataFrame to CSV
    agg_df.write.mode("overwrite").csv("output/processed_csv", header=True)

    # 8. Save output DataFrame to JSON
    agg_df.write.mode("overwrite").json("output/processed_json")

    # Stop Spark session
    spark.stop()


if __name__ == "__main__":
    main()
