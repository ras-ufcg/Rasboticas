import random
jogo = int(input('Iniciar o jogo? [0/1]: '))
palpites=0
while (jogo != 0):
    sorteado = random.randint(1, 9)
    jogada = int(input("Adivinhe o numero sorteado [1-9]: "))
    while jogada != sorteado:
        palpites+=1
        if jogada < sorteado:
            print('Palpite baixo!')
            jogada = int(input("Adivinhe o numero sorteado [1-9]: "))
        elif jogada > sorteado:
            print('Palpite alto')
            jogada = int(input("Adivinhe o numero sorteado [1-9]: "))
    print('Parabenns! Voce acertou! O numero é', sorteado, '\nQuantidade de palpites:', palpites)
    jogo = int(input("\n\nJogar novamente? [0/1]:  "))