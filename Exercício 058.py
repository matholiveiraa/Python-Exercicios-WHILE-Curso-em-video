#O computador vai pensar um número onde o jogador terá de acertar
#Enquanto o jogador não acertar repita a pergunta
#No final mostre quantos erros

import time

print("Iremos fazer um jogo contigo!")

time.sleep(3)

print("Será sorteado um número de 1 a 10 e vc terá de acertar!!!")

time.sleep(2)

print("Vamos lá? Você terá de digitar o número!")

time.sleep(1)

n = 10


erros = -1

tentativa = ""

while tentativa != n:
    tentativa = int(input("Tente acertar o número: "))
    erros+=1
if tentativa == n:
    print(f"Você acertou, com exatas {erros} falhas!!")
