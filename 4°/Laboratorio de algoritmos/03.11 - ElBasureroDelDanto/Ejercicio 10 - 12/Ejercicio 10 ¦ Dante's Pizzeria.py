pizzas = [
    "primavera",
    "cuatro quesos",
    "muzzarrella",
]

mensajes = [
    "Me gusta (demasiado) la pizza de {pizza}.",
    "Si no te gusta la pizza de {pizza}, no tenes buen gusto.",
    "La pizza de {pizza}, una verdadera obra de arte moderna."
]

for pizza in pizzas:
    print(mensajes[pizzas.index(pizza)].replace("{pizza}", pizza))
print()

print("La pizza, simbolo de unión y felicidad\nMagnus Opus de la humanidad\nConsiderada sagrada por milenios y incontables civilizaciones\n¡Larga vida a la pizza y a sus creadores!")