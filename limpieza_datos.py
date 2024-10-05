import pandas as pd
import os
from glob import glob

# Rutas de las carpetas donde se encuentran los archivos CSV y Excel
folder_path1 = r'TU_URL'
folder_path2 = r'TU_URL'
folder_path3 = r'TU_URL'

# Carpeta donde se guardarán los archivos limpios
output_folder = r'TU_URL'

# Función para limpiar y guardar archivos CSV o Excel como CSV
def clean_and_save(file_path, output_folder):
    try:
        # Leer archivo CSV o Excel
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file_path)
        else:
            print(f"El archivo {file_path} no es compatible (debe ser CSV o Excel).")
            return
        
        # Eliminar duplicados basados en todas las columnas
        df.drop_duplicates(inplace=True)
        
        # Eliminar filas con valores nulos
        df.dropna(inplace=True)
        
        # Obtener el nombre del archivo sin la extensión
        file_name, file_extension = os.path.splitext(os.path.basename(file_path))
        
        # Construir el nombre del archivo limpio en formato CSV
        clean_file_name = f"{file_name}_CLEAN.csv"
        
        # Ruta de guardado del archivo limpio en la carpeta de salida
        clean_file_path = os.path.join(output_folder, clean_file_name)
        
        # Guardar el DataFrame limpio como CSV
        df.to_csv(clean_file_path, index=False)
        
        print(f"Archivo limpio guardado en: {clean_file_path}")
    
    except Exception as e:
        print(f"Error al procesar el archivo {file_path}: {e}")

# Función para verificar y crear el directorio de salida si no existe
def create_output_folder(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Creado directorio de salida: {output_folder}")
    else:
        print(f"Directorio de salida existente: {output_folder}")

# Verificar y crear el directorio de salida si no existe
create_output_folder(output_folder)

# Lista de carpetas y extensiones para buscar
folders_and_extensions = [
    (folder_path1, '*.csv', '*.xls*'),
    (folder_path2, '*.csv', '*.xls*'),
    (folder_path3, '*.csv', '*.xls*')
]

# Iterar sobre cada carpeta y extensiones para buscar archivos
for folder, csv_ext, excel_ext in folders_and_extensions:
    # Verificar si la carpeta existe y buscar archivos
    if os.path.exists(folder):
        csv_files = glob(os.path.join(folder, csv_ext))
        excel_files = glob(os.path.join(folder, excel_ext))

        # Mostrar los archivos encontrados en cada carpeta
        print(f"Archivos CSV encontrados en {folder}: {len(csv_files)}")
        print(f"Archivos Excel encontrados en {folder}: {len(excel_files)}")

        # Llamar a la función para limpiar y guardar cada archivo CSV encontrado
        for file_path in csv_files:
            clean_and_save(file_path, output_folder)

        # Llamar a la función para limpiar y guardar cada archivo Excel encontrado
        for file_path in excel_files:
            clean_and_save(file_path, output_folder)
    else:
        print(f"Carpeta {folder} no encontrada.")

