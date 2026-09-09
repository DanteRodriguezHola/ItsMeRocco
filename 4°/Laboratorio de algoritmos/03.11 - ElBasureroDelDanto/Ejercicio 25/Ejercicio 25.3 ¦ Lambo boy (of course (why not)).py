def hacer_auto(fabricante, modelo, **info_auto):
    info_auto.update({"fabricante": fabricante})
    info_auto.update({"modelo": modelo})
    return info_auto

lambo = hacer_auto("Automobili Lamborghini S.p.A.", "Lamborghini",
                   propietario = "Mi primillo shico",
                   color = "rojo"
                   )

print(lambo)