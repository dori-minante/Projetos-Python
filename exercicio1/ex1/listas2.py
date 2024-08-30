# O primeiro índice é referente a cada item da lista
# O segundo índice é referente a cada caractere da string
# Assim, podemos acessar não só a cada dado dentro da lista, mas também cada caractere das strings de um índice da lista

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
for item in mochila:
    for letra in item:
        print(letra, end='')
    print()

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
for i in range(0,len(mochila),1):
    for j in range(0,len(mochila[i]),1):
        print(mochila[i][j], end='')
    print()

# Imagine uma situação na qual você deve realizar o cadastro de uma lista de compras em um sistema. Cada produto comprado,
# deverá ser registrado com seu nome, quantidade e valor unitário

# item = [] #lista vazia
# mercado = []
# for i in range(3): #um laço que cadastra até 3 itens
#      item.append(input('Digite o nome do item:'))
#      item.append(int(input('Digite a quantidade:')))
#      item.append(float(input('Digite o valor:')))
#      mercado.append(item[:]) #cópia
#      item.clear() #limpar a lista para cadastrar o próximo
# print(mercado)

#outra resolução
mercado = []
for i in range(3):
     nome = input('Digite o nome do item:')
     qtd = int(input('Digite a quantidade:'))
     valor = float(input('Digite o valor:'))
     mercado.append([nome, qtd, valor])
print(mercado)

soma = 0
print('Lista de compras:')
print('-' * 20)
print('item | quantidade | valor unitário | total do item')
for item in mercado:
     print('{} | {} | {} | {}'.format(item[0], item[1], item[2], item[1] * item[2]))
     soma += item[1] * item[2]
print('-' * 20)
print(f'Total a ser pago: {soma}')
