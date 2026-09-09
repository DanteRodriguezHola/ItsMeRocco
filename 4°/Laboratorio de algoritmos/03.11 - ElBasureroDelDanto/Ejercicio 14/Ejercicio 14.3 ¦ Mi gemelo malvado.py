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

usuarios_minusculas = usuarios_actuales.copy()

for indice in range(len(usuarios_minusculas)):
    usuarios_minusculas[indice] = usuarios_minusculas[indice].lower()

for usuario_nuevo in usuarios_nuevos:
    if usuario_nuevo.lower() in usuarios_minusculas:
        print(f"'{usuario_nuevo}' ya esta en uso. Consíguete la tuya.")

    else:
        print(f"¡'{usuario_nuevo}' te queda como anillo al dedo!")