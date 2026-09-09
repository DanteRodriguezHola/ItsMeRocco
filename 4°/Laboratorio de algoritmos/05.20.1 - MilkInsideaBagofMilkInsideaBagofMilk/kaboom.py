def kaboom(numero):
    if numero < 0:
        print("¡Kaboom!")

    else:
        print(numero)

        kaboom(numero - 1)

kaboom(1)