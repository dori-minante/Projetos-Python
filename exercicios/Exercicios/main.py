#Escreva as seguintes expressões em linguagem python:
#a) O somatório dos 5 primeiros números inteiros e positivos

print(1 + 2 + 3 + 4 + 5)

#b) A média entre 23,19 e 31

print((23 + 19 + 31) / 3)

#c) O número de vezes que 73 cabe em 403
# / - divisão com casas decimais
# // - divisão somente com a parte inteira

print(403 // 73)

#d) A sobra quando 403 é dividido por 73
# % - módulo/resto da divisão
print(403 % 73)

#e) 2 elevado à 10ª potência

print(2 ** 10)

#f) O valor absoluto da diferença entre 54 e 57
# abs - valor absoluto

print(abs(54 - 57))

#g) O menor valor entre 34, 29 e 31
#min - menor valor do que estiver em parênteses

print(min(34, 29, 31))

# Exercicios de atribuição
# a) Atribuir o valor inteiro 3 a variável a
# b) Atribuir o valor 4 a variável b
# c) Atribuir a variavel c o valor da expressão a*a + b*b

a = 3
b = 4
c = a * a + b * b

print(c)

# Strings
# Execute as seguintes atribuições:
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
# Agora, utilizando operadores + e*, crie saídas a seguir:
# a) 'ant bat cod'
# b) 'ant ant ant ant ant ant ant ant ant ant'
# c) 'ant bat bat cod cod cod'
# d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
# e) 'batbatcod batbatcod batbatcod batbatcod'

# a)
res = s1 + ' ' + s2 + ' ' + s3
print(res)

# b)
res = 10 * (s1 + ' ')
print(res)

# c)
res = (s1 + ' ') + 2 * (s2 + ' ') + 3 * (s3 + ' ')
print(res)

# d)
res = 7 * (s1 + ' ' + s2 + ' ')
print(res)

# e)
res = 4 * (s1 + s2 + s3 + ' ')
print(res)