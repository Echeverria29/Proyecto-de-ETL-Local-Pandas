import csv
import requests
from os import path, makedirs
import time
from urllib.parse import urlparse, parse_qs

# Lista de URLs a consultar
urls = [
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=124",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=205c",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=210",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=213e",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=712",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=F01",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=F01c",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=F03",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=F03c",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=F10",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=F10c",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=F11",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=F12",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=F12c",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=F13",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=F14",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=F16",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=F18",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=F29",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=F30n",
    "https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=F33"
]

# Códigos a buscar dentro de los paraderos
codigos_buscar = ["PF88", "PF725", "PF176", "PF94", "PF960", "PF512", "PF212"]

max_retries = 3      # Número máximo de intentos
retry_delay = 10     # Tiempo de espera entre intentos en segundos

def obtener_datos(url):
    intentos = 0
    while intentos < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al realizar la solicitud a la API '{url}': {e}")
            intentos += 1
            print(f"Intento {intentos}/{max_retries}. Reintentando en {retry_delay} segundos...")
            time.sleep(retry_delay)
        except ValueError as ve:
            print(f"Error al decodificar JSON de la respuesta de la API '{url}': {ve}")
            return None

    print(f"No se pudo obtener datos de la API '{url}' después de {max_retries} intentos.")
    return None

try:
    escritorio = path.expanduser("~")  # Ruta al directorio de escritorio del usuario actual
    folder_path = r'TU_URL'
    archivo_salida = path.join(folder_path, "all_recorridos.csv")  # Ruta completa al archivo de salida

    headers = ["id", "cod", "pos_latitud", "pos_longitud", "name", "comuna", "servicio_id", "servicio_cod", "destino", "horarios"]

    # Crear directorio si no existe
    if not path.exists(folder_path):
        makedirs(folder_path)

    with open(archivo_salida, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)

        for url in urls:
            data = obtener_datos(url)

            if data:
                parsed_url = urlparse(url)
                query_params = parse_qs(parsed_url.query)
                codsint = query_params['codsint'][0]

                nombre_archivo = f"paraderos_{codsint}.csv"
                archivo_salida = path.join(folder_path, nombre_archivo)

                for sentido in ["ida", "regreso"]:
                    paraderos = data.get(sentido, {}).get("paraderos", [])

                    rows = []
                    for paradero in paraderos:
                        if paradero["codSimt"] in codigos_buscar:
                            for servicio in paradero["servicios"]:
                                # Obtener horarios para cada servicio si existen
                                if sentido in data and "horarios" in data[sentido]:
                                    horarios = data[sentido]["horarios"]
                                    # Convertir lista de horarios a texto separado por comas
                                    horarios_texto = ", ".join(f"{h['tipoDia']}: {h['inicio']}-{h['fin']}" for h in horarios)
                                else:
                                    horarios_texto = ""  # Si no hay horarios disponibles, dejar como cadena vacía

                                # Verificar si el servicio tiene un destino definido
                                destino = servicio.get("destino", "")

                                row = [
                                    paradero["id"],
                                    paradero["cod"],
                                    paradero["pos"][0],  # Latitud
                                    paradero["pos"][1],  # Longitud
                                    paradero["name"],
                                    paradero["comuna"],
                                    servicio["id"],
                                    servicio["cod"],
                                    destino,  # Incluir destino del servicio
                                    horarios_texto  # Incluir horarios como texto separado por comas
                                ]
                                rows.append(row)

                    if rows:
                        writer.writerows(rows)
                        print(f"Se han encontrado {len(rows)} paraderos en '{sentido}' para la URL '{url}'.")
                    else:
                        print(f"No se encontraron paraderos en '{sentido}' para la URL '{url}' con los códigos especificados.")

                print(f"Los datos de la URL '{url}' han sido agregados al archivo '{nombre_archivo}'.")
            else:
                print(f"No se pudieron obtener datos de la URL '{url}'.")

    print(f"Todos los datos han sido guardados en '{archivo_salida}'.")

except OSError as oe:
    print(f"Error de sistema operativo: {oe}")
except csv.Error as cse:
    print(f"Error al escribir el archivo CSV: {cse}")
except Exception as e:
    print(f"Error inesperado: {e}")
