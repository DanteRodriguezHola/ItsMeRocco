def construir_perfil(nombre, apellido, **info_usuario):
    info_usuario["nombre"] = nombre
    info_usuario["apellido"] = apellido
    
    return info_usuario

perfil_dante = construir_perfil("Dante", "Rodriguez",
                                apodo = "DantSteam",
                                personalidad = "perdedor",
                                banda_favorita = "They Might Be Giants"
                                )

print(perfil_dante)