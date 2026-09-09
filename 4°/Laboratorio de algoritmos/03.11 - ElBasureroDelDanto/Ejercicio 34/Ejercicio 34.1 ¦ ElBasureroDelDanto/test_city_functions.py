from city_functions import devolver_ciudad_pais

def test_devolver_ciudad_pais():
    ciudad_pais = devolver_ciudad_pais("Buenos Aires", "Argentina")
    assert ciudad_pais == "Buenos Aires, Argentina"

test_devolver_ciudad_pais()