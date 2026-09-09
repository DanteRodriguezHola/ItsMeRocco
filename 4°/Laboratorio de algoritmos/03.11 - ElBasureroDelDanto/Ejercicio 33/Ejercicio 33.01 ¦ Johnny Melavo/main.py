from pathlib import Path

archivo = Path("guest.txt")
nombre = input("Ingrese su nombre --> ").title()
archivo.write_text(nombre)