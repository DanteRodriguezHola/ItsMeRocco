from random import choice

loteria = ("6", "13", "27", "34", "41", "58", "69", "75", "82", "93",
           "P", "Y", "T", "H", "O", "N")

ticket_ganador = []

for repetir in range(4):
    elemento = choice(loteria)
    ticket_ganador.append(elemento)

ticket_ganador.sort()
    
print(f"Ticket ganador: {ticket_ganador}")
print("¡Cualquier persona cuyo boleto tenga los mismos numeros/letras es el ganador de esta semana!")