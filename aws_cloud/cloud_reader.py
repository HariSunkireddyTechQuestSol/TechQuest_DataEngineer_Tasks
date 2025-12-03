import os
import pandas as pd

def list_cloud_files(cloud_folder="cloud"):
    print("Files in cloud storage:")
    for f in os.listdir(cloud_folder):
        print(" -", f)

def read_cloud_file(filename, cloud_folder="cloud"):
    filepath = os.path.join(cloud_folder, filename)
    df = pd.read_csv(filepath)
    print(f"Read file: {filename}")
    return df

if __name__ == "__main__":
    list_cloud_files()
