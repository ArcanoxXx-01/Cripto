import os
import pandas as pd

def merge():
    """
    Devuelve la unión de todos los csv presentes en 'db' en un nuevo archivo 'merge.csv' después de guradarlo en './db/merge'
    """

    # Ruta donde están los CSV
    folder_path = './db'

    # Combinar todos los CSV en un solo DataFrame
    dataframes = []
    for file in os.listdir(folder_path):
        if file.endswith('.csv'):
            df = pd.read_csv(os.path.join(folder_path, file))
            dataframes.append(df)

    # Concatenar los DataFrames
    merged_df = pd.concat(dataframes, ignore_index=True)

    merged_df.to_csv('./db/merge/merge.csv',index=False)
    
    return merged_df