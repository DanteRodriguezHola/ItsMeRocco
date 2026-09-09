from pathlib import Path

learning_python = Path("learning_python.txt")
contenido = learning_python.read_text()
print(contenido)
print()

lineas = contenido.splitlines()
for linea in lineas:
    print(linea)