USE tienda_online;

SELECT
	tiempos1.antiguedad AS 'antiguedad',
    COUNT(tiempos1.id_cliente) AS 'cantidad_clientes'
    
FROM
	(SELECT
		clientes2.id_cliente AS 'id_cliente',
		CASE
			WHEN DATEDIFF(CURRENT_DATE(), clientes2.fecha_registro) / 365 < 1 THEN 
				'Nuevo'
			
			WHEN DATEDIFF(CURRENT_DATE(), clientes2.fecha_registro) / 365 between 1 and 3 THEN 
				'Intermedio'
			
			ELSE
				'Viejo'
		END AS 'antiguedad'
		
	FROM
		clientes AS clientes2) AS tiempos1
	
GROUP BY
	antiguedad;
