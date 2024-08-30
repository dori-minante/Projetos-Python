# Crie um programa para ler o nome, ano de nascimento e sexo de diferentes pessoas
# Armazene os dados em um dicionário com listas
# Ao encerrar o cadastro, apresente:
# o total de cadastros efetuados
#a média das idades das pessoas
# uma lista de mulheres com menos de 30 anos
# uma lista com homens com idade acima da média

cadastro = {'nome':[], 'sexo':[], 'ano':[]}

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N] ')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NÃO.')
        continue

    nome = input('Qual o nome? ')
    sexo = input('Qual o sexo? ')
    ano = input('Qual o ano de nascimento? ')
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print(cadastro)