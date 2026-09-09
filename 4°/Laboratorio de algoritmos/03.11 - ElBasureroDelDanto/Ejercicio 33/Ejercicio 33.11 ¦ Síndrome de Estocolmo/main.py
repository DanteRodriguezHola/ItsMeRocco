from pathlib import Path
import json

def obtener_usuario_guardado(path):
    if path.exists():
        contenido = path.read_text()
        info_usuario = json.loads(contenido)
        return info_usuario
    
    else:
        return None

def obtener_nuevo_usuario(path):
    info_usuario = {
        "nombre": input("Ingrese su nombre --> "),
        "edad": input("Ingrese su edad --> "),
        "pais": input("Ingrese su país --> "),
    }

    contenido = json.dumps(info_usuario)
    path.write_text(contenido)
    return info_usuario

def preguntar_usuario_correcto(info_usuario):
    print(f"¿Es este tu nombre de usuario correcto? {info_usuario['nombre']}")

    respuesta = input("Ingrese aquí (sí/no) --> ")

    if respuesta.lower() == "no":
        return False
    
    else:
        return True

def saludar_usuario():
    path = Path('username.json')
    info_usuario = obtener_usuario_guardado(path)

    if info_usuario:
        usuario_correcto = preguntar_usuario_correcto(info_usuario)

        if usuario_correcto:
            print("¡Bienvenido usuario!\nEsto es lo que me acuerdo de tí:")
            for dato, valor in info_usuario.items():
                print(f"- {dato.capitalize()}: {valor.title()}")
        else:
            info_usuario = obtener_nuevo_usuario(path)
            print(f"\nTe vamos a recordar cuando vuelvas, {info_usuario['nombre']}.")
    else:
        info_usuario = obtener_nuevo_usuario(path)
        print(f"\nTe vamos a recordar cuando vuelvas, {info_usuario['nombre']}.")

saludar_usuario()