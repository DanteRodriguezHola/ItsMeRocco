class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre = nombre_restaurante.title()
        self.tipo = tipo_cocina.capitalize()
        
    def describir_restaurante(self):
        print(f"Nombre del restaurante: {self.nombre}")
        print(f"Tipo de cocina: {self.tipo}\n")
        
    def abrir_restaurante(self):
        print(f"El restaurante '{self.nombre}' está abierto al público.\n")
        
restaurante = Restaurante("Restaurante Cualquiera", "Comida Argentina")

print(f"Nombre del restaurante: {restaurante.nombre}")
print(f"Tipo de cocina: {restaurante.tipo}\n")

restaurante.describir_restaurante()
restaurante.abrir_restaurante()
