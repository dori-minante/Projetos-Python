# Escreva um algoritmo em python que calcule a tabuada de todos os números de 1 até 10, e, para cada número, vamos calcylar
#a tabuada multiplicando-o pelo intervalo de 1 até 10

#solução com 2x while

tabuada = 1
while tabuada <= 10:
    print(f'TABUADA DO {tabuada}: ')
    i = 1
    while i <=10:
        print(f'{tabuada} x {i} = {tabuada * i}')
        i += 1
    tabuada += 1

# solução com 2x for

for tabuada in range(1,11,1):
    print(f'TABUADA DO {tabuada}:')
    for i in range(1,11,1):
        print(f'{tabuada} x {i} = {tabuada * i}')

# solução com while + for

tabuada = 1
while tabuada <= 10:
    print(f'TABUADA DO {tabuada}:')
    for i in range(1, 11, 1):
        print(f'{tabuada} x {i} = {tabuada * i}')
    tabuada += 1