# Operador not: serve para negar um resultado lógico ou o resultado de uma expressão booleana
# Na prática significa que o resultado final de uma expressão será invertido.

# Operador and: este operador irá prover um resultado verdadeiro se, e somente se, ambas as entradas forem verdadeiras

# Operador or: este operador irá prover um resultado verdadeiro se ao menos uma das entradas for verdadeira.

# Ordem dos operadores:
# 1. parênteses;
# 2. Operadores aritméticos de potenciação ou raiz;
# 3. Operadores aritméticos de multiplicação, divisão e módulo;
# 4. Operadores aritméticos de adição e subtração;
# 5. Operadores relacionais;
# 6. Operadores lógicos not;
# 7. Operadores lógicos and;
# 8. Operadores lógicos or;
# 9. Atribuições

# Exercício:
# Um aluno, para passar de ano, precisa ser aprovado em todas as matérias que está cursando
# Assuma que a média para aprovação é a partir de 7 e que o aluno cursa 3 matérias somente.
# Escreva um algoritmo que leia a nota final do aluno em cada matéria e informe na tela se ele passou de ano ou não

m1 = float(input('Digite a nota da 1ª matéria: '))
m2 = float(input('Digite a nota da 2ª matéria: '))
m3 = float(input('Digite a nota da 3ª matéria: '))
if m1 >= 7 and m2 >= 7 and m3 >= 7:
    print('O aluno está aprovado de ano!');
else:
    print('O aluno não passou de ano!');