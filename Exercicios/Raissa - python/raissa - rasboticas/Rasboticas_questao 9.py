'''Raissa Taina Pordeus Ferreira
Questa 09 - Esta questao era numeros aleatorios entre 1 e 9, para o usuario acertar'''
from random import randint
a = (randint(1,9))
b = input("Advinhe um numero no intervalo entre 1 e 9:\n")
b = int(b);
if (a == b):
  print("Voce acertou!!!!")
else:
  print("Voce errou. Tente novamemnte.")