def insertion_sort(lista):
    longitud_lista = len(lista)

    for i in range(1, longitud_lista):
        indice_insercion = i
        valor_actual = lista[i]

        for j in range(i - 1, -1, -1):
            if lista[j] > valor_actual:
                lista[j + 1] = lista[j]
                indice_insercion = j

            else:
                break

        lista[indice_insercion] = valor_actual

    return lista

insertion_sort([1, 0, 4, 5, 3])