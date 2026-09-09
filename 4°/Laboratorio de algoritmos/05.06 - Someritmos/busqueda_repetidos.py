# 
# BUSQUEDA DE ELEMENTOS REPETIDOS
# 
# Cantidad de operaciones: () + 1
# 1 = 2
# 2 = 5
# 3 =  

def busqueda_repetidos(lista):
    for e in range(len(lista)): # 3
        for j in range(e + 1, len(lista)):  # 
            if lista[e] == lista[j]: # 3
                return True
    
    return False # 1

if __name__ == "__main__":
    resultado = busqueda_repetidos(lista = [1, 2, 3, 4, 5])
    print(resultado)