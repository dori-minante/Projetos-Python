# Dicionários:
# Estrutura de dados dinâmica, podemos alterar dados e tamanho
# Indexados por chaves (palavras-chave)
# Representados em Python por {}

mochila = ('Laptop', 'Smartphone', 'Power Bank', 'Carregadores e Cabos')
print('Tupla: ', mochila)
mochila = ['Laptop', 'Smartphone', 'Power Bank', 'Carregadores e Cabos']
print('Lista: ', mochila)
mochila = {'Laptop':1, 'Smartphone':2, 'Power Bank':3, 'Carregadores e Cabos':4}
print('Dicionário: ', mochila)

game = {'nome':'Super Mario',
     'desenvolvedora':'Nintendo',
     'ano':1990}
print(game)

print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])

# Métodos para dicionários:
# values: obtém somente os dados
# keys: obtém somente as chaves
# items: obtém o par chave:dado

print(game.values())

for values in game.values():
    print(values)

print(game.keys())

for keys in game.keys():
    print(keys)

print(game.items())

for keys, values in game.items():
    print(f'{keys} = {values}')

# Listas com dicionários: uma lista contendo, em cada índice, um dicionário

games = []
game1 = {'nome':'Super Mario',
     'videogame':'Super Nintendo',
     'ano':1990}
game2 = {'nome':'Zelda Ocarina of Time',
     'videogame':'Nintendo 64',
     'ano':1998}
game3 = {'nome':'Pokemon Yellow',
     'videogame':'Game Boy',
     'ano':1999}
games = [game1, game2, game3]
print(games)

#outra maneira de fazer:

games = []
for i in range(3):
     game['nome'] = input('Qual o nome do jogo?')
     game['videogame'] = input('Para qual videogame ele foi lançado? ')
     game['ano'] = input('Qual o ano de lançamento?')
     games.append(game.copy())
print('-' * 20)
for jogos in games:
     for chave, valor in jogos.items():
        print(f'O campo {chave} tem o valor {valor}.')

# Dicionários com listas

games = {'nome':['Super Mario', 'Zelda Ocarina of Time','Pokemon Yellow'],
     'videogame':['Super Nintendo','Nintendo 64','Game Boy'],
     'ano':[1990,19998,1999]}
print(games)

# inserção dos dados no dicionário com listas via teclado

games = {'nome':[],'videogame':[],'ano':[]} #palavra chave e lista vazia
for i in range(3): #cadastra 3 dados
     nome = input('Qual o nome do jogo?')
     videogame = input('Para qual video-game ele foi lançado?')
     ano = input('Qual o ano de lançamento?')
     games['nome'].append(nome)
     games['videogame'].append(videogame)
     games['ano'].append(ano)
print('-' * 20)
print(games)