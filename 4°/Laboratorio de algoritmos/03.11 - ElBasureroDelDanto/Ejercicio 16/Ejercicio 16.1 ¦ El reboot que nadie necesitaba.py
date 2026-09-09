glosario = {
    "algoritmo": "método que describe cómo se resuelve un problema en término de las acciones que se ejecutan y especifica el orden en que se ejecutan estas acciones. Los algoritmos ayudan al programador a planificar un programa antes de su escritura en un lenguaje de programación.",
    "lenguaje máquina": "lenguaje con el nivel más bajo de comprensión para el ser humano y el único entendido por el procesador.",
    "código": "conjunto de palabras o símbolos que contienen instrucciones para la computadora.",
    "framework": "son como colecciones de herramientas, componentes y soluciones que puedes encontrar en un mismo paquete que facilitan la creación de aplicaciones complejas.",
    "paradigma de programación": "modelo de estructura utilizado por el lenguaje de programación. Hay varios paradigmas existentes y cada lenguaje utiliza uno o varios paradigmas.",
    "variable": "contenedor para almacenar distintos tipos de datos. El tipo de dato se infiere automaticamente.",
    "indentación": "sangría presente al inicio de una linea de código que define las estructuras de los bloques de codigo.",
    "comentario": "lineas de código que comienzan con #, utilizadas para hacer comentarios respecto al código.",
    "boolean": "tipo de dato que puede almacenar 'True' o 'False'.",
    "integer": "tipo de dato que permite almacenar numeros enteros."
    }

for termino, definicion in glosario.items():
    print(f"- {termino.title()}:\n\n\t{definicion.capitalize()}\n\n")