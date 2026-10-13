USE tienda_online;

SELECT
	COUNT(clientes1.id_cliente) AS 'Cantidad de clientes que no han realizado ningún pedido'
    
FROM
	clientes AS clientes1
    
WHERE
	clientes1.id_cliente NOT IN
		(SELECT
			pedidos2.id_cliente
            
		FROM
			pedidos AS pedidos2)