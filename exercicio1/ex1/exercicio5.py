# Uma empresa concedeu um bônus de 20% para todos seus funcionários com mais de cinco anos de empresa. Todos
# os outros que não se enquadram nesta categoria receberam uma bonificação de 10%, somente. Escreva um algoritmo que leia o salário do funcionário e seu
# tempo de empresa, e apresente a bonificação de cada funcionário na tela.

salario = float(input('Qual seu salário?'))
ano_admissao = int(input('Qual seu ano de admissão na empresa?'))
ano_atual = int(input('Em que ano estamos?'))
tempo = ano_atual - ano_admissao
if (tempo > 5):
 bonus = salario * 0.2
else:
 bonus = salario * 0.1
print(f'Você tem {tempo} anos dentro desta empresa.')
print(f'Seu Salário é de {salario}.')
print(f'E sua bonificação é de {bonus}.')
print(f'Salário final {bonus + salario}.')