from pathlib import Path
import json

archivo = Path("numero.json")

if archivo.exists():
    contenido = archivo.read_text()
    numero = json.loads(contenido)

    print(f"¡Conozco tu número favorito! Era el {numero}.")

else:
    print(f"No conozco tu número favorito... :/")