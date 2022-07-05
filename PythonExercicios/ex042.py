#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digire o comprimento da terceira reta: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:

    if r1 == r2 and r1 == r3: #r1 == r2 == r3:
        print('Com das medidas \033[34m{}\033[m, \033[34m{}\033[m e \033[34m{}\033[m, temos o \033[31mTriângulo EQUILÁTERO.'.format(r1, r2, r3))

    elif r1 != r2 and r1 != r3 and r2 != r3:    #r1 != r2 != r3 != r1:
        print('Com das medidas \033[34m{}\033[m, \033[34m{}\033[m e \033[34m{}\033[m, temos o \033[33mTriângulo ESCALENO.'.format(r1, r2, r3))

    else:
        print('Com das medidas \033[34m{}\033[m, \033[34m{}\033[m e \033[34m{}\033[m, temos o \033[32mTriângulo ISÓSCELES.'.format(r1, r2, r3))

else:
    print('\033[31mCom as medidas {}, {} e {} você não consegue formar um triângulo.'.format(r1, r2, r3))

