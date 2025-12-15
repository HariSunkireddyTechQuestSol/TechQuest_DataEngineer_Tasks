from uploader import upload_to_cloud
from cloud_reader import list_cloud_files
from etl_process import etl_process

def run_simulation():
    print("\n=== SIMULATED S3 + ETL PIPELINE ===")

    print("\n[1] Uploading files to cloud/")
    upload_to_cloud()

    print("\n[2] Listing cloud/ files")
    list_cloud_files()

    print("\n[3] Running ETL")
    final_df = etl_process()

    print("\nPipeline complete!")
    print(final_df.head())

if __name__ == "__main__":
    run_simulation()
