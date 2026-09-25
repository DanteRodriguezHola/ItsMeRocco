SELECT
	country1.Continent AS "Continent",
    COUNT(country1.Code) AS "Countries",
    SUM(country1.Population) AS "TotalPopulation",
    TRUNCATE((SUM(country1.Population) / (SELECT SUM(country2.Population) FROM world.country AS country2) * 100), 2) AS "GlobalPercentage",
    TRUNCATE((SELECT SUM(country2.Population * country2.LifeExpectancy) / SUM(country1.Population) FROM world.country AS country2 WHERE country2.Continent = country1.Continent), 1) AS "ThoughtfulExpectancy",
    TRUNCATE((SELECT AVG(country2.LifeExpectancy) FROM world.country AS country2 WHERE country2.Continent = country1.Continent), 1) AS "SimpleExpectancy"
    
FROM
	world.country AS country1
    
GROUP BY
	country1.Continent

HAVING
	SUM(country1.Population) > 0
    
ORDER BY
	SUM(country1.Population) DESC