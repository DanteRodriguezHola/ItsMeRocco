def obtener_indice(key, n):
    return hash(key) % n

print(obtener_indice(9, 11))
print(obtener_indice(26, 11))
print(obtener_indice(50, 11))
print(obtener_indice(15, 11))
print(obtener_indice(2, 11))
print(obtener_indice(21, 11))
print(obtener_indice(36, 11))
print(obtener_indice(22, 11))
print(obtener_indice(32, 11))