a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = []
for numero in a:
    if numero < 5:
        b.append(numero)
print('Menores que 5 =', b)
num_usuario = int(input("Digite um numero: "))
for num1 in a:
    if num1 < num_usuario:
        c.append(num1)
print('Menores que', num_usuario, '=', c)
