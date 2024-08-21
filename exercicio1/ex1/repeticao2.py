# Escreva um algoritmo que calcule a sua média de notas em determinada disciplina
# Vamos assumir que a média final é dada pela média aritmética de cinco notas digitadas

soma = 0
cont = 1
# variável de contagem que vai até 5

while (cont <= 5):
    x = float(input(f'Digite a {cont}ª nota: '))
    soma = soma + x
    cont = cont + 1
media = soma / 5
print(f'Média final: {media}')