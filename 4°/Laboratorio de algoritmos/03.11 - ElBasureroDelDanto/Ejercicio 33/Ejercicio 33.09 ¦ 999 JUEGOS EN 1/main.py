from pathlib import Path
import json

archivo = Path("numero.json")

if archivo.exists():
    contenido = archivo.read_text()
    numero = json.loads(contenido)

    print(f"¡Conozco tu número favorito! Era el {numero}.")

else:
    while True:
        try:
            numero = float(input("Ingrese su numero favorito --> "))

        except ValueError:
            print("Debe ingresar un numero.\n")

        else:
            numero = json.dumps(numero)
            archivo.write_text(numero)
            break