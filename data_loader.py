import pandas as pd

def cargar_datos(file_path):
    df = pd.read_excel(file_path)
    df = df.dropna()
    return df