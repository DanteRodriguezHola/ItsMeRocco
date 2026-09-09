"""
Implementá todos los algoritmos de recorrido vistos en clase 
(in-order, post-order, pre-order, level-order) 
y utilizalos para recorrer el árbol del punto anterior
"""

class Queue:
    def __init__(self):
        self.array = []

    def enqueue(self, nuevo_dato:any):
        self.array.append(nuevo_dato)

    def dequeue(self):
        return self.array.pop(0)
    
    def peek(self):
        return self.array[0]

    def size(self):
        return len(self.array)
    
    def isEmpty(self):
        return self.size() == 0
    
    def show(self):
        print(self.array)

class Nodo:
    def __init__(self, data:any):
        self.data = data

        self.left_child = None
        self.right_child = None

def in_order(nodo:Nodo):
    if nodo.left_child:
        in_order(nodo.left_child)

    print(nodo.data, end = "; ")

    if nodo.right_child:
        in_order(nodo.right_child)

def pre_order(nodo:Nodo):
    print(nodo.data, end = "; ")

    if nodo.left_child:
        pre_order(nodo.left_child)

    if nodo.right_child:
        pre_order(nodo.right_child)

def post_order(nodo:Nodo):
    if nodo.left_child:
        post_order(nodo.left_child)

    if nodo.right_child:
        post_order(nodo.right_child)

    print(nodo.data, end = "; ")

def level_order(nodo:Nodo):
    nodos = []
    queue = Queue()

    nodos.append(nodo.data)
    queue.enqueue(nodo)

    while not queue.isEmpty():
        nodo_actual:Nodo = queue.peek()

        if nodo_actual.left_child:
            nodos.append(nodo_actual.left_child.data)
            queue.enqueue(nodo_actual.left_child)

        if nodo_actual.right_child:
            nodos.append(nodo_actual.right_child.data)
            queue.enqueue(nodo_actual.right_child)

        queue.dequeue()

    for nodo in nodos:
        print(nodo, end = "; ")

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

print("In order:")
in_order(Nodo_A)
print()
print()

print("Pre order:")
pre_order(Nodo_A)
print()
print()

print("Post order:")
post_order(Nodo_A)
print()
print()

print("Level order:")
level_order(Nodo_A)
print()
print()