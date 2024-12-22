# Proyecto de Descarga, Transformación y Limpieza de Datos

Este proyecto tiene como objetivo descargar archivos desde fuentes externas (APIs y páginas web), realizar transformaciones sobre los datos y guardarlos en formato CSV en el escritorio local. Además, se ejecuta un proceso de limpieza de datos eliminando duplicados y valores nulos para preparar los archivos para su análisis posterior.
![](https://github.com/Echeverria29/Proyecto-de-ETL-Local-Pandas/blob/main/images/1_UUiMc7cdMV0YT9T8zcxgEQ.jpg)

## Contenido
- [Requisitos](#requisitos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instrucciones de Ejecución](#instrucciones-de-ejecución)

---

## Requisitos

Para ejecutar este proyecto de manera local, asegúrate de tener instalados los siguientes paquetes:

- **pandas**: Para manipulación y limpieza de datos  
- **requests**: Para realizar solicitudes HTTP  
- **beautifulsoup4**: Para hacer scraping en páginas web  
- **os y glob**: Para manejo de archivos y carpetas locales  

Instala todas las dependencias con:

$ pip install -r requirements.txt

## Estructura del Proyecto
El proyecto está organizado de la siguiente manera:

- **arquitecture/**
    Arquitecura del proyecto:
    - `Arquitectura3.drawio.png` 

- **data/**
    Archivos relacionados con datasets:
    - `csv y excel descargados.rar` 
    - `csv y excel limpios.rar` 

- **images/**
    Imagenes del proyecto:
    - `1_UUiMc7cdMV0YT9T8zcxgEQ.jpg` 
    
- **scripts/**  
  Scripts Python del proyecto:  
  - `des_excel_csv.py` - Descargar y Convertir Archivos  
  - `diarios_general_csvunido.py` - Procesar APIs  
  - `web_scraping.py` - Web Scraping  
  - `limpieza_datos.py` -  Limpieza de Datos 



## Instrucciones de Ejecución

## Descargar y Convertir Archivos
Ejecuta el script des_excel_csv.py para descargar archivos Excel desde una URL, convertirlos a CSV y guardarlos en la carpeta especificada:
python scripts/des_excel_csv.py

## Procesar APIs
Ejecuta el script para consultar datos desde APIs y almacenarlos en formato CSV:
python scripts/diarios_general_csvunido.py

## Web Scraping
Ejecuta web_scraping.py para descargar archivos ZIP desde una página web y convertirlos a CSV:
python scripts/web_scraping.py

## Limpieza de Datos
Limpia los archivos CSV eliminando duplicados y filas con valores nulos con el siguiente comando:
python scripts/limpieza_datos.py
