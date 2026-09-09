#
# BÚSQUEDA LINEAL
# 
# Cantidad de operaciones: 2n + 1
# 
# #

def busqueda_lineal(lista, elemento_buscado):
    for elemento in lista:
        if elemento == elemento_buscado:
            return True
        
    return False