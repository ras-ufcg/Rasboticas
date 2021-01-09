import random

aleatorio = random.randint(1, 9)

num = int(input("Digite um número: "))

if num == aleatorio:
    print("\nVocê adivinhou o número gerado aleatoriamente")
if num > aleatorio:
    print("\nVocê inseriu um número mais alto do que o gerado aleatoriamente")
if num < aleatorio:
    print("\nVocê inseriu um número mais baixo do que o gerado aleatoriamente")

print("\nO número aleatório era:",aleatorio)