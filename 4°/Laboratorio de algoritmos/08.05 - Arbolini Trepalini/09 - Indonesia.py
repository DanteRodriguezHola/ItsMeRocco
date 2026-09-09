"""
Implementá una función que se llame inverse_polish_parser
que tome como argumento un string como el siguiente “4 5 + 5 3 - *” 
y que devuelva un árbol que represente dicha expresión. 
Para esto, usá un Stack
(podés armar uno rápido de cero o reutilizar el que ya tenías hecho del cuatrimestre pasado). 
Si querés asegurarte de haberlo hecho bien, 
podés recorrer y printear el árbol que armó tu parser 
con el método post-order 
y debería devolver el mismo string que le pasaste a la función.
"""

class Stack:
    def __init__(self):
        self.array = []

    def push(self, nueva_data:any):
        self.array.append(nueva_data)

    def pop(self):
        return self.array.pop(-1)

    def peek(self):
        return self.array[-1]

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

def inverse_polish_parser(expresion_sufija:str):
    stack = Stack()
    operadores = "+-*/"

    expresion_sufija = expresion_sufija.split()
    for indice in range(len(expresion_sufija)):
        caracter = Nodo(expresion_sufija[indice])

        if caracter.data in operadores:
            operador = caracter
            operador.right_child = stack.pop()
            operador.left_child = stack.pop()

            stack.push(operador)

        else:
            stack.push(caracter)

    return stack.pop()

def post_order(nodo:Nodo):
    if nodo.left_child:
        post_order(nodo.left_child)

    if nodo.right_child:
        post_order(nodo.right_child)

    print(nodo.data, end = "; ")

nodo_raiz = inverse_polish_parser("4 5 + 5 3 - *")

print("Post order:")
post_order(nodo_raiz)
print()
print()