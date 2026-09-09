# === Lista doblemente enlazada ===

class EnzaladaDoble:
    def __init__(self):
        self.lista = None

class Nodo:
    def __init__(self, data):
        self.data = data
        self.anterior = None
        self.siguiente = None


nodo_1 = Nodo("I")
nodo_2 = Nodo("Palindrome")
nodo_3 = Nodo("I")
nodo_4 = Nodo("(manonam)")

nodo_1.siguiente = nodo_2
nodo_2.siguiente = nodo_3
nodo_3.siguiente = nodo_4

nodo_4.anterior = nodo_3
nodo_3.anterior = nodo_2
nodo_2.anterior = nodo_1

enzalada_doble = EnzaladaDoble()
enzalada_doble.cabeza = nodo_1