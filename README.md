# Proyecto de ETL Local Pandas
Este proyecto tiene como objetivo principal descargar, transformar y limpiar datos desde diversas fuentes web, guardarlos localmente en archivos CSV, y procesarlos utilizando Pandas para realizar análisis y preparar los datos para usos posteriores.
![](https://github.com/Echeverria29/Proyecto-de-ETL-Local-Pandas/blob/main/1_UUiMc7cdMV0YT9T8zcxgEQ.jpg)
# Descripción del Proyecto 🚀
El proyecto consiste en descargar archivos desde fuentes externas (APIs y páginas web), realizar transformaciones sobre los datos, y guardarlos en formato CSV en el escritorio local. Además, se ejecuta un proceso de limpieza de datos eliminando duplicados y valores nulos para preparar los archivos para su análisis posterior.

# Arquitectura de la Solución 🏗️
Pandas: Utilizado para procesar y limpiar los datos.
Requests: Para descargar los archivos desde fuentes web.
BeautifulSoup: Para extraer enlaces de descarga desde una página web.
OS y glob: Para manejo de archivos y carpetas locales.
CSV y Excel: Como formatos principales de entrada y salida.
Archivos de Código
Función: download_and_save_as_csv
Esta función descarga archivos Excel desde una URL y los convierte a formato CSV, guardando el archivo CSV en la carpeta especificada. Posteriormente elimina el archivo Excel original para ahorrar espacio en el disco.
![](https://github.com/Echeverria29/Proyecto-de-ETL-Local-Pandas/blob/main/Aquitectura3.drawio.png)
# Pre-requisitos 📋
Python 3.x: Para ejecutar el código y utilizar las bibliotecas.
Pandas: Biblioteca principal para manipulación de datos.
Requests: Para manejar las solicitudes HTTP.
BeautifulSoup: Para hacer scraping de páginas web.
OS y glob: Para manejo de archivos locales.
# Instalación 🔧
Asegúrate de tener instaladas las bibliotecas necesarias con el siguiente comando:
bash
Copiar código
pip install pandas requests beautifulsoup4
Configura las rutas locales donde se descargarán y guardarán los archivos CSV y Excel.
# Ejecución del Proyecto ⚙️
Descargar y Convertir: Ejecuta la función download_and_save_as_csv para descargar archivos Excel y guardarlos como CSV.
Procesar APIs: Ejecuta obtener_datos para consultar APIs y almacenar los datos en formato CSV.
Web Scraping: Ejecuta function_data3_local para extraer archivos ZIP desde la web, descomprimirlos y convertirlos.
Limpieza de Datos: Ejecuta clean_and_save para eliminar duplicados y filas con valores nulos de los archivos.
# Construido con 🛠️
Pandas - Para manipulación y limpieza de datos.
Requests - Para realizar solicitudes HTTP.
BeautifulSoup - Para hacer scraping de enlaces en páginas web.
OS y glob - Para manejo de archivos y directorios locales.
# Autor ✒️
Orlando Echeverría Hernández
Expresiones de Gratitud 🎁
Comparte este proyecto con otros.
