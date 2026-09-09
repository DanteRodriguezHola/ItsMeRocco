def bubble_sort(lista):
    tamano_lista = len(lista)

    for i in range(tamano_lista):
        intercambiado = False

        for j in range((tamano_lista - i) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True

        if not intercambiado:
            break

    return lista

