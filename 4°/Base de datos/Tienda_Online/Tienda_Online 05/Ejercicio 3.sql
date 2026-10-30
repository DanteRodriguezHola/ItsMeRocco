USE tienda_online;

SELECT
	empleados1.id_empleado AS 'id',
    CONCAT(empleados1.nombre, ' ', empleados1.apellido) AS 'vendedor',
    ventas1.total AS 'total'

FROM
	empleados AS empleados1
    
	JOIN (
		SELECT
			empleados2.id_empleado AS 'id_empleado',
			ROUND(SUM((detalles2.precio_unitario * detalles2.cantidad) * (1 - (detalles2.descuento_pct / 100))), 2) AS 'total'
			
		FROM
			detalle_pedidos AS detalles2
			
			JOIN pedidos AS pedidos2 ON
				pedidos2.id_pedido = detalles2.id_pedido
				
				JOIN empleados AS empleados2 ON
					empleados2.id_empleado = pedidos2.id_empleado
					
		GROUP BY
			id_empleado) AS ventas1 ON
				ventas1.id_empleado = empleados1.id_empleado
                
WHERE
	total > (
		SELECT
			AVG(ventas2.total)
		
        FROM
			(SELECT
				ROUND(SUM((detalles3.precio_unitario * detalles3.cantidad) * (1 - (detalles3.descuento_pct / 100))), 2) AS 'total'
			
			FROM
				detalle_pedidos AS detalles3
				
				JOIN pedidos AS pedidos3 ON
					pedidos3.id_pedido = detalles3.id_pedido
					
					JOIN empleados AS empleados3 ON
						empleados3.id_empleado = pedidos3.id_empleado
						
			GROUP BY
				empleados3.id_empleado) AS ventas2)
                
ORDER BY
	total DESC;