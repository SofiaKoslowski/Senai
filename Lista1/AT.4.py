# 4. A granja Frangotech possui um controle automatizado de cada frango da sua produção. 
# No pé direito do frango há um anel com um chip de identificação; 
# no pé esquerdo são dois anéis para indicar o tipo de alimento que ele deve consumir. 
# Sabendo que o anel com chip custa R$4,00 e o anel de alimento custa R$3,50, 
# faça um algoritmo para calcular o gasto total da granja para marcar todos os seus frangos.

qnt_frango = int(input("Insira a quantidade de frangos: ")) # Insere o valor na variável

valor_aneis = (qnt_frango*4.00) + (qnt_frango*(3.50*2)) # Calcula o valor dos aneis

print(f"O valor para marcar todos os frangos vai ser: {valor_aneis}") # Exibe o resultado