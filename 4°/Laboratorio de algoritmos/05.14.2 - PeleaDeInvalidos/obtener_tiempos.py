from random import randint, seed
from time import time

def obtener_tiempos_por_tamano(algoritmo):
    tamanos_lista = [10, 50, 100, 500, 
                     1000, 1500, 2000, 2500, 
                     3000, 3500, 4000, 4500,
                     5000, 6000, 7000, 8000,
                     9000, 10000]
    
    tiempos_tamano = {}

    for tamano_lista in tamanos_lista:
        lista = crear_lista_aleatoria(tamano_lista, semilla = tamano_lista)
        tiempo_ejecucion = obtener_tiempo_ejecucion(algoritmo, lista)

        tiempos_tamano.update({str(tamano_lista): tiempo_ejecucion})

    return tiempos_tamano

def obtener_tiempo_ejecucion(algoritmo, lista):
    tiempo_inicio = time()

    algoritmo(lista)

    tiempo_final = time()

    tiempo_ejecucion = (tiempo_final - tiempo_inicio)

    print(f"{algoritmo.__name__} (n = {len(lista)}): ~ {tiempo_ejecucion}s")

    return tiempo_ejecucion


def crear_lista_aleatoria(numero_elementos, semilla):
    seed(semilla)

    return [randint(0, numero_elementos) for repetir in range(numero_elementos)]



