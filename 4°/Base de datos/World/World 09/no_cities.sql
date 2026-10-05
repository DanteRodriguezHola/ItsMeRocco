SELECT
	country1.Code AS "Code",
    country1.Name AS "Country",
    country1.Continent AS "Continent",
    country1.Population AS "Population",
    country1.SurfaceArea AS "SurfaceArea"

FROM
	world.country AS country1
    LEFT JOIN world.city AS city1
		ON city1.CountryCode = country1.Code
        
WHERE
	city1.CountryCode IS NULL