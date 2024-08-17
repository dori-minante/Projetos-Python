# Escreva um algoritmo que leia um nome e uma idade
# Caso o nome digitado seja Vinicius, escreva isso na tela
# Caso o usuário digite qualquer outro nome, verifique sua idade. Se for menor que 18 anos, informe que é de menor.
# Se for maior que 120 anos, informe que essa pessoa possivelmente não existe.

nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

if nome == 'Vinicius':
    print('Olá, Vinicius!')
elif idade < 18:
    print('Você não é o Vinicius! E é menor de idade!')
elif idade > 120:
    print('Você provavelmente não existe!')