class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre = nombre_restaurante.title()
        self.tipo = tipo_cocina.capitalize()
        
    def describir_restaurante(self):
        print(f"Nombre del restaurante: {self.nombre}")
        print(f"Tipo de cocina: {self.tipo}\n")
        
    def abrir_restaurante(self):
        print(f"El restaurante '{self.nombre}' está abierto al público.\n")
        
mcdonalds = Restaurante("McDonalds", "Comida rápida")
la_conga = Restaurante("La Conga", "Comida peruana")
jerrys_bait_shop = Restaurante("Jerry's Bait Shop", "Bar")

restaurantes = [mcdonalds, la_conga, jerrys_bait_shop]

for restaurante in restaurantes:
    restaurante.describir_restaurante()