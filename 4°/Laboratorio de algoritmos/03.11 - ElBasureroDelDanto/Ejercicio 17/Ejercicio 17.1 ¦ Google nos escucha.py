paul_info = {
    "nombre": "Paul",
    "apellido": "McCartney",
    "edad": 83,
    "ciudad": "Liverpool"
    }

john_info = {
    "nombre": "John",
    "apellido": "Linnell",
    "edad": 66,
    "ciudad": "Nueva York"
    }

alfred_info = {
    "nombre": "Alfred",
    "apellido": "Yankovic",
    "edad": 66,
    "ciudad": "Lynwood"
    }

gente = [paul_info, john_info, alfred_info]

for persona in gente:
    print(persona["nombre"])
    print(persona["apellido"])
    print(persona["edad"])
    print(persona["ciudad"])
    print()