USE universidad;

SELECT
	departamento1.id AS 'ID',
    departamento1.nombre AS 'Nombre'
    
FROM
	departamento AS departamento1

WHERE
	ID NOT IN (SELECT id_departamento FROM profesor);