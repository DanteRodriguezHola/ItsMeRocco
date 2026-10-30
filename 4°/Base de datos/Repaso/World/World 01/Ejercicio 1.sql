USE `world`;

DROP procedure IF EXISTS `codigo_pais`;

DELIMITER $$

USE `world`$$

CREATE PROCEDURE `codigos_pais` (IN PName CHAR(32))
BEGIN
    
	SELECT
		country1.Code
        
	FROM
		country AS country1
        
	WHERE
		country1.Name = PName;

END$$

DELIMITER ;