import random

# Crie um jogo de pedra, papel ou tesoura
# Vc deverá jogar contra o computador
# Vc irá sempre escolher uma das opções: 1 - pedra, 2 - papel, 3 - tesoura

# o computador irá sempre sortear um número de 1 até 3
# armazene todos os resultados em uma lista e no final apresente o vencedor
# encerre o programa ao digitar 0

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def vencedor (jogador1, jogador2):
    global v1, v2, empate
    if jogador1 == 1: #Pedra
        if jogador2 == 1: #Pedra
            empate += 1
        elif jogador2 == 2: #Papel
            v2 += 1
        elif jogador2 == 3: #Tesoura
            v1 += 1
    elif jogador1 == 2: #Papel
        if jogador2 == 1: #Pedra
            v1 += 1
        elif jogador2 == 2: #Papel
            empate += 1
        elif jogador2 == 3: #Tesoura
            v2 += 1
    elif jogador1 == 3:  # Tesoura
        if jogador2 == 1: #Pedra
            v2 += 1
        elif jogador2 == 2: #Papel
            v1 += 1
        elif jogador2 == 3: #Tesoura
            empate += 1

    resultados = [v1, v2, empate]
    return resultados

#programa principal
print('JOKENPO')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

jogadas = []
resultados = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valida_int('Escolha sua jogada: ', 0, 3)
    if not j1:
        break
    j2 = random.randint(1,3) # ramdom vai gerar um número aleatório
    jogadas.append([j1, j2])
    resultados = vencedor(j1 , j2)

for jogada in jogadas:
    for dado in jogada:
        print(dado, end= ' ')
    print()

print(f'Número de vitórias do Jogador 1: {resultados[0]}') #jogador1 é indice 0
print(f'Número de vitórias do Jogador 2: {resultados[1]}') #jogador2 é indice 1
print(f'Número de empates: {resultados[2]}') #empate é indice 2
