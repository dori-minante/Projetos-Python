# Listas:
#estruturas de dados dinâmica, podemos alterar dados e tamanho
# indexada por valores numéricos inteiros
# representadas por []

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print('Tupla: ', mochila)
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print('Lista: ', mochila)

mochila[2] = 'Laranja'
print('Lista: ', mochila)

mochila.append('Ovos') #adiciona no final da lista
print('Lista: ', mochila)

mochila.insert(1,'Canivete') #insere no índice informado
print('Lista: ', mochila)

del mochila[1] #deleta do índice informado
print('Lista: ', mochila)

mochila.remove('Ovos') #deleta o dado informado
print('Lista: ', mochila)

#mesma referência
lista_original = [5, 7, 9, 11]
lista_referenciada = lista_original
print(lista_original)
print(lista_referenciada)

lista_referenciada[0] = 2
print(lista_original)
print(lista_referenciada)

#cópia
lista_original = [5, 7, 9, 11]
lista_referenciada = lista_original[:] #cria uma cópia da original
print(lista_original)
print(lista_referenciada)

lista_referenciada[0] = 2
print(lista_original)
print(lista_referenciada)

# o que são métodos?
# uma lista é um objeto de uma classe dentro do python
# paradigmas de programação orientada a objetos (POO)
# método é equivalente a função
    #mochila.append('Ovos')
    #variável.função(parâmetro)