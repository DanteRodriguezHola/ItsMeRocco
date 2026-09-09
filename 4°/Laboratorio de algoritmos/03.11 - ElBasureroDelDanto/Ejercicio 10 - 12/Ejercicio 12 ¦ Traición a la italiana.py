pizzas_yo = [
    "primavera",
    "cuatro quesos",
    "muzzarrella",
]

pizzas_amigo = pizzas_yo.copy()

pizzas_yo.append("fugazza")
pizzas_amigo.append("fugazzeta")

print("Mis pizzas favoritas son:")
for pizza in pizzas_yo:
    print(f"- {pizza}")
print()

print("Las pizzas favoritas de mi amig@ son:")
for pizza in pizzas_amigo:
    print(f"- {pizza}")