# 22.    Faça um algoritmo que calcule e mostre a tabuada de um número digitado pelo usuário.

num = int(input("Inira um número: "))

for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")