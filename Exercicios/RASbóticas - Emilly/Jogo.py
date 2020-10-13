from random import randint
from time import sleep
print('=-'*15)
print('Pedra, Papel e Tesoura')
print('=-'*15)

nome = str(input('Digite seu nome'))

print('''Suas opções são:
     [0] - Pedra
     [1] - Papel
     [2] - Tesoura''')

itens = ['Pedra', 'Papel', 'Tesoura']

opcao = 'Yes'

while opcao == 'Yes':
    jogador = int(input("Qual é a sua jogada?"))
    computador = randint(0,2)
    print('Pedra')
    sleep(1)
    print('Papel')
    sleep(1)
    print('E Tesoura!!!')

    print('=-'*15)
    print('O computador jogou', itens[computador])
    print(nome,'jogou', itens[jogador])
    print('=-'*15)

    print('O resultado é...')
    sleep(1)


    if computador == 0: #Computador jogou pedra
        if jogador == 0:
            print('Empate')
        elif jogador == 1:
            print(nome, 'venceu!')
        elif jogador == 2:
            print('Computador venceu!')

    if computador == 1: #Computador jogou papel
        if jogador == 1:
            print('Empate')
        elif jogador == 2:
            print(nome, 'venceu!')
        elif jogador == 0:
            print('Computador venceu!')

    if computador == 2: #Computador jogou tesoura
        if jogador == 2:
            print('Empate')
        elif jogador == 0:
            print(nome, 'venceu!')
        elif jogador == 1:
            print('Computador venceu!')
        else:
            print('Jogada Inválida')
            
    opcao = str(input('''Deseja jogar novamente? Digite ''Yes''
                       Para encerrar o jogo aperte em qualquer tecla'''))
                       

