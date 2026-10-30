USE tienda_online;

CREATE VIEW `vista_resumen_clientes` AS
	SELECT
		clientes1.id_cliente AS 'id',
		clientes1.nombre AS 'nombre',
		clientes1.apellido AS 'apellido',
		COUNT(DISTINCT pedidos1.id_pedido) AS 'cantidad_pedidos',
		ROUND(SUM((detalles1.precio_unitario * detalles1.cantidad) * (1 - (detalles1.descuento_pct / 100))), 2) AS 'total_gastado'

	FROM
		pedidos AS pedidos1
		
		JOIN detalle_pedidos AS detalles1 ON
			detalles1.id_pedido = pedidos1.id_pedido
			
		JOIN clientes AS clientes1 ON
			clientes1.id_cliente = pedidos1.id_cliente

	GROUP BY
		id,
		nombre,
		apellido;