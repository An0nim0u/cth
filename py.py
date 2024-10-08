import requests
import os
import json
from wifi import Cell

# URL del servidor
url = "https://5e75-186-166-142-157.ngrok-free.app "

def obtener_wifi():
    while True:
        # Obtenemos las celdas Wi-Fi disponibles
        celdas = Cell.all('wlan0')  # Asegúrate de que 'wlan0' es la interfaz correcta
        for celda in celdas:
            # En este caso, solo tomamos la primera celda (la más fuerte o conectada)
            if celda.signal:  # Si hay señal
                # Aquí, como un ejemplo, se obtienen las coordenadas de la red
                # Dependiendo de la aplicación, podrías obtener más información
                # sobre la red Wi-Fi, pero las coordenadas no se obtienen generalmente
                # directamente de una red Wi-Fi. 
                # En su lugar, se puede usar la dirección MAC para obtener la ubicación 
                # a través de una API externa, pero para fines de este código, sólo
                # se ilustrará el envío de datos ficticios.
                
                # Suponiendo que tenemos datos ficticios para latitud y longitud
                latitud = "12.345678"  # Coordenadas ficticias
                longitud = "98.765432"  # Coordenadas ficticias
                geolocalizacion = "Wi-Fi"

                enviar_datos(latitud, longitud, geolocalizacion)
                break  # Salimos del bucle después de obtener la primera celda
        time.sleep(10)  # Esperar un tiempo antes de la siguiente consulta

def enviar_datos(latitud, longitud, geolocalizacion):
    payload = {
        'latitud': latitud,
        'longitud': longitud,
        'geolocalizacion': geolocalizacion
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Datos enviados con éxito.")
        else:
            print(f"Error al enviar datos: {response.status_code}")
    except Exception as e:
        print(f"Error en la solicitud: {e}")

if __name__ == "__main__":
    obtener_wifi()
