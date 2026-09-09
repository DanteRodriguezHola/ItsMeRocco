from pathlib import Path

primer_libro = Path("the princess and the tiger.txt")
segundo_libro = Path("pride and prejudice.txt")
tercer_libro = Path("of the just shaping of letters.txt")

libros = [primer_libro, segundo_libro, tercer_libro]

for libro in libros:
    contenido = libro.read_text()
    the_cantidad = contenido.lower().count("the ")
    print(f"Cantidad de veces que aparece 'the' en {libro}: {the_cantidad}")