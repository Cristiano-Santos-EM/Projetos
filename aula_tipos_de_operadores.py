##aula_tipos_de_operadores.py

##principais operadores
soma = 1 + 1
print(soma)

subtracao = 5 - 1
print(subtracao)

multiplicacao = 3 * 3
print(multiplicacao)

divisao = 5 / 2
print(divisao)

potencia = 2 ** 3
print(potencia)

## resto da divisao
modulo = 10 % 3
print(modulo)

##expressoes e prioridades de execucao
x = 10 - 5 * 2
print(x)

y = (10 - 5) * 2
print(y)

saldo = 450
saque = 200

print(saldo < saque)

print( saldo != saque)

print( saldo == saque)

saldo += 10
print(saldo)

saldo *= 10
print(saldo)

saldo /=2
print(saldo)

saldo **=2
print(saldo)

print((saldo > 0 and saque > 0) or 1 * 2 >= 0)


## operadores de identidade

curso = "curso de python"
nome_curso = curso 

print(curso is nome_curso)

print(curso is not nome_curso)

print(saldo is saque)

## operadores de associação
frutas = ["uva", "laranja", "maçã"]
saques_feitos = [100, 50]

print("python" in curso)
print("uva" in frutas)
print("pera" in frutas)
print(300 in saques_feitos)