SELECT 
	city1.Name AS "City",
    country1.Name AS "Country",
    city1.Population AS "PopulationCity",
    
    (
		SELECT
			TRUNCATE(AVG(city2.Population), 0)
            
        FROM
			world.city AS city2
            
		WHERE city2.CountryCode = City1.CountryCode
    ) AS "AverageCountry",
    
    TRUNCATE((city1.Population / (
		SELECT
			TRUNCATE(AVG(city2.Population), 0)
            
        FROM
			world.city AS city2
            
		WHERE city2.CountryCode = City1.CountryCode
    )), 2) AS "Times"
    
FROM
	world.city AS city1
    JOIN world.country AS country1
		ON country1.Code = city1.CountryCode
        
WHERE
	city1.Population > (
		SELECT
			TRUNCATE(AVG(city2.Population), 0)
            
        FROM
			world.city AS city2
            
		WHERE city2.CountryCode = city1.CountryCode
    ) * 3

ORDER BY
	(city1.Population / (
		SELECT
			TRUNCATE(AVG(city2.Population), 0)
            
        FROM
			world.city AS city2
            
		WHERE city2.CountryCode = City1.CountryCode
    )) DESC
    
LIMIT
	10;