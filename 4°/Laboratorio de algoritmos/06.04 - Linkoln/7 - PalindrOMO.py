class EnlazadaSimple:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, nuevo_nodo):
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            
        else:
            ultimo_nodo = self.acceder_ultimo_nodo()
            ultimo_nodo.siguiente = nuevo_nodo

    def acceder_ultimo_nodo(self):
        ultimo_nodo = self.cabeza
        
        while ultimo_nodo.siguiente != None:
            ultimo_nodo = ultimo_nodo.siguiente
        
        return ultimo_nodo
    
    def buscar_nodo(self, dato_buscado):
        nodo_actual = self.cabeza

        while nodo_actual:
            if nodo_actual.dato == dato_buscado:
                return nodo_actual
            
            nodo_actual = nodo_actual.siguiente

        return None
    
    def eliminar_nodo(self, dato_buscado):
        pass
    
    def ordenar_lista(self): # === En este caso, utilize selection sort ===
        nodo_inicial = self.cabeza
        
        while nodo_inicial:
            nodo_minimo = nodo_inicial
            nodo_actual = nodo_inicial.siguiente
            
            while nodo_actual:
                if nodo_actual.dato < nodo_minimo.dato:
                    nodo_minimo = nodo_actual
                    
                nodo_actual = nodo_actual.siguiente
                    
            nodo_inicial.dato, nodo_minimo.dato = nodo_minimo.dato, nodo_inicial.dato
            nodo_inicial = nodo_inicial.siguiente

    def imprimir_lista(self):
        nodo_actual = self.cabeza

        while nodo_actual:
            print(nodo_actual.dato, end = " --> ")
            nodo_actual = nodo_actual.siguiente

        print("None")

    def obtener_tamano_lista(self):
        cantidad_nodos = 0
        nodo_actual = self.cabeza

        while nodo_actual:
            cantidad_nodos += 1
            nodo_actual = nodo_actual.siguiente

        return cantidad_nodos
    
    def es_ciclica(self):
        nodo_tortuga = self.cabeza
        nodo_conejo = self.cabeza

        while nodo_conejo:
            nodo_tortuga = nodo_tortuga.siguiente
            
            try:
                nodo_conejo = nodo_conejo.siguiente.siguiente

            except AttributeError:
                nodo_conejo = None

            if nodo_tortuga == nodo_conejo:
                return True
            
        return False

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

nodo_1 = Nodo(1)
nodo_2 = Nodo(2)
nodo_3 = Nodo(3)
nodo_4 = Nodo(4)

nodo_1.siguiente = nodo_2
nodo_2.siguiente = nodo_3
nodo_3.siguiente = nodo_4

enlazada_1 = EnlazadaSimple()
enlazada_1.cabeza = nodo_1

print(enlazada_1.es_ciclica())

nodo_5 = Nodo("A")
nodo_6 = Nodo("B")
nodo_7 = Nodo("C")
nodo_8 = Nodo("D")

nodo_5.siguiente = nodo_6
nodo_6.siguiente = nodo_7
nodo_7.siguiente = nodo_8

nodo_8.siguiente = nodo_6

enlazada_2 = EnlazadaSimple()
enlazada_2.cabeza = nodo_5

print(enlazada_2.es_ciclica())