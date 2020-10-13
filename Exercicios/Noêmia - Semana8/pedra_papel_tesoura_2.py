from random import randint
from time import sleep

print('--'*20)
print('PEDRA, PAPEL, TESOURA, LAGARTOS E SPOCK')
print('--'*20)

nome = str(input("Digite seu nome: "))

print('''Suas opções são:
     [0] - Pedra
     [1] - Papel 
     [2] - Tesoura
     [3] - Lagarto
     [4] - Spock ''')

itens = ['PEDRA', 'PAPEL', 'TESOURA', 'LAGARTO', 'SPOCK']

opcao = 's' 

while(opcao == 's'):

    print('''Suas opções são:
     [0] - Pedra
     [1] - Papel 
     [2] - Tesoura
     [3] - Lagarto
     [4] - Spock ''')
    jogador = int(input("Faça sua jogada: "))
    computador = randint(0,2)

    print('--'*20)
    print('PEDRA')
    sleep(1)
    print('PAPEL')
    sleep(1)
    print('TESOURA')
    sleep(1)
    print('LAGARTO')
    sleep(1)
    print('E SPOCK!')
    print('--'*20)
    sleep(1)
    print('O COMPUTADOR JOGOU ', itens[computador])
    print(nome, ' JOGOU ', itens[jogador])
    print('--'*20)
    sleep(1)
    print('O RESULTADO É... \n')
    sleep(1)

    if computador == 0: #Computador jogou pedra
        if jogador == 0: #pedra
            print('EMPATE!')
        elif jogador == 1: #papel
            print(nome,  'VENCEU!')
        elif jogador == 2: #tesoura
            print('COMPUTADOR VENCEU!')
        elif jogador == 3: #lagarto
            print('COMPUTADOR VENCEU!')
        elif jogador == 4: #spock
            print(nome,  'VENCEU!')
        else:
            print('JOGADA INVÁLIDA')

    if computador == 1: #Computador jogou papel
        if jogador == 0: #pedra
            print('COMPUTADOR VENCEU!')
        elif jogador == 1: #papel
            print('EMPATE!')
        elif jogador == 2: #tesoura
            print(nome, 'VENCEU!')
        elif jogador == 3: #lagarto
            print(nome, 'VENCEU!')
        elif jogador == 4: #spock
            print('COMPUTADOR VENCEU!')
        else:
            print('JOGADA INVÁLIDA')

    if computador == 2: #Computador jogou tesoura
        if jogador == 0: #pedra
            print(nome, 'VENCEU!')
        elif jogador == 1: #papel
            print('COMPUTADOR VENCEU!')
        elif jogador == 2: #tesoura
            print('EMPATE!')
        elif jogador == 3: #lagarto
            print('COMPUTADOR VENCEU!')
        elif jogador == 4: #spock
            print(nome, 'VENCEU!')
        else:
            print('JOGADA INVÁLIDA')
    
    if computador == 3: #Computador jogou lagarto
        if jogador == 0:
            print(nome, 'VENCEU!')
        elif jogador == 1: #papel
            print('COMPUTADOR VENCEU!')
        elif jogador == 2: #tesoura
            print(nome, 'VENCEU!')
        elif jogador == 3: #lagarto
            print('EMPATE!')
        elif jogador == 4: #spock
            print('COMPUTADOR VENCEU!')
        else:
            print('JOGADA INVÁLIDA')
    
    if computador == 4: #Computador jogou spock
        if jogador == 0:
            print('COMPUTADOR VENCEU!')
        elif jogador == 1: #papel
            print(nome, 'VENCEU!')
        elif jogador == 2: #tesoura
            print('COMPUTADOR VENCEU!')
        elif jogador == 3: #lagarto
            print(nome, 'VENCEU!')
        elif jogador == 4:
            print('EMPATE!')
        else:
            print('JOGADA INVÁLIDA')

    opcao = str(input('\nDESEJA JOGAR NOVAMENTE? DIGITE "s" \nPARA ENCERRAR APERTE QUALQUER TECLA\n'))

print('-'*15)
print('JOGO ENCERRADO!')
print('-'*15)