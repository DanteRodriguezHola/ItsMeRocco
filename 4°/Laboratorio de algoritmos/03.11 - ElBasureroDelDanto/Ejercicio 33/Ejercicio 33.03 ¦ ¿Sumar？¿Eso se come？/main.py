try:
    primer_numero = int(input("Ingrese un número entero --> "))
    segundo_numero = int(input("Ingrese otro número entero --> "))

except ValueError as VE:
    print("\nERES UN MALDITO cabeza de chorlito. TE PEDÍ NUMEROS ENTEROS, NO TEXTO NI OTROS TIPOS DE NUMEROS. VOY A ASESINAR A TÍ Y A TODA TU FAMILIA en minecraft.")
    print(f"Error: {VE}")

else:
    suma = primer_numero + segundo_numero
    print(f"\nResultado de la suma: {suma}")