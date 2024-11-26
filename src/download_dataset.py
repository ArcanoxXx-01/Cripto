import os
from kaggle.api.kaggle_api_extended import KaggleApi

os.environ["KAGGLE_CONFIG_DIR"] ="/home/dario/Escritorio/Projects/3º/Cripto/.kaggle/kaggle.json"

api = KaggleApi()
api.authenticate()

dataset_name = "odins0n/crypto-price-interactive-dashboard-daily-update"
destination_folder = "/home/dario/Escritorio/Projects/3º/Cripto/db"

# Descargar el dataset y descomprimirlo
api.dataset_download_files(dataset_name, path=destination_folder, unzip=True)

print(f"Dataset descargado y extraído en {destination_folder}")
