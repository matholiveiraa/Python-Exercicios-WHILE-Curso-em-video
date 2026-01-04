#Esse agora é ir ver quantos números digitados foram pares e impares:

b = 1
pares = 0
impares = 0
while b != 0:
    b = int(input("Digite um valor: "))
    if b != 0:
        if b % 2 == 0:
            pares+=1
        else:
            impares+=1
print("Acabou")
print(f"Quantidade pares {pares}")
print(f"Quantidade impares {impares}")