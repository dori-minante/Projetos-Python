# Escopo de variáveis
# Um escopo é a propriedade que determina onde uma variável pode ser utilizada dentro de um programa

#Escopo local
# Criado sempre que uma função é chamada
# Variáveis criadas, seja no campo de um parâmetro ou dentro do corpo da função,
# fazem parte do escopo local daquela função e são chamadas de variáveis locais.
# Essas variáveis só existem dentro daquela própria função

#Escopo global
# Variáveis globais pertencem a um escopo global e são variáveis criadas dentro do programa principal.
# Uma variável global existem também em todas as funções invocadas ao longo do programa

# Escreva uma função para validar uma string. Essa função recebe como parâmetro a string, o número mínimo e máximo de caracteres.
# Retorne verdadeiro se o tamanho da string estiver entre os valores de mínimo e máximo,
# e falso, caso contrário

def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while ((tam < min) or (tam > max)):
        s1 = input(pergunta)
        tam = len(s1)
    return s1

#programa principal
x = valida_string('Digite uma string: ', 10, 30)
print('Você digitou a string: {}. \n Dado válido. Encerrando o programa...'.format(x))