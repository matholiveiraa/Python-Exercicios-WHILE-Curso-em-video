#Faça um programa que leia o sexo de uma pessoa
#Mas só aceita os valores "M" ou "F"
#Caso for errado peça a digitação novamente até ter um valor correto!



sexo = str(input("Digite seu Sexo corretamente: ")).upper()

while sexo != ("M") and sexo!= ("F"): #MUITA ATENÇÂOOOO
    sexo = str(input("Digite seu Sexo corretamente: ")).upper()
print("Acabou")