usuarios_actuales = [
    "GuitarHero",
    "Estudiante del Huergo",
    "SkibidiPomni",
    "user666",
    "Mr. Game & Watch",
]

usuarios_nuevos = [
    "VVVinesauce",
    "DantBasura",
    "hhhherrrrooo",
    "game and watch",
    "USER666",
    "Huergo del Estudiante",
    "skibidiPOMNI",
]

for usuario_nuevo in usuarios_nuevos:
    for usuario_actual in usuarios_actuales:
        if usuario_nuevo.lower() == usuario_actual.lower():
            existe = True
            break

        else:
            existe = False
    
    if existe:
        print(f"'{usuario_nuevo}' ya esta en uso. Consíguete la tuya.")
    else:
        print(f"¡'{usuario_nuevo}' te queda como anillo al dedo!")