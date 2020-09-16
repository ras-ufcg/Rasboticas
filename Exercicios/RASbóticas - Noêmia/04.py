divisor = int(input("Digite um numero: "))
lista_original = list(range(1, divisor+1))
divisores = []
for num in lista_original:
    if divisor % num== 0:
        divisores.append(num)
print(divisores)
