while True:
    edad = int(input("Ingrese aquí su edad --> "))
    
    if edad < 3:
        print("Usted tiene entrada gratuita. Disfrute de la función.")
        
    elif edad >= 3 and edad <= 12:
        print("Su entrada cuesta $10. Disfrute de la función.")
        
    else:
        print("Su entrada cuesta $15. Disfrute de la función.")
    print()