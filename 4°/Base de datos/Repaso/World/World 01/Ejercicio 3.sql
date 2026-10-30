USE `world`;

DROP procedure IF EXISTS `paises_idiomas`;

DELIMITER $$

USE `world`$$

CREATE PROCEDURE `paises_idiomas` (IN PIdioma CHAR(30), IN PPorcertaje INT)
BEGIN

	# 3.1 #
    
    SELECT
		country1.Name as 'nombre',
        language1.Percentage as 'porcentaje'
        
	FROM
		countrylanguage AS language1
		
        JOIN country AS country1 ON
			country1.Code = language1.CountryCode
            
	WHERE
		language1.Name = PIdioma AND
        language1.Percentage > PPorcentaje;
        
	# 3.2 #
    
    SELECT
		country1.Continent AS 'continente',
		COUNT(language1.CountryCode) AS 'cantidad'
    
	FROM
		countrylanguage AS language1
		
		JOIN country AS country1 ON
			country1.Code = language1.CountryCode
			
	WHERE
		language1.Language = PIdioma

	GROUP BY
		continente;
        
	# 3.3 #
    
    SELECT
		country1.Name AS 'pais',
		language1.Language AS 'idioma'
		
	FROM
		countrylanguage AS language1
		
		JOIN country AS country1 ON
			country1.Code = language1.CountryCode
			
	WHERE
		language1.Language != PIdioma AND
		country1.Code IN (
			SELECT
				language2.CountryCode
				
			FROM
				countrylanguage AS language2
				
			WHERE
				language2.Language = PIdioma
			);
            
END$$

DELIMITER ;