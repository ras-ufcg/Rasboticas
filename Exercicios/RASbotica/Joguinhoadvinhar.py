import random
numero = random.randint(1,9)
aposta = 0
contador = 0

print("Joguinho advinhador. Qual será o número de 1 a 9?")
for aposta != numero and aposta != "exit":
    aposta = input("Qual seu palpite?")

    if aposta == "exit":

        break

    aposta = int(aposta)
    contador += 1

    if aposta < numero:
        print("Aposta muito baixa")

    elif aposta > numero:
        print("Aposta muito alta")

        else:
            print("Acertô, pivete!!")
            print("Você precisou de", contador,"chances para acertar")
            
