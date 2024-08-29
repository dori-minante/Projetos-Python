# variáveis:
# simples: armazenam somente um dado
# compostas? armazenam um conjunto de dados

# Estrutura de dados:
# É um conjunto de dados organizados de uma maneira específica na memória do programa
# A maneira como os dados estão organizados na memória, como podem ser buscados, manipulados e acessados
# é o que define e diferencia as estruturas de dados

# TUPLA:
# Estrutura de dados estática, imutável e representada por ()

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila)

print(mochila[0]) #print do Elemento 1 - Índice 0
print(mochila[2]) #print do Elemento 3 - Índice 2
print(mochila[0:2]) #print dos Elementos 1 e 2 - Índice 0 e 1
print(mochila[2:]) # print dos elementos a partir do índice 2
print(mochila[-1]) #print do último

for item in mochila:
 print('Na minha mochila tem: {}'.format(item))


# Suponha que vc quer realizar o somatório de diversos valores, porém não sabe quantos valores serão somados.
# Pode ser que sejam somente 2, ou 10, ou mesmo 100 números
# Como criar uma função capaz de receber um número tão variável de parâmetros?

def soma(*num): # o * significa que a variável será uma tupla de tamanho qualquer, depende de quantos dados eu passsar como parâmetro
    acumulador = 0
    print(f'Tupla: {num}')
    for i in num:
        acumulador += i
    return acumulador

# programa principal
print(f'Resultado: {soma(1,2)}\n')
print(f'Resultado: {soma(1,2,3,4,5,6,7,8,9)}\n')