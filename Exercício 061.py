#Refaça o desafio 051, lendo o primeiro termo da razão e a p.a
#Mostrando os 10 primeiros termos da progressao usando a estrutura while
#termo geral an= a1 + (n -1) * r
import time

print("Iremos fazer um programa que calculará para você a P.A")

time.sleep(2)

print("Primeiro você colocará o termo inicial")

time.sleep(2)

print("Depois a razão")

time.sleep(2)

print("Vamos lá?")

termoinicial = int(input("Digite o termo inicial: "))

time.sleep(2)

razao = int(input("Digite a razão: "))


a10 = termoinicial + (9*razao)
elemento = 0

while elemento < 10:
    elemento += 1
    print(f"a{elemento} = {termoinicial} + ({(elemento-1)*razao}) = {termoinicial+(elemento-1)*razao}")
    



    
