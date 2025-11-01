import os
from kaggle.api.kaggle_api_extended import KaggleApi

DATASET = "maharshipandya/-spotify-tracks-dataset"
OUTPUT_DIR = os.path.join("data", "raw")

def download_spotify_data():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    print(f"Downloading {DATASET} into {OUTPUT_DIR}...")

    api = KaggleApi()
    api.authenticate()  # reads kaggle.json automatically
    api.dataset_download_files(DATASET, path=OUTPUT_DIR, unzip=True)

    print("Download complete!")

if __name__ == "__main__":
    download_spotify_data()
