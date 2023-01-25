
palav = str(input("Digite uma palavra: "))
reverso = palav [::-1]#comando que pega o elemento do fim ao começo
print("O reverso dessa palavra é:")
print(reverso)
if palav == reverso:
    print("Essa palavra é um palíndromo")
else:
     print("Essa palavra não é um palíndromo")



