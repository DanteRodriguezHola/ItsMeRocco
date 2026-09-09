from obtener_tiempos import obtener_tiempos_por_tamano
from matplotlib import pyplot

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort

def obtener_nombre_algoritmo(algoritmo):
    nombre_algoritmo = algoritmo.__name__

    nombre_formateado = nombre_algoritmo.replace("_", " ").title()
    
    return nombre_formateado

def graficar_algoritmos(multiplicador, escala, repeticiones, *algoritmos):
    for algoritmo in algoritmos:
        nombre_algoritmo = obtener_nombre_algoritmo(algoritmo)
        tiempos_por_tamano = obtener_tiempos_por_tamano(algoritmo, multiplicador, escala, repeticiones)

        tamanos = tiempos_por_tamano.keys()
        tiempos = tiempos_por_tamano.values()

        pyplot.plot(tamanos, tiempos, label = nombre_algoritmo)
        pyplot.legend()

    pyplot.xlabel("Tamaños de lista (n)")
    pyplot.ylabel("Tiempo de ejecución (milisegundos)")

    pyplot.show()

graficar_algoritmos(500, 500, 20,
                    bubble_sort,
                    selection_sort,
                    insertion_sort,
                    quick_sort)