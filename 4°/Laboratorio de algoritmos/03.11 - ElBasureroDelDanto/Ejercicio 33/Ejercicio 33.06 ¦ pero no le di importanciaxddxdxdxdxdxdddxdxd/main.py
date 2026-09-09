from pathlib import Path

archivo_perros = Path("perros.txt")
archivo_gatos = Path("gatos.txt")

archivos_mascotas = [archivo_perros, archivo_gatos]

for archivo in archivos_mascotas:
    try:
        contenido = archivo.read_text()
        print(contenido, end = "\n\n")
    
    except FileNotFoundError as FNFE:
        pass