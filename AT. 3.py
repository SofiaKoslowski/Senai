#3. A empresa Hipotheticus paga R$10,00 por hora normal trabalhada, e R$15,00 por hora extra. 
# Faça um algoritmo para calcular e imprimir o salário bruto e o salário líquido de um determinado funcionário. 
# Considere que o salário líquido é igual ao salário bruto descontando-se 10% de impostos.

hora_normal = float(input("Insira a quantidade de horas normais trabalhadas: ")) # Insere o valor nas variáveis.
hora_extra = float(input("Insira a quantidade de horas extras trabalhadas: "))

hora_normal = hora_normal*10.00 # Faz o calculo de quanto foi ganho por hora.
hora_extra = hora_extra*15.00

salario_bruto = hora_normal + hora_extra # Faz o calculo dos salarios
salario_liquido = salario_bruto*0.10

print (f"O salário bruto ficou no valor de R$ {salario_bruto}, e o líquido ficou no valor de R$ {salario_liquido}.")
# Imprime o resultado final