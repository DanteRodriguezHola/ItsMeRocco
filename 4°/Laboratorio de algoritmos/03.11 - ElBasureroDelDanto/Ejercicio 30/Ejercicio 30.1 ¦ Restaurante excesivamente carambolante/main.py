from restaurante import Restaurante

restaurante = Restaurante("Restaurante Cualquiera", "Comida Mexicana")
restaurante.describir_restaurante()
restaurante.abrir_restaurante()
restaurante.establecer_clientes_atendidos(500_000)
restaurante.incrementar_clientes_atendidos(1_000_000)
print(restaurante.clientes_atendidos)