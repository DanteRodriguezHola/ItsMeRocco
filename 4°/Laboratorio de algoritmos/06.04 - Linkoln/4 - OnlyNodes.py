class EnlazadaSimple:
    def __init__(self):
        self.cabeza = None
  
    def agregar_nodo(self, nueva_data):
        nuevo_nodo = Nodo(nueva_data)
        
        if self.esta_vacia():
            self.cabeza = nuevo_nodo

        else:
            nodo_final = self.obtener_nodo_final()
            nodo_final.siguiente = nuevo_nodo

    def obtener_nodo_final(self):
        nodo_final = self.cabeza

        while nodo_final.siguiente:
            nodo_final = nodo_final.siguiente

        return nodo_final
    
    def insertar_nodo(self, nueva_data, data_anterior):
        nodo_anterior = self.buscar_nodo(data_anterior)

        if not nodo_anterior:
            return
        
        nodo_siguiente = nodo_anterior.siguiente
        nuevo_nodo = Nodo(nueva_data)

        nodo_anterior.siguiente = nuevo_nodo
        nuevo_nodo.siguiente = nodo_siguiente

    def buscar_nodo(self, data_buscada):
        nodo_actual = self.cabeza

        while nodo_actual:
            if nodo_actual.data == data_buscada:
                return nodo_actual
            
            nodo_actual = nodo_actual.siguiente

        return None
    
    def eliminar_nodo(self, data_buscada):
        if self.esta_vacia():
            return None
        
        if self.cabeza.data == data_buscada:
            nodo_eliminado = self.cabeza
            self.cabeza = self.cabeza.siguiente
            return nodo_eliminado

        nodo_actual = self.cabeza

        while nodo_actual.siguiente:
            if nodo_actual.siguiente.data == data_buscada:
                nodo_eliminado = nodo_actual.siguiente
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                return nodo_eliminado
            
            nodo_actual = nodo_actual.siguiente

        return None
    
    def ordenar(self):
        # === Decidi utilizar Selection Sort ===

        nodo_inicial = self.cabeza

        while nodo_inicial:
            nodo_minimo = nodo_inicial
            nodo_actual = nodo_inicial.siguiente

            while nodo_actual:
                if nodo_actual.data < nodo_minimo.data:
                    nodo_minimo = nodo_actual

                nodo_actual = nodo_actual.siguiente

            nodo_inicial.data, nodo_minimo.data = nodo_minimo.data, nodo_inicial.data
            nodo_inicial = nodo_inicial.siguiente
    
    def imprimir(self):
        nodo_actual = self.cabeza

        while nodo_actual:
            print(nodo_actual.data, end = " --> ")
            nodo_actual = nodo_actual.siguiente

        print("None")
    
    def tamano(self):
        cantidad_nodos = 0
        nodo_actual = self.cabeza

        while nodo_actual:
            cantidad_nodos += 1
            nodo_actual = nodo_actual.siguiente

        return cantidad_nodos

    def esta_vacia(self):
        return self.cabeza == None

class Nodo:
    def __init__(self, data):
        self.data = data

        self.siguiente = None

enlazada_simple = EnlazadaSimple()

enlazada_simple.agregar_nodo(3)
enlazada_simple.agregar_nodo(7)
enlazada_simple.agregar_nodo(11)
enlazada_simple.agregar_nodo(1)
enlazada_simple.imprimir()

enlazada_simple.insertar_nodo(4,11)
enlazada_simple.imprimir()

enlazada_simple.ordenar()
enlazada_simple.imprimir()

enlazada_simple.eliminar_nodo(3)
enlazada_simple.imprimir()

print(enlazada_simple.esta_vacia())
print(enlazada_simple.tamano())