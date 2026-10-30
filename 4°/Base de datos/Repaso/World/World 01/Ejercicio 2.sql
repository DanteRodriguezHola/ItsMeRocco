USE world;

SELECT
	country1.Name AS 'nombre',
    COUNT(DISTINCT city1.District) AS 'pcias_estados'
    
FROM
	city AS city1
    
    JOIN country AS country1 ON
		country1.Code = city1.CountryCode
        
GROUP BY
	nombre;
	