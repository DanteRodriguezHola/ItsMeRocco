"""
Armá el siguiente árbol binario con la clase Nodo del punto anterior.
"""

class Nodo:
    def __init__(self, data:any):
        self.data = data

        self.left_child = None
        self.right_child = None

Nodo_A = Nodo("A")
Nodo_B = Nodo("B")
Nodo_C = Nodo("C")
Nodo_D = Nodo("D")
Nodo_E = Nodo("E")
Nodo_F = Nodo("F")
Nodo_G = Nodo("G")

Nodo_A.left_child = Nodo_B
Nodo_B.left_child = Nodo_C
Nodo_C.left_child = Nodo_D
Nodo_B.right_child = Nodo_E
Nodo_A.right_child = Nodo_F
Nodo_F.left_child = Nodo_G