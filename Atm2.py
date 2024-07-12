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
    conta_corrente[cpf]["contas"].update({idconta : {"saldo" : 0}})
  else:
    usuarios.update({cpf :{"nome" : nome, "nascimento" : nascimento, "endereco" : endereco}})
    conta_corrente.update({cpf : {"contas" : {idconta : {"saldo" : 0}}}})
def deposito(saldo,valor_deposito):
  if valor_deposito <= 0:
    print("Você não depositou nenhum valor.")

  else:
    saldo += valor_deposito
    return(print(f"Seu saldo agora é {saldo}"))        
def menu_clear():

    sleep(5)
    

    clear = lambda: os.system('cls')
    clear()
def depositar():

def sacar():


























#loop para a tela de login do ATM

while True:

  login = input("Você quer fazer login? (Y) ou Você quer se cadastrar? (N)")
  login = login.upper()


#Procedimento para criar uma conta 

  if login == "N":
    cpf = input("Diga seu CPF: ")
    nome = input("Diga seu Nome:")
    endereco = input("Diga aonde o nome da sua rua,bairro,cidade/estado")
    nascimento = input("Diga sua data de nascimento:")


    usarios_cadastrados += 1
    criar_usuarios(cpf,usarios_cadastrados,nome,nascimento,endereco)
    print (conta_corrente.items())




#Procedimento para Entrar em uma conta

  elif login == "Y":
    cpf = input("Diga seu CPF")
    nome = usuarios[cpf]["nome"]
    if cpf in usuarios:
      idconta =  input(f"Ola,{nome} Informe o numero da sua conta 0001-X")
      saldo = conta_corrente[cpf]["contas"][idconta]["saldo"]
      print(saldo)

    else:
      break  