UPDATE 
    world.metropoli AS metropoli1

SET
    EsCapital = IF(metropoli1.CityID = (SELECT country2.Capital FROM world.country AS country2 WHERE country2.Code = metropoli1.CodigoPais), 'S', 'N')
