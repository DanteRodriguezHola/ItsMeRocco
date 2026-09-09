ciudades = {
    "Estambul": {
            "poblacion": 15701602,
            "país": "turquía",
            "dato de color": "Estambul fue alguna vez Constantinopla, así que si tenias una cita en Constantinopla, ella estará esperandote en Estambul."
    },

    "Albuquerque": {
        "poblacion": 561008,
        "país": "Estados Unidos",
        "dato de color": "Aquí le robaron a Miracle Machine su lucky snorquel."
    },

    "Cochamamba": {
        "poblacion": 665505,
        "país": "Bolivia",
        "dato de color": "Esta ciudad es especial para mí: aquí nacieron mi mamá, abuela, abuelo y muchos otros de mis familiares :D"
    }
    }

for ciudad, info in ciudades.items():
    print(f"{ciudad.title()}:")
    for dato, valor in info.items():
        print(f"- {dato.capitalize()}: {str(valor)}")
    print()
