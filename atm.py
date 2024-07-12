
saldo=0
deposito = 0
saque = 0
saque_dia = 0
limit_saque=500
voltar_menu = -1
extrato_saque =3 
extrato_deposito = 1




#Assumi que era uma maquina eletronica, então não teria como sacar ou depositar por exemplo 50 centavos



menu = -1
while True:

  menu = int(input("""

    #####---Bem vindo---#####
         [1] Deposito
         [2] Saque
         [3] Extrato
         [0] Sair
    #####---------------#####
    
    """ ))
  

  if menu == 1:
        deposito = int(input("Qual o valor que você deseja depositar? "))
        if deposito <= 0:
          print("Esse valor é invalido")
        else:
          saldo = saldo + deposito
          extrato_deposito += 1
          
          print(f"Seu saldo agora é R$: {saldo}")
          
  elif menu == 2:
    if saque_dia < 3:
      saque = int(input("Qual o valor que você deseja Sacar? "))
      while True:
          if saque <= 0:
            print("Esse valor é invalido")
            break

          elif saldo <= 0:
            print("Você não tem saldo disponivel")
            break

          else:
             if saque > 500:
                print("Saque limite só vai até 500 Reais")
                break
             else:
              saldo = saldo - saque
              saque_dia += 1
              extrato_saque += 1
              
              print(f"Aguarde para retirar R$: {saque}, saldo restante: R$: {saldo}")
              break
         
    else: print("Você não pode mais realizar saques hoje")    


  elif menu == 3:
    print(f"Seu saldo é {saldo}")
    if extrato_saque == 1 or extrato_deposito == 1:
       print("Não houve Transação")
    else:
       print(f"saque{saque}")
       print(f"deposito{deposito}")
      
    

  elif menu == 0:
    break

 
