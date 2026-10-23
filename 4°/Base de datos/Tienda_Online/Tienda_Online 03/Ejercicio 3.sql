USE tienda_online;

SELECT
	productos1.id_producto AS 'ID',
    productos1.nombre AS 'Producto',
    ventas1.TotalVendido AS 'TotalVendido'
    
FROM
	productos AS productos1
    
    JOIN (
    SELECT
		detalles2.id_producto AS 'id_producto',
		SUM(detalles2.cantidad) AS 'TotalVendido'

	FROM
		detalle_pedidos AS detalles2

		JOIN pedidos AS pedidos2 ON
			pedidos2.id_pedido = detalles2.id_pedido AND
			pedidos2.estado != 'cancelado'

	GROUP BY
		id_producto) AS ventas1 ON 
        ventas1.id_producto = productos1.id_producto
    
WHERE
	TotalVendido = (
		SELECT
			MAX(TotalVendido)
            
		FROM (
			SELECT
				detalles2.id_producto AS 'id_vendido',
				SUM(detalles2.cantidad) AS 'TotalVendido'

			FROM
				detalle_pedidos AS detalles2

				JOIN pedidos AS pedidos2 ON
					pedidos2.id_pedido = detalles2.id_pedido AND
					pedidos2.estado != 'cancelado'

			GROUP BY
				id_vendido) AS UnidadesVendidas2
			)