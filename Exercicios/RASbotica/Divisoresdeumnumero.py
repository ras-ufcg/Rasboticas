
numero = int(input("\n\nDigite um numero para verificação: "))

print("Lista de divisores desse numero:")

listRange = list (range(1, numero+1))

divisoresList = []

for num in listRange:

    if numero % num == 0:
        divisoresList.append(num)

print(divisoresList)
