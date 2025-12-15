from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("ReadCSV").getOrCreate()

    df = spark.read.csv("../input/data.csv", header=True, inferSchema=True)

    print("=== Preview ===")
    df.show(5)

    spark.stop()

if __name__ == "main":
   main()