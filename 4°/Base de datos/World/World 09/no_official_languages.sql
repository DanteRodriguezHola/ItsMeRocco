SELECT
	country1.Code,
    country1.Name,
    country1.Continent,
    country1.Population,
    (SELECT COUNT(language2.Language) FROM world.countrylanguage AS language2 WHERE language2.CountryCode = country1.Code) AS "RegisteredLanguages"
    
FROM
	world.country AS country1
        
WHERE
	country1.Population > 1000000 AND
    NOT EXISTS (SELECT 1 FROM world.countrylanguage AS language2 WHERE language2.CountryCode = country1.Code AND language2.IsOfficial = "T")