invitados = [
    "Vinny Vinesauce",
    "Toddler Hiway",
    "Alfred Matthew Yankovic",
    "Mortadelo"
]

print(f"¡{invitados[0]}, estas invitad@ a cenar conmigo!")
print(f"¡{invitados[1]}, estas invitad@ a cenar conmigo!")
print(f"¡{invitados[2]}, estas invitad@ a cenar conmigo!")
print(f"¡{invitados[3]}, estas invitad@ a cenar conmigo!")
print()

print(f"Que mal que no puedas venir, {invitados[1]}. ¡Espero verte pronto!")
print()

invitados[1] = "Ikuya Kita"

print(f"¡{invitados[0]}, estas invitad@ a cenar conmigo!")
print(f"¡{invitados[1]}, estas invitad@ a cenar conmigo!")
print(f"¡{invitados[2]}, estas invitad@ a cenar conmigo!")
print(f"¡{invitados[3]}, estas invitad@ a cenar conmigo!")
print()

print("Gente, ¡Consegui una mesa más grande! ¡Esperen nuevo invitados!")
print()

invitados.insert(0, "Carl Johnson")
invitados.insert(3, "John Linnell")
invitados.append("Eso Brad")

print(f"¡{invitados[0]}, estas invitad@ a cenar conmigo!")
print(f"¡{invitados[1]}, estas invitad@ a cenar conmigo!")
print(f"¡{invitados[2]}, estas invitad@ a cenar conmigo!")
print(f"¡{invitados[3]}, estas invitad@ a cenar conmigo!")
print(f"¡{invitados[4]}, estas invitad@ a cenar conmigo!")
print(f"¡{invitados[5]}, estas invitad@ a cenar conmigo!")
print(f"¡{invitados[6]}, estas invitad@ a cenar conmigo!")
print()

print("Gente, me di cuenta que no llegara la mesa a tiempo. Solo van a ir los que diga yo.")

print(f"Lo siento, {invitados.pop()}, pero ya no estas invitad@. ¡Espero verte pronto!")
print(f"Lo siento, {invitados.pop()}, pero ya no estas invitad@. ¡Espero verte pronto!")
print(f"Lo siento, {invitados.pop()}, pero ya no estas invitad@. ¡Espero verte pronto!")
print(f"Lo siento, {invitados.pop()}, pero ya no estas invitad@. ¡Espero verte pronto!")
print(f"Lo siento, {invitados.pop()}, pero ya no estas invitad@. ¡Espero verte pronto!")
print()

print(f"¡{invitados[0]}, aún estas invitad@ a cenar conmigo!")
print(f"¡{invitados[1]}, aún estas invitad@ a cenar conmigo!")
print()

del(invitados[1])
del(invitados[0])

print(invitados)