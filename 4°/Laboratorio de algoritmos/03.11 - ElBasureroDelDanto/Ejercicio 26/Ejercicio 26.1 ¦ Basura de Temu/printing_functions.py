def imprimir_modelos(no_impresos, completados):
    while no_impresos:
        diseno_actual = no_impresos.pop()
        print(f"Imprimiendo modelo: {diseno_actual.capitalize()}")
        completados.append(diseno_actual)
        
def mostrar_modelos(completados):
    print("\nLos siguentes modelos han sido impresos:")
    for modelo in completados:
        print(f"- {modelo.capitalize()}")