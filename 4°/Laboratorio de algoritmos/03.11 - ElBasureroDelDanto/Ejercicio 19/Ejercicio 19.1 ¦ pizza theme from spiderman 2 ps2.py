ingrediente = ""

while ingrediente != "salir":
    if ingrediente:
        print(f"\nEntendido. Su pizza ahora tiene {ingrediente.lower()}.\n")
    
    print("Ingrese un ingrediente que quiera añadir a su pizza.\nIngrese 'salir' para finalizar.\n\n")
    ingrediente = input("Ingrese aquí --> ")