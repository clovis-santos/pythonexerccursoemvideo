#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

'''n = int(input('Digite um número para cálculo do fatorial: '))
fat = 1
i = 2
while i <= n:
    fat = fat * i
    i = i + 1

print('O fatorial do número {} é {}.'.format(n, fat)) '''

'''from math import factorial
n = int(input('Digite um número: '))
fat = factorial(n)
print('O fatorial de {} é {}'.format(n, fat))'''


'''n = int(input('Digite um número: '))
cont = n
fat = 1
print('Calculando o \033[1:31m{}!\033[m \033[1:33m=>\033[m'.format(n), end=' ')
while cont > 0:
    print('{}'.format(cont), end=' ')
    print('x' if cont > 1 else '=', end=' ')
    fat *= cont
    cont -= 1
print('\033[1:34m{}'.format(fat))'''

n = int(input('Digite um número: '))
fat = 1
print('Calculando o \033[1:31m{}!\033[m \033[1:33m=>\033[m'.format(n), end=' ')
for cont in range(n, 0, -1):
    print('{}'.format(cont), end=' ')
    print('x' if cont > 1 else '=', end=' ')
    fat *= cont
print('\033[1:34m{}'.format(fat))





