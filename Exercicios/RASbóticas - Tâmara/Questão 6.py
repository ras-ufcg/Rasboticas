string = str(input("Digite uma palavra: "))
print("\na palavra:", string[0:])  #exibindo a lista a partir do elemento inicial

contrario = string[:: -1]  #exibindo a lista a partir do último elemento
print("contrário:", contrario)

if string == contrario:
    print("\nA palavra digitada é um palíndromo")
else:
    print("\nA palavra digitada não é um palíndromo")