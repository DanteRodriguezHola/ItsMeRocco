def hornear_sandwich(*ingredientes):
    print("Su sandwich tiene:")
    for ingrediente in ingredientes:
        print(f"- {ingrediente.capitalize()}")
    print()
    
hornear_sandwich("queso", "jamon", "mayonesa")
hornear_sandwich("chorizo", "salsa criolla", "chimichurri", "tomate")
hornear_sandwich("milanesa")