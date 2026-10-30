USE tienda_online;

SELECT
	*
    
FROM
	(SELECT
		categorias2.nombre AS 'categoria',
		productos2.nombre AS 'producto',
		SUM(detalles2.cantidad) AS 'unidades_vendidas',
		RANK() OVER (
			PARTITION BY
				categorias2.nombre
				
			ORDER BY
				SUM(detalles2.cantidad) DESC
		)  AS 'ranking'
		
		
	FROM
		detalle_pedidos AS detalles2
		
		JOIN pedidos AS pedidos2 ON
			pedidos2.id_pedido = detalles2.id_pedido
			
		JOIN productos AS productos2 ON
			productos2.id_producto = detalles2.id_producto
			
			JOIN categorias AS categorias2 ON
				categorias2.id_categoria = productos2.id_categoria
				
	GROUP BY
		categoria,
		producto) AS mas_vendidos1
        
WHERE
	ranking <= 3;
        
