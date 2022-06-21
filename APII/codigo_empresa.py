import sqlite3
 
#Menu principal
def menu_1(): 
   print("Administrar problemas")
   print("Ocorrências")

#Menu dos problemas
def menu_problemas(): 
   print(" 1. Cadastrar problema")
   print(" 2. Editar problema")
   print(" 3. Remover problema")
   print(" 4. Ocorrencias")
   print(" 5. Sair")

#Inserção dos problemas e soluções
def cadastro_de_problemas():
   con = sqlite3.connect("C:\\Users\\Samara\\Desktop\\Projeto APII - Ariel\\AssistenteVirtual.db")
   cursor = con.cursor()
   print("|===-===-=== CADASTRO DE PROBLEMAS ===-===-===-|")
   id= int(input("Id:"))
   solucao = str(input("Solução:"))
   consultaInsert = ("INSERT INTO cabeamento (id, solucao) VALUES (?,?);")
   cursor.execute (consultaInsert,(id,solucao))
   con.commit()
   con.close()

#Edição dos problemas
def editar_problema():
    con = sqlite3.connect("C:\\Users\\Samara\\Desktop\\Projeto APII - Ariel\\AssistenteVirtual.db")
    cursor = con.cursor()
    id = int(input("Digite o ID do problema que será atualizado:  "))
    coluna = str("nome")
    editar = str(input("Atualização do nome do problema: "))
    consultaUpdate = "UPDATE cabeamento "+coluna+ "=? WHERE id = ?;"
    cursor.execute(consultaUpdate,(editar,id))
    con.commit()
    con.close()
    print("Alteração concluída")

#Remoção dos problemas
def remover_problema(): 
   id = int(input("Digite o ID do problema a ser removido: "))
   con = sqlite3.connect("C:\\Users\\Samara\\Desktop\\Projeto APII - Ariel\\AssistenteVirtual.db")
   cursor = con.cursor()
   consultaDelete = "DELETE FROM cabeamento WHERE id =?;"
   cursor.execute(consultaDelete,[(id)])
   con.commit()
   con.close()

#Ocorrências feitas pelos clientes
def ocorrencias():
   print("As ocorrências dos clientes: ")
   con = sqlite3.connect("C:\\Users\\Samara\\Desktop\\Projeto APII - Ariel\\AssistenteVirtual.db")
   cursor = con.cursor()
   cursor.execute("SELECT*FROM ocorrencias;")
   for linha in cursor.fetchall():
        print("________________________________________")
        print("Id: ",linha[0])
        print("Assunto: ",linha[1])
        print("Descrição: ",linha[2])
   con.close()


#Funções de menus
def sair():
   print("Implementação finalizada")

def opcao_invalida(): 
   print("Você digitou uma opção inválida")

#Navegação nos menus
opcao1 = 1
while (opcao1!=4):
   menu_1()
   menu_problemas()
   opcao = int(input("Digite a opção: "))
   if (opcao ==1):
      cadastro_de_problemas()
      print("Alteração concluída")
      menu_1()
      opcao = input("Opção:  ")
   elif(opcao == 2):
      editar_problema()
      print("Alteração concluída")
      menu_1()
      opcao = input("opção: ")    
   elif(opcao == 3):
      remover_problema()
      print("Remoção concluída")
      menu_1()
      opcao = input("opção:")
   elif(opcao == 5):
      sair()
   elif (opcao == 4):
     ocorrencias()
   else:
     opcao_invalida()
