'''Raissa Taina Pordeus Ferreira
Questa 06 -Esta questao pede uma string ao usuario e retorna se ela e palindroma ou nao'''
p1=input("informe uma palavra: ")
p2=p1[::-1]
if p1 == p2:
    print ("e um palindromo")
else:
    print ("nao e um palindromo")