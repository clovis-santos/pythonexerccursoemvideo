#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
# para cada jogo, cadastrando tudo em uma lista composta.

''' Minha Solução

from random import randint
import time

lista = []

print('-' * 40)
titulo = 'JOGA NA MEGA SENA'
print('\033[1:31m', titulo.center(40),'\033[m')
print('-' * 40)
jogos = int(input('\nQuantos jogos deseja fazer? '))
print()
print('\033[1:33m-=\033[m' * 5, end='')
print(f'\033[1:34m SORTEANDO\033[m \033[1:33m{jogos}\033[m \033[1:34mJOGOS\033[m ', end='')
print('\033[1:33m-=\033[m' * 5)
print()

for i in range(jogos):
    for c in range(6):
        num = randint(1, 60)
        lista.append(num)
    print(f'\033[1:35mJogo {i+1}:\033[m {lista} ')
    time.sleep(1)
    lista.clear()
print()
print('\033[1:33m*\033[m' * 40)
tit = 'BOA SORTE!'
print('\n\033[1:36m', tit.center(40),'\033[m')
'''

# Solução Guanabara

from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print('     JOGA NA MEGA SENA     ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-=' * 5, f'SORTEANDO {quant} JOGOS ', '-=' * 5)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5 , '< BOA SORTE! >', '-=' * 5







