# 24. João recebeu seu salário de R$ 1200,00 e precisa pagar duas contas (C1=R$ 200,00 e C2=R$120,00) que estão atrasadas. 
# Como as contas estão atrasadas, João terá de pagar multa de 2% sobre cada conta. 
# Faça um algoritmo que calcule e mostre quanto restará do salário do João

C1 = 200.00 
C2 = 120.00

multa1 = C1 + (C1 * (100/2))
multa2 = C2 + (C2 * (100/2))

print ("O valor final da conta 1 é: ", multa1)
print ("O valor final da conta 2 é: ", multa2)