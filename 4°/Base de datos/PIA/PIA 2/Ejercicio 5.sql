USE universidad;

SELECT
	matricula1.id_persona AS 'ID Alumno',
    CONCAT(persona1.apellido, ', ', persona1.primer_nombre) AS 'Alumno',
    asignatura1.nombre AS 'Asignatura',
    matricula1.id_curso AS 'Curso'
    
FROM
	matricula_asignatura AS matricula1
    
    JOIN persona AS persona1 ON
		persona1.id = matricula1.id_persona AND
        persona1.tipo = 'Alumno'
        
	JOIN asignatura AS asignatura1 ON
		asignatura1.id = matricula1.id_asignatura
        
ORDER BY
	Alumno,
	Asignatura