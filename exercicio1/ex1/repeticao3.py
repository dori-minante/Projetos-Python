# Escreva um algoritmo que calcule a soma de notas em determinada disciplina

soma = 0
cont = 1

while (cont <= 5):
    x = int(input(f'Digite o {cont}º número: '))
    soma += x # Equivalente: soma = soma + x
    cont += 1  # Equivalente: cont = cont + x
print(f'Somatório: {soma}')