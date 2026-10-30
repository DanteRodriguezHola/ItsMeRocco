USE `world`;

DROP procedure IF EXISTS `datos_continente`;

DELIMITER $$

USE `world`$$

CREATE PROCEDURE `datos_continente` (IN PContinente ENUM('Asia', 'Europe', 'North America', 'Africa', 'Oceania', 'Antarctica', 'South America'))
BEGIN
	
	SELECT
		country1.Region AS 'region',
		COUNT(country1.Code) AS 'cantidad_paises',
		SUM(country1.Population) AS 'poblacion_total'
		
	FROM
		country AS country1

	WHERE
		country1.Continent = PContinente
		
	GROUP BY
		region;
        
END$$

DELIMITER ;