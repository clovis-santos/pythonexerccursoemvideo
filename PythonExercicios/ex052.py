#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1:33m', end=' ')
        tot = tot + 1
    else:
        print('\033[1:31m', end=' ')
    print('{}'.format(c), end=' ')

print('\n\n\033[mO número {} foi dividido {} vezes.'.format(n, tot))

if tot == 2:
    print('\n\033[1:34mO número\033[m \033[1:33m{}\033[m \033[1:34mé Primo!!!\033[m'.format(n))
else:
    print('\n\033[1:31mO número\033[m \033[1:33m{}\033[m \033[1:31mNão é Um Número Primo!!!\033[m'.format(n))
