"""
Implementá en Python una clase Nodo que se asemeje a un nodo de un árbol.
"""


class Nodo:
    def __init__(self, data:any):
        self.data = data

        self.left_child = None
        self.right_child = None