# Escreva um algoritmo que leia um valor e que imprima a quantidade de cédulas necessárias para pagar esse mesmo valor.
# Para simplificar, vamos trabalhar apenas com valores inteiros e com cédulas de R$ 100, R$ 50,00 R$ 20, R$ 10, R$ 5 e R$ 1

valor = int(input('Digite o valor em R$: '))

while True:
    if valor >= 100:
        cont100 = valor // 100 #pegar apenas a parte inteira da divisão
        valor = valor - cont100 * 100
        print(f'Cédulas de 100: {cont100}')

    if valor >= 50:
        cont50 = valor // 50 #pegar apenas a parte inteira da divisão
        valor = valor - cont50 * 50
        print(f'Cédulas de 50: {cont50}')

    if valor >= 20:
        cont20 = valor // 20 #pegar apenas a parte inteira da divisão
        valor = valor - cont20 * 20
        print(f'Cédulas de 20: {cont20}')

    if valor >= 10:
        cont10 = valor // 10 #pegar apenas a parte inteira da divisão
        valor = valor - cont100 * 10
        print(f'Cédulas de 10: {cont10}')

    if valor >= 5:
        cont5 = valor // 5 #pegar apenas a parte inteira da divisão
        valor = valor - cont5 * 5
        print(f'Cédulas de 5: {cont5}')

    if valor:
        cont1 = valor
        print(f'Cédulas de 1: {cont1}')