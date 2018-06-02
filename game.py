import android , random

droid = android.Android()


cana = [0,0,0,0,1,0,0,0,0]
mud = [0,1]
pontos = 0
chances = 0
print('='*25)
print('Comandos: ')

while True:
    if (chances == 0):
        bola = random.randint(0,8)
        print(bola)
        if (bola == 0):
            if (cana[0] == 1):
                pontos += 1
                chances = 0
        
            elif (cana[0] == 0):
                cana[0] = '+'
                chances = 5
                
        elif (bola == 1):
            if (cana[1] == 1):
                pontos += 1
                chances = 0
                
            elif (cana[1] == 0):
                cana[1] = '+'
                chances = 5
                
        elif (bola == 2):
            if (cana[2] == 1):
                pontos += 1
                chances = 0
                
            elif (cana[2] == 0):
                cana[2] = '+'
                chances = 5
        
        elif (bola == 3):
            if (cana[3] == 1):
                pontos += 1
                chances = 5
                
            elif (cana[3] == 0):
                cana[3] = '+'
                chances = 0
        
        elif (bola == 4):
            if (cana[4] == 1):
                pontos += 1
                chances = 0
                
            elif (cana[4] == 0):
                cana[4] = '+'
                chances = 5
                
        elif (bola == 5):
            if (cana[5] == 1):
                pontos += 1
                chances = 0
                
            elif (cana[5] == 0):
                cana[5] = '+'
                chances = 5
                
        elif (bola == 6):
            if (cana[6] == 1):
                pontos += 1
                chances = 0
                
            elif (cana[6] == 0):
                cana[6] = '+'
                chances = 5
                
        elif (bola == 7):
            if (cana[7] == 1):
                pontos += 1
                chances = 0
                
            elif (cana[7] == 0):
                cana[7] = '+'
                chances = 5
                
        elif (bola == 8):
            if (cana[8] == 1):
                pontos += 1
                chances = 0
                
            elif (cana[8] == 0):
                cana[8] = '+'
                chances = 5
            
    
    
    
    
    

    canvas = '''
Pontos: {}

{}{}{}
{}{}{}
{}{}{}
'''.format(pontos,cana[0],cana[1],cana[2],cana[3],cana[4],cana[5],cana[6],cana[7],cana[8])
    
    droid.dialogCreateAlert('Mapa',canvas)
    droid.dialogSetNeutralButtonText('Continuar')
    droid.dialogShow()
    droid.dialogGetResponse()
    droid.dialogCreateAlert('Comandos')
    droid.dialogSetItems(['Subir', 'Descer', 'Direita', 'Esquerda', 'Sair'])
    droid.dialogShow()
    
    main = droid.dialogGetResponse().result


    #Menu de Sair
    #Item 4
    
    if (main['item'] == 4):
        print('Sair')
        exit()


    #Menu de Subir
    #Item 0
    
    elif (main['item'] == 0):
        print('Subir')
        if (cana[0] == 1):
            print('Nao e possivel!')
            droid.dialogCreateAlert('Não é Possivel!')
            droid.dialogSetNeutralButtonText('Ok')
            droid.dialogShow()
            droid.dialogGetResponse()
            
        elif (cana[1] == 1):
            print('Nao e possivel!')
            droid.dialogCreateAlert('Não é Possivel!')
            droid.dialogSetNeutralButtonText('Ok')
            droid.dialogShow()
            droid.dialogGetResponse()
            
        elif (cana[2] == 1):
            print('Nao e possivel!')
            droid.dialogCreateAlert('Não é Possivel!')
            droid.dialogSetNeutralButtonText('Ok')
            droid.dialogShow()
            droid.dialogGetResponse()
            
        elif (cana[3] == 1):
            if (cana[0] == '+'):
                pontos += 1
                chances =+ 0
            else:
                pass
            
            cana[3] =- 0
            cana[0] =+ 1
        
        elif (cana[4] == 1):
            if (cana[1] == '+'):
                pontos += 1
                chances =+ 0
            
            else:
                pass
                
            cana[4] =- 0
            cana[1] =+ 1
            
        elif (cana[5] == 1):
            if (cana[2] == '+'):
                pontos += 1
                chances =+ 0
            
            else:
                pass
                
            cana[5] =- 0
            cana[2] =+ 1
            
        elif (cana[6] == 1):
            if (cana[3] == '+'):
                pontos += 1
                chances =+ 0
            
            else:
                pass
                
            cana[6] =- 0
            cana[3] =+ 1
            
        elif (cana[7] == 1):
            if (cana[4] == '+'):
                pontos += 1
                chances =+ 0
                
            else:
                pass
                
            cana[7] =- 0
            cana[4] =+ 1
            
        elif (cana[8] == 1):
            if (cana[5] == '+'):
                pontos += 1
                chances =+ 0
                
            else:
                pass
            
            cana[8] =- 0
            cana[5] =+ 1
            
    #Menu de Descer
    #Item 1
    
    elif (main['item'] == 1):
        print('Descer')
        if (cana[0] == 1):
            if (cana[3] == '+'):
                pontos += 1
                chances =+ 0
            else:
                pass
            
            cana[0] =- 0
            cana[3] =+ 1
        
        elif (cana[1] == 1):
            if (cana[4] == '+'):
                pontos += 1
                chances =+ 0
            else:
                pass
            
            cana[1] =- 0
            cana[4] =+ 1
    
        elif (cana[2] == 1):
            cana[2] =- 0
            cana[5] =+ 1
            
        elif (cana[3] == 1):
            if (cana[6] == '+'):
                pontos += 1
                chances =+ 0
            else:
                pass
            
            cana[3] =- 0
            cana[6] =+ 1
        
        elif (cana[4] == 1):
            if (cana[7] == '+'):
                pontos += 1
                chances =+ 0
            else:
                pass
            
            cana[4] =- 0
            cana[7] =+ 1
            
        elif (cana[5] == 1):
            if (cana[8] == '+'):
                pontos += 1
                chances =+ 0
            else:
                pass
            
            cana[5] =- 0
            cana[8] =+ 1
            
        elif (cana[6] == 1):
            print('Não é Possivel!')
            droid.dialogCreateAlert('Não é Possivel!')
            droid.dialogSetNeutralButtonText('Ok')
            droid.dialogShow()
            droid.dialogGetResponse()
            
        elif (cana[7] == 1):
            print('Não é Possivel!')
            droid.dialogCreateAlert('Não é Possivel!')
            droid.dialogSetNeutralButtonText('Ok')
            droid.dialogShow()
            droid.dialogGetResponse()
            
        elif (cana[8] == 1):
            print('Não é Possivel!')
            droid.dialogCreateAlert('Não é Possivel!')
            droid.dialogSetNeutralButtonText('Ok')
            droid.dialogShow()
            droid.dialogGetResponse()
        
    #Menu da Direita
    #Item 2
    
    elif (main['item'] == 2):
        print('Direita')
        if (cana[0] == 1):
            if (cana[1] == '+'):
                pontos += 1
                chances =+ 0
            else:
                pass
            
            cana[0] =- 0
            cana[1] =+ 1
        
        elif (cana[1] == 1):
            if (cana[2] == '+'):
                pontos += 1
                chances =+ 0
            else:
                pass
            
            cana[1] =- 0
            cana[2] =+ 1
    
        elif (cana[2] == 1):
            print('Não é Possivel!')
            droid.dialogCreateAlert('Não é Possivel!')
            droid.dialogSetNeutralButtonText('Ok')
            droid.dialogShow()
            droid.dialogGetResponse()
            
        elif (cana[3] == 1):
            if (cana[4] == '+'):
                pontos += 1
                chances =+ 0
            else:
                pass
            
            cana[3] =- 0
            cana[4] =+ 1
        
        elif (cana[4] == 1):
            if (cana[5] == '+'):
                pontos += 1
                chances =+ 0
            else:
                pass
            
            cana[4] =- 0
            cana[5] =+ 1
            
        elif (cana[5] == 1):
            print('Não é Possivel!')
            droid.dialogCreateAlert('Não é Possivel!')
            droid.dialogSetNeutralButtonText('Ok')
            droid.dialogShow()
            droid.dialogGetResponse()
            
        elif (cana[6] == 1):
            if (cana[7] == '+'):
                pontos += 1
                chances = 0
            else:
                pass
            
            cana[6] =- 0
            cana[7] =+ 1
            
        elif (cana[7] == 1):
            if (cana[8] == '+'):
                pontos += 1
                chances =+ 0
            else:
                pass
            
            cana[7] =- 0
            cana[8] =+ 1
            
        elif (cana[8] == 1):
            print('Não é Possivel!')
            droid.dialogCreateAlert('Não é Possivel!')
            droid.dialogSetNeutralButtonText('Ok')
            droid.dialogShow()
            droid.dialogGetResponse()
    
    #Menu da Esquerda
    #Item 3
    
    elif (main['item'] == 3):
        print('Esquerda')
        if (cana[0] == 1):
            print('Não é Possivel!')
            droid.dialogCreateAlert('Não é Possivel!')
            droid.dialogSetNeutralButtonText('Ok')
            droid.dialogShow()
            droid.dialogGetResponse()
            
        elif (cana[1] == 1):
            if (cana[0] == '+'):
                pontos += 1
                chances = 0
            else:
                pass
            
            cana[1] =- 0
            cana[0] =+ 1
    
        elif (cana[2] == 1):
            if (cana[1] == '+'):
                pontos += 1
                chances = 0
            else:
                pass
            
            cana[2] =- 0
            cana[1] =+ 1
            
        elif (cana[3] == 1):
            print('Não é Possivel!')
            droid.dialogCreateAlert('Não é Possivel!')
            droid.dialogSetNeutralButtonText('Ok')
            droid.dialogShow()
            droid.dialogGetResponse()
        
        elif (cana[4] == 1):
            if (cana[3] == '+'):
                pontos += 1
                chances = 0
            else:
                pass
            
            cana[4] =- 0
            cana[3] =+ 1
            
        elif (cana[5] == 1):
            if (cana[4] == '+'):
                pontos += 1
                chances = 0
            else:
                pass
            
            cana[5] =- 0
            cana[4] =+ 1
            
        elif (cana[6] == 1):
            print('Não é Possivel!')
            droid.dialogCreateAlert('Não é Possivel!')
            droid.dialogSetNeutralButtonText('Ok')
            droid.dialogShow()
            droid.dialogGetResponse()
            
        elif (cana[7] == 1):
            if (cana[6] == '+'):
                pontos += 1
                chances = 0
            else:
                pass
            
            cana[7] =- 0
            cana[6] =+ 1
            
        elif (cana[8] == 1):
            if (cana[7] == '+'):
                pontos += 1
                chances = 0
            else:
                pass
            
            cana[8] =- 0
            cana[7] =+ 1
    
    
    else:
        pass