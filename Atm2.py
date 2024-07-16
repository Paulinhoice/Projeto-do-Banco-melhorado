from time import sleep
import os

usarios_cadastrados = 2

#database usaurios e contas cadastradas

usuarios = {
  "11011011074" : {"nome" : "Paulo", "nascimento" : "1992", "endereco" : "Rua padre dudu, Dudulandia, Duducity-MG"}}

conta_corrente = {"11011011074" : {"contas" : {"1": {"saldo" :"100"},"2":{"saldo" :"550"}}}
    
}



def criar_usuarios(cpf,idconta,nome,nascimento,endereco):

  if cpf in conta_corrente:
    conta_corrente[cpf]["contas"].update({str(idconta): {"saldo" : 0}})
  else:
    usuarios.update({cpf :{"nome" : nome, "nascimento" : nascimento, "endereco" : endereco}})
    conta_corrente.update({cpf : {"contas" : {str(idconta) : {"saldo" : 0}}}})

def deposito(cpf,idconta,valor_deposito):
  if valor_deposito <= 0:
    print("Você não depositou nenhum valor.")

  else:
    conta_corrente[cpf]["contas"][idconta]["saldo"] += valor_deposito
    print(f"Seu saldo agora é {conta_corrente[cpf]['contas'][idconta]['saldo']}")

def menu_clear():

    sleep(5)
    

    clear = lambda: os.system('cls')
    clear()

def sacar(cpf,idconta,valor_sacado):
  if valor_sacado <= 0:
    print("Você não sacou nenhum valor.")
  elif valor_sacado > conta_corrente[cpf]["contas"][idconta]["saldo"]:
    print("Você não possui um saldo insuficiente")
  else: 
    conta_corrente[cpf]["contas"][idconta]["saldo"] -= valor_sacado
    print(f"Seu saldo agora é {conta_corrente[cpf]['contas'][idconta]['saldo']}")

def extrato(cpf,idconta):
  saldo = conta_corrente[cpf]["contas"][idconta]["saldo"]
  print(f"seu saldo é {saldo}")

#loop para a tela de login do ATM

while True:

  login = input("Você quer fazer login? (Y) ou Você quer se cadastrar? (N)")
  login = login.upper()


#Procedimento para criar uma conta 

  if login == "N":
    cpf = input("Diga seu CPF: ")
    nome = input("Diga seu Nome: ")
    endereco = input("Diga aonde o nome da sua rua,bairro,cidade/estado: ")
    nascimento = input("Diga sua data de nascimento: ")


    usarios_cadastrados += 1
    criar_usuarios(cpf,usarios_cadastrados,nome,nascimento,endereco)
    informarid = usarios_cadastrados
    print(f"O id da sua conta é {informarid}")




#Procedimento para Entrar em uma conta

  elif login == "Y":
    cpf = input("Diga seu CPF: ")
    
    if cpf in usuarios:
      nome = usuarios[cpf]["nome"]
      idconta =  input(f"Ola,{nome} Informe o numero da sua conta 0001-X ")
      
      if idconta in conta_corrente[cpf]["contas"]:
        saldo = conta_corrente[cpf]["contas"][idconta]["saldo"]
      
        menu = -1
        while menu != 0:
          menu = int(input("""

          #####---Bem vindo---#####
            [1] Deposito
            [2] Saque
            [3] Extrato
            [0] Sair
          #####---------------#####
    
            """ ))
        


        #Executando Procendimentos bancaerios do banco
      
          if(menu == 1):
            valor_depositado = float(input(f"Quanto você deseja depositar {nome}?: "))
            deposito(cpf,idconta,valor_depositado)
            
          elif(menu == 2):
            valor_sacado = float(input(f"Quando você deseja sacar {nome}?: "))
            sacar(cpf,idconta,valor_depositado)

          elif(menu == 3):
            extrato(cpf,idconta)



    else:
      print("Não localizamos seu usuario")
      login == "notfound"