lista1 = list(range(10, 20, 2))
lista2 = list(range(1, 20, 3))
lista3 = list(set(lista2).intersection(lista1))
print('a =', lista1,'\nb =', lista2,'\nIntercessão =', lista3)