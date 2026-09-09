lugares_favoritos = {
    "Marcos": [
        "La Bombonera",
        "La DantSteam House",
        "La Marcos House"],
    "Benja": [
        "La cancha de Huracan",
        "La Benja House",
        "La isla de su amigo Jeff"], # Juro que no hare este chiste devuelta ._.
    "Dante": [
        "Buenos Aires",
        "Avellaneda",
        "Hashley",]
    }

for persona, lugares in lugares_favoritos.items():
    print(f"Los lugares favoritos de mi amigo {persona} son:")
    for lugar in lugares:
        print(f"- {lugar}")
    print()