CREATE VIEW `country_summary` AS
	SELECT
		country1.Code,
		country1.Name,
		country1.Continent,
		country1.Region,
		
		# Capital
		IFNULL(
			(SELECT
				city2.Name
				
			FROM
				world.city AS city2
				JOIN world.country AS country2
					ON country2.Capital = city2.ID
					
			WHERE
				country2.Code = country1.Code),
			NULL) AS "Capital",
		
		# City Count
		(SELECT
			count(city2.ID)
		
		FROM 
			world.city AS city2
		
		WHERE
			city2.CountryCode = country1.Code) AS "CityCount",
		
		country1.Population AS "TotalPopulation",
		
		# Urban Population
		IFNULL(
			(SELECT 
				SUM(city2.Population)
			
			FROM
				world.city AS city2
			
			WHERE
				city2.CountryCode = country1.Code),
			0) AS "UrbanPopulation",
			
		# Urbanized Population
		CAST(
			(NULLIF(
				(SELECT 
					SUM(city2.Population)
			
				FROM
					world.city AS city2
				
				WHERE
					city2.CountryCode = country1.Code),
			0) / country1.Population) * 100 
		AS DECIMAL(4, 1)) AS "UrbanizedPopulation",
			
		# Main Official Language
		IFNULL(
			(SELECT
				language2.Language
				
			FROM 
				world.countrylanguage AS language2

			WHERE
				language2.CountryCode = country1.Code AND
				language2.IsOfficial = "T"
				
			ORDER BY
				language2.Percentage DESC
				
			LIMIT
				1),
		NULL) AS "MainOfficialLanguage"
		
	FROM
		world.country AS country1
