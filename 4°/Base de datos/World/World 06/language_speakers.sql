SELECT
	language1.Language,
    COUNT(language1.Language) AS "CountryCount",
    
    SUM(
		(SELECT
			TRUNCATE(country2.Population * language1.Percentage, 0)
		
		FROM
			world.country AS country2
			
		WHERE
			country2.Code = language1.CountryCode)
	) AS "Speakers",
    
	GROUP_CONCAT(
		(SELECT
			country2.Code
	
		FROM
			world.country AS country2
            
		WHERE
			country2.Code = language1.CountryCode
            
		ORDER BY
			country2.Population DESC)
	SEPARATOR ", ") AS "CountryCodes"
    
    
FROM
	world.countrylanguage AS language1

WHERE
	language1.IsOfficial = "T"
    
GROUP BY
	language1.Language
    
HAVING
	COUNT(language1.Language) > 5 AND 
    SUM((SELECT
		TRUNCATE(country2.Population * language1.Percentage, 0)
	
	FROM
		world.country AS country2
        
	WHERE
		country2.Code = language1.CountryCode)) > 50000000
        
ORDER BY
	SUM((SELECT
		TRUNCATE(country2.Population * language1.Percentage, 0)
	
	FROM
		world.country AS country2
        
	WHERE
		country2.Code = language1.CountryCode)) DESC;