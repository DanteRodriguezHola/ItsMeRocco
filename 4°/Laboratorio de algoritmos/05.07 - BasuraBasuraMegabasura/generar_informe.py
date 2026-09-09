from leer_ventas import leer_ventas
from ingresos_por_genero import ingresos_por_genero

def generar_informe(nombre_archivo):
    ventas = leer_ventas(nombre_archivo)
    generos_ingreso = ingresos_por_genero(ventas)

    ingresos = generos_ingreso.values()
    ingreso_total = sum(ingresos)

    print("Ingresos por género:")
    print()

    for genero, ingreso in generos_ingreso.items():
        print(f"{genero}: ${ingreso}")

    print()
    print(f"Ingreso total: ${ingreso_total}")
    