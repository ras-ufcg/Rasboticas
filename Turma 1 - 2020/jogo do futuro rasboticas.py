from random import randint
import random
import string

print('\n','-'*15,'Jogo do Futuro', '-'*15)
verificacao = int(input('\n\nInforme um numero não nulo e positivo para verificacao: '))
while verificacao >0:
  while verificacao > 0:
      print('\n','='*64, '\n\n   Com foco, rasah e determinacao, apresentamos:\n                  Jogo do futuro\n\n','='*64)
      nome = str(input('\nQual o seu nome? '))
      idade = int(input('\nQual a sua idade? '))
      filhos = int(input('\nVocê pretende ter filhos? Se sim, digite 1. Se não, digite 0: '))
      if (filhos == 1):
        quantfilhos = int(input('\nQuantos filhos voce pretende ter? '))
      amante = int(input('\nVocê pretende casar? Se sim, digite 1. Se não, digite 0: '))
      if (amante == 1):
        preferencia = int(input('\nVocê pretende casar com homem ou mulher? Digite 0 para homem e 1 para mulher:'))
      verificacao1 = int(input('Seus dados estao corretos? Se sim, digite 1, caso não, digite 0 para repetir o preenchimento de dados:'))
      if (verificacao1 == 1):
        break
  #segundo laco de repeticao
  if (verificacao1 == 1):
  #para gerar a idade em que o usuario ficara rico
    print('='*64)
    print('Bem vindx ao futuro!! Raissa e Sarah vêm do futuro para anunciar os seguintes fatos:')
    print('\n\n', nome, 'você ficará rico com ', randint(idade,100), 'anos')
    if (filhos == 1):
      print('Você pretende ter',quantfilhos, 'filhos')
      print('Mas tera ',randint(0,6))
    if (amante == 1):
        if (preferencia == 0):
          aleatorio = randint(1,4)
          if (aleatorio == 1):
            print('Seu pretendente terá os olhos castanhos')
          if (aleatorio == 2):
            print('Seu pretendete terá os olhos azuis')
          if(aleatorio == 3):
            print('Seu pretendente terá os olhos verdes')
          if (aleatorio == 4):
            print('Seu pretendente terá os olhos pretos')
          print('e tera', randint(18,50), 'anos.')
          lista = ['enfermeiro', 'designer', 'advogado', 'engenheiro', 'professor', 'policial', 'ator', 'empresário',
                    'médico']
          profissao = random.choice(lista)
          print('A profissao dele será', profissao)
          letras = string.ascii_uppercase
          codigo = ''.join(random.choice(letras))
          print('A inicial do nome dele será:', codigo)
          print('='*64)
        if (preferencia == 1):
          aleatorio = randint(1,4)
          if (aleatorio == 1):
            print('Sua pretendente terá os olhos castanhos')
          if (aleatorio == 2):
            print('Sua pretendete terá os olhos azuis')
          if(aleatorio == 3):
            print('Sua pretendente terá os olhos verdes')
          if (aleatorio == 4):
            print('Sua pretendente terá os olhos pretos')
          print('e tera ', randint(18,50), 'anos.')
          lista = ['enfermeira', 'designer', 'advogada', 'engenheira', 'professora', 'policial', 'atriz', 'empresaria', 'medica']
          profissao = random.choice(lista)
          print('A profissao dela será', profissao)
          letras = string.ascii_uppercase
          codigo = ''.join(random.choice(letras))
          print('A inicial do nome dela será: ', codigo)
          print('='*64)
    repetirjogo = int(input('Deseja jogar novamente? digite 1 para sim e 0 para nao '))
    if (repetirjogo == 1):
      verificacao = 1
    if (repetirjogo == 0):
      print('\nFIM!!')
      verificacao = 0
