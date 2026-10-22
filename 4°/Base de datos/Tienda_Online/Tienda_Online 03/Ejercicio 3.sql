USE tienda_online;

SELECT
	*
    
FROM
	(
    SELECT
		productos2.id_producto AS 'ID',
		productos2.nombre AS 'Nombre',
		SUM(detalles2.cantidad) AS 'TotalVendido'

	FROM
		detalle_pedidos AS detalles2

		JOIN pedidos AS pedidos2 ON
			pedidos2.id_pedido = detalles2.id_pedido AND
			pedidos2.estado != 'cancelado'

		JOIN productos AS productos2 ON
			productos2.id_producto = detalles2.id_producto

	GROUP BY
		ID,
		Nombre
	) AS UnidadesVendidas1
    
WHERE
	UnidadesVendidas1.TotalVendido = (
		SELECT
			MAX(TotalVendido)
            
		FROM
			(
			SELECT
				productos2.id_producto AS 'ID',
				productos2.nombre AS 'Nombre',
				SUM(detalles2.cantidad) AS 'TotalVendido'

			FROM
				detalle_pedidos AS detalles2

				JOIN pedidos AS pedidos2 ON
					pedidos2.id_pedido = detalles2.id_pedido AND
					pedidos2.estado != 'cancelado'

				JOIN productos AS productos2 ON
					productos2.id_producto = detalles2.id_producto

			GROUP BY
				ID,
				Nombre
			) AS UnidadesVendidas2
		)