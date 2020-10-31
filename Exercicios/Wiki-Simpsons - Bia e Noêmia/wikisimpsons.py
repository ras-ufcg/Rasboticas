from time import sleep

print('\t'+'-'*32) #exibindo os 'tracinhos' entre as mensagens
print('\tBem-vindo ao jogo Wiki-Simpsons!')
print('\t'+'-'*32, '\n')
sleep(2) #função para o código 'dormir'
print('\tNeste jogo iremos tentar descobrir o personagem que o\n\t'
        'usuário pensou, baseado nas características informadas.\n')
print('\t'+'-'*41)
sleep(3) 
print('\tOs personagens que você pode pensar, são: ')
sleep(3)
print('\n\n\t[1] - Homer Simpsons\n\t'
        '[2] - Marge Simpson\n\t[3] - Bart Simpson\n\t[4] - Lisa Simpson\n\t[5] - '
        'Maggie Simpson\n\t[6] - Moe Szyslak\n\t[7] - Barney Gumble\n\t[8] - Robert '
        'Terwilliger\n\t[9] - Abraham Simpson\n\t[10] - Herschel Krustofski\n\t[11] - '
        'Ajudante de Papai Noel\n\t[12] - Bola de Neve\n\t[13] - Charles Montgomery '
        'Burns\n\t[14] - Waylon Smithers\n\t[15] - Lenny Leonard\n\t[16] - '
        'Carl Carlson\n\t[17] - Ralph Wiggum\n\t[18] - Ned Flanders\n\t[19] - O Cara '
        'dos Quadrinhos\n\t[20] - Nelson Muntz\n\t[21] - Martin Prince\n\t[22] - '
        'Milhouse Van Houten\n\t[23] - Seymour Skinner\n\t[24] - Edna Krabappel\n\t'
        '[25] - Jardineiro Willie\n\t[26] - Otto Mann\n\t[27] - Dr. Julius Hibberts\n\t'
        '[28] - Clancy Wiggum\n\t[29] - Apu Nahasapeemapetilon\n\t[30] - Rod Flanders\n'
        '\t[31] - Todd Flanders\n\t[32] - Selma Bouvier\n\t[33] - Patty Bouvier\n\t')
print('\t'+'-'*41)
opcaoUsuario = str(input('\n\tContinuar?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
print('\t'+'-'*41)

#se o usuario digitar alguma letra q não seja 's' ou 'n' entra nesse loop para pedir uma entrada válida:
while opcaoUsuario != 's' and opcaoUsuario != 'n':
  opcaoUsuario = str(input('\n\tEsta opção é inválida! Quer continuar jogando?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
  print('\t'+'-'*41)

while opcaoUsuario == 's': #caso o usuario digite 's' entra nesse loop
  print('\n\n\tSeu personagem é: ')
  genero = str(input('\n\t[a] - Homem\n\t[b] - Mulher\n\t[c] - Animal\n\t\t')) 
  if genero == 'c':
    gato1 = str(input('\tSeu personagem só aparece quando precisa de algo?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
    if gato1 == 's':
      acertou = str(input('\tSeu personagem é um gato?\n\t[s] - Sim\n\t[n] - Não\n\t\t')) 
      if acertou == 's':
        gato = str(input('\tSeu personagem é Bola de Neve?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
        if gato == 's':
          print('\n\t'+'*'*40)
          print('Seu personagem é um gato da família que é sempre indiferente a não ser quando precisa de alguma coisa. Bola de Neve II é uma substituta mais agressiva, mais alegre do que a primeira gata da família Simpson. Sabem-se que Bola de Neve II já foi dançar em um baile e faz pequenos truques, quase nunca perto de nenhum membro da família, exceto no episódio em que os Simpsons tem um grande elefante de estimação. Ela tem um relacionamento familiar confiável, com o cachorro de estimação dos Simpson. Na verdade, é tão confiável que sabe-se que os dois ficam se acariciando quando não tem ninguém olhando.')
          print('\t'+'*'*40)
    else:
      cao1 = str(input('\tSeu personagem foi adotado na véspera de natal?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
      if cao1 == 's':
        acertou = str(input('\tSeu personagem é um cachorro?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
        if acertou == 's':
          cao = str(input('\tSeu personagem é Ajudante de Papai Noel?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
          if cao == 's':
            print('\n\t'+'*'*40)
            print('\tSeu personagem foi adotado pela família na véspera de Natal, o cãozinho tornou-se um membro da família Simpsons. Com poucas exceções, o ajudante de Pai Natal não faz qualquer som que se assemelha a uma casca. No entanto, ele tem uma capacidade de pensar como uma pessoa. Certa vez, ele faz um som semelhante a "borracha", e Homer disse que o cachorro falava Inglês. Ele também é mostrado para ter uma bola de circo montado nas patas traseiras e proferir a frase "Nós te amamos! " em uma tentativa de ser dada alguma atenção da família Simpson. Além disso, ele era mascote da Duff, e era conhecido como Suds McDuff (uma referência a uma vida semelhante mascote real, Spuds MacKenzie). ')
            print('\t'+'*'*40)
      else: 
        print('\tEste personagem não existe no joguinho!') #se o usuário disser 'n' no if do cao1

  elif genero == 'b':
    adultoCrianca = str(input('\n\tSeu personagem é adulto ou criança?\n\t[a] - Adulto\n\t[c] - Criança\n\t\t'))
    if adultoCrianca == 'c':
      sax = str(input('\n\tSeu personagem é uma excelente saxofonista?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
      if sax == 's':
        qi = str(input('\n\tSeu personagem tem QI de 159?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
        if qi == 's':
          acertou = str(input('\tSeu personagem é Lisa Simpson?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
          if acertou == 's':
            print('\n\t'+'*'*40)
            print('\tSeu personagem é uma estudante da segunda série que toca saxofone. Inteligente, é ela quem guia a família moralmente. Carismática, doce e inteligente, eis a definição perfeita para Lisa Simpson. O conhecimento de Lisa abrange uma vasta gama de assuntos, matemática, física, astronomia, medicina, história, geografia, ciências, biologia, religião, etc, de fato uma menina muito dedicada. Ela apresenta características raramente vistas em Springfield, como espiritualidade e a busca de soluções por meios pacíficos.')
            print('\t'+'*'*40)
          else:
            print('\tEste personagem não existe no joguinho!') #se o usuário disser 'n' no if do acertou
        else:
            print('\tEste personagem não existe no joguinho!') #se o usuário disser 'n' no if do qi     
      else: 
        humor = str(input('\n\tSeu personagem está sempre de bom-humor?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
        if humor == 's':
          bebe = str(input('\tSeu personagem é um bebê e vive chupando chupeta?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
          if bebe == 's':
            acertou = str(input('\tSeu personagem é Maggie Simpson??\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
            if acertou == 's':
              print('\n\t'+'*'*40)
              print('\tBebê que adora uma chupeta. Está sempre de bom-humor e não consegue nem andar nem falar. É a filha mais nova de Homer e Marge. São comuns as piadas onde Homer esquece o nome dela ou até mesmo de sua existência, não são muitos os episódios onde Maggie tem destaque, mas em alguns significativos episódios podemos perceber que ela é muito inteligente.')
              print('\t'+'*'*40)
            else:
              print('\tEste personagem não existe no joguinho!') #se o usuário disser 'n' no if do acertou
          else:
            print('\tEste personagem não existe no joguinho!') #se o usuário disser 'n' no if do bebe
        else:
            print('\tEste personagem não existe no joguinho!') #se o usuário disser 'n' no if do humor
    else:
      gemea = str(input('\n\tSeu personagem tem uma irmã gêmea?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
      if gemea == 's':
        fumante = str(input('\n\tSeu personagem vive fumando?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
        if fumante == 's':
          iguana = str(input('\n\tSeu personagem possui uma iguana de estimação?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
          if iguana == 's':
            acertou = str(input('\tSeu personagem é Selma Bouvier?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
            if acertou == 's':
              print('\n\t'+'*'*40)
              print(' Seu personagem é uma das irmãs fumantes de Marge. Assim como Patty, é cínica e dependente do cigarro. Ao contrário de Homer, que normalmente faz um esforço para ser educado com as gêmeas em respeito a Marge, Patty e Selma não hesitam em desprezar Homer. Houve vários casos em que elas não pareciam se importar com Homer quando este enfrentou uma situação de risco de vida. As irmãs partilham um apartamento.Selma tem procurado ativamente um marido, tendo se casado cinco vezes. Seu nome atual evoluiu em Selma Bouvier-Terwilliger-Hutz-McClure-Stu-Simpson.Ela não estava pronta para ter filhos e acabou adotando Jub Jub, a iguana da tia dela.')
              print('\t'+'*'*40)
            else: 
              print('\tEste personagem não existe no joguinho!')      
          else:
            acertou = str(input('\tSeu personagem é Patty Bouvier?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
            if acertou == 's':
              print('\n\t'+'*'*40)
              print('Seu personagem é uma das irmãs fumantes de Marge. Assim como sua irmã Selma, é cínica e dependente ao fumo. Ambas odeiam Homer. Houve vários casos em que eles não parecem se importar quando Homer enfrentou uma situação de risco de vida.  A marca favorita de cigarros da Patty é identificado como "Lady Laramie 100s", e seu hábito havia começado "antes mesmo que tivessem nascido". As irmãs partilham um apartamento.')
              print('\t'+'*'*40)
            else: 
              print('\tEste personagem não existe no joguinho!') #se o usuário disser 'n' no if do acertou
        else: 
          print('\tEste personagem não existe no joguinho!')
      else: 
        dona = str(input('\n\tSeu personagem é uma dona de casa?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
        if dona == 's':
          paciente = str(input('\n\tSeu personagem é uma mulher dedicada e paciente?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
          if paciente == 's':
            acertou = str(input('\tSeu personagem é Marge Simpson?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
            if acertou == 's':
              print('\n\t'+'*'*40)
              print('Seu personagem é a esposa de Homer Simpson e mãe de Lisa, Bart e Maggie Simpson no desenho animado Os Simpsons. Ela é mais conhecida por causa de seus longos cabelos azuis e de sua personalidade muito paciente. Com poucas exceções, Marge gasta a maior parte de seu tempo como dona de casa, cuidando de Maggie, ajudando Lisa ou defendendo Bart da raiva de seu pai.')
              print('\n\t'+'*'*40)
            else: 
              print('\tEste personagem não existe no joguinho!') #se o usuário disser 'n' no if do acertou
          else:
            print('\tEste personagem não existe no joguinho!') #se o usuário disser 'n' no if do paciente
           
        else:
          prof = str(input('\n\tSeu personagem é uma professora?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
          if prof == 's':
            estresse = str(input('\n\tSeu personagem está sempre estressado e desiludido?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
            if estresse == 's':
              acertou = str(input('\n\tSeu personagem é Edna Krabappel?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
              if acertou == 's':
                print('\n\t'+'*'*40)
                print('Seu personagem é uma professora de Bart que sempre o manda escrever algo no quadro negro. Manteve um relacionamento frustrado com o Diretor Skinner, onde chegaram a firmar noivado, porém, ela o deixou no altar, pois não o amava e nem ele a ela. Casou-se com Ned Flanders. Sempre arranja um tempo para fumar, principalmente no fundo da sala de aula durante as exibições de filmes educacionais. Edna Krabappel já foi despedida de seu cargo de professora (Por dar um tapa em Bart), porém foi readmitida ')
                print('\n\t'+'*'*40)
              else:
                print('\tEste personagem não existe no joguinho!') #se o usuário disser 'n' no if do acertou
            else: 
              print('\tEste personagem não existe no joguinho!') #se o usuário disser 'n' no if do estresse
          else: 
            print('\tEste personagem não existe no joguinho!') #se o usuario disser 'n' no if da professora
  elif genero == 'a':
    adultoCrianca = str(input('\n\tSeu personagem é adulto ou criança?\n\t[a] - Adulto\n\t[c] - Criança\n\t\t'))
    if adultoCrianca == 'c':
      jovem = str(input('\n\tSeu personagem é ruivo e tem um irmão mais velho?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
      if jovem == 's':
        familia = str(input('\n\tSeu personagem faz parte da Família Flanders?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
        if familia == 's':
          acertou = str(input('\n\tSeu personagem é Todd Flanders?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
          if acertou == 's':
            print('\n\t'+'*'*40)
            print('Seu personagem é  o membro mais jovem da Família Flanders, ele toca violino muito bem e faz parte da banda da escola de Springfield!')
            print('\n\t'+'*'*40)
          else:
            print('\tEste personagem não existe no joguinho!')
        else:
          print('\tEste personagem não existe no joguinho!')

      else: 
        estudo = str(input('\n\tSeu personagem é o pior aluno da classe?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
        if estudo == 's':
          skate = str(input('\n\tSeu personagem anda de skate?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
          if skate == 's':
            acertou = str(input('\n\tSeu personagem é Bart Simpson?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
            if acertou == 's':
              print('\n\t'+'*'*40)
              print('\tSeu personagem é um estudante da quarta série que nunca se sai bem nos estudos e que gosta de andar de skate e mascar chiclete. É o pesadelo do Skinner, o garoto Ai, Caramba!, o El Barto e um dos piores alunos da classe da Sra. Krabappel. Seu principal objeto característico é seu Skate e seu estilingue, usados para perturbar os outros cidadãos de Springfield. Já passou trotes na Taverna do Moe, embora não tenha sido visto fazendo isso no desenho há bastante tempo, e ele adora chocolate, capuccino e dias que nevam pois ele adora faltar nas aulas. Bart diz-se mal compreendido. Categorizado frequentemente como pouco inteligente e desordeiro')
              print('\n\t'+'*'*40)
            else: 
              print('\tEste personagem não existe no joguinho!')
          else: 
            print('\tEste personagem não existe no joguinho!')
        else:
          turma = str(input('\n\tSeu personagem é da turma de Bart no colégio?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
          if turma == 's':
            encrenca = str(input('\n\tSeu personagem é um encrenqueiro profissional?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
            if encrenca == 's':
              maior = str(input('\n\tSeu personagem é a MAIOR criança da turma?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
              if maior == 's':
                acertou = str(input('\n\tSeu personagem é Nelson Muntz?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                if acertou == 's':
                  print('\n\t'+'*'*40)
                  print('\tSeu personagem é um encrenqueiro profissional. É a maior criança da turma de Bart no colégio. Seu bordão é HAHA! Ao longo dos anos, Nelson Muntz aterrorizou praticamente todos em Springfield, e regularmente ri da desgraça do povo. Nelson mostra o vislumbre ocasional da humanidade.')
                  print('\n\t'+'*'*40)
                else:
                  print('\tEste personagem não existe no joguinho!')
              else: 
                print('\tEste personagem não existe no joguinho!')
            else:
              maior = str(input('\n\tSeu personagem é o melhor amigo de Bart somente durante a \tépoca de provas?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
              if maior == 's':
                nerd = str(input('\n\tSeu personagem é nerd e é líder da turma?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                if nerd == 's':
                  acertou = str(input('\n\tSeu personagem é Martin Prince?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                  if acertou == 's':
                    print('\n\t'+'*'*40)
                    print('\tSeu personagem é um nerd, e o melhor amigo de Bart somente durante a época de provas, líder de turma da classe. Vive tomando pancadas e puxões de cueca do Nelson por ser cdf, dedo duro e o aluno mais estudioso da sala.')
                    print('\n\t'+'*'*40)
                  else:
                    print('\tEste personagem não existe no joguinho!')
                else:
                  print('\tEste personagem não existe no joguinho!')
              else:
                maior = str(input('\n\tSeu personagem é o melhor amigo de Bart, de verdade?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                if maior == 's':
                  maior = str(input('\n\tSeu personagem possuí um amor platônico por Lisa Simpson?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                  if maior == 's':
                    acertou = str(input('\n\tSeu personagem é Milhouse Van Houten?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                    if acertou == 's':
                      print('\n\t'+'*'*40)
                      print('\tSeu personagem é o melhor amigo de Bart. Seguidor fiel do filho de Homer. Apesar de ser considerado nerd, ele possui apenas uma inteligência mediana e péssima habilidade com pessoas. Ele constantemente se mete em problemas causados por Bart.')
                      print('\n\t'+'*'*40)
                    else:
                      print('\tEste personagem não existe no joguinho!')
                  else:
                    print('\tEste personagem não existe no joguinho!')
                else: 
                  print('\tEste personagem não existe no joguinho!')        
          else:
            turma = str(input('\n\tSeu personagem é da turma de Lisa?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
            if turma == 's':
              img = str(input('\n\tSeu personagem diz ter vários amigos, todos imaginários?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))  
              if img == 's':
                filho = str(input('\n\tSeu personagem é o filho do policial Clancy Wiggum?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                if filho == 's':
                  acertou = str(input('\n\tSeu personagem é Ralph Wiggum?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                  if acertou == 's':
                    print('\n\t'+'*'*40)
                    print('\tSeu personagem é um colega de classe de Lisa e filho do policial Clancy Wiggum. É considerado especial por causa de suas brincadeiras com amigos invisíveis.')
                    print('\n\t'+'*'*40)
                  else: 
                    print('\tEste personagem não existe no joguinho!') 
                else:
                  print('\tEste personagem não existe no joguinho!') 
              else:
                print('\tEste personagem não existe no joguinho!')     
            else:
              religioso = str(input('\n\tSeu personagem reza por quase tudo, em qualquer \n\toportunidade?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
              if religioso == 's':
                acertou = str(input('\n\tSeu personagem é Rod Flanders?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                if acertou == 's':
                  print('\n\t'+'*'*40)
                  print('\tSeu personagem reza por quase tudo em todas as oportunidades. Além de orar, Rod gosta de jogar sadiamente com seu irmão e comer lotes de nachos  do estilo Flanders ')
                  print('\n\t'+'*'*40)
                else:
                  print('\tEste personagem não existe no joguinho!') 
              else:
                print('\tEste personagem não existe no joguinho!')
    else:
      usina = str(input('\n\tSeu personagem trabalha na usina?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
      if usina == 's':
        barba = str(input('\n\tSeu personagem tem barba/bigode?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
        if barba == 's':
          perso12 = str(input('\n\tSeu personagem é um homem de família, alcoólotra e \n\tpreguiçoso?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
          if perso12 == 's':
            perso1 = str(input('\n\tSeu personagem ama donuts?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
            if perso1 == 's':
              acertou = str(input('\n\tSeu personagem é Homer Simpson?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
              if acertou == 's':
                print('\n\t'+'*'*40)
                print('\tSeu personagem nasceu em Springfield (mesmo dizendo que nasceu em Connecticut). Sendo o primeiro filho de Mona Simpson. Em 1960, Ele colocou quinze gizes de cera em seu nariz, que danificou seu cérebro, resultando numa debilidade mental, explicando sua inteligência abaixo da média. Ele foi criado num curral de bodes. Trabalha na usina nuclear de Springfield, ama cerveja e donuts. É um homem de família devotado, quando se lembra de ser')
                print('\n\t'+'*'*40)
              else:
                print('\tEste personagem não existe no joguinho!')  
            else:
              print('\tEste personagem não existe no joguinho!')
          else: 
             print('\tEste personagem não existe no joguinho!')

        else:
          fisico1 = str(input('\n\tSeu personagem trabalha como físico na usina?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
          if fisico1 == 's':
            fisico = str(input('\n\tSeu personagem é negro?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
            if fisico == 's':
              acertou = str(input('\n\tSeu personagem é Carl Carlson?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
              if acertou == 's':
                print('\n\t'+'*'*40)
                print('\tSeu personagem é um físico da Usina nuclear pertencente ao bando de Lenny e Homer, ele é um dos melhores amigos de Homer desde a infância. É um dos quatro principais bêbados e causadores de acidente da Taverna do Moe. É um afro-americano e Budista, mas mesmo sendo assim tão diferente conseguiu se formar em física nuclear.')
                print('\n\t'+'*'*40)
              else:
                print('\tEste personagem não existe no joguinho!') 
            else:
              print('\tEste personagem não existe no joguinho!')
          else:
            dono2 = str(input('\n\tSeu personagem é um malígno dono?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
            if dono2 == 's':
              dono = str(input('\n\tSeu personagem é egoísta e vive com seu assistente pra \n\ttodo lugar?\n\t[s] - Sim\n\t [n] - Não\n\t\t'))
              if dono == 's':
                acertou = str(input('\n\tSeu personagem é Charles Montgomery Burns?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                if acertou == 's':
                  print('\n\t'+'*'*40)
                  print('\tSeu personagem é um Bilionário, egoísta, maquiavélico, estrategista e cruel Devido à sua impressionante idade ele tornou-se extremamente frágil, adquiriu inúmeras doenças, dificuldades para levantar uma pena e a inacreditável e totalmente inútil capacidade de espirrar e ter seu cérebro exposto, e como se já não bastasse suar uma gota pode lhe provocar desmaios...')
                  print('\n\t'+'*'*40)
                else:
                  print('\tEste personagem não existe no joguinho!')  
              else:
                print('\tEste personagem não existe no joguinho!')
            else:
              vadiar1 =str(input('\n\tSeu personagem ama vadiar e passa seu tempo na Taverna do \tMoe com Home e Carl ao vez de trabralhar?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
              if vadiar1 == 's':
                vadiar = str(input('\n\tSeu personagem é o melhor amigo de Carl Carlson?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                if vadiar == 's':
                  acertou = str(input('\n\tSeu personagem é Lenny Leonard?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                  if acertou == 's':
                    print('\n\t'+'*'*40)
                    print('\tSeu personagem é um dos melhores amigo de Homer e também trabalha na Usina Nuclear de Springfield, possui um mestrado em física nuclear, mas não é retratado como um acadêmico. Lenny parece ser um simples, e muitas vezes ingênuo operário trabalhando cujo melhor amigo é Carl Carlson')
                    print('\n\t'+'*'*40)
                  else:
                    print('\tEste personagem não existe no joguinho!')
                else:
                  print('\tEste personagem não existe no joguinho!')
              else: 
                print('\tEste personagem não existe no joguinho!') 
      else:
        motorista1 = str(input('\n\tSeu personagem é um motorista de ônibus escolar?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
        if motorista1 == 's':
          motorista = str(input('\n\tSeu personagem está sempre com um fone de ouvido?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
          if motorista == 's':
            acertou = str(input('\n\tSeu personagem é Otto Mann?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
            if acertou == 's':
              print('\n\t'+'*'*40)
              print('\tSeu personagem é um motorista do ônibus escolar e grande guitarrista. Otto é simples e despreocupado. Só gosta de rock e de noites com amigos.')
              print('\n\t'+'*'*40)
            else:
              print('\tEste personagem não existe no joguinho!')  
          else:
            print('\tEste personagem não existe no joguinho!') 
        else:
          jardim1 = str(input('\n\tSeu personagem é um Zelador?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
          if jardim1 == 's':
            jardim = str(input('\n\tSeu personagem é um escoceses grosseiro?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
            if jardim == 's':
              acertou = str(input('\n\tSeu personagem é o Zelador Willie?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
              if acertou == 's':
                print('\n\t'+'*'*40)
                print('\tSeu personagem  é o zelador da Escola Elementar de Springfield. Descendente de escoceses, o trabalho de Willie é supervisionar as crianças durante o recreio e limpar as salas. Ele é reconhecido por seu cabelo vermelho e sotaque escocês grosseiro. Ele é, muitas vezes, um formidável inimigo ou um aliado inestimável para Bart e Lisa Simpson.')
                print('\n\t'+'*'*40)
              else:
                print('\tEste personagem não existe no joguinho!')
            else:
              print('\tEste personagem não existe no joguinho!')
          else:
            tv1 = str(input('\n\tSeu personagem tem um programa infantil na TV?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
            if tv1 == 's':
              tv = str(input('\n\tSeu personagem é um palhaço infeliz?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
              if tv == 's':
                acertou = str(input('\n\tSeu personagem é Herschel Krustofski?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                if acertou == 's':
                  print('\n\t'+'*'*40)
                  print('\tSeu personagem é conhecido como Krusty, o Palhaço. Tem um programa infantil na TV. Faz de tudo para conseguir uma grana. É idolatrado por Bart. É um veterano do entretenimento cansado de sua fama e de lidar com crianças. Devido a sua infelicidade tornou-se viciado em jogo, cigarros, álcool, Percodan, Pepto-Bismol e Xanax.')
                  print('\n\t'+'*'*40)
                else:
                  print('\tEste personagem não existe no joguinho!')  
              else:
                print('\tEste personagem não existe no joguinho!')
            else:
              loja1 = str(input('\n\tSeu personagem é dono de uma loja de quadrinhos?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
              if loja1 == 's':
                loja = str(input('\n\tSeu personagem é arrogante e interesseiro?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                if loja == 's':
                  acertou = str(input('\n\tSeu personagem é o O Cara dos Quadrinhos?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                  if acertou == 's':
                    print('\n\t'+'*'*40)
                    print('\tSeu personagem é um Homem de 45 anos, sem amigos. É dono de uma loja de quadrinhos.Tem um imenso cuidado (e ciúme) com os quadrinhos que vende, sabe de todos que tem e já leu todos. Ele é sarcástico e mau humorado, não trata bem seus clientes, a não ser que o cliente esteja segurando uma grande quantidade de dinheiro! É o típico Nerd, sempre está na Internet e é fã de séries antigas de TV.')
                    print('\n\t'+'*'*40)
                  else:
                    print('\tEste personagem não existe no joguinho!')  
                else:
                  print('\tEste personagem não existe no joguinho!')
              else:
                diretor = str(input('\n\tSeu personagem é diretor de uma escola?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                if diretor == 's':
                  acertou = str(input('\n\tSeu personagem é um burocrata educacional estereotipado?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                  if acertou == 's':
                    buroc = str(input('\n\tSeu personagem é o Saymour Skinner?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                    if buroc == 's':
                      print('\n\t'+'*'*40)
                      print('\tSeu personagem ele se esforça para controlar a escola em ruínas e está constantemente envolvido em uma batalha contra os seus recursos inadequados, professores apáticos e amargos, e os estudantes muitas vezes turbulentos e sem entusiasmo, sendo Bart Simpson um exemplo de destaque.')
                      print('\n\t'+'*'*40)
                    else:
                      print('\tEste personagem não existe no joguinho!')
                else:
                  assistente1 = str(input('\n\tSeu personagem é Assistente pessoal de um chefe \n\timportante?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                  if assistente1 == 's':
                    assistente = str(input('\n\tSeu personagem está sempre com seu patrão realizando \n\tdiversas atividades?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                    if assistente == 's':
                      acertou = str(input('\n\tSeu personagem é Waylon Smithers?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                      if acertou == 's':
                        print('\n\t'+'*'*40)
                        print('\tSeu personagem é o típico "lambe-botas" de Monty Burns, o rapaz realiza absolutamente tudo para seu maquiavélico chefe, desde o preparo de suas refeições até colocá-lo na cama para dormir, certa vez Smithers mencionou que ao total realiza 2799 tarefas para Burns.')
                        print('\n\t'+'*'*40)
                      else:
                        print('\tEste personagem não existe no joguinho!')  
                    else:
                      print('\tEste personagem não existe no joguinho!')
                  else:
                    irresponsavel = str(input('\n\tSeu personagem é um policial irresponsável e possuí \n\tcabelos azuis?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                    if irresponsavel == 's':
                      chefe = str(input('\n\tSeu personagem é Chefe da polícia de \n\tSpringfield?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                      if chefe == 's':
                        acertou = str(input('\n\tSeu personagem é Clancy Wiggum?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                        if acertou == 's':
                          print('\n\t'+'*'*40)
                          print('\tÉ o Chefe de Polícia da cidade de Springfield. Pode ser \nconsiderado como uma pessoa irresponsável, incompetente e \ncorrupta. É o pai de Ralph Wiggum,é o Delegado do Departamento de Polícia de Springfield, o braço longo e atarracado da lei.')
                          print('\n\t'+'*'*40)
                        else:
                          print('\tEste personagem não existe no joguinho!')
                    else:
                      asilo = str(input('\n\tSeu personagem mora em um asilo?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                      if asilo == 's':
                        pai = str(input('\n\tSeu personagem é o pai de Homer?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                        if pai == 's':
                          acertou = str(input('\n\tSeu personagem é Abraham Simpson II?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                          if acertou == 's':
                            print('\n\t'+'*'*40)
                            print('\n\tSeu personagem é o pai de Homer. Sua memória é um depósito de eventos históricos - reais e imaginários.  É um octogenário, pai de Homer Simpson, de Herbert Powell Simpson e Abbie Winston Simpson; avô de Lisa Simpson, Bart Simpson e Maggie Simpson. Mora no Asilo de Springfield junto com seus amigos. Ele tinha sua própria casa, que vendeu para que com o dinheiro seu filho Homer conseguisse comprar a sua e se casar.')
                            print('\n\t'+'*'*40)
                          else:
                            print('\tEste personagem não existe no joguinho!')
                        else:
                          print('\tEste personagem não existe no joguinho!')    
                      else:
                        boxe = str(input('\n\tSeu personagem é o dono de um bar em Springfield?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                        if boxe == 's':
                          bar = str(input('\n\tSeu personagem é um ex lutador de box\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                          if bar == 's':
                            acertou = str(input('\n\tSeu personagem é Moe Szyslak?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                            if acertou == 's':
                              print('\n\t'+'*'*40)
                              print('\n\tSeu personagem é um ex-lutador de boxe. É o proprietário e barman da Taberna do Moe, ele e amargo e quase sempre desprezado por todos incluindo seus melhores amigos. Ainda mora com a mãe. Ninguém sabe como Moe conseguiu manter seu bar aberto todos esses anos, na maior parte das noites tem somente três ou quatro fregueses entre eles com certeza Barney Gumble.')
                              print('\n\t'+'*'*40)
                            else:
                              print('\tEste personagem não existe no joguinho!')
                          else:
                            print('\tEste personagem não existe no joguinho!')
                        else:
                          mercado = str(input('\n\tSeu personagem é proprietário do mercadinho de \n\tSpringfield?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                          if mercado == 's':
                            m = str(input('\n\tSeu personagem é natural da índia?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                      
                            if m == 's':
                              acertou = str(input('\n\tSeu personagem é Apu Nahasapeemapetilon?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                              if acertou == 's':
                                print('\n\t'+'*'*40)
                                print('\n\tSeu personagem nasceu na Índia, porém imigrou ilegalmente para os Estados Unidos e então se naturalizou americano. É casado com Manjula e é pai de oito filhos. Apu trabalha no Kwik-E-Mart, um mercadinho de Springfield, do qual é dono. No Kwik-E-Mart, Apu oferece a preços exorbitantes deliciosos cachorros-quentes, saborosos burritos congelados para microondas e o sempre popular suco de frutas.')
                                print('\n\t'+'*'*40)
                              else:
                                print('\tEste personagem não existe no joguinho!')  
                            else:
                              print('\tEste personagem não existe no joguinho!')
                          else:
                            cerveja1 = str(input('\n\tSeu personagem não consegue ficar sóbrio?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                            if cerveja1 == 's':
                              cerveja = str(input('\n\tSeu personagem passa grande parte do seu tempo \n\tno Bar do Moe?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                              if cerveja == 's':
                                acertou = str(input('\n\tSeu personagem é Barney Gumble?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                                if acertou == 's':
                                  print('\n\t'+'*'*40)
                                  print('\n\tSeu personagem é um bêbado, mas quando sóbrio tem alma de poeta. É o cliente mais assíduo da Taverna do Moe, que utiliza este pub como uma albergaria. Suas marcas mais visíveis são suas expressões perdidas, seus audíveis arrotos após cada embriaguez e seu jeito desleixado de ser e viver. Antes de ser alcoólatra, Barney era muito inteligente e tentava entrar em Harvard. ')
                                  print('\n\t'+'*'*40)
                                else:
                                  print('\tEste personagem não existe no joguinho!')  
                              else:
                                print('\tEste personagem não existe no joguinho!')
                            else:
                              conhecido1 = str(input('\n\tSeu personagem é maligno e possui grandes cabelos \n\tvermelhos?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                              if conhecido1 == 's':
                                conhecido = str(input('\n\tSeu personagem é conhecido como Sideshow Bob?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                                if conhecido == 's':
                                  acertou = str(input('\n\tSeu personagem é Robert Terwilliger?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                                  if acertou == 's':
                                    print('\n\t'+'*'*40)
                                    print('\n\tSeu personagem é conhecido como Sideshow Bob. Bart frustrou seus planos de dominar o mundo e se tornou seu inimigo mortal. Ele cometeu crimes dos mais variados: incriminou falsamente o palhaço Krusty no roubo da loja "Kwik-E-Mart", mas acabou desmascarado e preso, elegeu-se prefeito da cidade de Springfield por um esquema de manipulação de votos onde ele colocava nomes de pessoas mortas como sendo seus eleitores, tentou assassinar Selma Bouvier em um motel em plena lua-de-mel, entre vários outros.')
                                    print('\n\t'+'*'*40)
                                  else:
                                    print('\tEste personagem não existe no joguinho!')  
                                else:
                                  print('\tEste personagem não existe no joguinho!')
                              else:
                                medico1 = str(input('\n\tSeu personagem é um médico?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                                if medico1 == 's':
                                  medico = str(input('\n\tSeu personaguem oferece um pirulito sempre que você vai no \tconsutório dele?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                                  if medico == 's':
                                    acertou = str(input('\n\tSeu personagem é Dr. Julius Hibberts?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                                    if acertou == 's':
                                      print('\n\t'+'*'*40)
                                      print('\n\tSeu personagem é um médico do Hospital Geral de Springfield. É o médico da família Simpson desde o nascimento de Bart tem o péssimo hábito de rir nas horas mais impróprias, sobretudo no que diz respeitos às injúrias de seus pacientes, como quando expressou apenas uma leve surpresa quando ambos os rins de Abe Simpson explodiram.')
                                      print('\n\t'+'*'*40)
                                    else:
                                      print('\tEste personagem não existe no joguinho!')  
                                  else:
                                    print('\tEste personagem não existe no joguinho!')
                                else:
                                  familia1 = str(input('\n\tSeu personagem comanda uma "Família modelo"?\n\t[s] - Sim\n\t[n]- Não\n\t\t'))
                                  if familia1 == 's':
                                    familia = str(input('\n\tSeu personagem acha que tudo é pecado?\n\t[s] - Sim\n\t[n]- Não\n\t\t'))
                                    if familia == 's':
                                      perso2 = str(input('\n\tSeu personagem é Ned Flanders?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
                                      if perso2 == 's':
                                        print('\n\t'+'*'*40)
                                        print('\n\tSeu personagem é o vizinho da família Simpson. Muito preocupado com seus filhos, Ned impede que eles assistam certos programas da televisão e comam doces com açúcar. Homer realmente demonstra odiar Ned Flanders (embora tenham se tornado amigos em alguns episódios),e já disse que Flanders é mais puro até mesmo do que Jesus.')
                                        print('\n\t'+'*'*40)
                                      else: 
                                        print('\tEste personagem não existe no joguinho!')  
                                    else: 
                                      print('\tEste personagem não existe no joguinho!')
                                  else:
                                    print('\tSuas opções esgotaram!\n') 
  else:
    print('\tComando errado!\n')
  print('\t'+'-'*41)
  opcaoUsuario = str(input('\n\tContinuar jogando?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
  print('\t'+'-'*41)
  
  #se o usuario digitar alguma letra q não seja 's' ou 'n' entra nesse loop para pedir uma entrada válida:
  while opcaoUsuario != 's' and opcaoUsuario != 'n':
    opcaoUsuario = str(input('\n\tEsta opção é inválida! Quer continuar jogando?\n\t[s] - Sim\n\t[n] - Não\n\t\t'))
    print('\t'+'-'*41)

print('\n\tEspero breve vê-lo, bye!\n\n') #exibe essa mensagem caso o usuario nao queira mais jogar