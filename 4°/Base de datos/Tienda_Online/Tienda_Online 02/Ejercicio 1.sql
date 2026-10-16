USE tienda_online;

SELECT
    categorias1.nombre AS 'Categoria',
    ROUND(SUM((detalles1.cantidad * detalles1.precio_unitario) * (1 - (detalles1.descuento_pct / 100))), 2) AS 'TotalFacturado'

    
FROM
	detalle_pedidos AS detalles1
    
    JOIN pedidos AS pedidos1 ON
		pedidos1.id_pedido = detalles1.id_pedido AND
        pedidos1.estado = 'entregado'
        
	JOIN productos AS productos1 ON
		productos1.id_producto = detalles1.id_producto
		
		JOIN categorias AS categorias1 ON
			categorias1.id_categoria = productos1.id_categoria

GROUP BY
	categorias1.nombre

            
