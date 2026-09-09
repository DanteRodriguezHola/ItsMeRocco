from matplotlib import pyplot

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort

from obtener_tiempos import obtener_tiempos_por_tamano

tiempos_tamano_bubble = obtener_tiempos_por_tamano(algoritmo = bubble_sort)

tamanos_bubble = tiempos_tamano_bubble.keys()
tiempos_bubble = tiempos_tamano_bubble.values()

tiempos_tamano_selection = obtener_tiempos_por_tamano(algoritmo = selection_sort)

tamanos_selection = tiempos_tamano_selection.keys()
tiempos_selection = tiempos_tamano_selection.values()

tiempos_tamano_insertion = obtener_tiempos_por_tamano(algoritmo = insertion_sort)

tamanos_insertion = tiempos_tamano_insertion.keys()
tiempos_insertion = tiempos_tamano_insertion.values()

pyplot.title("Bubble Sort vs. Selection Sort vs Insertion Sort")
pyplot.xlabel("Tamaño del array (n)")
pyplot.ylabel("Tiempo de ejecución (segundos)")

pyplot.plot(tamanos_bubble, tiempos_bubble, marker = "+")
pyplot.plot(tamanos_selection, tiempos_selection, marker = "*")
pyplot.plot(tamanos_insertion, tiempos_insertion, marker = "o")

pyplot.legend(["Bubble Sort", "Selection Sort", "Insertion Sort"])

pyplot.show()

