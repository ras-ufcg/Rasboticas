# Jogo pedra, papel e tesoura, largato ou spock
from random import randint
from time import sleep


print('-='*15)
print(' PEDRA, PAPEL, TESOURA, LARGATO OU SPOCK ')
print('-='*15)
opcao = 'YES'
nome = str(input("Digite seu nome: "))

print(''' Escolha sua jogada:
          [0] PEDRA
          [1] PAPEL
          [2] TESOURA
          [3] LARGATO
          [4] SPOCK ''')

print('-='*15)

while opcao == 'YES':
  jogador = int(input("Digite sua jogada: "))
  computador = randint(0,2)

  print('-='*15)
  print('PEDRA')
  sleep
  print('PAPEL')
  sleep
  print('TESOURA')
  sleep
  print('LARGATO')
  sleep
  print('SPOCK')
  print('-='*15)

  itens = ['Pedra', 'Papel', 'Tesoura', 'Largato', 'Spock']
  print('-='*15)
  print('O COMPUTADOR JOGOU', itens[computador])
  print(nome, 'JOGOU' , itens[jogador])
  print('-='*15)

  if computador == 0:       #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
      print("EMPATE") 
    elif jogador == 1:
      print(nome, "VENCEU!")
    elif jogador == 2:
      print("COMPUTADOR VENCEU")
    elif jogador == 3:
      print('COMPUTADOR VENCEU')
    elif jogador == 4:
      print(nome, 'VENCEU')
    else: 
      print("JOGADA INVÁLIDA")
      
  if computador == 1:       #COMPUTADOR JOGOU PAPEL
    if jogador == 1:
      print("EMPATE") 
    elif jogador == 2:
      print(nome, "VENCEU!")
    elif jogador == 0:
      print("COMPUTADOR VENCEU")
    elif jogador == 3:
      print(nome, 'VENCEU')
    elif jogador == 4:
      print('COMPUTADOR VENCEU')   
    else: 
      print("JOGADA INVÁLIDA")    

  if computador == 2:       #COMPUTADOR JOGOU TESOURA
    if jogador == 2:
      print("EMPATE") 
    elif jogador == 0:
      print(nome, "VENCEU!")
    elif jogador == 1:
      print("COMPUTADOR VENCEU")
    elif jogador == 3:
      print('COMPUTADOR VENCEU')
    elif jogador == 4:
      print(nome, 'VENCEU')    
    else: 
      print("JOGADA INVÁLIDA")  

  if computador == 3:       #COMPUTADOR JOGOU LARGATO
    if jogador == 3:
      print("EMPATE") 
    elif jogador == 0:
      print(nome, "VENCEU!")
    elif jogador == 1:
      print("COMPUTADOR VENCEU")
    elif jogador == 2:
      print(nome, 'VENCEU')
    elif jogador == 4:
      print('COMPUTADOR VENCEU')    
    else: 
      print("JOGADA INVÁLIDA")    

  if computador == 4:       #COMPUTADOR JOGOU SPOCK
    if jogador == 4:
      print("EMPATE") 
    elif jogador == 0:
      print(nome, "VENCEU!")
    elif jogador == 1:
      print("COMPUTADOR VENCEU")
    elif jogador == 2:
      print('COMPUTADOR VENCEU')
    elif jogador == 3:
      print(nome, 'VENCEU')    
    else: 
      print("JOGADA INVÁLIDA")

  opcao = str(input('''Você deseja continuar? Se sim digite YES: 
                    Se não aperte qualquer tecla. '''))
