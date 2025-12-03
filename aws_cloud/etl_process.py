import os
import pandas as pd

def etl_process(cloud_folder="cloud", report_folder="reports"):
    os.makedirs(report_folder, exist_ok=True)
    aggregated = []

    for file in os.listdir(cloud_folder):
        if file.endswith(".csv"):
            path = os.path.join(cloud_folder, file)
            df = pd.read_csv(path)

            df["source_file"] = file
            df["row_total"] = df.select_dtypes("number").sum(axis=1)

            aggregated.append(df)
            print(f"Processed: {file}")

    final_df = pd.concat(aggregated)
    output_path = os.path.join(report_folder, "final_report.csv")
    final_df.to_csv(output_path, index=False)

    print(f"ETL complete → {output_path}")
    return final_df

if __name__ == "__main__":
    etl_process()
