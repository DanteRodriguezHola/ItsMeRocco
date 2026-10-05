INSERT INTO world.metropoli
	(CityID,
    Nombre,
    CodigoPais,
    Continente,
    Poblacion)
    
SELECT
	city1.ID AS "CityID",
    city1.Name AS "Nombre",
    country1.Code AS "CodigoPais",
    country1.Continent AS "Continente",
    city1.Population AS "Poblacion"
    
FROM
	world.city AS city1
    JOIN world.country AS country1
		ON country1.Code = city1.CountryCode
        
WHERE
	city1.Population >= 1000000;
	