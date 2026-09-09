class Usuario:
    def __init__(self, nombre_usuario, apellido_usuario, edad_usuario, pais_usuario, genero_usuario):
        self.nombre = nombre_usuario.title()
        self.apellido = apellido_usuario.title()
        self.edad = edad_usuario
        self.pais = pais_usuario.title()
        self.genero = genero_usuario.title()
    
    def describir_usuario(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"País: {self.pais}")
        print(f"Género: {self.genero}\n")
        
    def saludar_usuario(self):
        print(f"¡Hola {self.nombre} {self.apellido}! ¡Me alegro de verte! :D\n")