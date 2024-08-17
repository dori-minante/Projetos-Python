# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências,
# I para indústrias e C para comércios

# Calcule de acordo com a tabela a seguir:

#  - Residencial: faixa (kWh) até 500 o preço é R$ 0,40
                            # acima de 500 o preço é R$ 0,65

#  - Comercial: faixa (kWh) até 1000 o preço é R$ 0,55
                            # acima de 1000 o preço é R$ 0,60

#  - Industrial: faixa (kWh) até 5000 o preço é R$ 0,55
                            # acima de 5000 o preço é R$ 0,60

kwh = float(input('Quantos kWh? '))
tipo = input('Qual o tipo da instalação? (R, C ou I) ')

if (tipo == 'R'):
    if kwh >= 500:
        preco = 0.65
    else:
        preco = 0.4
    print(f'Total a pagar: R$ {kwh * preco}')
elif (tipo == 'C'):
    if kwh >= 1000:
        preco = 0.6
    else:
        preco = 0.55
    print(f'Total a pagar: R$ {kwh * preco}')

elif (tipo == 'I'):
    if kwh >= 5000:
        preco = 0.6
    else:
        preco = 0.55
    print(f'Total a pagar: R$ {kwh * preco}')
else:
    print('Instalação inválida. Encerrando...')
