# 15. Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um algoritmo que receba o 
# salário fixo de um funcionário e o valor de suas vendas, calcule e mostre a comissão e o salário final do funcionário.

salario_fixo = float(input("Insira seu salário: "))
vendas = int(input("Insira quantas vendas foram feitas: "))

comissao = vendas * (100/4)

salario_final = salario_fixo + comissao
print ("O salário final é: ",salario_final)