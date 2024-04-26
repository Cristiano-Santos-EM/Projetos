print("Hello World!")

 #declaração de variavel tipada, lembrando que não é obrigatorio, pois o python identifica o tipo conforme o valor de atribuição
mensagem = str("Mensagem Texto")
print (mensagem)

#--------------- VARIAVEIS E TIPOS DE DADOS --------------
# VARIAVEIS que não foram definidos os tipos explicitamente.
# tipos de variveis principais:  int, float, bool, str, bytes, bytearray, memoryview
#outros tipos de VARIAVEIS: 
# Sequencia -> list(), tuple(), range()
# Mapa -> dict(); chave e valor;
# Coleção -> set(), frozenset ()

idade = 23
nome = "José"

#na função de print, usar "f" antes do conteudo, permite fazer uso de variaveis com {}
print(f"A pessoa {nome} possui {idade}")

#declaração de variaveis na mesma linha, necessário determinar o valor de cada variavel na mesma sequencia!
melhorIdade, nomeExperiente = (60, "Antônio")

print(f"A melhor idade é {melhorIdade} nome {nomeExperiente}")

#CONSTANTES, em python não há comando para constantes, a sugestão é usar por convenção tudo em maiusculo para identificar visualmente a intenção de ser constante.
ESTADOS_DO_BRASIL = ["GO", "SP", "MG"]

print(ESTADOS_DO_BRASIL)


#---------- CONVERSÃO DE TIPOS ----------

preco = 7
preco = float(preco)
print(preco)

#também pode ser feito em operação de divisão
#divisão utilizando uma / converte para float, se for duas // então converte para inteiro

print(10 / 2)
print(10 // 2)


#----- entrada de DADOS ----------
nome = input("Informe seu nome: ")
idade = input("Informe idade: ")

print(f"retorno: {nome} {idade}")

print("Teste inclusão fim de caractere!", end=" ...\n")

print ("Separa", "Entre", "Palavras", sep="@" )
