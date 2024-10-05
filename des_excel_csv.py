from urllib.parse import urlparse, parse_qs
from os import path, makedirs
import requests
import pandas as pd
import os

def download_and_save_as_csv(url, file_name):
    try:
        # Realizar la solicitud GET para obtener el archivo Excel
        response = requests.get(url)
        response.raise_for_status()  # Asegurarse de que la solicitud fue exitosa

        # Guardar el contenido del archivo Excel en disco
        with open(file_name, 'wb') as f:
            f.write(response.content)
        
        # Cargar el archivo Excel en un DataFrame de Pandas
        df = pd.read_excel(file_name)

        # Guardar el DataFrame como archivo CSV
        csv_file = file_name.replace('.xlsx', '.csv')  # Nombre de archivo CSV
        df.to_csv(csv_file, index=False)  # Guardar DataFrame como CSV
        
        # Eliminar el archivo Excel para conservar solo el CSV
        os.remove(file_name)

        return f"Archivo {file_name} descargado y guardado como {csv_file} en tu escritorio."

    except Exception as e:
        return f"Error al descargar o convertir el archivo {file_name}: {str(e)}"

# URLs de los archivos Excel y nombres de archivo locales
excel_link1 = "https://drive.google.com/uc?export=download&id=1oMR_0jfwsykVS0Eci6qqnBSg3MqGLGrv"
excel_link2 = "https://drive.google.com/uc?export=download&id=13YIuilBbmgo-f3Nn5XTPX-hMRfpvXUCc"

file_name1 = "colectivos.xlsx"
file_name2 = "metro.xlsx"

# Verificar si el directorio existe, si no, crearlo
folder_path = r'TU_URL'
if not path.exists(folder_path):
    makedirs(folder_path)

# Descargar y convertir el primer archivo Excel a CSV
result1 = download_and_save_as_csv(excel_link1, path.join(folder_path, file_name1))
print(result1)

# Descargar y convertir el segundo archivo Excel a CSV
result2 = download_and_save_as_csv(excel_link2, path.join(folder_path, file_name2))
print(result2)
