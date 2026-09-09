def hacer_album(titulo, artista, canciones = None):
    album = {
        "titulo": titulo,
        "artista": artista,
        }
    
    if canciones:
        album.update({"canciones": canciones})
        
    return album

primer_album = hacer_album("Lincoln", "They Might Be Giants")
segundo_album = hacer_album("Flying Beagle", "Himiku Kikuchi", 8)
tercer_album = hacer_album("Magical Mystery Tour", "The Beatles")

print(primer_album)
print(segundo_album)
print(tercer_album)