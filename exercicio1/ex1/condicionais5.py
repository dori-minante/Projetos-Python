# Escreva um algoritmo em Python em que o usuário escolhe se ele quer comprar maçãs, laranjas ou bananas. Deverá ser
# apresentado na tela um menu com a opção 1 para maçã, 2 para laranja e 3 para banana.
# Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar.
# O algoritmo deve calcular o preço total a pagar do produto escolhido e mostrá-lo na tela.
# Considere que uma maçã custa R$ 2,30, uma laranja R$ 3,60 e uma banana 1,85

# Fazendo o exercicio agora com Elif

print('Escolha o que deseja comprar:')
print('1 - Maça')
print('2 - Laranja')
print('3 - Banana')

produto = int(input('Qual sua escolha? '))
qtd = int(input('Quantas unidades? '))

if (produto == 1):
    pagar = qtd * 2.3
    print(f'Você comprou {qtd} maças. Total à pagar: R$ {pagar}')
elif (produto == 2):
    pagar = qtd * 3.6
    print(f'Você comprou {qtd} laranjas. Total à pagar: R$ {pagar}')
elif (produto == 3):
    pagar = qtd * 1.85
    print(f'Você comprou {qtd} bananas. Total à pagar: R$ {pagar}')
else:
   print('Produto inexistente!')
