from random import randint

class Dado():
    def __init__(self, caras_dado = 6):
        self.caras = caras_dado
        
    def tirar_dado(self):
        resultado = randint(1, self.caras)
        
        print(f"Resultado: {resultado}")
        print(f"Caras del dado: {self.caras}\n")
        
dado_seis = Dado()

for repetir in range(10):
    dado_seis.tirar_dado()
    
dado_diez = Dado(10)
dado_veinte = Dado(20)

for repetir in range(10):
    dado_diez.tirar_dado()
    
for repetir in range(10):
    dado_veinte.tirar_dado()