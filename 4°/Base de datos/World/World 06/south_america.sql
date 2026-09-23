SELECT
	country1.Name AS "Country",
    city1.Name AS "City",
    city1.District AS "District",
    city1.Population AS "Population",
    (SELECT
		COUNT(*)
	
    FROM
		world.city AS city2
        
	WHERE
		city2.CountryCode = city1.CountryCode AND
		city2.Population > city1.Population
	) + 1 AS "Ranking"
    
FROM
	world.city AS city1
    JOIN world.country AS country1
		ON country1.Code = city1.CountryCode
        
WHERE
	country1.Region = "South America" AND
    (SELECT
		COUNT(*)
	
    FROM
		world.city AS city2
        
	WHERE
		city2.CountryCode = city1.CountryCode AND
		city2.Population > city1.Population
	) + 1 <= 3;