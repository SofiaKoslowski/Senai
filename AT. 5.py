# 5. Como calcular a quantidade de novelos de lã necessários para produzir cada blusa em uma confecção, 
# considerando que cada blusa requer uma quantidade de 120 metros de fio e que cada novelo contém 125 de metros de fio?

qnt_blusa = int(input("Insira a quantidade de blusas a fazer: ")) # Insere o valor na variável

fio_blusa = qnt_blusa*120 # Faz o calculo da quantidade de fios necessários para a produção da blusa.
novelo = fio_blusa/125 # Faz o calculo da quantidade de novelos necessários para a produção da blusa.

print(f"A quantidade necessárias de novelos é: {novelo}") # Exibe a resposta ao usuário.