from random import choice

loteria = ("06", "13", "27", "34", "41", "58", "69", "75", "82", "93",
           "P", "Y", "T", "H", "O", "N")

ticket_ganador = []

for repetir in range(4):
    elemento = choice(loteria)
    ticket_ganador.append(elemento)

ticket_ganador.sort()
    
print(f"Ticket ganador: {ticket_ganador}")
print("¡Cualquier persona cuyo boleto tenga los mismos numeros/letras es el ganador de esta semana!\n")

mi_ticket = []
contador = 0

while mi_ticket != ticket_ganador:
    mi_ticket.clear()
    
    for repetir in range(4):
        elemento = choice(loteria)
        mi_ticket.append(elemento)
    
    contador += 1

print("¡Tenemos un ganador!")
print(f"{ticket_ganador} = {mi_ticket}")
print(f"Cantidad de veces que se genero un nuevo ticket: {contador}")
