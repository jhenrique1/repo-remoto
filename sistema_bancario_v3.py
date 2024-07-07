import textwrap

from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class historico:
    def __init__(self, transacao):
        self.transacao = transacao


class cliente:
    def __init__ (self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self,conta,transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self,conta):
        self.contas.append(conta)


class pessoa_fisica(cliente): #Classe pessoa_fisica é filha da classe cliente
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.nome = nome
      
class conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self._numero = numero
        self._cliente = cliente
        self.agencia = "0001"
        self.historico = Historico()

    @classmethod
    def nova_conta(cls,cliente,numero):
            return cls(numero,cliente)
        
    @property
    def saldo(self):
        return self._saldo
        
    @property
    def numero(self):
        return self._numero
        
    @property
    def agencia(self):
        return self._agencia
        
    @property
    def cliente(self):
        return self._cliente
        
    @property
    def historico(self):
        return self._historico

    def sacar(self,valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Saldo insuficente para essa operacao!")
        
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado")
            return True
        else:
            print("Valor digitado é invalido")
        return False
    
    def depositar(self,valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado!")
            return True
        else:
            print("Valor digitado é inválido")
            return False
        return True
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("OO valor do saque excede o limite.")

        elif excedeu_saques:
            print("Número máximo de saques excedido.")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

        


# def menu():
#     menu = """\n
#     ================ MENU ================
#     [d]\tDepositar
#     [s]\tSacar
#     [e]\tExtrato
#     [nc]\tNova conta
#     [lc]\tListar contas
#     [nu]\tNovo usuário
#     [q]\tSair
#     => """
#     return input(textwrap.dedent(menu))



# def depositar(saldo, valor, extrato, /):
#     if valor > 0:
#         saldo += valor
#         extrato += f"Depósito:\tR$ {valor:.2f}\n"
#         print("\n=== Depósito realizado com sucesso! ===")
#     else:
#         print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

#     return saldo, extrato


# def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
#     excedeu_saldo = valor > saldo
#     excedeu_limite = valor > limite
#     excedeu_saques = numero_saques >= limite_saques

#     if excedeu_saldo:
#         print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

#     elif excedeu_limite:
#         print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

#     elif excedeu_saques:
#         print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

#     elif valor > 0:
#         saldo -= valor
#         extrato += f"Saque:\t\tR$ {valor:.2f}\n"
#         numero_saques += 1
#         print("\n=== Saque realizado com sucesso! ===")

#     else:
#         print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

#     return saldo, extrato


# def exibir_extrato(saldo, /, *, extrato):
#     print("\n================ EXTRATO ================")
#     print("Não foram realizadas movimentações." if not extrato else extrato)
#     print(f"\nSaldo:\t\tR$ {saldo:.2f}")
#     print("==========================================")


# def criar_usuario(usuarios):
#     cpf = input("Informe o CPF (somente número): ")
#     usuario = filtrar_usuario(cpf, usuarios)

#     if usuario:
#         print("\n@@@ Já existe usuário com esse CPF! @@@")
#         return

#     nome = input("Informe o nome completo: ")
#     data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
#     endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

#     usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

#     print("=== Usuário criado com sucesso! ===")


# def filtrar_usuario(cpf, usuarios):
#     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
#     return usuarios_filtrados[0] if usuarios_filtrados else None


# def criar_conta(agencia, numero_conta, usuarios):
#     cpf = input("Informe o CPF do usuário: ")
#     usuario = filtrar_usuario(cpf, usuarios)

#     if usuario:
#         print("\n=== Conta criada com sucesso! ===")
#         return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

#     print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


# def listar_contas(contas):
#     for conta in contas:
#         linha = f"""\
#             Agência:\t{conta['agencia']}
#             C/C:\t\t{conta['numero_conta']}
#             Titular:\t{conta['usuario']['nome']}
#         """
#         print("=" * 100)
#         print(textwrap.dedent(linha))


# def main():
#     LIMITE_SAQUES = 3
#     AGENCIA = "0001"

#     saldo = 0
#     limite = 500
#     extrato = ""
#     numero_saques = 0
#     usuarios = []
#     contas = []

#     while True:
#         opcao = menu()

#         if opcao == "d":
#             valor = float(input("Informe o valor do depósito: "))

#             saldo, extrato = depositar(saldo, valor, extrato)

#         elif opcao == "s":
#             valor = float(input("Informe o valor do saque: "))

#             saldo, extrato = sacar(
#                 saldo=saldo,
#                 valor=valor,
#                 extrato=extrato,
#                 limite=limite,
#                 numero_saques=numero_saques,
#                 limite_saques=LIMITE_SAQUES,
#             )

#         elif opcao == "e":
#             exibir_extrato(saldo, extrato=extrato)

#         elif opcao == "nu":
#             criar_usuario(usuarios)

#         elif opcao == "nc":
#             numero_conta = len(contas) + 1
#             conta = criar_conta(AGENCIA, numero_conta, usuarios)

#             if conta:
#                 contas.append(conta)

#         elif opcao == "lc":
#             listar_contas(contas)

#         elif opcao == "q":
#             break

#         else:
#             print("Operação inválida, por favor selecione novamente a operação desejada.")


# main()