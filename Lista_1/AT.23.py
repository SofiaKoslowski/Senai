# 23. Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
# a)  a idade dessa pessoa em anos;
# b)  a idade dessa pessoa em meses;
# c)  a idade dessa pessoa em dias;
# d)  a idade dessa pessoa em semanas.

ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade_anos = ano_nascimento - ano_atual
idade_messes = idade_anos * 12
idade_dias = idade_messes * 365
idade_semanas = idade_dias /7

print("A idade em anos é: ", idade_anos)
print("A idade em messes é: ", idade_messes)
print("A idade em dias é: ", idade_dias)
print("A idade em semanas é: ", idade_semanas)