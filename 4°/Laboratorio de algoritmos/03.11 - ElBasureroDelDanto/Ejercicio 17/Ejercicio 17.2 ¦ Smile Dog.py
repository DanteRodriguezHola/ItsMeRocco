gary_info = {
    "nombre": "Gary",
    "animal": "Caracol",
    "duenio": "Bob Esponja"
}

louie_info = {
    "nombre": "Louie",
    "animal": "Perro",
    "duenio": "Sabrina Carpenter"
}

tiro_al_blanco_info = {
    "nombre": "Tiro al Blanco",
    "animal": "Caballo",
    "duenio": "Woody"
}

mascotas = [gary_info, louie_info, tiro_al_blanco_info]

for mascota in mascotas:
    for dato, info in mascota.items():
        print(f"- {dato.capitalize()}: {info}")
    print()