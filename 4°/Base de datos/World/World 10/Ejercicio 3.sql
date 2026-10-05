UPDATE 
	world.metropoli AS metropoli1

SET
	PctPoblacionPais = TRUNCATE(metropoli1.Poblacion / (SELECT country2.Population FROM world.country AS country2 WHERE country2.Code = metropoli1.CodigoPais) * 100, 2)