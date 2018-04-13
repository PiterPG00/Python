import sqlite3, time, io
tempo = time.localtime()
ano = tempo[0]
mes = tempo[1]
dia = tempo[2]
hora = tempo[3]
minuto = tempo[4]

conn = sqlite3.connect('school.db')
c = conn.cursor()

def criar_db():
    c.execute('CREATE TABLE tarefas (materia, pra_fazer, mes, dia, hora, minuto)')


def inserir(materia,o_qfazer,mes,dia,hora,minuto):
    c.execute('INSERT INTO tarefas VALUES(?,?,?,?,?,?)',(materia,o_qfazer,mes,dia,hora,minuto))
    conn.commit()

def listar_materia(materia):
    mate0 = 'SELECT * FROM tarefas WHERE materia = ?'
    for materia in c.execute(mate0,(materia,)):
        print("""
======================================
Materia:
{}

O Que é Para Fazer:
{}

Mês: {} | Dia: {} | Hora: {}:{}
=======================================

""".format(materia[0],materia[1],materia[2],materia[3],materia[4],materia[5]))

def listar_mes(mes):
    mes0 = 'SELECT * FROM tarefas WHERE mes = ?'
    for mes in c.execute(mes0,(mes,)):
        print("""
======================================
Materia:
{}

O Que é Para Fazer:
{}

Mês: {} | Dia: {} | Hora: {}:{}
=======================================

""".format(mes[0],mes[1],mes[2],mes[3],mes[4],mes[5]))
        
def listar_dia(dia):
    dia0 = 'SELECT * FROM tarefas WHERE dia = ?'
    for dia in c.execute(dia0,(dia,)):
        print("""
======================================
Materia:
{}

O Que é Para Fazer:
{}

Mês: {} | Dia: {} | Hora: {}:{}
=======================================

""".format(dia[0],dia[1],dia[2],dia[3],dia[4],dia[5]))

def delete_hora(hora):
    del_hora = 'DELETE FROM tarefas WHERE materia = ?'
    for hora in c.execute(del_hora,(hora,)):
        print("""
======================================
Materia:
{}

O Que é Para Fazer:
{}

Mês: {} | Dia: {} | Hora: {}:{}
=======================================

DELETADO COM SUCESSO!


""".format(hora[0],hora[1],hora[2],hora[3],hora[4],hora[5]))
        
#SE QUISER CRIAR UM NOVO BANCO DE DADOS TIRE OS '''
'''
try:
    criar_db()
except:
    print('Erro ao criar Banco de Dados!')
else:
    print('Banco de Dados Criado com sucesso!')
'''
#SE QUISER CRIAR UM NOVO BANCO DE DADOR COLOQUE """ NO IF (FC2 == 3)
print("""
______________________________________
|          Script por @PiterPG       |
|====================================|
|            SCRIPT ESCOLA           |
|                                    |
|         SISTEMA DE TAREFAS         |
|====================================|""")




while True:

    fc = int(input('\n\n1 - Cadastrar Nova Tarefa \
                   \n2 - Pesquisar Tarefas \
                   \n3 - Apagar Tarefas \
                   \n4 - Criar um Novo Banco de Dados \
                   \n0 - Sair\nO que Você deseja Fazer? '))
    if (fc == 0):
        print('BANCO DE DADOS SALVO!')
        print('Saindo...')
        conn.close()
        time.sleep(3)
        exit()
        
    elif (fc == 1):
        try:
            print('|=============================|')
            print('|     CADASTRO DE TAREFA      |')
            print('|=============================|')
            time.sleep(1)
            materia = str(input('\nDigite o Nome da Materia: '))
            o_qfazer = str(input('Digite o Que é Para Fazer: '))
            inserir(materia,o_qfazer,mes,dia,hora,minuto)

        except:
            print('\nERRO AO CADASTRAR TAREFA!')

        else:
            print('\nCadastrado no MÊS {} , DIA {} , HORA {}:{}'.format(tempo[1],tempo[2],tempo[3],tempo[4])) 
            print('CADASTRADO COM SUCESSO!')

    elif (fc == 2):
        print("""
        _____________
        | CONSULTAR |
        |===========|
        |1 - Materia|
        |2 - Mês    |
        |3 - Dia    |
        |4 - Todos  |
        |           |
        |0 - Sair   |
        |===========|
        """)
              
        fc2 = int(input('Deseja Consultar Por Qual? '))
        if (fc2 == 1):
            try:
                print('Pesquisar Tarefa pela Materia')
                time.sleep(1)
                materia = str(input('Digite o nome da Materia: '))
                print('PUXANDO DADOS CUJO NOME DA MATERIA SEJA ({})\n'.format(materia))
                time.sleep(3)
                print('CADASTROS COM A MATERIA ({}) \nCONSULTADO DIA {} , HORA {}:{}\n'.format(materia,tempo[2],tempo[3],tempo[4]))
                listar_materia(materia)


            except:
                print('ERRO AO CONSULTAR!')

            
        elif (fc2 == 2):
            try:
                print('Consultar Tarefa pelo Mês!')
                time.sleep(1)
                mes = int(input('Digite o Mês: '))
                print('CADASTROS COM O MÊS ({}) \nCONSULTADO DIA {} , HORA {}:{}\n'.format(mes,tempo[2],tempo[3],tempo[4]))
                listar_mes(mes)
                time.sleep(3)
            except:
                print('ERRO AO CONSULTAR!')
        elif (fc2 == 3):
            try:
                print('Pesquisar Cadastro pelo Dia')
                time.sleep(1)
                dia = int(input('Digite o Dia: '))
                print('CADASTROS COM O DIA ({}) \nCONSULTADO DIA {} , HORA {}:{}\n'.format(dia,tempo[2],tempo[3],tempo[4]))
                listar_dia(dia)
                
            except:
                print('Erro ao Consultar!')
        elif (fc2 == 4):
            try:
                print('Mostrar todos os Cadastros!')
                time.sleep(1)
                c.execute('SELECT * FROM tarefas;')
                for linha in c.fetchall():
                    print(linha)
            except:
                print('ERRO')
    elif (fc == 3):
        fc2 = int(input('\n0 - Sair\n1 - Hora\nQual Você deseja? '))
        if (fc2 == 0):
            pass
        elif (fc2 == 1):
            try:
                print('\nAPAGAR CADASTRO PELA HORA!')
                del_hora = int(input('Digite a Hora: '))
                c.execut('DELETE FROM tarefas WHERE hora = ?',(del_hora))

            except:
                print('erro')
            
    elif (fc == 4):
        print('EM BREVE!')
#PARA CRIAR UM NOVO BANCO DE DADOS , COLOQUE O ''' ACIMA!
