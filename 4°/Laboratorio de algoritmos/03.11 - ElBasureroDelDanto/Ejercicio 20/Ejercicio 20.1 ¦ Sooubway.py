pedidos_sandwiches = [
    "milanesa",
    "bondiola",
    "trancapecho",
    "jamon y queso",
    "pollo"
    ]

sandwiches_terminados = []

while pedidos_sandwiches:
    sandwich = pedidos_sandwiches.pop(0)
    print(f"Preparando tu sánguche de {sandwich.lower()}...")
    sandwiches_terminados.append(sandwich)

print("\nSandwiches terminados:")
for sandwich in sandwiches_terminados:
    print(f"- {sandwich.capitalize()}")