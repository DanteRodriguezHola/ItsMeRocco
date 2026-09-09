def ingresos_por_genero(ventas):
    generos_ingreso = {}

    for venta in ventas:
        precio = venta.get("precio")
        cantidad = venta.get("cantidad")

        ingreso = precio * cantidad
        ingreso = round(ingreso, 2)
        
        if ingreso == 0:
            continue

        genero = venta.get("genero")
        generos = generos_ingreso.keys()

        if genero in generos:
            generos_ingreso[genero] += ingreso

        else:
            generos_ingreso.update({genero: ingreso})

    return generos_ingreso

