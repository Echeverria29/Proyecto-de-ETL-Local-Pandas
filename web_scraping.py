import requests
from bs4 import BeautifulSoup
import zipfile
from io import BytesIO
import os
import csv
import pandas as pd

def function_data3_local():
    # URL de la página web
    url = "https://www.dtpm.cl/index.php/noticias/gtfs-vigente"

    # Realizar la solicitud GET para obtener el contenido de la página
    response = requests.get(url)
    response.raise_for_status()  # Asegurarse de que la solicitud fue exitosa

    # Analizar el contenido HTML de la página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar el enlace del archivo ZIP
    zip_link = soup.find('a', string='GTFS')['href']
    zip_url = "https://www.dtpm.cl" + zip_link

    # Descargar el archivo ZIP
    zip_response = requests.get(zip_url)
    zip_response.raise_for_status()  # Asegurarse de que la solicitud fue exitosa

    # Directorio donde se guardarán los archivos descargados y descomprimidos
    output_dir = r"C:\Users\josue\Desktop\descarga datos\csv y excel descargados\webscraping"
    os.makedirs(output_dir, exist_ok=True)

    # Guardar el archivo ZIP descargado
    zip_filename = os.path.join(output_dir, "gtfs_data.zip")
    with open(zip_filename, "wb") as zip_file:
        zip_file.write(zip_response.content)

    # Descomprimir el archivo ZIP
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
        extracted_files = zip_ref.namelist()  # Obtener lista de archivos descomprimidos dentro del bloque

    # Contadores para archivos encontrados y convertidos
    total_files = len(extracted_files)
    excel_count = 0
    csv_count = 0
    txt_count = 0
    converted_count = 0

    # Convertir archivos a CSV si son archivos de texto
    for file_name in extracted_files:
        file_path = os.path.join(output_dir, file_name)

        if file_name.lower().endswith('.txt'):
            # Leer el archivo de texto
            df = pd.read_csv(file_path, sep='\t')

            # Crear nombre de archivo CSV
            csv_filename = os.path.splitext(file_name)[0] + '.csv'
            csv_path = os.path.join(output_dir, csv_filename)

            # Guardar como CSV con separador ','
            df.to_csv(csv_path, index=False, sep=',')
            converted_count += 1
            txt_count += 1

        elif file_name.lower().endswith('.xlsx') or file_name.lower().endswith('.xls'):
            # Si es un archivo Excel, contar pero no convertir
            excel_count += 1

        elif file_name.lower().endswith('.csv'):
            # Si es un archivo CSV, contar pero no convertir
            csv_count += 1

    # Eliminar el archivo ZIP después de procesar todos los archivos
    os.remove(zip_filename)

    # Eliminar archivos Excel y TXT después de procesar todos los archivos
    for file_name in extracted_files:
        if file_name.lower().endswith('.xlsx') or file_name.lower().endswith('.xls') or file_name.lower().endswith('.txt'):
            file_path = os.path.join(output_dir, file_name)
            os.remove(file_path)

    # Crear el mensaje de resumen
    summary_message = f"""
    Archivos encontrados:
    - Total: {total_files}
    - Excel: {excel_count}
    - CSV: {csv_count}
    - TXT: {txt_count}

    Archivos convertidos a CSV: {converted_count}
    """

    return summary_message.strip()

# Llamada a la función para ejecutar localmente
if __name__ == "__main__":
    result = function_data3_local()
    print(result)
