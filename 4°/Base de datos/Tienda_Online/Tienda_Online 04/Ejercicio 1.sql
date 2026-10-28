USE tienda_online;

SELECT
	MONTH(pedidos1.fecha_pedido) AS 'id_mes',
    DATE_FORMAT(pedidos1.fecha_pedido, '%M') AS 'mes',
    COUNT(pedidos1.id_pedido) AS 'cantidad_pedidos',
    CASE
		WHEN COUNT(pedidos1.id_pedido) < 15 THEN 'Baja demanda'
        WHEN COUNT(pedidos1.id_pedido) between 15 and 24 THEN 'Demanda media'
        ELSE 'Alta demanda'
	END AS 'demanda'
    
FROM
	pedidos AS pedidos1
    
WHERE
	YEAR(pedidos1.fecha_pedido) = 2025

GROUP BY
	id_mes, mes
    
ORDER BY
	id_mes;