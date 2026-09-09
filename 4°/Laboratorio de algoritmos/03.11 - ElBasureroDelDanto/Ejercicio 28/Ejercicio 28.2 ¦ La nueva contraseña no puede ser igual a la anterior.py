class Usuario:
    def __init__(self, nombre_usuario, apellido_usuario, edad_usuario, pais_usuario, genero_usuario):
        self.nombre = nombre_usuario.title()
        self.apellido = apellido_usuario.title()
        self.edad = edad_usuario
        self.pais = pais_usuario.title()
        self.genero = genero_usuario.title()
        self.intentos_login = 0
        
    def describir_usuario(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"País: {self.pais}")
        print(f"Género: {self.genero}\n")
        
    def saludar_usuario(self):
        print(f"¡Hola {self.nombre} {self.apellido}! ¡Me alegro de verte! :D\n")
        
    def incrementar_intentos_login(self):
        self.intentos_login += 1
        
    def reiniciar_intentos_login(self):
        self.intentos_login = 0
        
usuario = Usuario("Fulano", "De Tal", 0, "Nemo", "Ninguno")

usuario.incrementar_intentos_login()
usuario.incrementar_intentos_login()
usuario.incrementar_intentos_login()
usuario.incrementar_intentos_login()
usuario.incrementar_intentos_login()
print(usuario.intentos_login)

usuario.reiniciar_intentos_login()
print(usuario.intentos_login)