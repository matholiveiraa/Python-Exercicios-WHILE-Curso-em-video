#Crie um programa que leia vários núemros inteiro pelo teclado
#No final da execução mostra a média entre todos os valores e qual foi o maior e menor
#O programa deve perguntar ao usuario se ele quer continuar ou não

import time

print("Iremos te fazer um programa onde você irá dar varios números")

time.sleep(2)

print("Iremos calcular a média para você e qual será o maior e menor valor que você digitar!!")

continuar = "S"
alteracao = ""
listanumeros = []


while continuar  == "S":
    n = int(input("Digite um novo valor: "))
    listanumeros.append(n)
    maxlista = max(listanumeros)
    minlista = min(listanumeros)
    print(listanumeros)
    continuar = str(input("Deseja continuar N para não e S para Sim: ")).upper()
    if continuar == "N":
        print("Obrigado, aqui estão seus dados:")
        print(f"{listanumeros}, essa é a lista")
        print(f"Valor maximo: {maxlista}, Valor mínimo: {minlista}")
        print(f"{sum(listanumeros) / len(listanumeros)} é a média!")

    
