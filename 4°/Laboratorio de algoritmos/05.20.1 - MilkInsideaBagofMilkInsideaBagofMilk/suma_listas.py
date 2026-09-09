def sumar_lista(lista):
    longitud_lista = len(lista)
    
    if longitud_lista == 1:
        return lista[0]
    
    else:
        mitad_lista = longitud_lista // 2
        
        primera_mitad = lista[ : mitad_lista]
        segunda_mitad = lista[mitad_lista : ]

        return sumar_lista(primera_mitad) + sumar_lista(segunda_mitad)
    
sumar_lista([])
    

    