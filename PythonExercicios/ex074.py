#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e
# colocar em uma tupla. Depois disso, mostre a listagem de números gerados e
# também indique o menor e o maior valor que estão na tupla.

from random import randint

n = randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)
print(f'Foram sorteados os números: \033[1:35m{n}\033[m')

#maior = -1
#menor = 11
#for cont in range(0, len(n)):
#    if n[cont] > maior:
#        maior = n[cont]
#    if n[cont] < menor:
#        menor = n[cont]

print(f'O menor número sorteado foi \033[1:34m{min(n)}\033[m')
print(f'O maior número sorteado foi \033[1:31m{max(n)}\033[m')


