from obtener_datos_venta import *

from csv import reader
from os import path

def leer_ventas(nombre_archivo):
    if not path.exists(nombre_archivo):
        print(f"No se encontro el archivo '{nombre_archivo}'.")
        return
    
    try:
        with open(nombre_archivo, encoding = "utf-8", newline = "") as archivo_csv:
            contenido = list(reader(archivo_csv))

            encabezado = ["titulo", "genero", "precio", "cantidad"]
            contenido.remove(encabezado)

            ventas = []

            for linea in contenido:
                venta = obtener_venta(linea)
                ventas.append(venta)

            return ventas
    
    except UnicodeDecodeError:
        print("El archivo utiliza un encodificación distinta a utf-8.")
        return

def obtener_venta(venta):
    venta = {
        "titulo": obtener_titulo(venta),
        "genero": obtener_genero(venta),
        "precio": obtener_precio(venta),
        "cantidad": obtener_cantidad(venta),
    }

    return venta