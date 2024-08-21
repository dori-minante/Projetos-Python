# Crie um algoritmo que receba um valor do tipo inteiro via teclado
# No entando, o programa só deve aceitar, obrigatóriamente, VALORES INTEIROS E POSITIVOS
# Qualquer valor negativo, ou igual a zero, deve ser rejeitado pelo programa e um novo valor deve ser solicitado

# validadando a entrada
x = int(input('Digite um valor maior do que zero: '))
while (x <= 0):
    x = int(input('Digite um valor maior do que zero: '))
print(f'Você digitou {x}. Encerrando o programa...')