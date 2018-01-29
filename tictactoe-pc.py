campo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ganhou = ['\033[1;32m','\033[m']
while True:
    print('''
      ___________________
      |     |     |     |
      |  {}  |  {}  |  {}  |
      |     |     |     |
      |=====×=====×=====|
      |     |     |     |
      |  {}  |  {}  |  {}  |
      |     |     |     |
      |=====×=====×=====|
      |     |     |     |
      |  {}  |  {}  |  {}  |
      |     |     |     |
      |=====×=====×=====|
      '''.format(
      	campo[0],
      	campo[1],
      	campo[2],
      	campo[3],
      	campo[4],
      	campo[5],
      	campo[6],
      	campo[7],
      	campo[8]))
    while True:
        jogador1 = int(input('Jogador1 - Digite o Valor: '))
        if (jogador1 == 1):
            if (campo[0] == 1):
                campo[0] = "X"
                break
            elif (campo[0] == "O" or campo[0] == "X"):
                print('\nVocê Não Pode Jogar Aqui!')
                print('Escolha Outro Canto!\n') 
        
        elif (jogador1 == 2):
            if (campo[1] == 2):
                campo[1] = "X"
                break
            elif (campo[1] == "O" or campo[1] == "X"):
                print('\nVocê Não Pode Jogar Aqui!')
                print('Escolha Outro Canto!') 
        
        elif (jogador1 == 3):
            if (campo[2] == 3):
                campo[2] = "X"
                break
            elif (campo[2] == "O" or campo[2] == "X"):
                print('\nVocê Não Pode Jogar Aqui!')
                print('Escolha Outro Canto!') 
        
        elif (jogador1 == 4):
            if (campo[3] == 4):
                campo[3] = "X"
                break
            elif (campo[3] == "O" or campo[3] == "X"):
                print('\nVocê Não Pode Jogar Aqui!')
                print('Escolha Outro Canto!') 
        
        elif (jogador1 == 5):
            if (campo[4] == 5):
                campo[4] = "X"
                break
            elif (campo[4] == "O" or campo[4] == "X"):
                print('\nVocê Não Pode Jogar Aqui!')
                print('Escolha Outro Canto!') 
        
        elif (jogador1 == 6):
            if (campo[5] == 6):
                campo[5] = "X"
                break
            elif (campo[5] == "O" or campo[5] == "X"):
                print('\nVocê Não Pode Jogar Aqui!')
                print('Escolha Outro Canto!') 
        
        elif (jogador1 == 7):
            if (campo[6] == 7):
                campo[6] = "X"
                break
            elif (campo[6] == "O" or campo[6] == "X"):
                print('\nVocê Não Pode Jogar Aqui!')
                print('Escolha Outro Canto!') 
        
        elif (jogador1 == 8):
            if (campo[7] == 8):
                campo[7] = "X"
                break
            elif (campo[7] == "O" or campo[7] == "X"):
                print('\nVocê Não Pode Jogar Aqui!')
                print('Escolha Outro Canto!') 
        
        elif (jogador1 == 9):
            if (campo[8] == 9):
                campo[8] = "X"
                break
            elif (campo[8] == "O" or campo[8] == "X"):
                print('\nVocê Não Pode Jogar Aqui!')
                print('Escolha Outro Canto!') 

        elif (jogador1 > 9):
            print('Escolha de 1 á 9!')
        else:
            print('Erro!')
    
    print('''
      ___________________
      |     |     |     |
      |  {}  |  {}  |  {}  |
      |     |     |     |
      |=====×=====×=====|
      |     |     |     |
      |  {}  |  {}  |  {}  |
      |     |     |     |
      |=====×=====×=====|
      |     |     |     |
      |  {}  |  {}  |  {}  |
      |     |     |     |
      |=====×=====×=====|
      '''.format(
      	campo[0],
      	campo[1],
      	campo[2],
      	campo[3],
      	campo[4],
      	campo[5],
      	campo[6],
      	campo[7],
      	campo[8]))
    
    if (campo[0] == "X"):
        if (campo[1] == "X"):
            if (campo[2] == "X"):
                print('''
      ___________________
      |     |     |     |
      |  {}{}{}  |  {}{}{}  |  {}{}{}  |
      |     |     |     |
      |=====×=====×=====|
      |     |     |     |
      |  {}  |  {}  |  {}  |
      |     |     |     |
      |=====×=====×=====|
      |     |     |     |
      |  {}  |  {}  |  {}  |
      |     |     |     |
      |=====×=====×=====|
      '''.format(
      	ganhou[0],
      	campo[0],
      	ganhou[1],
      	ganhou[0],
      	campo[1],
      	ganhou[1],
      	ganhou[0],
      	campo[2],
      	ganhou[1],
      	campo[3],
      	campo[4],
      	campo[5],
      	campo[6],
      	campo[7],
      	campo[8]))
                print('        \033[1;4;32mJogador1 Ganhou!\033[m')
                exit()
        
        elif (campo[3] == "X"):
            if (campo[6] == "X"):
                print('''
      ___________________
      |     |     |     |
      |  {}{}{}  |  {}  |  {}  |
      |     |     |     |
      |=====×=====×=====|
      |     |     |     |
      |  {}{}{}  |  {}  |  {}  |
      |     |     |     |
      |=====×=====×=====|
      |     |     |     |
      |  {}{}{}  |  {}  |  {}  |
      |     |     |     |
      |=====×=====×=====|
      '''.format(
      	ganhou[0],
      	campo[0],
      	ganhou[1],
      	campo[1],
      	campo[2],
      	ganhou[0],
      	campo[3],
      	ganhou[1],
      	campo[4],
      	campo[5],
      	ganhou[0],
      	campo[6],
      	ganhou[1],
      	campo[7],
      	campo[8]))
                print('        \033[1;4;32mJogador1 Ganhou!\033[m')
                exit()
       
        elif (campo[4] == "X"):
            if (campo[8] == "X"):
                print('''
      ___________________
      |     |     |     |
      |  {}{}{}  |  {}  |  {}  |
      |     |     |     |
      |=====×=====×=====|
      |     |     |     |
      |  {}  |  {}{}{}  |  {}  |
      |     |     |     |
      |=====×=====×=====|
      |     |     |     |
      |  {}  |  {}  |  {}{}{}  |
      |     |     |     |
      |=====×=====×=====|
      '''.format(
      	ganhou[0],
      	campo[0],
      	ganhou[1],
      	campo[1],
      	campo[2],
      	campo[3],
      	ganhou[0],
      	campo[4],
      	ganhou[1],
      	campo[5],
      	campo[6],
      	campo[7],
      	ganhou[0],
      	campo[8],
      	ganhou[1]))
                print('        \033[1;4;32mJogador1 Ganhou!\033[m')
                exit()

    elif (campo[1] == "X"):
        if (campo[4] == "X"):
            if (campo[7] == "X"):
                print('''
        ___________________
        |     |     |     |
        |  {}  |  {}{}{}  |  {}  |
        |     |     |     |
        |=====×=====×=====|
        |     |     |     |
        |  {}  |  {}{}{}  |  {}  |
        |     |     |     |
        |=====×=====×=====|
        |     |     |     |
        |  {}  |  {}{}{}  |  {}  |
        |     |     |     |
        |=====×=====×=====|
        '''.format(

            campo[0],

            ganhou[0],
            campo[1],
            ganhou[1],

            campo[2],
            campo[3],

            ganhou[0],
            campo[4],
            ganhou[1],

            campo[5],
            campo[6],

            ganhou[0],
            campo[7],
            ganhou[1],

            campo[8]))
                print('        \033[1;4;32mJogador1 Ganhou!\033[m')
                exit()
    elif (campo[2] == "X"):
        if (campo[5] == "X"):
            if (campo[8] == "X"):
                print('''
        ___________________
        |     |     |     |
        |  {}  |  {}  |  {}{}{}  |
        |     |     |     |
        |=====×=====×=====|
        |     |     |     |
        |  {}  |  {}  |  {}{}{}  |
        |     |     |     |
        |=====×=====×=====|
        |     |     |     |
        |  {}  |  {}  |  {}{}{}  |
        |     |     |     |
        |=====×=====×=====|
        '''.format(

            campo[0],
            campo[1],

            ganhou[0],
            campo[2],
            ganhou[1],

            campo[3],
            campo[4],


            ganhou[0],
            campo[5],
            ganhou[1],

            campo[6],
            campo[7],

            ganhou[0],
            campo[8],
            ganhou[1]))
                print('        \033[1;4;32mJogador1 Ganhou!\033[m')
                exit()
        elif (campo[4] == "X"):
            if (campo[6] == "X"):
                print('''
        ___________________
        |     |     |     |
        |  {}  |  {}  |  {}{}{}  |
        |     |     |     |
        |=====×=====×=====|
        |     |     |     |
        |  {}  |  {}{}{}  |  {}  |
        |     |     |     |
        |=====×=====×=====|
        |     |     |     |
        |  {}{}{}  |  {}  |  {}  |
        |     |     |     |
        |=====×=====×=====|
        '''.format(

            campo[0],
            campo[1],

            ganhou[0],
            campo[2],
            ganhou[1],

            campo[3],

            ganhou[0],
            campo[4],
            ganhou[1],

            campo[5],

            ganhou[0],
            campo[6],
            ganhou[1],

            campo[7],
            campo[8]))
                print('        \033[1;4;32mJogador1 Ganhou!\033[m')
                exit()
    elif (campo[3] == "X"):
        if (campo[4] == "X"):
            if (campo[5] == "X"):
                print('''
        ___________________
        |     |     |     |
        |  {}  |  {}  |  {}  |
        |     |     |     |
        |=====×=====×=====|
        |     |     |     |
        |  {}{}{}  |  {}{}{}  |  {}{}{}  |
        |     |     |     |
        |=====×=====×=====|
        |     |     |     |
        |  {}  |  {}  |  {}  |
        |     |     |     |
        |=====×=====×=====|
        '''.format(

            campo[0],
            campo[1],
            campo[2],

            ganhou[0],
            campo[3],
            ganhou[1],

            ganhou[0],
            campo[4],
            ganhou[1],

            ganhou[0],
            campo[5],
            ganhou[1],

            campo[6],
            campo[7],
            campo[8]))
                print('        \033[1;4;32mJogador1 Ganhou!\033[m')
                exit()

    elif (campo[6] == "X"):
        if (campo[7] == "X"):
            if (campo[8] == "X"):
                print('''
        ___________________
        |     |     |     |
        |  {}  |  {}  |  {}  |
        |     |     |     |
        |=====×=====×=====|
        |     |     |     |
        |  {}  |  {}  |  {}  |
        |     |     |     |
        |=====×=====×=====|
        |     |     |     |
        |  {}{}{}  |  {}{}{}  |  {}{}{}  |
        |     |     |     |
        |=====×=====×=====|
        '''.format(

            campo[0],
            campo[1],
            campo[2],
            campo[3],
            campo[4],
            campo[5],

            ganhou[0],
            campo[6],
            ganhou[1],

            ganhou[0],
            campo[7],
            ganhou[1],

            ganhou[0],
            campo[8],
            ganhou[1]))
                print('         \033[1;4;32mJogador1 Ganhou!\033[m')
                exit()

    while True:
        jogador2 = int(input('Jogador2 - Digite o Valor: '))
        if (jogador2 == 1):
            if (campo[0] == 1):
                campo[0] = "O"
                break
            elif (campo[0] == "X" or campo[0] == "O"):
                print('\nVocê Não Pode Jogar Aqui!')
                print('Escolha Outro Canto!\n') 
        
        elif (jogador2 == 2):
            if (campo[1] == 2):
                campo[1] = "O"
                break
            elif (campo[1] == "X" or campo[1] == "O"):
                print('\nVocê Não Pode Jogar Aqui!')
                print('Escolha Outro Canto!') 
        
        elif (jogador2 == 3):
            if (campo[2] == 3):
                campo[2] = "O"
                break
            elif (campo[2] == "X" or campo[2] == "O"):
                print('\nVocê Não Pode Jogar Aqui!')
                print('Escolha Outro Canto!') 
        
        elif (jogador2 == 4):
            if (campo[3] == 4):
                campo[3] = "O"
                break
            elif (campo[3] == "X" or campo[3] == "O"):
                print('\nVocê Não Pode Jogar Aqui!')
                print('Escolha Outro Canto!') 
        
        elif (jogador2 == 5):
            if (campo[4] == 5):
                campo[4] = "O"
                break
            elif (campo[4] == "X" or campo[4] == "O"):
                print('\nVocê Não Pode Jogar Aqui!')
                print('Escolha Outro Canto!') 
        
        elif (jogador2 == 6):
            if (campo[5] == 6):
                campo[5] = "O"
                break
            elif (campo[5] == "X" or campo[5] == "O"):
                print('\nVocê Não Pode Jogar Aqui!')
                print('Escolha Outro Canto!') 
        
        elif (jogador2 == 7):
            if (campo[6] == 7):
                campo[6] = "O"
                break
            elif (campo[6] == "X" or campo[6] == "O"):
                print('\nVocê Não Pode Jogar Aqui!')
                print('Escolha Outro Canto!') 
        
        elif (jogador2 == 8):
            if (campo[7] == 8):
                campo[7] = "O"
                break
            elif (campo[7] == "X" or campo[7] == "O"):
                print('\nVocê Não Pode Jogar Aqui!')
                print('Escolha Outro Canto!') 
        
        elif (jogador2 == 9):
            if (campo[8] == 9):
                campo[8] = "O"
                break
            elif (campo[8] == "X" or campo[8] == "O"):
                print('\nVocê Não Pode Jogar Aqui!')
                print('Escolha Outro Canto!') 

        elif (jogador2 > 9):
            print('Escolha de 1 á 9!')
        else:
            print('Erro!')
    
    else:
        print('Erro!')