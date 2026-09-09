Explicá en detalle qué hace la siguiente función y cómo lo hace (“n” es la cantidad de buckets).

*def obtener_indice(key, n):*
    *return hash(key) % n*

**=== RESOLUCIÓN DEL EJERCICIO ===**

Lo que hace la función "obtener indice" es devolver el indice de una clave en un hash table.
Para eso, utiliza la función incorporada **hash** para obtener el valor hash de la clave,
para despues hacer su modelo segun el tamaño del hash table (la cantidad de buckets).

Por ejemplo, si a la funcion le paso como argumentos:

- **key** = 67 
- **n** = 9

Me devolvera como indice **4**