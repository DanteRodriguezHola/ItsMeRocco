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
        
class Admin(Usuario):
    def __init__(self, nombre_usuario, apellido_usuario, edad_usuario, pais_usuario, genero_usuario):
        super().__init__(nombre_usuario, apellido_usuario, edad_usuario, pais_usuario, genero_usuario)
        self.privilegios = [
            "Hacer publicaciones",
            "Eliminar publicaciones",
            "Bloquear usuarios",
            "Acceder a los archivos clasificados del gobierno de E.E.U.U.",
            "Entrar al nivel 7 de la Deep Web",
            "Aceptar la solicitud de Laura (a 5km de distancia)", 
            "Saber si Woody y Tiro al Blanco cruzaron el Gran Cañon a tiempo"
            ]
        
    def mostrar_privilegios(self):
        print(f"Esos son tus privilegios de administrador, {self.nombre} {self.apellido}:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}.")
            
admin = Admin("Peluchin", "Kaker", 17, "Argentina", "Hombre")
admin.mostrar_privilegios()