#Menu Delicato doceria
#Criadoras: Beatriz, Lunara e Nívia
#07/06/2021 V.1

from time import sleep
from sys import exit 
import cv2

imagem = cv2.imread("logo.png")
cv2.imshow("DelicatoDoceria", imagem)
cv2.waitKey(0)

#Função para exibir cadápio da doceria

def exibeCardapio():
  arq_menu= open("cardapiodoceria.txt", "a")
  arq_menu = open("cardapiodoceria.txt", "r")
  for i in arq_menu.readlines():
    print(i)
  arq_menu.close()
  main()  

#Função que mostra e salva classificações ao menu

ja_pedi=[] #variável que armazena pratos já provados
def jaPedidos():
  #MENU
  opc = int(input(''' Escolha uma opção:
  [1] - Adicionar nova avaliação
  [2] - Exibir avaliações dos já pedidos
  [3] - Menu Principal
  '''))
  if opc == 1: #Adicionar avaliação
    arquivo = open("ja_pedi.txt", "a") #arquivo que armazena notas
    name = input("Digite o nome da delícia pedida: ")
    avaliacao = input("Digite sua avaliação (0-5):")
    ja_pedi.append(name) #Add o pedido ao seu histórico
    ja_pedi.append(' ')
    ja_pedi.append(avaliacao) #Add avaliação do pedido ao histórico
    ja_pedi.append('\n') 
    arquivo.writelines(ja_pedi) #inserindo os dados da lista no arquivo.
    arquivo.close()

  elif opc == 2: #Exibir avaliações
    arquivo = open("ja_pedi.txt", "r") #Abrindo o arquivo com avaliações para leitura
    while True:
      j=0 #Ordenar
      for i in arquivo:
        val=i.split() #Separar nomes/avaliação
        print('[', j+1,']', val[0],'\nNota:', val[1],'\n')
        j+=1
      arquivo.close()
      print("Retornando ao Menu Principal...")
      sleep(2)
      main()
    
    
  elif opc == 3:   #Menu Principal
    main()
  else:    #Se digitar um numero errado
    print("ERROR 404 NOT FOUND")
    print("Retornando ao Menu Principal...")
    sleep(1)
  main()
  
def sobreDoceria():
  #arq_doceria=("doceria.txt", "a")
  arq_doceria = open("doceria.txt", "r")
  for i in arq_doceria.readlines():
    print(i)
  arq_doceria.close()
    
  main()  

#Escolha seu pedido

def escolhapedido():
  pedido = 0
  qtd = 0
  valor = 0
  pagar = 0
  while True:
    pedido = int(input("Digite o número correspondente ao seu pedido 1-7: "))
    if pedido>7 or pedido<1:      #Se digitar um numero errado
      print("ERROR 404 NOT FOUND")
      pedido = int(input("Digite o número correspondente ao seu pedido 1-7: "))
    qtd = int(input("Digite a quantidade de itens desejada: "))
    with open("valores.txt") as f:
      valor = int(f.readlines()[pedido - 1])
    print(valor)
    pagar += (valor * qtd)
    var = input("Já encerrou seu pedido? (Sim ou Não) ")
    while var!= "Não" and var!= "Sim":    #Se digitar entrada errada
      print("ERROR 404 NOT FOUND")
      var = input("Já encerrou seu pedido? (Sim ou Não) ")
    if var == "Sim":
      print("O valor a ser pago é de %d reais" %pagar)
      break
    
  main()

#MENUPRINCIPAL

def main():
  print("\n")
  print("Bem-vindo à Delicato Doceria!!!")
  opcao = int(input('''Escolha a opção desejada: \n
     1 - Nosso cardápio
     2 - Seu histórico e avaliação de pedidos
     3 - Conheça nosso cantinho
     4 - Escolha seu pedido
     5 - Exit
     
     Digite aqui o número da sua opção: '''))

  if opcao == 1:   #Nosso cardápio
    exibeCardapio()
  elif opcao == 2: #Histórico e avaliação de pedidos
    jaPedidos()
  elif opcao == 3: #Conheça nosso cantinho
    sobreDoceria()
  elif opcao == 4: #Escolha seu pedido
    escolhapedido()
  else:
    print("Obrigado pela confiança e volte sempre!")
    exit()

#Programa Principal

main()
