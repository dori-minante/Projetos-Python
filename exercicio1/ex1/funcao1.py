# def realce():
#     #corpo da função
#     print('|','__' * 10,'|')
#     print('|','__' * 10, '|')
#
# # programa principal
# realce()
# print('        MENU')
# realce()

def sub2(x, y):
    res = x -y
    print(res)

#programa principal
sub2(5, 7)

sub2(7,5)

# Escreva uma rotina qye crie uma borda ao redor de uma palavra, para destacá-la como sendo um título.
# A rotina deve receber como parâmetro a palavra a ser destacada.
# O tamanho da caixa de texto deverá ser adaptável, de acordo com o tamanho da palavra.

def borda(s1):
    tam = len(s1)
    # só imprime caso exista algum caractere
    if tam:
        print('+','-' * tam,'+')
        print('|',s1,'|')
        print('+', '-' * tam, '+')

# Programa principal
borda('Olá, Mundo!')
borda('Lógica de Programação e Algoritmos')