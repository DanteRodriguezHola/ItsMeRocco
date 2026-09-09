def propagar(vector_fosforos):
    NUEVO = 0
    ENCENDIDO = 1
    CARBONIZADO = -1

    primer_fosforo = 0
    penultimo_fosforo = len(vector_fosforos) - 1

    # Como el ultimo fosforo no tiene vecino proximo, se excluye.

    for indice_positivo in range(primer_fosforo, penultimo_fosforo, 1):
        fosforo_actual = vector_fosforos[indice_positivo]
        siguente_fosforo = vector_fosforos[indice_positivo + 1]

        if fosforo_actual == NUEVO or fosforo_actual == CARBONIZADO:
            continue

        elif fosforo_actual == ENCENDIDO:
            if siguente_fosforo == ENCENDIDO or siguente_fosforo == CARBONIZADO:
                continue

            elif siguente_fosforo == NUEVO:
                vector_fosforos[indice_positivo + 1] = ENCENDIDO

    ultimo_fosforo = len(vector_fosforos) - 1
    segundo_fosforo = 0

    # Como el primer fosforo no tiene vecino anterior, se excluye.

    for indice_negativo in range(ultimo_fosforo, segundo_fosforo, -1):
        fosforo_actual = vector_fosforos[indice_negativo]
        anterior_fosforo = vector_fosforos[indice_negativo - 1]

        if fosforo_actual == NUEVO or fosforo_actual == CARBONIZADO:
            continue

        elif fosforo_actual == ENCENDIDO:
            if anterior_fosforo == ENCENDIDO or anterior_fosforo == CARBONIZADO:
                continue

            elif anterior_fosforo == NUEVO:
                vector_fosforos[indice_negativo - 1] = ENCENDIDO

    print(vector_fosforos)

propagar([0, -1, 1])

