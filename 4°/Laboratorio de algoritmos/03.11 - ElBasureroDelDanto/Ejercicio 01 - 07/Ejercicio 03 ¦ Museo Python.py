# .isascii()

# Devuelve "True" si todos los caracteres de un string pertenecen al codigo ASCII.
# Por lo contrario, devuelve "False".

"empanada".isascii() # True
"pingüinos".isascii() # False
"# 51".isascii() # True
"♪ 27".isascii() #False

# .count(sub, start, end)

# Devuelve la cantidad de veces que aparece un substring en un string dentro del rango 'start-end'
# En caso de que se de un substring vacio, devuelve el largo del string más uno.

"banana banana banana banana".count("banana") # 4
"banana banana banana banana".count("banana", 7) # 3
"banana banana banana banana".count("banana", 7, 21) # 2
"banana banana banana banana".count("") # 28
