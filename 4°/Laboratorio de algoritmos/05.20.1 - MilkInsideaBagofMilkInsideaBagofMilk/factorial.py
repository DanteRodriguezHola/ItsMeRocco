def factorial(numero):
    if numero == 0:
        return 1
    
    elif numero <= 2:
        return numero

    else:
        return numero * factorial(numero - 1)
