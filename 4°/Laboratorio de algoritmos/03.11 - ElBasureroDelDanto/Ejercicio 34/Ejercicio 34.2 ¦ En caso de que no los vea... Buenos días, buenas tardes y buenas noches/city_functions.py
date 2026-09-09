def devolver_ciudad_pais(ciudad, pais, poblacion = None):
    if poblacion:
        return f"{ciudad.title()}, {pais.title()} - Población: {poblacion}"
    else:
        return f"{ciudad.title()}, {pais.title()}"