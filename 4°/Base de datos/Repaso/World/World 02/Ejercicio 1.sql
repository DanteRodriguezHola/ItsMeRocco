USE `world`;

DROP procedure IF EXISTS `comparo_paises`;

DELIMITER $$

USE `world`$$

CREATE PROCEDURE `comparo_paises` (IN PCodigoPais1 CHAR(3), IN PCodigoPais2 CHAR(3))
BEGIN
	DECLARE PCodigoGanador CHAR(3);
    DECLARE Poblacion1 INT;
    DECLARE Poblacion2 INT;
    
    SET Poblacion1 = (SELECT co1.population FROM country AS co1 WHERE co1.Code = PCodigoPais1);
    SET Poblacion2 = (SELECT co1.population FROM country AS co1 WHERE co1.Code = PCodigoPais2);
    
    IF Poblacion1 > Poblacion2 THEN
		SET PCodigoGanador = PCodigoPais1;
        
	ELSEIF Poblacion2 > Poblacion1 THEN
		SET PCodigoGanador = PCodigoPais2;
    
    ELSE
		SET PCodigoGanador = '---';
	
    END IF;
    
	IF PCodigoGanador = '---' THEN
		SELECT Poblacion1 AS 'La misma cantidad de habitantes en ambos paises';
        
	ELSE
		SELECT
			country1.Name AS 'pais',
			country1.Continent AS 'continente',
			(SELECT 
				language2.Language 
			
			FROM 
				countrylanguage AS language2 
			
			WHERE 
				language2.CountryCode = country1.Code AND
				language2.IsOfficial = 'T'
			
			ORDER BY 
				language2.Percentage 
			
			LIMIT 1)
			AS 'idioma_oficial',
			country1.Population AS 'habitantes',
			(SELECT 
				COUNT(DISTINCT city2.District) 
			
			FROM
				city AS city2 
			
			WHERE
				city2.CountryCode = country1.Code
			
			GROUP BY 
				city2.CountryCode)
			AS 'estados_pcias'
			
		FROM
			country AS country1
            
		WHERE
			country1.Code = PCodigoGanador;
	
    END IF;
    
END$$

DELIMITER ;