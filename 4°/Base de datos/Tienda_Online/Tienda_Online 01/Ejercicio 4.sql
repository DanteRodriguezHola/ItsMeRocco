USE tienda_online;

SELECT
	CONCAT(clientes1.nombre, ' ', clientes1.apellido) AS 'Cliente',
    CONCAT(empleados1.nombre, ' ', empleados1.apellido) AS 'Empleado',
    pedidos1.fecha_pedido AS "Fecha pedido",
    pedidos1.estado AS "Estado"
    
    
FROM
	pedidos AS pedidos1
    
    JOIN clientes AS clientes1 ON
		clientes1.id_cliente = pedidos1.id_cliente
        
	JOIN empleados AS empleados1 ON
		empleados1.id_empleado = pedidos1.id_empleado

WHERE
	pedidos1.estado = 'entregado' AND
    YEAR(pedidos1.fecha_pedido) = 2025
    
ORDER BY
	pedidos1.fecha_pedido ASC;