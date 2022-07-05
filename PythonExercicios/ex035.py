#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digire o comprimento da terceira reta: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('Com as medidas {}, {} e {} você consegue formar um triângulo.'.format(r1, r2, r3))
else:
    print('Com das medidas {}, {} e {} você não consegue formar um triângulo.'.format(r1, r2, r3))
