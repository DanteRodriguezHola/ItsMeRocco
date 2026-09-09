def particion(lista, bajo, alto):
    pivote = lista[alto]
    i = bajo - 1

    for j in range(bajo, alto):
        if lista[j] <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[alto] = lista[alto], lista[i + 1]

    return i + 1

def quick_sort(lista, bajo = 0, alto = None):
    if alto == None:
        alto = len(lista) - 1

    if bajo < alto:
        indice_pivote = particion(lista, bajo, alto)
        
        quick_sort(lista, bajo, indice_pivote - 1)
        quick_sort(lista, indice_pivote + 1, alto)