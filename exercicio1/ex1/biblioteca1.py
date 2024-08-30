from math import sqrt

print(sqrt(9))

#import math

#print(math.sqrt(9))

# Dada uma lista contendo as notas de alunos em uma disciplina, escreva uma expressão para:
# notas = [9,7,7,10,3,9,6,6,2]

notas = [9,7,7,10,3,9,6,6,2]

# a) Encontrar quantos alunos tiraram nota 7
print(notas.count(7))

# b) Alterar a última nota para 4
notas[-1] = 4
print(notas)

# c) encontrar a maior nota
print(max(notas))

# d) ordenar a lista de notas
notas.sort()
print(notas)

# e) a média das notas
print(sum(notas) / len(notas))

