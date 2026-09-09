ingrediente = ""

while ingrediente != "salir":
    if ingrediente:
        print(f"\nEntendido. Su pizza ahora tiene {ingrediente.lower()}.\n")
    
    print("Ingrese un ingrediente que quiera añadir a su pizza.\nIngrese 'salir' para finalizar.\n\n")
    ingrediente = input("Ingrese aquí --> ")

ingresos = 0

while ingresos < 3:
    edad = int(input("Ingrese aquí su edad --> "))
    
    if edad < 3:
        print("Usted tiene entrada gratuita. Disfrute de la función.")
        
    elif edad >= 3 and edad <= 12:
        print("Su entrada cuesta $10. Disfrute de la función.")
        
    else:
        print("Su entrada cuesta $15. Disfrute de la función.")

    ingresos += 1
    print()
    
ingrediente = ""

while True:
    if ingrediente == "salir":
        break
    
    if ingrediente:
        print(f"\nEntendido. Su pizza ahora tiene {ingrediente.lower()}.\n")

    print("Ingrese un ingrediente que quiera añadir a su pizza.\nIngrese 'salir' para finalizar.\n\n")
    ingrediente = input("Ingrese aquí --> ")
