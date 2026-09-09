class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre = nombre_restaurante.title()
        self.tipo = tipo_cocina.capitalize()
        self.clientes_atendidos = 0
        
    def describir_restaurante(self):
        print(f"Nombre del restaurante: {self.nombre}")
        print(f"Tipo de cocina: {self.tipo}\n")
        
    def abrir_restaurante(self):
        print(f"El restaurante '{self.nombre}' está abierto al público.\n")
        
    def establecer_clientes_atendidos(self, cantidad):
        self.clientes_atendidos = cantidad
        
    def incrementar_clientes_atendidos(self, cantidad):
        self.clientes_atendidos += cantidad