from pathlib import Path
import json

archivo = Path("numero.json")

while True:
    try:
        numero = float(input("Ingrese su numero favorito --> "))

    except ValueError:
        print("Debe ingresar un numero.\n")

    else:
        numero = json.dumps(numero)
        archivo.write_text(numero)
        break