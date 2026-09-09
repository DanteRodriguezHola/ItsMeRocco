from pathlib import Path

guest_book = Path("guest_book.txt")

nombre = ""
nombres = ""

while nombre.lower() != "salir":
    if nombre:
        nombres += nombre.title() + "\n"
    
    print("Ingrese su nombre.\nIngrese 'salir' para finalizar el programa.\n")

    nombre = input("Ingrese aquí --> ")
    print()

guest_book.write_text(nombres)