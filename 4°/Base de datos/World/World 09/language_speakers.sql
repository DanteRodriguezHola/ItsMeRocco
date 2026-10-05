SELECT
	language1.Language,
    COUNT(language1.Language) AS "CountryCount",
    SUM(TRUNCATE(country1.Population * language1.Percentage, 0)) AS "Speakers",
    GROUP_CONCAT(country1.Code ORDER BY country1.Population DESC SEPARATOR ", ") AS "CountryCodes"
    
    
FROM
	world.countrylanguage AS language1
    JOIN world.country AS country1
		ON country1.Code = language1.CountryCode

WHERE
	language1.IsOfficial = "T"
    
GROUP BY
	language1.Language
    
HAVING
	COUNT(language1.Language) > 5 AND 
    SUM(TRUNCATE(country1.Population * language1.Percentage, 0)) > 50000000
        
ORDER BY
	SUM((SELECT
		TRUNCATE(country2.Population * language1.Percentage, 0)
	
	FROM
		world.country AS country2
        
	WHERE
		country2.Code = language1.CountryCode)) DESC;