pedidos_sandwiches = [
    "milanesa",
    "pastrón",
    "bondiola",
    "trancapecho",
    "pastrón",
    "jamon y queso",
    "pastrón",
    "pollo",
    "pastrón",
    ]

sandwiches_terminados = []

print("¡AVISO!\nNos quedamos sin sánguches de pastrón. Disculpe las molestias.\n")

while "pastrón" in pedidos_sandwiches:
    pedidos_sandwiches.remove("pastrón")
    
while pedidos_sandwiches:
    sandwich = pedidos_sandwiches.pop(0)
    print(f"Preparando tu sánguche de {sandwich.lower()}...")
    sandwiches_terminados.append(sandwich)

print("\nSandwiches terminados:")
for sandwich in sandwiches_terminados:
    print(f"- {sandwich.capitalize()}")