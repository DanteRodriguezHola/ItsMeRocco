from generar_informe import generar_informe

from sys import argv

if __name__ == "__main__":
    try:
        nombre_archivo_csv = argv[1]

    except IndexError:
        print("No se proporciono un archivo .csv para analizar.")

    else:
        generar_informe(nombre_archivo_csv)