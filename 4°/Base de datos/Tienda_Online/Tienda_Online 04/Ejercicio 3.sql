USE tienda_online;

SELECT
	empleados1.id_empleado AS 'id_empleado',
    empleados1.nombre AS 'nombre',
    empleados1.apellido AS 'apellido',
    empleados1.puesto AS 'puesto',
    CONCAT(jefes1.nombre, ' ', jefes1.apellido) AS 'jefe',
    empleados1.fecha_contratacion AS 'fecha_contratacion',
    ROUND((DATEDIFF(CURRENT_DATE(), empleados1.fecha_contratacion) / 365), 0) AS 'anos_antiguedad'
    
    
FROM
	empleados AS empleados1
    
    LEFT JOIN empleados AS jefes1 ON
		jefes1.id_empleado = empleados1.id_jefe
        
ORDER BY
	anos_antiguedad DESC;