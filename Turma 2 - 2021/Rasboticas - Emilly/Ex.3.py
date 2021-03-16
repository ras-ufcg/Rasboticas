import numpy as np
a = 1

while (a != 0):
  num = float(input("Digite um número que deseja obter o seno e o cosseno: "))
  seno = np.sin(num)
  cos = np.cos(num)
  print("Seno: {}, Cosseno: {}, Numero: {}".format(seno, cos, num))
  a = int(input("Deseja continuar? 1 - sim / 0 - não"))
