from time import sleep
import os

contas_registradas = 2


usuarios = {
  "11011011074" : {"nome" : "Paulo", "nascimento" : "1992", "endereco" : "Rua padre dudu, Dudulandia, Duducity-MG"}
}

accounts = {
   "11011011074" : {"contas" : {"1": {"saldo" :"100"},"2":{"saldo" :"0"}}},
   "11231231231" : {"contas" : {"1": {"saldo" :"100"},"2":{"saldo" :"0"}}}

}




#se o cpf já tiver registradado, deve ir para um menu pra selecionar a conta
#se não tiver registrado registre e ja crie uma conta autoamticamente e informar ao cliente


def criar_usuarios(cpf,nome,nascimento,endereco,):
      
      usuarios[cpf] = {"nome" : nome, "nascimento" : nascimento, "endereco" : endereco, }
      
      
       

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

lista = ["teste", "teste2"]

saldo = (accounts["11011011074"]["contas"]["1"]["saldo"])
print(saldo) 