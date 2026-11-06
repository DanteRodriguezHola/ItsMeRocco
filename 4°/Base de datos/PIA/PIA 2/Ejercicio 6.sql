USE universidad;

SELECT
	grado1.id AS 'ID',
    grado1.nombre AS 'Asignatura',
    SUM(IF(asignatura1.tipo = 'basica', 1, 0)) AS 'Basicas',
    SUM(IF(asignatura1.tipo = 'obligatoria', 1, 0)) AS 'Obligatorias',
    SUM(IF(asignatura1.tipo = 'optativa', 1, 0)) AS 'Optativas',
    COUNT(asignatura1.id) AS 'Total'
    
FROM
	grado AS grado1
    
    JOIN asignatura AS asignatura1 ON
		asignatura1.id_grado = grado1.id

GROUP BY
	ID,
    Asignatura
    
ORDER BY
	Total DESC