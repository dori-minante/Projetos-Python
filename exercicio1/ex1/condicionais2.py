# O exemplo que vamos resolver agora descobre se um número inteiro digitado é par ou é ímpar.
# Para resolvermos este exercício, devemos pensar em que teste lógico deve ser feito para descobrirmos se um número é par ou ímpar.
# Se pegarmos qualquer valor numérico e inteiro e dividirmos por 2, que é
# par, e esta divisão resultar em resto zero, sabemos que o número digitado é
# divisível por 2 e, portanto, é par3. Caso o resto desta divisão não dê zero,
# significa que o número não é divisível por 2 e, portanto, é ímpar.
# Na linguagem Python, podemos obter o resto de uma divisão diretamente
# utilizando o símbolo de percentual. Deste modo, podemos escrever a expressão
# lógica 𝑥𝑥 % 2 == 0. Ou seja, obtemos o resto da divisão por 2 e, em seguida, pela
# comparação lógica de igualdade verificamos se é igual a zero.
# Para a verificação do múltiplo de 7, podemos novamente fazer o teste por meio do resto da divisão, pois um múltiplo de 7 deve, obrigatoriamente, ser divisível por 7 (resto
# zero).

# par ou ímpar e múltiplo de 7

x = int(input('Digite um valor inteiro: '))
if (x % 2 == 0):
 print('O número é par!')
else:
 print('O número é ímpar!')
if (x % 7 == 0):
 print('Múltiplo de 7!')
else:
 print('Não é múltiplo de 7!')