USE tienda_online;

SELECT
	clientes1.id_cliente AS 'ID',
    clientes1.nombre AS 'Nombre',
    clientes1.apellido AS 'Apellido',
    clientes1.email AS 'Email'
    
FROM
	clientes AS clientes1
    
WHERE
	clientes1.id_cliente NOT IN
		(SELECT
			pedidos2.id_cliente
            
		FROM
			pedidos AS pedidos2)