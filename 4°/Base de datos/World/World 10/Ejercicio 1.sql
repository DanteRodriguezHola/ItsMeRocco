CREATE TABLE `world`.`metropoli` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `CityID` INT NOT NULL,
  `Nombre` VARCHAR(35) NOT NULL,
  `CodigoPais` CHAR(3) NOT NULL,
  `Continente` VARCHAR(20) NOT NULL,
  `Poblacion` INT NOT NULL,
  `PctPoblacionPais` DECIMAL(5,2) NULL DEFAULT NULL,
  `EsCapital` ENUM('S', 'N') NOT NULL DEFAULT 'N',
  `FechaCarga` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `CityID_UNIQUE` (`CityID` ASC) VISIBLE,
  INDEX `fk_metropoli_country_idx` (`CodigoPais` ASC) INVISIBLE,
  CONSTRAINT `fk_metropoli_city`
    FOREIGN KEY (`CityID`)
    REFERENCES `world`.`city` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_metropoli_country`
    FOREIGN KEY (`CodigoPais`)
    REFERENCES `world`.`country` (`Code`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
