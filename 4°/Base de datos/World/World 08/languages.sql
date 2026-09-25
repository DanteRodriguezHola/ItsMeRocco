SELECT
	country1.Name AS "Country",
    country1.Region AS "Region",
    COUNT(language1.Language) AS "OfficialLanguages",
    GROUP_CONCAT(CONCAT(language1.Language, " (", language1.Percentage, "%)") ORDER BY language1.Percentage DESC SEPARATOR " | ") AS "Details",
    SUM(language1.Percentage) AS "Percentage"
    
FROM
	world.countrylanguage AS language1
    JOIN world.country AS country1
		ON country1.Code = language1.CountryCode

WHERE
	language1.IsOfficial = "T"
    
GROUP BY
	country1.Name, country1.Region
    
HAVING
	COUNT(language1.Language) >= 3
    
ORDER BY
	COUNT(language1.Language) DESC,
    country1.Name ASC