USE tienda_online;

SELECT
	productos1.id_producto AS 'ID', 
    productos1.nombre AS 'Nombre',
    ROUND(AVG(resenas1.calificacion), 2) AS 'PromedioCalificacion',
    COUNT(resenas1.id_resena) 'CantidadReseñas'
    
FROM
	resenas AS resenas1
    
    JOIN productos AS productos1 ON
		productos1.id_producto = resenas1.id_producto
        
GROUP BY
	productos1.id_producto, productos1.nombre
    
HAVING
	COUNT(resenas1.id_resena) >= 5

ORDER BY
	ROUND(AVG(resenas1.calificacion), 2) DESC;