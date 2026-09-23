SELECT
	country1.Name AS "Country",
    country1.Continent AS "Continent",
    city1.Name AS "Capital",
    city1.Population AS "Captial Population",
    (SELECT city2.Name FROM world.city AS city2 WHERE city2.CountryCode = country1.Code ORDER BY city2.Population DESC LIMIT 1) AS "Most Populated City",
    (SELECT city2.Population FROM world.city AS city2 WHERE city2.CountryCode = country1.Code ORDER BY city2.Population DESC LIMIT 1) AS "Most Populated City Population",
    (SELECT city2.Population FROM world.city AS city2 WHERE city2.CountryCode = country1.Code ORDER BY city2.Population DESC LIMIT 1) - city1.Population AS "Diference"

FROM
	world.country AS country1
    JOIN world.city AS city1
		ON city1.ID = country1.Capital

WHERE
	(SELECT city2.ID FROM world.city AS city2 WHERE city2.CountryCode = country1.Code ORDER BY city2.Population DESC LIMIT 1) != country1.Capital

ORDER BY
	(SELECT city2.Population FROM world.city AS city2 WHERE city2.CountryCode = country1.Code ORDER BY city2.Population DESC LIMIT 1) - city1.Population DESC

LIMIT
	12;