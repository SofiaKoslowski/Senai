# 1.A lanchonete Gostosura vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de queijo, uma fatia de presunto e uma rodela de hambúrguer. 
# Sabendo que cada fatia de queijo ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, 
# faça um algoritmo em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades (em quilos) de queijo,
# presunto e carne necessários para compra.

sanduiche = int(input("Insira a quantidade de sanduíches a fazer: ")) # Insere o valor na variável

queijo = 100
presunto = 50 # Insere o valor as variáveis
hamburger = 100

queijo_kg = queijo*sanduiche
presunto_kg = presunto*sanduiche # Calcula a qauntidade de produtos de acordo com o número inserido pelo usuario
hamburger_kg = hamburger*sanduiche

queijo_total = queijo_kg / 1000
presunto_total = presunto_kg / 1000 # Faz a conversão de gramas para kg
hamburger_total = hamburger_kg / 1000

print(f"É necessário comprar: {queijo_total} quilos de queijo, {presunto_total} quilos de presunto e {hamburger_total} quilos de hambúrger.")
# Exibe o resultato final