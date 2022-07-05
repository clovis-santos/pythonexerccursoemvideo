#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('\033[1:33m*\033[m'*25)

print('\033[1:34mO maior peso foi\033[m \033[1:31m{}\033[m'.format(maior))

print('\033[1:33m*\033[m'*25)

print('\033[1:34mO menor peso foi\033[m \033[1:31m{}\033[m'.format(menor))


