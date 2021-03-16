import numpy as np
matrizA = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
for l in range(0,4):
  for c in range(0,4):
    matrizA[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

matrizB = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
for l in range(0,4):
  for c in range(0,4):
    matrizB[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
   
print()    
print(matrizA,"\n")
print(matrizB,"\n")

print('''O que voce quer calcular? 
     [0] - Soma
     [1] - Subtraçao
     [2] - Multiplicaçao
     [3] - Divisao
     [4] - Produto
     [5] - Concatenaçao''')

itens = ['Soma', 'Subtraçao', 'Multiplicaçao', 'Divisao', 'Produto', 'Concatenaçao']

opcao = 'Yes'

while opcao == 'Yes' :
    usuario = int(input("Qual você escolhe? "))
    print('O usuario escolheu: ', itens[usuario])
    print('=-'*15)

    print('O resultado é...')

    if usuario == 0:
      Soma = np.add(matrizA,matrizB)
      print(Soma)
      
    elif usuario == 1:
      Sub = np.subtract(matrizA,matrizB)
      print(Sub)

    elif usuario == 2:
      Mult = np.dot(matrizA,matrizB)
      print(Mult)

    elif usuario == 3:
      Div = np.divide(matrizA,matrizB)
      print(Div)

    elif usuario == 4:
      Prod = np.matmul(matrizA,matrizB)
      print(Prod)

    elif usuario == 5:
      Conc = np.concatenate((matrizA,matrizB))
      print(Conc)

    else:
        print("Inválido")

    opcao = str(input('''Deseja calcular novamente? Digite ''Yes''
                       Para encerrar aperte em qualquer tecla'''))
