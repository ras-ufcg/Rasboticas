num = int(input("Digite um numero: "))
if num%2 == 0 & num%4 == 0:
    print("O numero eh par e multiplo de 4")
elif num%2 == 0 & num%4 != 0:
    print("O numero eh par")
elif num%2 != 0:
    print("O numero eh impar")
num1 = int(input("Numero para verificar multiplo: "))
num2 = int(input("Numero para dividir: "))
if num1%num2==0:
    print("a divisao foi exata, ou seja eh multiplo")
else: 
    print("a divisao foi inexata, ou seja nao eh multiplo")