SELECT
	metropoli1.Continente AS 'Continente',
    COUNT(metropoli1.ID) AS 'Metropolis',
    MAX(metropoli1.PctPoblacionPais) AS "MayorPeso",
    (SELECT COUNT(metropoli2.ID) FROM world.metropoli AS metropoli2 WHERE metropoli2.Continente = metropoli1.Continente AND metropoli2.EsCapital = 'S') AS "Capitales"

FROM 
	world.metropoli AS metropoli1
    
GROUP BY
	metropoli1.Continente