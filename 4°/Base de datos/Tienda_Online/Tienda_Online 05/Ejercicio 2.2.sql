USE tienda_online;

SELECT
	*

FROM
	vista_resumen_clientes AS resumen_clientes1
    
ORDER BY
	resumen_clientes1.total_gastado DESC
    
LIMIT
	10;