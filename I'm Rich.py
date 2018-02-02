import time

nome = str(input('Digite seu Nome: '))
print("\n{}, Bem Vindo ao Game I'm Rich".format(nome))
loja = [' ',' ',' ',' ',]
sair = {'tp': 'time.sleep(0.5)'}
valores = [3,5,10,15]
valor = [100,300,500,1000]
codigo = 'PiterPG'
inserir_codigo = ' '
ganha = [3]
ganha_codigo = [5]
tempo = 0
money = 100

tuto = str(input('Deseja um Tutorial? (S/N) '))

if (tuto.upper() == 'SIM' or tuto.upper() == 'S'):
    print('''
Em 3 Segundos irá Abrir o Menu!
Digite '1' ou'Loja' Para Abrir a Loja!
''')

    time.sleep(3)
    
    print('''
     ________________________
     |  Bem Vindo ao Menu!  |
     |======================|
     |         Opções       |
     |1 - Loja              |
     |2 - Informações       |
     |3 - Em Breve!         |
     |                      |
     |0 - Sair              |
     |======================|
    ''')
    
    opcao = str(input('Qual Você deseja? '))
    
    if (opcao.upper() == '1' or opcao.upper() == 'LOJA'):
        print("Escolha o Patins , Digite '2' ou 'Patins' \nPara Comprar!")
        print('''
     _________________________
     |  Bem Vindo a Loja!    |
     |=======================|
     |  Você tem R${}
     |=======================|
     |        Opções         |
     |1- A Pé      R$0    [X]|
     |2- Patins    R$100  [{}]|
     |3- Patinete  R$300  [{}]|
     |4- Skate     R$500  [{}]|
     |5- Bicicleta R$1000 [{}]|
     |                       |
     |0 - Sair               |
     |=======================|
    '''.format(money,loja[0],loja[1],loja[2],loja[3]))
        opcao1 = str(input('Digite o que você deseja '))
        time.sleep(2.5)
        
        if (opcao1.upper() == '2' or opcao1.upper() == 'PATINS'):
            loja[0] = 'X'
            money -= 100
            print('''
     _________________________
     |  Bem Vindo a Loja!    |
     |=======================|
     |  Você tem R${}
     |=======================|
     |        Opções         |
     |1- A Pé      R$0    [X]|
     |2- Patins    R$100  [{}]|
     |3- Patinete  R$300  [{}]|
     |4- Skate     R$500  [{}]|
     |5- Bicicleta R$1000 [{}]|
     |                       |
     |0 - Sair               |
     |=======================|
    '''.format(money,loja[0],loja[1],loja[2],loja[3]))
            print('Parabens Você acabou de Comprar um Patins!')
            print("\nAgora Digite '0' ou 'Sair' Para Sair da Loja!\n")
            opcao = str(input('Digite o Que Você Deseja: '))
            if (opcao.upper() == '0' or opcao.upper() == 'SAIR'):
                print()
            
elif (tuto.upper() == 'NAO' or tuto.upper() == 'N'):
    print('\nTemos um Profissional Aqui!')
    print('Vamos Começar o Game!')
    money -= 100
    loja[0] = 'X'
print('='*35)
print('''
Ooow , Você tem um Patins 
Então Você Vai Receber mais Dinheiro
Pois com um Patins Você , entrega as Pizza
Mais Rapido!

Então Vamos Começar!
A cada 10 Segundos, Dá uma opcão
Para você Abrir o Menu!

BOA SORTE E BOM JOGO!''')
print('='*35)
time.sleep(0.5)
print('Você tem R${}'.format(money))
while True:
    if (inserir_codigo == codigo):
        money += ganha_codigo[0]
    elif (inserir_codigo == ' '):
        money += ganha[0]
    tempo += 1
    time.sleep(1)
    if (tempo == 10):
        print('Você tem R${}'.format(money))
        tempo = 0
        abrir = str(input('Deseja Abrir o Menu? (S/N) '))
        if (abrir.upper() == 'SIM' or abrir.upper() == 'S'):
            print('''
     ________________________
     |  Bem Vindo ao Menu!  |
     |======================|
     |         Opções       |
     |1 - Loja              |
     |2 - Informações       |
     |3 - Em Breve!         |
     |                      |
     |0 - Sair              |
     |======================|
    ''')
            abrir2 = str(input('Deseja Acessar Qual? '))
            
            
            if (abrir2 == '1' or abrir2.upper() == 'LOJA'):
                print('''
     _________________________
     |  Bem Vindo a Loja!    |
     |=======================|
     |  Você tem R${}
     |=======================|
     |        Opções         |
     |1- A Pé      R$0    [X]|
     |2- Patins    R$100  [{}]|
     |3- Patinete  R$300  [{}]|
     |4- Skate     R$500  [{}]|
     |5- Bicicleta R$1000 [{}]|
     |                       |
     |0 - Sair               |
     |=======================|
     '''.format(money,loja[0],loja[1],loja[2],loja[3]))
                while True:
                    abrir2 = input('Digite o Que você Deseja? ')
                    if (abrir2 == '0' or abrir2.upper() == 'SAIR'):
                        print('Saindo em 3')
                        time.sleep(0.5)
                        print('2')
                        time.sleep(0.5)
                        print('1')
                        print('\nMinerando Dinheiro...\n')
                        break
                        
                    elif (abrir2 == '3' or abrir2.upper() == 'PATINETE'):
                        if (loja[1] == 'X'):
                            while True:
                                print('Você Já Possui este Item!')
                                break
                        
                        elif (money > valor[1]):
                            loja[1] = 'X'
                            money -= valor[1]
                            print('''
     _________________________
     |  Bem Vindo a Loja!    |
     |=======================|
     |  Você tem R${}
     |=======================|
     |        Opções         |
     |1- A Pé      R$0    [X]|
     |2- Patins    R$100  [{}]|
     |3- Patinete  R$300  [{}]|
     |4- Skate     R$500  [{}]|
     |5- Bicicleta R$1000 [{}]|
     |                       |
     |0 - Sair               |
     |=======================|
    '''.format(money,loja[0],loja[1],loja[2],loja[3]))
                    
                        elif (money < valor[1]):
                            falta = valor[1] - money
                            print('\nVocê Não Pode comprar isto!')
                            print('Saldo Insuficiente para Esta Transação!')
                            print('Você tem R${} ,E Faltam R${}\n'.format(money,falta))
            elif (abrir2 == '2' or abrir2.upper() == 'INFORMACOES'):
                print('''
     __________________________
     |Bem Vindo as Informações|
     |========================|
     |          Opções        |
     |1 - Codigo Promocional  |
     |2 - Equipe de Criador   |
     |                        |
     |0 - Sair                |
     |========================|
     ''')
                abrir3 = str(input('Digite o Que Você Deseja: '))
                while True:
                    if (abrir3 == '1' or abrir3.upper() == 'CODIGO'):
                        inserir_codigo = str(input('Digite o Codigo Promocional: '))
                        if (inserir_codigo == codigo):
                     	       money += 100
                     	       print('Codigo Correto!\nAdicionado R$100 na Conta!')
                     	       break
                     	       
        elif (abrir.upper() == 'N' or abrir.upper() == 'NAO'):
            tempo = 0
            
    