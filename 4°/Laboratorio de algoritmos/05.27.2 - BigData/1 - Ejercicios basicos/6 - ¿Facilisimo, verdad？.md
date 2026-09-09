Suponé que una queue **Q** inicialmente vacía ejecutó un total de 

- 32 operaciones *enqueue*
- 10 operaciones *peek*
- 15 operaciones *dequeue*, de las cuales 5 tiraron errores **Empty** (vacío) que fueron atrapados e ignorados. 

¿Cuál es el tamaño actual de **Q**?

**=== RESOLUCIÓN DEL EJERCICIO ===**

Como las operaciones *peek* no modifican a **Q**, podemos ignorarlas.

Como 5 operaciones *dequeue* tiraror errores **Empty**, osea, se hicieron cuando la lista estaba vacia,
podemos suponer que estas 5 se hicieron al inicio, ya que **Q** estaba vacia inicialmente.

Luego, suponemos que realizaron 32 operaciones *enqueue* seguidas, que sumaron 32 elementos a **Q**.
**Q** ahora tiene 32 elementos.

Por ultimo, suponemos que se realizan las 10 operaciones *dequeue* restantes, quitando 10 elementos a **Q**.
Finalmente, **Q** tiene 22 elementos en total.

El tamaño actual de **Q** es de 22 elementos.