nomecurso = "PYthon"

print(nomecurso.upper())
#PYTHON

print(nomecurso.lower())
#python

print(nomecurso.title())
#Python

nomecurso = "   Python   "
print(nomecurso.strip())
#"Python"

print(nomecurso.lstrip())
#"Python   "

print(nomecurso.rstrip())
#"    Python"

#-----------------------------------
#Junções e centralizações de String

nomecurso = "Python"
print(nomecurso.center(10, "#"))
# "##Python##"

#substitui o uso de estrutura de repetição, for ou while.
print(".".join(nomecurso))
# "P.y.t.h.o.n"

#------------------------------------
#Interpolação de variaveis

#Usar %s para parametros strings dentro do texto
#Usar %d para parametros numero dentro de texto
#Exemplo de uso MÉTODO ANTIGO, EVITAR USAR DESSA FORMA (OLD STYLE)
nome = "José"
idade= 20
profissao = "Analista"
empresa = "Nasa"
dicionario_pessoa = {'nome': "Ana", 'idade': 30, 'funcao': "Contadora", 'trabalho': "Digitadora"}

print("Olá, meu nome é %s. Eu tenho %d anos de idade" % (nome, idade))

#Método format (Similar ao OLD STYLE)
print("Olá, meu nome é {}. Eu tenho {} anos de idade".format(nome, idade))

#Método format especificando a posição dos parametros (MELHOR USUAL, pois facilita a posição de informar os parametros em format)
print("Olá, meu nome é {0}. Eu tenho {1} anos de idade e trabalho como {2} na empresa {3}".format(nome, idade, profissao, empresa))

#Método format usando nome de identificadores na string
print("Olá, meu nome é {nome}. Eu tenho {idade} anos de idade e trabalho como {funcao} na empresa {trabalho}".
      format(nome = nome, idade = idade, funcao = profissao, trabalho=empresa))


#--------------- Os dois mais recomendados para USO no dia a dia -----------------------------
#Método format usando nome de identificadores na string usando um DICIONARIO com as colunas igual ao mesmo nome dos identificadores
print("Olá, meu nome é {nome}. Eu tenho {idade} anos de idade e trabalho como {funcao} na empresa {trabalho}".format(**dicionario_pessoa))

#Método abreviado, mas facilmente usado! usando a notação "f" já pode usar diretamente a variavel.
print(f"Meu nome é {nome} e tenho {idade} anos de idade.")

#tratando formatação de valores
PI = 3.14159
print(f"Valor de PI: {PI: .2f}")
#Valor de PI: 3.14

#Formatando antecedendo 10 espaços
print(f"Valor de PI: {PI:10.2f}")
#Valor de PI:          3.14


#------------------------------------------------------
#Fatiamento de Strings

nome = "Cristiano Arquitetura Software"

print(nome[0])
#"G"

print(nome[:9])
#"Cristiano"

print(nome[10:])
#"Arquitetura Software"

print(nome[10:16]) #SUBSTRING
#"Arquit"

print(nome[10:16:2]) #Filtra de 10 a 16 com passo 2
#"Aqi"

print(nome[:])
#"Cristiano Arquitetura Software"

print(nome[::-1]) #Reverso (Espelhamento)
#"erawtfoS arutetiuqrA onaitsirC"

#-----------------------------------------------------
# Strings multiplas linhas ou Strings TRIPLAS
# Usual para manter um determinado texto formato com espaços não perdendo edentação

nome = "Guilherme"

mensagem = f'''
   Olá meu nome é {nome},
 Eu estou aprendendo Python.
       Essa mensagem tem diferentes recuos.
'''
print(mensagem)

#também pode ser usado com aspas duplas tres vezes, é o mesmo efeito.
mensagem = f"""
   Olá meu nome é {nome},
 Eu estou aprendendo Python.
       Essa mensagem tem diferentes recuos.
"""
print(mensagem)