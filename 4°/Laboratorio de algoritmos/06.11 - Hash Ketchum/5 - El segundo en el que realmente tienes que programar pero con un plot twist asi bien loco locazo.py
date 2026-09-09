class HashMap:
    def __init__(self, tamano):
        self.tamano = tamano
        self.buckets = [[] for _ in range(tamano)]

    def agregar_elemento(self, nueva_llave, nuevo_valor):
        indice = self.hash(nueva_llave)
        elemento = [nueva_llave, nuevo_valor]

        self.buckets[indice].append(elemento)

    def eliminar_elemento(self, llave_buscada):
        indice = self.hash(llave_buscada)

        bucket_buscado = self.buckets[indice]

        for elemento in bucket_buscado:
            llave = elemento[0]

            if llave == llave_buscada:
                bucket_buscado.remove(elemento)
                return
    
    def buscar_elemento(self, llave_buscada):
        indice = self.hash(llave_buscada)

        bucket_buscado = self.buckets[indice]

        for elemento in bucket_buscado:
            llave = elemento[0]

            if llave == llave_buscada:
                return elemento
            
    def reemplazar_valor(self, llave_buscada, nuevo_valor):
        indice = self.hash(llave_buscada)

        bucket_buscado = self.buckets[indice]

        for elemento in bucket_buscado:
            llave = elemento[0]

            if llave == llave_buscada:
                elemento[1] = nuevo_valor
                return
    
    def imprimir(self):
        print(self.buckets)

    def hash(self, llave):
        return hash(llave) % self.tamano
    
hash_map = HashMap(4)

hash_map.agregar_elemento(6, "Manzana")
hash_map.agregar_elemento(1, "Naranja")
hash_map.agregar_elemento(9, "Banana")
hash_map.agregar_elemento(8, "Uvas")
hash_map.agregar_elemento(7, "Kiwi")
hash_map.imprimir()

hash_map.eliminar_elemento(8)
hash_map.imprimir()

hash_map.reemplazar_valor(1, "Mandarina")
hash_map.imprimir()

print(hash_map.buscar_elemento(7))