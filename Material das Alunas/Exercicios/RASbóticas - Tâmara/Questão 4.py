num = int(input("Digite um número: "))

listaNumeros = list(range(1, num + 1)) #função range: start = 1 stop = num + 1

listaDivisores = [] #lista vazia para os valores que irão ser encontrados

for elemento in listaNumeros:
    if num % elemento == 0:
        listaDivisores.append(elemento)

print(listaDivisores)
