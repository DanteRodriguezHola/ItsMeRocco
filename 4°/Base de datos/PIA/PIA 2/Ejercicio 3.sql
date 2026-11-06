USE universidad;

SELECT
	profesor1.id_profesor AS 'ID',
	persona1.primer_nombre AS 'Nombre',
    persona1.apellido AS 'Apellido'
    
FROM
	profesor AS profesor1
    
    JOIN persona AS persona1 ON
		persona1.id = profesor1.id_profesor

WHERE
	ID NOT IN (SELECT IFNULL(id_profesor, 0) FROM asignatura);