USE tienda_online;

SELECT
	productos1.nombre AS 'Nombre',
    categorias1.nombre AS 'Categoria',
    productos1.precio AS 'Precio'		
    
FROM
	productos AS productos1
    
    JOIN categorias AS categorias1
		ON categorias1.id_categoria = productos1.id_categoria
        
WHERE
	productos1.precio > (
		SELECT
			AVG(productos2.precio)
            
		FROM
			productos AS productos2
            
		WHERE
			productos2.id_categoria = productos1.id_categoria
		)