import os
import shutil

def upload_to_cloud(local_folder="data", cloud_folder="cloud"):
    os.makedirs(cloud_folder, exist_ok=True)

    for file in os.listdir(local_folder):
        src = os.path.join(local_folder, file)
        dst = os.path.join(cloud_folder, file)

        if os.path.isfile(src):
            shutil.copy(src, dst)
            print(f"Uploaded: {file}")

if __name__ == "__main__":
    upload_to_cloud()
