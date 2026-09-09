lenguajes_favoritos = {
    "juan": "python",
    "sara": "c",
    "eduardo": "rust",
    "agustina": "c#",
    }

encuesta = [
        "eduardo",
        "john",
        "filemon",
        "agustina",
        "juan",
        "benjamin",
        "santino",
        "lucia",
        "beto",
        "sara",
        "franco",
        "marcos"
    ]

for encuestado in encuesta:
    if encuestado in lenguajes_favoritos.keys():
        print(f"Gracias por responder que tu lenguaje favorito era {lenguajes_favoritos[encuestado].title()}, {encuestado.title()}.\nNos vemos pronto.")
    
    else:
        print(f"{encuestado.title()}, te invitamos a responder cual es tu lenguaje favorito. ¡Nos vemos muy pronto!")
    print()