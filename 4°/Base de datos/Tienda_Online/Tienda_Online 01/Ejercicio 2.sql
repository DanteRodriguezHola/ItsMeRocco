USE tienda_online;

SELECT
	productos1.nombre AS 'Producto',
    categorias1.nombre AS 'Categoría',
    proveedores1.razon_social AS 'Razón social',
    productos1.precio AS 'Precio',
    productos1.stock AS 'Stock'
    
    
FROM
	productos AS productos1

    JOIN categorias AS categorias1 ON
		categorias1.id_categoria = productos1.id_categoria
        
	JOIN  proveedores AS proveedores1 ON
		proveedores1.id_proveedor = productos1.id_proveedor
    
WHERE
	productos1.activo = 1
    
ORDER BY
	productos1.precio DESC
    
LIMIT
	15;