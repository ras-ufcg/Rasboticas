palavra = str(input("Digite uma palavra: "))
inverte = palavra[::-1] 
if palavra == inverte:
    print(palavra, 'é um palíndromo!')
else:
    print(palavra, 'não é um palíndromo!')