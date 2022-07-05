#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maior = 0
menor = 0

for c in range(0, 7, 1):
    ano = int(input('Digite o ano do seu nascimento: '))
    anoatual = date.today().year
    idade = anoatual - ano
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1

print('\033[1:33m*\033[m'*80)

print('\033[1:34mDas pessoas que você informou a idade,\033[m \033[1:33m{}\033[m \033[1:34mjá atingiram a Maior Idade.\033[m'.format(maior))

print('\033[1:33m*\033[m'*80)

print('\033[1:34mDas pessoas que você informou a idade,\033[m \033[1:33m{}\033[m \033[1:34mainda não atingiram a Maior Idade.\033[m'.format(menor))

