'''Raissa Taina Pordeus Ferreira
Questa 02 - informa se um numero e par ou impar'''
numero=input("Informe um numero")
numero=int(numero)
numero=numero%2
if numero == 0:
  print("seu numero e par")
elif numero!=0:
  print("seu numero e impar")
