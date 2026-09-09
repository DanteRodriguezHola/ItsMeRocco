class HashSet:
    def __init__(self, tamano):
        self.tamano = tamano
        self.buckets = [[] for _ in range(tamano)]

    def agregar_elemento(self, nuevo_elemento):
        indice = self.hash(nuevo_elemento)

        self.buckets[indice].append(nuevo_elemento)

    def eliminar_elemento(self, elemento_buscado):
        indice = self.hash(elemento_buscado)

        bucket_buscado = self.buckets[indice]

        for elemento in bucket_buscado:
            if elemento == elemento_buscado:
                bucket_buscado.remove(elemento_buscado)
                return

    def buscar_elemento(self, elemento_buscado):
        indice = self.hash(elemento_buscado)

        bucket_buscado = self.buckets[indice]

        for elemento in bucket_buscado:
            if elemento == elemento_buscado:
                return elemento
        
    def imprimir(self):
        print(self.buckets)

    def hash(self, elemento):
        return hash(elemento) % self.tamano


hash_set = HashSet(3)

hash_set.agregar_elemento(10)
hash_set.agregar_elemento(2)
hash_set.agregar_elemento(9)
hash_set.agregar_elemento(4)
hash_set.imprimir()

hash_set.eliminar_elemento(2)
hash_set.imprimir()

hola = hash_set.buscar_elemento(10)
print(hola)