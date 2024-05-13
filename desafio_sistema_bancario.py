from datetime import datetime
from enum import Enum

#Definição da Classe Cliente, dados básicos
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
    def exibir_dados(self):
        print(f"{self.nome} - {self.cpf}")

class Operacao:
    def __init__(self, tipo_operacao, valor, data):
        self.tipo_operacao = tipo_operacao
        self.valor = valor
        self.data = data
        
class TiposDeOperacao(Enum):
    SAQUE = "SAQUE"
    DEPOSITO = "DEPOSITO"


#Definição da Classe Conta (conta bancária), também dados básicos
class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.operacoes_saque = 0
        self.MAXIMO_OPERACOES_SAQUE = 3
        self.LIMITE_SAQUE = 500.00
        self.operacoes_realizadas = []

    def Depositar(self, valor):
        data = datetime.today()
        operacao = Operacao(TiposDeOperacao.DEPOSITO, valor, data)

        if valor > 0:
            self.saldo += valor
            self.operacoes_realizadas.append(operacao)

            print(f"Depósito realizado com sucesso! Seu novo saldo é R$ {self.saldo:.2f}")
            return True
        else:
            print("Para depósito, por favor informe um valor maior que zero!")
            return False

    def Sacar(self, valor):
        data = datetime.today()
        operacao = Operacao(TiposDeOperacao.SAQUE, valor, data)

        if valor > 0:
            if self.saldo >= valor:
                if valor > self.LIMITE_SAQUE:
                    print(f"Operação não permitida! Valor de saque superior ao limite de R$ {self.LIMITE_SAQUE:.2f}")
                    return False
                
                self.operacoes_saque += 1
                if self.operacoes_saque > self.MAXIMO_OPERACOES_SAQUE:
                    print(f"Limite de operações de saque excedido! Limite {self.MAXIMO_OPERACOES_SAQUE} operações!")
                    return False
                
                self.saldo -= valor
                self.operacoes_realizadas.append(operacao)

                print(f"Saque realizado com sucesso! Novo Saldo R$ {self.saldo:.2f}" )
                return True
            else:
                print(f"Saldo insuficiente! Por favor, informe um valor inferior a R$ {valor:.2f}!")
        else:
            print("Para saque, por favor informe um valor maior que zero!")

        return False

    def Extrato(self):
        operacoes = self.operacoes_realizadas

        print("EXTRATO BANCÁRIO")
        print(f"DATA    |OPERAÇÃO            |VALOR")
        print(f"--------|--------------------|---------")


        for operacao in operacoes:
            valor_formatado = operacao.valor if operacao.tipo_operacao != operacao.tipo_operacao.SAQUE else - operacao.valor
            print(f"{operacao.data.strftime("%d/%m/%y")} {operacao.tipo_operacao.value:<20} R${operacao.valor:.2f} ")

        print(" ")
        print(f"Saldo R$ {self.saldo:.2f}")
        print(f"---------------------------------------")



def MovimentacaoFinanceira(conta, cliente):
    while True:
        mensagem = """
====== INFORME UMA OPÇÃO ======
[D] - Depósitar
[S] - Sacar
[E] - Extrato
[X] - Sair
===============================
"""        
        opcao = input(mensagem).upper()

        if opcao == "D":
            valor_depositar = (input("Informe o valor para Depósito R$")).replace(",",".")
            try:
                valor_depositar = float(valor_depositar)
            except ValueError:
                print("Por favor informe um valor númerico!")
            
            conta.Depositar(valor_depositar)

        elif opcao == "S":
            valor_saque = (input("Informe o valor que deseja Sacar R$")).replace(",",".")
            try:
                valor_saque = float(valor_saque)
            except ValueError:
                print("Por favor informe um valor númerico!")

            conta.Sacar(valor_saque)

        elif opcao == "E":
            conta.Extrato()

        elif opcao == "X":
            print("Obrigado por usar nossos serviços!")
            break

        else:
            print("Opção Inválida! Por favor, informe a letra correspondente a opção desejada.")


cliente = Cliente("Raimundo Nonato", "01234567890")
conta = Conta(123, cliente)

MovimentacaoFinanceira(conta, cliente)