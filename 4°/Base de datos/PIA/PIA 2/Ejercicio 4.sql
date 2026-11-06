USE universidad;

SELECT
	profesor1.id_profesor AS 'ID',
    persona1.primer_nombre AS 'Nombre',
    persona1.apellido AS 'Apellido',
    COUNT(asignatura1.id) AS 'Asignaturas'
    
FROM
	profesor AS profesor1
    
    JOIN persona AS persona1 ON
		persona1.id = profesor1.id_profesor
        
	LEFT JOIN asignatura AS asignatura1 ON
		asignatura1.id_profesor = profesor1.id_profesor
        
GROUP BY
	profesor1.id_profesor,
    persona1.primer_nombre,
    persona1.apellido
    
ORDER BY
	COUNT(asignatura1.id) DESC;