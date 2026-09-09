# === Listas enlazadas simples circulares ===

class CircularSimple:
    def __init__(self):
        self.lista = None

class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

nodo_1 = Nodo("They'll Need a Crane")
nodo_2 = Nodo("It's Not My Birthday")
nodo_3 = Nodo("I'll Sink Manhattan")
nodo_4 = Nodo("Nightgown of the Sullen Moon")

nodo_1.siguiente = nodo_2
nodo_2.siguiente = nodo_3
nodo_3.siguiente = nodo_4
nodo_4.siguiente = nodo_1

circular_simple = CircularSimple()
circular_simple.lista = nodo_1