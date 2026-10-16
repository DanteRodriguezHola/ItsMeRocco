USE tienda_online;

SELECT
	clientes1.id_cliente AS 'ID',
    clientes1.nombre AS 'Nombre',
    clientes1.apellido AS 'Apellido',
    COUNT(pedidos1.id_pedido) AS 'CantidadPedidos'
    
FROM
	clientes AS clientes1
    
    JOIN pedidos AS pedidos1 ON
		pedidos1.id_cliente = clientes1.id_cliente
        
GROUP BY
	clientes1.id_cliente, clientes1.nombre, clientes1.apellido
    
HAVING
	COUNT(pedidos1.id_pedido) > 3

ORDER BY
	COUNT(pedidos1.id_pedido) DESC;