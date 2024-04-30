
##método uso da palavra chave "def"
## outro detalhe é o uso do ":" para definir o inicio do método e a identação do código é a definição do espoco.
## comandos if também usam : e identação é a definição do escopo.
def sacar(valor):
    saldo = 100

    if(saldo >= valor):
        print("valor sacado")
        print("retire o dinheiro")

    print("obrigado")

def depositar(valor):
    saldo = 100
    saldo += valor

    print(f"deposito de {valor} feito com sucesso!")
    print(f"novo saldo {saldo}")

def inicio_operacao():
    opcao = int(input("Informe [1] para Sacar \n [2] para Extrato: "))
    if(opcao == 1):
        valor = float(input("Informe o valor a sacar: "))

        ## exemplo de estrutura condicional ternaria
        status = "Sucesso no saque!" if(valor < 200) else "SEM SALDO!"
        
        print(status)

    elif (opcao == 2):
        print("Extrato emitido.")
    else :
        print("Informe um valor válido!")
        inicio_operacao()


inicio_operacao()

