
#---------------------------------------
#Rasboticas Movies
#Author: Projeto Rasboticas
#10/05/2021 V.1
#---------------------------------------
# -*- coding: utf-8 -*-
from time import sleep
from sys import exit 
import cv2

imagem = cv2.imread("Semana 7.png")
cv2.imshow("RASboticas", imagem)
cv2.waitKey(0)
#---------------------------------------
#Função que exibe as sugestões de filmes
#---------------------------------------
def exibeFilmes():
  arq_filmes=open("filmesSinopses.txt", "a")
  arq_filmes = open("filmesSinopses.txt", "r")
  for i in arq_filmes.readlines():
    print(i)
    sleep(0.5)
  arq_filmes.close()
  main()
  
seus_filmes=[] #variável que armazena filmes assistidos

#---------------------------------------
#função que exibe/armazena os filmes que você assistiu com suas respectivas classificações
#---------------------------------------
def filmesAssistidos():
  
  opc = int(input(''' Escolha uma opção:
  [1] - Adicionar um novo Filme/Classificação
  [2] - Exibir Filmes/Classificação
  [3] - Menu Principal
  '''))
  if opc == 1:
    arquivo = open("seus_filmes.txt", "a") #criando o arquivo que armazena seus filmes/notas

    name = input('Digite o nome do filme assistido: ')
    classificacao = input('Digite sua classificacao 0-5:')
    seus_filmes.append(name)
    seus_filmes.append(' ')
    seus_filmes.append(classificacao)
    seus_filmes.append('\n') 
    arquivo.writelines(seus_filmes)
    arquivo.close()

  elif opc == 2:
    arquivo = open("seus_filmes.txt", "r")
    #Exibindo seus filmes/notas
    while True:
      j=0
      for i in arquivo:
        val=i.split()
        print('[', j+1,']', val[0],'\nNota:', val[1],'\n')
        j+=1
      arquivo.close()
      print('Retornando ao Menu Principal...')
      sleep(2)
      main()
    
    
  elif opc == 3:
    main()
  else:
    print('ERROR 404 NOT FOUND')
    print('Retornando ao Menu Principal...')
    sleep(1)
  main()  
def conhecaProjeto():
  #arq_projeto=("rasboticas.txt", "a")
  arq_projeto = open("rasboticas.txt", "r")
  for i in arq_projeto.readlines():
    print(i)
    sleep(1)
  arq_projeto.close()
    
  main()  
#---------------------------------------
#Instruções do programa
#---------------------------------------
def instrucoes():
  #arq_intrucoes=("instrucoes.txt", "a")
  arq_intrucoes = open("instrucoes.txt", "r")
  for i in arq_intrucoes.readlines():
    print(i)
    sleep(0.5)
  arq_intrucoes.close()


  main()
#---------------------------------------
#MENUPRINCIPAL
#---------------------------------------
def main():
  print('\n\n')
  print('-'*35)
  print('Bem-vindas ao RASbóticas Movies!!!')
  print('-'*35)
  opcao = int(input('''Escolha a opção que você deseja: \n
        1 - Recomedações de Filmes
        2 - Suas Classificações
        3 - Conheça o Projeto Rasboticas
        4 - Instruções
        5 - Exit
        -----------------------------------
        Digite aqui o número da sua opção: 
        \n'''))

  if opcao == 1:#Exibir Filmes
    exibeFilmes()
  elif opcao == 2:#Filmes e Classificações
    filmesAssistidos()
  elif opcao == 3: #Projeto Rasboticas
    conhecaProjeto()
  elif opcao == 4: #Instruções de USO
    instrucoes()
  else:
    print('Obrigado por utilizar o RASboticas Movies!')
    exit()
#---------------------------------------
#Programa Principal
#---------------------------------------
main()