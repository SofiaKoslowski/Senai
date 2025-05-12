# 16. Faça um algoritmo que receba o peso de uma pessoa, calcule e mostre:
# a)  o novo peso se a pessoa engordar 15% sobre o peso digitado;
# b)  o novo peso se a pessoa emagrecer 20% sobre o peso digitado;

peso = float(input("Insira seu peso: "))

engordar = peso + (peso * (100/15))

emagrecer = peso - (peso * (100/20))

print ("O peso se a pessoa engordar ficará de ", engordar)
print ("O peso se a pessoa emagrecer ficará de ", emagrecer)