def selection_sort(lista):
    tamano_lista = len(lista)

    for i in range(tamano_lista):
        indice_menor = i

        for j in range(i + 1, tamano_lista):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

    return lista