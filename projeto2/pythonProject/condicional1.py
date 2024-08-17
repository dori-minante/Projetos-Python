# Se a idade é maior que 60, escreva: "Você tem direito aos beneficios!"

idade = 62

if (idade > 60):
    print('Você tem direito aos beneficios!')

# Se dano é maior que 10 e escudo é igual a 0, escreva: "Você está morto!"

dano = 13
escudo = 0

if (dano > 10 and escudo == 0):
    print('Você está morto!')

# Se pelo menos uma das variaveis booleanas norte, sul, leste e oeste resultarem em True,
# escreva: "Você escapou!"

norte = True
sul = False
leste = False
oeste = False

if (norte == True or sul == True or leste == True or oeste == True):
    print('Você escapou!')