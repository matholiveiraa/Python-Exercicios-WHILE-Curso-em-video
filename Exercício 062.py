#Refaça o desafio 061, lendo o primeiro termo da razão e a p.a
#Mostrando os 10 primeiros termos da progressao usando a estrutura while
#termo geral an= a1 + (n -1) * r
#agora apenas o usuário quer ter mais uma opção de p.a ou não quer mais
import time

print("Iremos fazer um programa que calculará para você a P.A")

time.sleep(2)

print("Primeiro você colocará o termo inicial")

time.sleep(2)

print("Depois a razão")

time.sleep(2)

print("Vamos lá?")

time.sleep(2)

print("Caso queira mais p.a depois iremos de te perguntar, caso não quiser aperte 0")

termoinicial = int(input("Digite o termo inicial: "))

time.sleep(2)

razao = int(input("Digite a razão: "))



a10 = termoinicial + (9*razao)
elemento = 0
elemento1 = 0
termosamais = 0

while elemento < 10:
    elemento += 1
    print(f"a{elemento} = {termoinicial} + ({(elemento-1)*razao}) = {termoinicial+(elemento-1)*razao}")
    

while True: #Criamos um bloco que se repetirá indefinidamente.

    termosamais = int(input("Quantos termos você quer mais? 0 para não?:")) #termosamais seria quantas p.a seriam a mais
    if termosamais == 0: #caso termosmais for igual a 0 o programa quebra
        break # break: É a "chave de desligar". Quando o usuário digita 0, o if detecta e quebra o loop principal.
    
    continuidade = elemento + termosamais #continuidade é igual a p.a + termosamais
    while elemento < continuidade: #enquanto p.a < continuidade
        elemento += 1 #desta forma a p.a "nunca alcança" a continuidade
        print(f"a{elemento} = {termoinicial} + ({(elemento-1)*razao}) = {termoinicial+(elemento-1)*razao}")