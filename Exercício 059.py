#Crie um programa que leia dois valores e mostre na tela um menu
#(1) somar
#(2) multiplicar
#(3) maior
#(4) novos numeros
#(5) sair do programa

import time

n1 = ""
n2 = ""

escolha = ""

print("Iremos fazer uma calculadora básica para você!")

time.sleep(3)

print("Você poderá escolhar de até 1 a 5 de escolhas sendo elas:")
print(" (1) = somar")
print(" (2) = multiplicar")
print(" (3) = maior")
print(" (4) = novos numeros")
print(" (5) = sair do programa")

time.sleep(5)


while escolha != 5:
    escolha = int(input("\nDigite qual a sua operação que deseja: ")) 
    n1 = int(input("\nDigite o primeiro valor: "))
    n2 = int(input("\nDigite o segundo valor: "))

    if escolha == 1:
        print(f"\nA soma dos dois é: {n1+n2} ")

    elif escolha == 2:
            print(f"\nA multiplicação dos dois é: {n1*n2} ")

    elif escolha == 3:
        if n1 > n2:
                print(f'\n{n1}, é maior')
        else:
                n2>n1
                print(f'\n{n2}, é maior')
                
    elif escolha == 4:
            n1 = int(input("\nDigite o novo valor do primeiro elemento: "))
            n2 = int(input("\nDigite o novo valor do segundo elemento: "))
            
    else:
            escolha == 5
            print("\nFinalizou!")
            break
            