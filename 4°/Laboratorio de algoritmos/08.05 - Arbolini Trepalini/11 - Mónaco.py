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

def calcular(nodo = None):
        operadores = "+-*/"
        
        if nodo.data in operadores:
            numero_1 = calcular(nodo.left_child)
            operador = nodo.data
            numero_2 = calcular(nodo.right_child)
    
            operacion = f"{numero_1}{operador}{numero_2}"
            return eval(operacion)
        
        else:
            return nodo.data
        
def evaluate(expresion_sufija:str):
    nodo_raiz = inverse_polish_parser(expresion_sufija)

    return calcular(nodo_raiz)

print(evaluate("2 3 * 3 1 - /"))