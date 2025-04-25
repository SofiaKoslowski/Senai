# 6. A fábrica de refrigerantes Meia-Cola vende seu produto em três formatos: lata de 350 ml, 
# garrafa de 600 ml e garrafa de 2 litros. Se um comerciante compra uma determinada quantidade de cada formato, 
# faça um algoritmo para calcular quantos litros de refrigerante ele comprou.

qnt_lata = int(input("Inira a quantidade de latas de 350ml compradas: "))
qnt_garrafa_ml = int(input("Inira a quantidade de garrafas de 600ml compradas: ")) # Insere o valor nas variáveis.
qnt_garrafa_litro = int(input("Inira a quantidade de garrafas de 2L compradas: "))

ml_lata = qnt_lata*350 # Faz o calculo de quantos litros por lata e por garrafa.
ml_garrafa = qnt_garrafa_ml*600

litro_lata = ml_lata / 1000 # Converte o "Ml" pra "L".
litro_garrafa = ml_garrafa / 1000

print(60 * "-")
total_litros = litro_lata + litro_garrafa + qnt_garrafa_litro # Calcula o tanto de litros comprados

print(f"A quantidade total foi de {total_litros} Litros.") # Exibe o resultado final

