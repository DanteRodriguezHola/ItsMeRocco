class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre = nombre_restaurante.title()
        self.tipo = tipo_cocina.capitalize()
        
    def describir_restaurante(self):
        print(f"Nombre del restaurante: {self.nombre}")
        print(f"Tipo de cocina: {self.tipo}\n")
        
    def abrir_restaurante(self):
        print(f"El restaurante '{self.nombre}' está abierto al público.\n")

class Heladeria(Restaurante):
    def __init__(self, nombre_restaurante, tipo_cocina, sabores_heladeria):
        super().__init__(nombre_restaurante, tipo_cocina)
        self.sabores = sabores_heladeria
    
    def mostrar_sabores(self):
        print(f"En la heladería {self.nombre} tenemos helados de:")
        for sabor in self.sabores:
            print(f"- {sabor.title()}")
        print()
        
heladeria = Heladeria("Heladería Cualquiera", "Helados", ["Vainilla", "Banana Split", "Queso Intenso"])

heladeria.mostrar_sabores()