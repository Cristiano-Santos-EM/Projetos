#lista com elementos ()
frutas = ["laranja", "maçã", "uva"]
print(frutas)

print(frutas[0])
print(frutas[1])

#indice -1 é referente ao último item
print(frutas[-1])
print(frutas[-3]) #pega do último item voltando

#lista vazia
frutas = []

#lista de letras, usando a classe list, neste caso não é um elemento só na lista. Cada letra é um elemento.
letras = list("python")
print(letras)

#função range gera um elemento (numero) de tamanho 10 elementos (0, 1, 2, ...9)
numeros = list(range(10))
print(numeros)

#como não é tipado, podemos ter diferentes tipos de elementos de diferentes tipos em uma lista

elementos_diversos = ["ferrari", "F8", 425555, 2020, 2024, "São Paulo", True]
print(elementos_diversos)


#MATRIZ
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0]) #[1, "a", 2]

print(matriz[0][0]) # 1

print(matriz[-1][-1]) # "c" (ultimo elemento linha x coluna)

#percorrendo uma lista
carros = ["gol", "celta", "bmw"]
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#outra forma

numeros = [1, 30 ,21, 2, 9 ,65, 34]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# outra forma, agora armazendo o numero ao quadrado.
quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)

#outra forma de fazer isso
pares = [numero for numero in numeros if numero % 2 ==0]

#----incluindo item na lista APPEND
lista = []
lista.append(1)
lista.append("Python")
lista.append([40,50,60])

print(lista) #[1, "Python", [40,50,60]]

#---- limpando a lista .CLEAR
lista.clear()
print(lista) #[]

#---- comando COPY
lista = [1, "Aula", [10,20,30]]
copia = lista.copy()

print(lista) #[1, "Aula", [10,20,30]]

print(id(copia), id(lista))

copia[0] = 999
print(lista)
print(copia)

#COUNT, traz a qutde de vezes que determinado valor aparece na lista.
cores = ["vermelho", "azul", "verde", "azul"]

cores.count("vermelho") #1
cores.count("azul") #2

#EXTEND serve para JUNTAR duas listas em uma.
linguagens = ["python", "js", "c"]
print(linguagens) #["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens) #["python", "js", "c", "java", "csharp"]

#INDEX
linguagens = ["python", "js", "c", "JAVA", "CSHARP"]

print(linguagens.index("JAVA")) #3 traz a primeira ocorrencia da posição que este conteudo está


#POP retira o ultimo elemento da lista, mas também pode-se remover um elemento especifico
linguagens = ["python", "js", "c", "JAVA", "CSHARP"]

linguagens.pop()
linguagens.pop(0)

#REMOVE remove um determinado elemento informando o objeto a ser removido. ele remove só a primeira ocorrencia .
linguagens.remove("JAVA")

#REVERSE inverte os elementos da lista do ultimo para o primeiro
linguagens.reverse()

#SORT ordenação da lista
linguagens.sort() #ordenação padrao alfabetica

linguagens.sort(reverse=True) #ordena a lista de traz para a frente.

linguagens.sort(key=lambda x: len(x)) #ordena a lista pelo tamanho do elemento (do menor para o maior)

#LEN para saber a quantidade de elementos da lista
len(linguagens)

#SORTED ordena iteraveis
sorted(linguagens, key=lambda x: len(x), reverse=True) #da mesma forma que o sort