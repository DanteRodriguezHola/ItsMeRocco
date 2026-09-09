rios_paises = {
    "amazonas": "brasil",
    "colorado": "argentina",
    "san lorenzo": "canadá"
    }

for rio, pais in rios_paises.items():
    print(f"El río {rio.title()} pasa por {pais.title()}.")
print()

for rio in rios_paises.keys():
    print(f"Río {rio.title()}")
print()

for pais in rios_paises.values():
    print(pais.title())