from pathlib import Path

pi = Path("pi.txt")
contenido = pi.read_text()

fecha = input("Ingrese su fecha de nacimiento (ddmmaa) --> ")

if fecha in contenido:
    print("¡Tu fecha de nacimiento aparece en el primer millon de digitos de pi! :D")
    
else:
    print("Tu fecha de nacimiento no aparece en el primer millon de digitos de pi. :C")