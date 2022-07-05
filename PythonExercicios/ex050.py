#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre
# a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for c in range(0, 6, 1):
    n = int(input('Digite um número: '))
    if (n % 2) == 0:
        soma = soma + n

print('\033[1:33m*\033[m'*40)

print('\033[1:34mA soma dos núemeros Pares digitados é\033[m \033[1:31m{}\033[m'.format(soma))

