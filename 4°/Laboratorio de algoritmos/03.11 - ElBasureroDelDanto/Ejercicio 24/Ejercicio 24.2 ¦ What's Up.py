def enviar_mensajes(mensajes, mensajes_enviados):
    while mensajes:
        mensaje_enviado = mensajes.pop(0)
        print(f"Enviando mensaje '{mensaje_enviado}'...")
        mensajes_enviados.append(mensaje_enviado)
        
mensajes = [
    "Todo se está incendiando",
    "Puntas de los dedos",
    "Oigo el viento soplar",
    "¡Ey! ¡Ahora, todo el mundo!",
    "¿Quién está parado en la ventana?",
    "Encontre un nuevo amiguito debajo de mi almohada",
    "Ven y destoza mi auto",
    "¿No eres tú el que me golpeó en el ojo?",
    "Por favor, pasa la leche",
    "Dejenme solo",
    "¿Quién está tocando en la pared?",
    "Totalmente solito, totalmente por mi cuenta",
    "¿Qué hace esa cosa azul aquí?",
    "Algo agarró mi mano",
    "No te entiendo",
    "Escucho un sonido",
    "Sussuro misterioso",
    "El día que el amor vino a jugar",
    "Estoy teniendo un ataque al corazón",
    "Puntas de los dedos",
    "Camino por pasillos oscurecidos"
    ]

mensajes_enviados = []

enviar_mensajes(mensajes, mensajes_enviados)

print()
print(mensajes)
print(mensajes_enviados)