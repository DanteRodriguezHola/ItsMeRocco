SELECT 
	summary.Name,
    summary.Capital,
    summary.TotalPopulation,
    summary.CityCount,
    summary.UrbanPopulation,
    summary.UrbanizedPopulation,
    summary.MainOfficialLanguage
    
FROM 
	world.country_summary AS summary
    
WHERE
	summary.Region = "South America"
    
ORDER BY
	summary.UrbanizedPopulation DESC;