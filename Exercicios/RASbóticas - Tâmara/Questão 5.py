listaB = [1, 1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 9, 10, 11, 11]
listaC = [2, 3, 4, 4, 6, 6, 8, 10, 11, 12]

listaX = []  #lista vazia para os elementos que foram comuns nas duas listas sem repetições

for elemento in listaB:
    if elemento in listaC:  #verificando se o elemento também está em listaC
        if elemento not in listaX:  #verificando se o elemento já está na listaX
            listaX.append(elemento)  #adicionando elemento a lista

print(listaX)