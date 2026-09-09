valor_maximo = 9 + 1
numeros = list(range(1, valor_maximo))

for numero in numeros:
    numero = str(numero)
    ultimo_digito = int(numero[-1])
    
    if ultimo_digito == 1 or ultimo_digito == 3:
        sufijo = "ero"

    elif ultimo_digito == 2:
        sufijo = "do"

    elif ultimo_digito >= 4 and ultimo_digito <= 6:
        sufijo = "to"
        
    elif ultimo_digito == 7:
        sufijo = "mo"
        
    elif ultimo_digito == 8:
        sufijo = "vo"
        
    elif ultimo_digito == 9:
        sufijo = "eno"

    elif ultimo_digito == 0:
        sufijo = "ésimo"
        
    print(numero + sufijo)
