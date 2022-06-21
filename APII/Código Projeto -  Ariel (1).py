import sqlite3
import pyttsx3 #Biblioteca para transcrever texto em voz
from time import sleep #Função utilizada para criar um espaço de tempo entre a execução dos menus
dicionario = {1001:"Maria Clara Alves", 1023:"Sandra Ferreira", 3039:"Emanuel Ian Justino"} #Armazenamento de informações básicas sobre o cliente (a funcionalidade pode ser aplicada ao banco de dados com mais complexidade)
#Funções
def id_Clientes(): #Função de identificação do assistente e primeira interação com o cliente
    id_cliente = int(input("Hello!!! Para iniciarmos preciso que você me informe o número do cliente: "))
    print("Bem vindo(a) ",dicionario[id_cliente],"!")
    print("Olá, aqui é Ariel,no que posso te ajudar hoje?")
    engine = pyttsx3.init()
    engine.say("Olá, aqui é Ariel,no que posso te ajudar hoje?")
    engine.runAndWait()

def menu_Principal(): #Função que apresenta o menu Principal. Irá orientar o cliente no atendimento
    print("COMPUTECH TECNOLOGIA")
    print("Menu de Opções \n 1. Resoluções de Problemas \n 2. Ocorrências e Reclamações \n 3. Atendimento Financeiro e Comercial \n 4. Encerrar atendimento")

def menu_Problemas(): #Primeiro Menu secundário. Apresenta os problemas recorrentes e específicos que a empresa irá alimentar no banco de dados
    print(10*("*"))
    print("Menu Soluções")
    print(10*("*"))
    print(" 1. Conexão Intermitente \n 2. Velocidade baixa \n 3. Problemas com o cabeamento \n 5. Retornar ao Menu Principal")

#Apresenta a 1oª slução para problemática 1. Ligada ao banco de dados
def conexao_1(): 
    con = sqlite3.connect("C:\\Users\\Samara\\Desktop\\Projeto APII - Ariel\\AssistenteVirtual.db")
    cursor = con.cursor()
    cursor.execute("SELECT*FROM conexao;")
    for linha in cursor.fetchall():
        print(20*"*")
        print("Tente: ",linha[0])
        print(linha[1])
        print(20*"*")
        con.close()
        
def conexao_2():
    con = sqlite3.connect("C:\\Users\\Samara\\Desktop\\Projeto APII - Ariel\\AssistenteVirtual.db")
    cursor = con.cursor()
    cursor.execute("SELECT*FROM conexao_2;")
    for linha in cursor.fetchall():
        print(20*"*")
        print("Tente: ",linha[0])
        print(linha[1])
        print(20*"*")
        con.close()

def velocidade_1():
    con = sqlite3.connect("C:\\Users\\Samara\\Desktop\\Projeto APII - Ariel\\AssistenteVirtual.db")
    cursor = con.cursor()
    cursor.execute("SELECT*FROM velocidade;")
    for linha in cursor.fetchall():
        print(20*"*")
        print("Tente: ")
        print(linha[1])
        print(20*"*")
        con.close()
    
def velocidade_2():
    con = sqlite3.connect("C:\\Users\\Samara\\Desktop\\Projeto APII - Ariel\\AssistenteVirtual.db")
    cursor = con.cursor()
    cursor.execute("SELECT*FROM velocidade_2;")
    for linha in cursor.fetchall():
        print(20*"*")
        print("Tente: ")
        print(linha[1])
        print(20*"*")
        con.close()

def cabeamento():
    con = sqlite3.connect("C:\\Users\\Samara\\Desktop\\Projeto APII - Ariel\\AssistenteVirtual.db")
    cursor = con.cursor()
    cursor.execute("SELECT*FROM cabeamento;")
    for linha in cursor.fetchall():
        print(20*"*")
        print("Tente: ")
        print(linha[1])
        print(20*"*")
        con.close()

#Menu para o cliente cadastrar problemas específicos que  necessitam atendimento técnico pessoal
def menu_Ocorrencias(): 
    print(10*("*"))
    print("Ocorrências e Reclamações")
    print(10*("*"))
    print(" 1. Abrir ocorrência de chamado técnico \n 2. Realizar reclamação \n 3. Retornar ao Menu Principal")

#Cadastro de chamados pelo cliente
def cadastro_Ocorrencias():
    print("********** CADASTRO DE NOVA OCORRÊNCIA **********")
    con = sqlite3.connect("C:\\Users\\Samara\\Desktop\\Projeto APII - Ariel\\AssistenteVirtual.db")
    cursor = con.cursor()
    id_cliente = int(input("Código do Cliente: "))
    assunto = input("Assunto: ")
    descricao = input("Detalhe a ocorrência: ")
    consultaInsert = "INSERT INTO ocorrencias(id_cliente, assunto, descricao) VALUES (?, ?, ?);"   
    cursor.execute(consultaInsert,(id_cliente, assunto, descricao))
    print("Recebemos seu chamado! Já estou encaminhando os detalhes para nossa equipe técnica, logo eles entraram em contato para solucionar sua ocorrência.")
    con.commit()
    con.close()

#Cdastro de reclamação pelo cliente
def cadastro_Reclamacao():
    print("********** SUGUESTÕES E RECLAMAÇÕES **********")
    con = sqlite3.connect("C:\\Users\\Samara\\Desktop\\Projeto APII - Ariel\\AssistenteVirtual.db")
    cursor = con.cursor()
    id_cliente = int(input("Me confirma novamente o Código do Cliente: "))
    assunto = input("Assunto: ")
    descricao = input("Detalhes a reclamação: ")
    consultaInsert = "INSERT INTO reclamacao(id_cliente, assunto, descricao) VALUES (?, ?, ?);"   
    cursor.execute(consultaInsert,(id_cliente, assunto, descricao))
    print("Muito obrigado por compartilhar conosco sua opinião. A nossa equipe de relacionamento está trabalhando fielmente para implementar novas sugestões e melhorar constantemente nossos serviços, e sua opinião nos ajuda muito a evoluir. OBRIGADOOO!!!")
    con.commit()
    con.close() 

#Contato de setores da empresa que necessitam de contato direto com o cliente
def menu_FinanceiroComercial(): 
    print(10*("*"))
    print("Para atendimento referente ao departamento financeiro ou comercial, por favor entrar em contato pelo e-mail conputech@computech.com.br ou pelo telefone (88) 3333 3444")
    engine = pyttsx3.init()
    engine.say("Para atendimento referente ao departamento financeiro ou comercial, por favor entrar em contato pelo e-mail conputech@computech.com.br ou pelo telefone (88) 3333 3444")
    engine.runAndWait()
    print(10*("*"))

#Código Principal de Interação entre o Assistente e o Cliente
id_Clientes()
menu = 0
while menu != 4:
    print("\n")
    menu_Principal() #Primeira interação. Cliente seleciona primeira funcionalidade
    menu = int(input("Hummm, o que você quer fazer agora? "))
    if menu == 1: #Menu de problemas. As opções são alimentadas pela empresa no decorrer do desenvolvimento
        menu_Problemas()
        cliente = int(input("Entendo, me diz no que posso te ajudar: "))
        #Apresentação ao cliente das soluções para cada problema cadastrado no banco de dados pela empresa
        if cliente == 1:
            conexao_1()
            cliente = int(input("Conseguiu resolver o problema?\n 1- Sim ou 2- Não:"))
            if cliente == 1:
                print("Fico feliz em ajudar.")
            elif cliente == 2:
                conexao_2()
                cliente = int(input("Conseguiu resolver o problema?\n 1- Sim ou 2- Não:"))
                if cliente == 1:
                    print("Fico feliz em ajudar.")
                elif cliente == 2:
                    print("Como não foi possivel te ajudar, vamos abrir uma ocorrência para que nossa equipe técnica possa se direcionar até você para um diagnóstico e resolução do problema?")
                    sleep(1)
                    cadastro_Ocorrencias()
        elif cliente == 2:
            velocidade_1()
            cliente = int(input("Conseguiu resolver o problema?\n 1- Sim ou 2- Não:"))
            if cliente == 1:
                print("Fico feliz em ajudar.")
            elif cliente == 2:
                velocidade_2()
                cliente = int(input("Conseguiu resolver o problema?\n 1- Sim ou 2- Não:"))
                if cliente == 1:
                    print("Fico feliz em ajudar.")
                elif cliente == 2:
                    print("Como não foi possivel te ajudar, vamos abrir uma ocorrência para que nossa equipe técnica possa se direcionar até você para um diagnóstico e resolução do problema?")
                    sleep(1)
                    cadastro_Ocorrencias() #Caso não haja solução, o cliente é orientado a abrir uma ocorrência
        elif cliente == 3:
            cabeamento()
            cliente = int(input("Conseguiu resolver o problema?\n 1- Sim ou 2- Não:"))
            if cliente == 1:
                print("Fico feliz em ajudar.")
                sleep(1)
            elif cliente == 2:
                print("Como não foi possivel te ajudar, vamos abrir uma ocorrência para que nossa equipe técnica possa se direcionar até você para um diagnóstico e resolução do problema?")
                sleep(1)
                cadastro_Ocorrencias()   
        elif cliente == 4: #Reinicia o atendimento. O cliente retorna ao menu principal
            menu_Principal()
        else:
            print("Desculpe, não consegui encontrar a opção.")
            cliente = int(input("Vamos tentar novamente. No que posso te ajudar?"))
            menu_Principal()
    elif menu == 2: #Opção para o cliente cadastro direto de ocorrência
        print("Uma pena que hoje não foi possível te ajudar, mas nossa equipe técnica tá a postos para resolver qualquer problema.")
        sleep(1)
        menu_Ocorrencias()
        cliente = int(input("O que você quer fazer agora? "))
        if cliente == 1:
            cadastro_Ocorrencias()
            sleep(1)
        elif cliente == 2:
            cadastro_Reclamacao()
            sleep(1)
        elif cliente == 3:
            menu_Principal()
        else: #Quando a opção informada pelo cliente não está no banco de dados, retorna ao menu Inicial
            print("Desculpe, não consegui encontrar a opção. Vou te direcionar a nosso menu principal, tá?")
            sleep(1)
            menu_Principal()
    elif menu == 3: #Informa o contato de setores da empresa
        menu_FinanceiroComercial()
    elif menu == 4: #Cliente encerra o atendimento
        print("Haaaa, fim de jogo. Que bom pude te ajudar! Vou estar sempre aqui, byebye!\n")
        sleep(1)
        print("Computech Tecnologia - Solução em Inovação")
    else: #Retorna ao menu inicial
        print("Hummm, não tenho essa opção, você pode me confirmar novamente qual caminho vamos seguir?")
        sleep(1)
        menu_Principal()
#Encerramento da Apresentação pelo Ariel
engine = pyttsx3.init()
engine.say("ARIEL agradece a atenção! Boa noite!")
engine.runAndWait()
