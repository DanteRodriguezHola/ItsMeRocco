while True:
    try:
        primer_numero = int(input("Ingrese un número entero --> "))
        segundo_numero = int(input("Ingrese otro número entero --> "))

    except ValueError as VE:
        print("\nbro realmente no sabe usar la computadora")
        print(f"Error: {VE}\n")

    else:
        suma = primer_numero + segundo_numero
        print(f"\nResultado de la suma: {suma}\n")