#isto é apenas um exemplo de código
#Primeiro contato com o laço de repetição

#For C in range(1,10):
#    print(C)
#print("Fim")

#Agora o mesmo programa feito em while!
import time

C=1
while C <= 10:
    print(C)
    time.sleep(1)
    C += 1

#Esse novo caso while servr pra quando eu não sei o limite!
N = 1
while N != 0:
    N = int(input("Digite um valor: "))
print("Fim")

Resposta = "S"
while Resposta == "S":
    A = int(input("Digite um valor: "))
    Resposta = str(input("Deseja continuar? [S/N]")).upper()
print("Fim")

#Esse agora é ir ver quantos números digitados foram pares e impares:

b = 1
while b != 0:
    b = int(input("Digite um valor: "))