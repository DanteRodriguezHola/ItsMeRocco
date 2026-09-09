#
# 
# 
# 
#
# 
# 
# 
# 
# 
# 
# 
# 
# 
# #

def obtener_filas(primera_matriz):
    filas = []

    for fila in primera_matriz:
        filas.append(fila)

    return filas

def obtener_columnas(segunda_matriz):
    cantidad_columnas = len(segunda_matriz[0])
    columnas = []

    for indice in range(cantidad_columnas):
        columna = []

        for fila in segunda_matriz:
            columna.append(fila[indice])

        columnas.append(columna)

    return columnas

def multiplicacion_matrices(primera_matriz, segunda_matriz):
    filas = obtener_filas(primera_matriz)
    columnas = obtener_columnas(segunda_matriz)

    cantidad_filas_columnas = len(filas[0])

    matriz_resultante = []
    for fila in filas:
        fila_resultante = []

        for columna in columnas:
            resultado = 0

            for indice in range(cantidad_filas_columnas):
                resultado += (fila[indice] * columna[indice])

            fila_resultante.append(resultado)

        matriz_resultante.append(fila_resultante)

    return matriz_resultante

if __name__ == "__main__":
    primera_matriz = [[1, 2],
                    [3, 4]]

    segunda_matriz = [[5, 6],
                    [7, 8],]

    resultado = multiplicacion_matrices(primera_matriz, segunda_matriz)

    print(resultado)