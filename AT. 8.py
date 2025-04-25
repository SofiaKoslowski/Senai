# 8. Num dia de sol, você deseja medir a altura de um prédio, porém, a trena não é suficientemente longa. 
# Assumindo que seja possível medir sua sombra e a do prédio no chão, e que você lembre da sua altura, 
# faça um algoritmo para ler os dados necessários e calcular a altura do prédio.

altura_pessoa = float(input("Qual é a sua altura? "))
sombra_pessoa = float(input("Qual é o tamanho da sua sombra? ")) # Insere o valor nas variáaveis
sombra_predio = float(input("Qual é o tamanho da sombra do prédio? "))

altura_predio = (altura_pessoa * sombra_predio) / sombra_pessoa # Calcula a altura do prédio

print("A altura do prédio é:", altura_predio, "metros") # Exibe o resultado