# 13. Faça um algoritmo que receba duas notas, calcule e mostre a média ponderada dessas notas, 
# considerando peso 2 para a primeira nota e peso 3 para a segunda nota.

nota1 = float(input("Digite a primeira nota:")) # Insere o valor nas variáveis
nota2 = float(input("Digite a segunda nota:"))

media = (nota2 * 2 + nota1 * 3) / (2 + 3) # Faz a conta

print("A média ponderada é:" , media) # Exibe o resultado final.
