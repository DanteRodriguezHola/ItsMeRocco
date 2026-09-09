from pathlib import Path

learning_python = Path("learning_python.txt")
contenido = learning_python.read_text()
lineas = contenido.splitlines()

for linea in lineas:
    mensaje = linea.replace("Python", "Javascript")
    print(mensaje)