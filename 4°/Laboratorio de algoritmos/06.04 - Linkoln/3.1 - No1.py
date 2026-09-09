# ==== Lista simple enlazada ===

class EnlazadaSimple:
    def __init__(self):
        self.lista = None

class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

nodo_1 = Nodo(2)
nodo_2 = Nodo(7)
nodo_3 = Nodo(6)
nodo_4 = Nodo(3)

nodo_1.siguiente = nodo_2
nodo_2.siguiente = nodo_3
nodo_3.siguiente = nodo_4

enlazada_simple = EnlazadaSimple()
enlazada_simple.lista = nodo_1