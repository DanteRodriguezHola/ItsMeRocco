destinos = {}
encuestando = True

while encuestando:
    nombre = input("Ingrese su nombre --> ")
    destino = input("Ingrese su destino soñado --> ")
    destinos.update({nombre: destino})
    
    respuesta = input("¿Quiere continuar la encuesta? (si/no) --> ")
    if respuesta.lower() == "no":
        encuestando = False
    print()

print("Resultados de la encuesta:")
for nombre, destino in destinos.items():
    print(f"- A {nombre.title()} le encantaría ir a {destino.title()}.")