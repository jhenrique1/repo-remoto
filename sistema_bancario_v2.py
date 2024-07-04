import textwrap

def menu(): 
    menu= """\n
    MENU \t

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [nu] Novo usuario
    [q] Sair
    => """
    return input(textwrap.dedent(menu))


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

    

def deposito(saldo,valor,extrato,/):

    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato    


def extrato (saldo, /, *, extrato):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario (usuarios):
    cpf = input ("Digite o CPF:")
    usuario = filtrar_usuario (cpf,usuarios)

    if usuario:
        print("Usuário já existente")
        return
    
    nome = input ("Digite o nome completo:")
    data_nascimento = input("Informe a data de nascimento (dia-mes-ano): ")
    endereco = input("Digite o endereço (logradouro, número, bairro, cidade/sigla do estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf":cpf, "endereco": endereco})

    print("Usuário criado!")

    
def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia,numero_conta,usuarioss):
    cpf = input (print("Digite o CPF do usuario: "))
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta,"usuario": usuario}
    
    print("Usuario não encontrado")



def main():
    agencia = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float (input ("Digite o valor do depósito: \n"))
            saldo, extrato = deposito (saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input ("Digite o valor do saque: \n"))
            
            saldo, extrato = sacar( saldo= saldo, valor = valor, extrato = extrato, limite= limite,
                                   numero_saques = numero_saques, limite_saques = LIMITE_SAQUES,)

        elif opcao == "e":
            extrato (saldo, extrato = extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len (contas) + 1
            conta = criar_conta (agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()

