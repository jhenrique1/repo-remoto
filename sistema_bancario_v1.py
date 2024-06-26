#Sistema Bancário V1


saldo = 0
limite_diario = 500
extrato = " "
numero_saques = 0
limite_saques = 3
valor = 0

menu = "Digite a opção desejada:\n[d] Depósito\n[s] Saque\n[e] Extrato\n[q] Sair \n" 

while True:

    opcao = input (menu)

    if opcao == "d":
        
        valor = float(input("Digite o valor que deseja depositar\n"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Falha na operação, valor inválido")


    elif opcao == "s":
        valor = float (input("Digite o valor que deseja sacar\n"))

        saque_excedido = valor > saldo 
        limite_excedido = valor > limite_diario
        saques_excedidos = numero_saques >= limite_saques

        if saque_excedido:
            print("Falha na operação, você não possui saldo suficiente")
        
        elif limite_excedido:
            print("Falha na operação, você excedeu o limite de saque")
        
        elif saques_excedidos:
            print("Falha na operação, você excedeu a quantidade de saques")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print ("Falha na operação, valor inválido")

    elif opcao == "e":
        print("Extrato")

        print("Não foram realizadas movimentações " if not extrato else extrato)

        print(f"\n Saldo: R$ {saldo:.2f}")

    
    elif opcao == "q":
        print("Operação cancelada")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")

    
