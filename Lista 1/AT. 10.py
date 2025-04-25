# 10. Calcule o volume de uma caixa d'água cilíndrica.

# V = π ⋅ r2 ⋅ h
# V é o volume do cilindro,
# r é o raio da base circular do cilindro,
# h é a altura do cilindro,
# π é uma constante aproximadamente igual a 3,14159.

R = float(input("Insira o tamanho da base do cilíndro: ")) # Insere o valor nas variáves.
h = float(input("Insira o tamanho da altura do cilíndro: "))

volume = 3.14 * (R ** 2) * h # Faz o calculo do volume.

print("O volume da caixa da água cilíndrica é: ", volume) # Exibe o resultado final.