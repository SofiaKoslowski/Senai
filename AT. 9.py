# 9. Um tonel de refresco é feito com 8 partes de água mineral e 2 partes de suco de maracujá. 
# Faça um algoritmo para calcular quantos litros de água e de suco são necessários para se fazer X litros de refresco 
# (informados pelo usuário).

qnt_tonel = float(input("Insira a quantidade do refresco em litros: ")) # Insere o valor nas variáveis.

litros_agua = ( 8 / 10 ) * qnt_tonel  # Calcula a quantidade de água e seco.
litros_suco = ( 2 / 10 ) * qnt_tonel

print(f"Serão necessários {litros_agua} litros de água e {litros_suco} litros de suco.") # Exibe o resultado final.