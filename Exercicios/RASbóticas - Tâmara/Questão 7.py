numeros = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

numerosPares = []

for elemento in numeros:
    if elemento % 2 == 0:
        numerosPares.append(elemento)

print(numerosPares)