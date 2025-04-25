# 2. Alguns países medem temperaturas em graus Celsius, e outros em graus Fahrenheit. 
# Faça um algoritmo para ler uma temperatura Celsius e imprimi-Ia em Fahrenheit 
# (pesquise como fazer este tipo de conversão).
#(°C × 1.8) + 32 = °F

celsius = float(input("Insira a temperatura em gruas Celsius: ")) # Insere o valor na variável
print(f"A temperatura em Fahrenheit é {(celsius * 1.8) + 32}") # Imprime o resultado final