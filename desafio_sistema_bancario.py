
#Definição da Classe Cliente, dados básicos
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
    def exibir_dados(self):
        print(f"{self.nome} - {self.cpf}")



#Definição da Classe Conta (conta bancária), também dados básicos
class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.operacoes_saque = 0
        self.MAXIMO_OPERACOES_SAQUE = 3
        self.LIMITE_SAQUE = 500.00

    def Depositar(self, valor_depositar):
        if valor_depositar > 0:
            self.saldo += valor_depositar
            print(f"Depósito realizado com sucesso! Novo Saldo: R$ {self.saldo}")
        else:
            print("Para depósito, por favor informe um valor maior que zero!")

    def Sacar(self, valor_sacar):
        if valor_sacar > 0:
            if self.saldo >= valor_sacar:
                if valor_sacar > self.LIMITE_SAQUE:
                    print(f"Operação não permitida! Valor de saque superior ao limite de R$ {self.LIMITE_SAQUE}")
                    return
                
                self.operacoes_saque += 1
                if self.operacoes_saque > self.MAXIMO_OPERACOES_SAQUE:
                    print(f"Limite de operações de saque excedido! Limite: {self.MAXIMO_OPERACOES_SAQUE}")
                    return
                
                self.saldo -= valor_sacar
                print(f"Saque realizado com sucesso! Novo Saldo: R$ {self.saldo}" )
            else:
                print(f"Saldo insuficiente! Por favor, informe um valor inferior a R$ {valor_sacar}!")
        else:
            print("Para saque, por favor informe um valor maior que zero!")


cliente = Cliente("Raimundo Nonato", "01234567890")
conta = Conta(123, cliente)

def MovimentacaoFinanceira(conta, cliente):
    while True:
        mensagem = """
====== INFORME UMA OPÇÃO ======
[1] - Depósitar
[2] - Sacar
[0] - Sair
        
        """        
        print(mensagem)
        opcao = int(input())
        if opcao == 1:
            valor_depositar = float(input("Informe o valor para Depósito: "))
            conta.Depositar(valor_depositar)

        elif opcao == 2:
            valor_saque = float(input("Informe o valor que deseja Sacar: "))
            conta.Sacar(valor_saque)

        elif opcao == 0:
            print("Obrigado por usar nossos serviços!")
            break

        else:
            print("Opção Inválida! Informe somente os números: 1, 2 ou 0 da opção desejada.")
            

MovimentacaoFinanceira(conta, cliente)

#TODO - Falta formatar em reais.
