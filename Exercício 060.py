#Faça um programa que leia um número
#E mostre seu fatorial
#Exemplo de fatorial (5!=5*4*3*2*1) = 120
#Ele quer o numero não resultado

from math import factorial

diminuir = 0

n = int(input("Digite o fatorial que deseja: "))
fatorial=factorial(n)
multiplicacao = 1 #todo de multiplicação deve ser 1 nunca 0! 0 é apenas adição e subtração

diminuir = n

while diminuir > 0 :
    print(diminuir,end='')
    multiplicacao *= diminuir
    diminuir += -1
    print("x" if diminuir >= 1 else "=" , end="" )
print(multiplicacao)

    

