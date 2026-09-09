class Auto:
    def __init__(self, marca_auto, modelo_auto, ano_auto):
        self.marca = marca_auto
        self.modelo = modelo_auto
        self.ano = ano_auto
        self.kilometraje = 0
        
    def obtener_nombre_descriptivo(self):
        nombre_largo = f"{self.ano} {self.marca} {self.modelo}"
        return nombre_largo
    
    def actualizar_odometro(self, kilometraje):
        self.kilometraje = kilometraje
        
    def incrementar_odometro(self, kilometros):
        self.kilometraje += kilometros
        
class Bateria:
    def __init__(self, capacidad_bateria = 40):
        self.capacidad = capacidad_bateria
        
    def describir_bateria(self):
        print(f"Este auto tiene una batería de {self.capacidad}KWh.")
        print()
    
    def obtener_autonomia(self):
        if self.capacidad == 40:
            rango = 150
            
        elif self.capacidad == 65:
            rango = 225
        
        print(f"Este auto tiene una autonomía de {rango} kilómetros.")
        print()
    
    def actualizar_bateria(self):
        if self.capacidad != 65:
            self.capacidad = 65

class AutoElectrico(Auto):
    def __init__(self, marca_auto, modelo_auto, ano_auto):
        super().__init__(marca_auto, modelo_auto, ano_auto)
        self.bateria = Bateria()
    
electrico = AutoElectrico("Marca Cualquiera", "Modelo Cualquiera", "2038")
electrico.bateria.obtener_autonomia()
electrico.bateria.actualizar_bateria()
electrico.bateria.obtener_autonomia()

                                                                               