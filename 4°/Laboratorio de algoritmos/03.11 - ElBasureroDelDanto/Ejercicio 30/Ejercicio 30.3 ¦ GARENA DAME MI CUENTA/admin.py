from user import Usuario

class Privilegios:
    def __init__(self):
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
        print(f"Esos son tus privilegios de administrador:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}.")
        
class Admin(Usuario):
    def __init__(self, nombre_usuario, apellido_usuario, edad_usuario, pais_usuario, genero_usuario):
        super().__init__(nombre_usuario, apellido_usuario, edad_usuario, pais_usuario, genero_usuario)
        self.privilegios = Privilegios()