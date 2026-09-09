¿Qué valores te devuelve la siguiente serie de operaciones,
si las ejecutás sobre un stack inicialmente vacío?

push(5), push(3), pop(), push(2), 
push(8), pop(), pop(), push(9), 
push(1), pop(), push(7), push(6), 
pop(), pop(), push(4), pop(), pop(). 

**=== RESOLUCIÓN DEL EJERCICIO ===**

push(5), push(3), pop(), push(2), 

*push(5)*

[5]

*push(3)*

[5, 3]

*pop()*

[5]

*push(2)*

[5, 2]

------

push(8), pop(), pop(), push(9), 

*push(8)*

[5, 2, 8]

*pop()*

[5, 2]

*pop()*

[5]

*push(9)*

------

push(1), pop(), push(7), push(6), 

[5, 9]

*push(1)*

[5, 9, 1]

*pop()*

[5, 9]

*push(7)*

[5, 9, 7]

*push(6)*

[5, 9, 7, 6]

-----

pop(), pop(), push(4), pop(), pop(). 

*pop()*

[5, 9, 7]

*pop()*

[5, 9]

*push(4)*

[5, 9, 4]

*pop()*

[5, 9]

*pop()*

[5]

Respuesta: Devuelve "[5]"