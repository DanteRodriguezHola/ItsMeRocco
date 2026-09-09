def obtener_titulo(datos_venta):
    titulo = datos_venta[0]
    
    return titulo
    
def obtener_genero(datos_venta):
    try:
        genero = datos_venta[1]

    except IndexError:
        return None
    
    else:
        if genero:
            return genero
        
        else:
            return "{desconocido}"
    
def obtener_precio(datos_venta):
    try:
        precio = float(datos_venta[2])
    
    except IndexError or ValueError:
        return 0
    
    else:
        return precio
    
def obtener_cantidad(datos_venta):
    try:
        cantidad = int(datos_venta[3])

    except IndexError or ValueError:
        return 0
    
    else:
        return cantidad