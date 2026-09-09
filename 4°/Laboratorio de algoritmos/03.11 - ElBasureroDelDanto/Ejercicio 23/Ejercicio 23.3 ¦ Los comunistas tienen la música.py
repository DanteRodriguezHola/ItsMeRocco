def hacer_album(titulo, artista, canciones = None):
    album = {
        "titulo": titulo,
        "artista": artista,
        }
    
    if canciones:
        album.update({"canciones": canciones})
        
    return album

preguntando = True

while preguntando:
    titulo = input("Ingrese el titulo del álbum --> ")
    artista = input("Ingrese el artista del álbum --> ")
    print()
    
    album = hacer_album(titulo, artista)
    print(album, end = "\n\n")
    
    respuesta = input("¿Desea continuar? (si/no) --> ")
    print()
    
    if respuesta.lower() == "no":
        preguntando = False
    