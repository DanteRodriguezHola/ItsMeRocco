SELECT
    city1.Name AS 'Nombre',
    city1.Population AS 'PoblacionCiudad',
    country1.Name AS 'Pais',
    country1.Population AS 'PoblacionPais',
    TRUNCATE((city1.Population / country1.Population) * 100, 2) AS 'ErrorPct'
    
FROM
    world.city AS city1
    JOIN world.country AS country1
        ON country1.Code = city1.CountryCode
        
WHERE
    city1.Population > country1.Population