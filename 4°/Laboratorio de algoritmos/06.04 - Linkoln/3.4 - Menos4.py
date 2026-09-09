# === Listas enlazadas doblemente circulares ===

class CircularDoble:
    def __init__(self):
        self.lista = None

class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None
        self.anterior = None

nodo_1 = Nodo("Red Dragon Tatto")
nodo_2 = Nodo("Denise")
nodo_3 = Nodo("Fine Day For a Parade")
nodo_4 = Nodo("Go, Hippie")
nodo_5 = Nodo("Hat and Feet")

nodo_1.siguiente = nodo_2
nodo_2.siguiente = nodo_3
nodo_3.siguiente = nodo_4
nodo_4.siguiente = nodo_5
nodo_5.siguiente = nodo_1

nodo_5.anterior = nodo_4
nodo_4.anterior = nodo_3
nodo_3.anterior = nodo_2
nodo_2.anterior = nodo_1
nodo_1.anterior = nodo_5

circular_doble = CircularDoble()
circular_doble.lista = nodo_1