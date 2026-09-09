# 
# BÚSQUEDA BINARIA
# 
# Cantidad de operaciones: log₂n
# 
# #


def busqueda_binaria(lista_ordenada, elemento_buscado):
    primer_indice = 0 # 1
    ultimo_indice = len(lista_ordenada)

    while primer_indice <= ultimo_indice:
        mitad_lista = (primer_indice + ultimo_indice) // 2

        elemento_medio = lista_ordenada[mitad_lista]

        if elemento_medio == elemento_buscado:
            return True
        
        elif elemento_medio < elemento_buscado:
            primer_indice = mitad_lista + 1

        elif elemento_medio > elemento_buscado:
            ultimo_indice = mitad_lista - 1

    return False