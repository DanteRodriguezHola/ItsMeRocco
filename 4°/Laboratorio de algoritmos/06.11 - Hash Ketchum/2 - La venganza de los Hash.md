Tenemos ocho objetos con los códigos hash: 

*217, 209, 265, 226, 234, 201, 207 y 223*
(es lo que devolvió la función hash del ejercicio anterior, antes de hacer el módulo). 

Los vamos a guardar en una hash table que arranca vacía, usando un arreglo de tamaño 8 (o sea, 8 buckets) y encadenamiento separado (separate chaining) para resolver las colisiones. 

Calculá las longitudes de las cadenas que se arman después de insertar todos estos objetos.

**=== RESOLUCIÓN DEL EJERCICIO ===**

Iniciamos creando nuestro hash table con 8 buckets.

**hash_table**:
[
    [], # 0
    [], # 1
    [], # 2
    [], # 3
    [], # 4
    [], # 5
    [], # 6
    [], # 7
]

Ahora, *necesitamos obtener los indices* de cada uno de los objetos.

217 % 8 = 1
209 % 8 = 1
265 % 8 = 1
226 % 8 = 2
234 % 8 = 2
201 % 8 = 1
207 % 8 = 7
223 % 8 = 7

Por ultimo, *insertamos cada objeto* en nuestro hash_table *según su indice.*

**hash_table**: 
[
    [] # 0
    [217, 209, 265, 201] # 1
    [226, 234] # 2
    [] # 3
    [] # 4
    [] # 5
    [] # 6
    [207, 223] # 7
]