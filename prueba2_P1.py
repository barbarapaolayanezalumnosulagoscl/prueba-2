notas = []
nota = float(input("Ingrese una nota (0 es para terminar): "))

while nota != 0:
    notas.append(nota)
    nota = float(input("Ingrese otra nota (0 es para terminar): "))

cantidad_notas = 0
suma_notas = 0
notas_bajo_4 = 0
notas_sobre_4 = 0

for n in notas:
    cantidad_notas += 1
    suma_notas += n
    if n < 4.0:
        notas_bajo_4 += 1
    else:
        notas_sobre_4 += 1

promedio = suma_notas / cantidad_notas

print("Cantidad de notas:", cantidad_notas)
print("______________________________")
print("Promedio de notas:", promedio)
print("______________________________")
print("Notas bajo 4.0:", notas_bajo_4)
print("______________________________")
print("Notas sobre 4.0:", notas_sobre_4)
