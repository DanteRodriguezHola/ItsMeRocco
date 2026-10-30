USE world;

SELECT
	language1.Language AS 'idioma',
	SUM(language1.Percentage * country1.Population) AS 'hablantes',
    ROUND(SUM(language1.Percentage * country1.Population) / (SELECT SUM(country2.Population) FROM country AS country2), 2) AS 'porcentaje_mundial'
    
FROM
	countrylanguage AS language1
    
    JOIN country AS country1
		ON country1.Code = language1.CountryCode
        
GROUP BY
	idioma
    
ORDER BY
	hablantes DESC
    
LIMIT
	5;