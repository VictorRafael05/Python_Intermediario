lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))    # Modelo sem list comprehension
lista = [
    (x, y) for x in range(3) for y in range(3)

]                             # Modelo com list comprehension

print(lista)