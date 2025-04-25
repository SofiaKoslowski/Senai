# 12. Faça um algoritmo que receba dois números, calcule e mostre a divisão do primeiro número pelo segundo. 
# Sabe-se que o segundo número não pode ser zero, portanto não é necessário se preocupar com validações.

primeiro_num = int(input("Insira o primeiro número: "))# Insere o valor ns variáveis
segundo_num = int(input("Insira o segundo número: "))

if segundo_num == 0:
    print("Número inválido, insira outro número.") # Não deixa o número ser zero

else:
    multiplicacao = primeiro_num * segundo_num # Faz a conta
    print(f"A multiplicação dos números são: {multiplicacao}") # Exibe o resultado da conta