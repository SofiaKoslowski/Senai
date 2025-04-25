# 7. Pedrinho tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar. 
# Faça um algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor total economizado, em reais. 
# Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real. Não havendo moeda de um tipo, 
# a quantidade respectiva é zero.

qnt_moeda_um = int(input("Insira a quantidade de moedas de 1 centavo: "))
qnt_moeda_cinco = int(input("Insira a quantidade de moedas de 5 centavos: "))
qnt_moeda_dez = int(input("Insira a quantidade de moedas de 10 centavos: "))   # Insere o valor nas variáveis.
qnt_moeda_vinte = int(input("Insira a quantidade de moedas de 25 centavos: "))
qnt_moeda_cinquenta = int(input("Insira a quantidade de moedas de 50 centavos: "))
qnt_moeda_um_real = int(input("Insira a quantidade de moedas de 1 real: "))

moeda_um = qnt_moeda_um / 100
moeda_cinco = qnt_moeda_cinco / 20
moeda_dez = qnt_moeda_dez / 10   # Converte os centavos para reais de acordo com a quantidade de moedas de cada valor.
moeda_vinte = qnt_moeda_vinte / 4
moeda_cinquenta = qnt_moeda_cinquenta / 2

valor_real = moeda_um + moeda_cinco + moeda_dez + moeda_vinte + moeda_cinquenta + qnt_moeda_um_real # Calcula o valor dos reais. 

print(50 * "-") # Deixa o codigo mais arrumado
print(f"O valor em reais ficou: R$ {valor_real}") # Exibe o valor final