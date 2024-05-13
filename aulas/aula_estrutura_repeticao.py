##estrutura FOR

texto = input("Informe uma letra: ")
VOGAIS = "AEIOU"

for letra in texto:
    if(letra.upper() in VOGAIS):
        print(letra.upper(), end=" ")


print("Agora teste com while....")

valor = int(input("Informe um numero: "))

while True:
    if(valor > 10):
        print("maior que 10! /n")
        valor = int(input("Informe um numero: "))
    else:
        break
