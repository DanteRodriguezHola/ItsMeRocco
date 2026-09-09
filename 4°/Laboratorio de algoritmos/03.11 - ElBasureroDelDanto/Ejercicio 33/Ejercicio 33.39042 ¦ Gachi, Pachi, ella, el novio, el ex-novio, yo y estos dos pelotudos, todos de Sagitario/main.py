from random import randint

class Paradoja:
    def __init__(self, cantidad_fechas):
        self.cantidad = cantidad_fechas
        self.cumples = []

        for repetir in range(self.cantidad):
            fecha = randint(1, 365)
            self.cumples.append(fecha)

    def comprobar_cumples(self):
        if len(self.cumples) != len(set(self.cumples)):
            print("¡Hay dos o más personas que cumplen el mismo día!")

        else:
            print("No hay personas que cumplan el mismo día.")
        print(f"Cantidad de fechas: {self.cantidad}\n")

cinco = Paradoja(5)
diez = Paradoja(10)
quince = Paradoja(15)
veinte = Paradoja(20)
cien = Paradoja(100)

casos = (cinco, diez, quince, veinte, cien)

for caso in casos:
    caso.comprobar_cumples()