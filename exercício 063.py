#Escreva um programa que leia um número n inteiro
#Qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci
#Início: A sequência começa com os números 0 e 1 (ou às vezes 1 e 1). 
#Para encontrar o próximo número, some os dois números imediatamente anteriores a ele

#Fórmula (Termo Geral):     
#Para menor que 2:
#Fn = Fn-1 + Fn-2

#Para maior que 2:



import time

print("Iremos criar um programa que calcula a sequencia de fibonacci pra você!")

time.sleep(2)

print("Você ira jogar um número e iremos mostrar a sequência para você")

time.sleep(2)

fn = int(input("Digite o número inteiro para saber a sequência: "))


contador = 0
proximotermo = 0 #proximotermo da sequencia
f2 = 1 #termoatual
f1 = 0 #termoanterior

while contador != fn:
    contador += 1
    if proximotermo == 0:
        print("0")
    proximotermo = (f1) + (f2)
    f1=f2
    f2=proximotermo
    print(f1)
