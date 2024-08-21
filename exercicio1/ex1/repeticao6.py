# Varredura de string

# caracter por caracter
# frase = "Lógica de Programação e Algoritmos"
# for i in range(0, len(frase), 1):
#     print(frase[i], end = "")

# Escreva um algoritmo que calcule a média dos números pares de 1 até 100 (1 e 100 inclusos). Implemente o laço usando for

soma = 0
qtd = 0
for i in range(1,101):
    if (i % 2 == 0):
        soma += i
        qtd += 1
media = soma / qtd
print(f'A média dos pares de 1 até 100 é: {media}')