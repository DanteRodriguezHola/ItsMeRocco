from city_functions import devolver_ciudad_pais

def test_devolver_ciudad_pais():
    ciudad_pais = devolver_ciudad_pais("Buenos Aires", "Argentina")
    assert ciudad_pais == "Buenos Aires, Argentina"

def test_devolver_ciudad_pais_poblacion():
    ciudad_pais = devolver_ciudad_pais("Buenos Aires", "Argentina", 67692763211338)
    assert ciudad_pais == "Buenos Aires, Argentina - Población: 67692763211338"

test_devolver_ciudad_pais()
test_devolver_ciudad_pais_poblacion()