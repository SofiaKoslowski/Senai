# 25. Faça um algoritmo que receba o valor dos catetos de um triângulo, calcule e mostre o valor da hipotenusa

cateto1 = float(input("Digite o primeiro cateto: "))
cateto2 = float(input("Digite o segundo cateto: "))

hipotenusa = (cateto1**2 + cateto2**2)**0.5

print("A hipotenusa é:", hipotenusa)