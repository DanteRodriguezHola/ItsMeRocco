from random import randint, seed
from time import time_ns

def obtener_tamanos_lista(inicio, pasos, repeticiones):
    tamanos_lista = []
    multiplicador = inicio

    for repetir in range(repeticiones):
        tamanos_lista.append(1 * multiplicador)
        multiplicador += pasos

    return tamanos_lista

def obtener_tiempos_por_tamano(algoritmo, inicio, pasos, repeticiones):
    tamanos_lista = obtener_tamanos_lista(inicio, pasos, repeticiones)
    
    tiempos_tamano = {}

    for tamano_lista in tamanos_lista:
        lista = crear_lista_aleatoria(tamano_lista, semilla = tamano_lista)
        tiempo_ejecucion = obtener_tiempo_ejecucion(algoritmo, lista)

        tiempos_tamano.update({str(tamano_lista): tiempo_ejecucion})

    return tiempos_tamano

def obtener_tiempo_ejecucion(algoritmo, lista):
    tiempo_inicio = time_ns()

    algoritmo(lista)

    tiempo_final = time_ns()

    tiempo_ejecucion = (tiempo_final - tiempo_inicio)

    print(f"{algoritmo.__name__} (n = {len(lista)}): ~ {tiempo_ejecucion}s")

    return tiempo_ejecucion


def crear_lista_aleatoria(numero_elementos, semilla):
    seed(semilla)

    return [randint(0, numero_elementos) for repetir in range(numero_elementos)]