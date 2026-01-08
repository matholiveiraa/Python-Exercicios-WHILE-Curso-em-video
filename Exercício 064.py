#O computador vai pensar um número onde o jogador terá de acertar
#Enquanto o jogador não acertar repita a pergunta
#No final mostre quantos erros

import time

print("Iremos fazer um jogo contigo!")

time.sleep(3)

print("Será sorteado um número de 1 a 999 e vc terá de acertar!!!")

time.sleep(2)

print("Vamos lá? Você terá de digitar o número!")

time.sleep(1)

n = 999 #valor para acertar

calculadordeerros = [] #lista com valores dentro

erros = -1 #conta erros 

tentativa = 0 #tentarivas

while tentativa != n: #enquanto tentativa for diferente da chave
    tentativa = int(input("Tente acertar o número: "))
    erros+=1 #some mais 1 erros
    calculadordeerros.append(tentativa)#coloque o numero digitado dentro da lista
if tentativa == n:
    calculadordeerros.remove(999) #aqui eu removi da lista o valor 999 para que ele n some junto
    print(f"Você acertou, com exatas {erros} falhas, e a soma deles é {sum(calculadordeerros)}") #aqui fiz um soma da calculadoradeerros que é um lista com valores dentro
