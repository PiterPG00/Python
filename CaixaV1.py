#Script por PiterPG
#Caixa V1
import time
vezes = 0
print(" "*12,"_"*23)
print(" "*12,"| #Script Por PiterPG |")
print(" "*12,"|     Sistema Caixa   |")
print(" "*12,"|       Versão 1.0    |")
print(" "*12,"^"*23)
while True:
    valor = float(input("\nDigite o Valor do Produto: R$ "))
    recebeu = float(input("Quanto Você Recebeu de Dinheiro: R$ "))
    troco = recebeu - valor
    falta = valor - recebeu
    if (valor > recebeu):
        print("\nFalta R$ {:.2f} Para Completar os R$ {:.2f}".format(falta,valor))
        dese = input("\n\nDeseja Esperar o Resto do Dinheiro? \n(Sim/Nao) ")
        if (dese.upper() == "SIM"):
            print("\nEsperando 5 Segundos!")
            time.sleep(1)
            recebeu2 = float(input("\nQuanto Você Recebeu Agora? "))
            recebeu3 = recebeu + recebeu2
            if (valor > recebeu3):
                falta2 = valor - recebeu3
                print("Agora está Faltando R$ {:.2f}\nPara os R$ {:.2f}".format(falta2,valor))
            elif (recebeu3 > valor):
                troco2 = recebeu3 - valor
                print("Você tem que dar R$ {:.2f} de Troco!".format(troco2))
            else:
                print("Não Precisa dar Troco!")
                print("Pois o Dinheiro está Completo!")
    elif (recebeu > valor):
        print("\nVocê Vai dar de Troco R$ {:.2f} ".format(troco))
    else:
        print("\nNão Precisa dar Troco!")
        print("Pois Está Completo o Dinheiro!")
    desejo = input("\nVocê Deseja Continuar? \n(Sim/Nao) ")
    if (desejo.upper() == "SIM"):
        vezes = vezes + 1
    else:
        if (vezes == 0):
            print("\nVocê Não Repetiu esse Programa Nenhuma Vez")
            print("Mesmo Assim , Volte Sempre!\n")
            print(" "*12,"_"*23)
            print(" "*12,"| #Script por PiterPG |")
            print(" "*12,"^"*23)
            exit()
        else:
            print("Você Repetiu esse Programa {} Vezes!".format(vezes))
            print("Volte Sempre!\n")
            print(" "*12,"_"*23)
            print(" "*12,"| #Script por PiterPG |")
            print(" "*12,"^"*23)
            exit()