#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep
import pygame

print('\033[1:31mVamos Brincar de Jokenpô?\033[m')

print('\033[1:33m*\033[m'*25)

lista = ['Pedra', 'Papel', 'Tesoura']
pc = choice(lista)

print('Digite \033[1:31m1\033[m para \033[31mPedra\033[m')
print('Digite \033[1:34m2\033[m para \033[34mPapel\033[m')
print("Digite \033[1;32m3\033[m para \033[32mTesoura")

print('\033[1:36m=\033[m'*25)

op = int(input('Qual opção? '))

print('\033[1:36mJO\033[m')
sleep(1)
print('\033[1:33mKEN\033[m')
sleep(1)
print('\033[1:35mPÔ\033[m')
sleep(2)

print('\033[1:32m=\033[m'*27)

if op == 1:
    op = 'Pedra'
    if pc == 'Pedra':
        print('O computador jogou \033[1:34m{}\033[m'.format(pc))
        print('Você jogou \033[1:33m{}\033[m'.format(op))
        print('\033[1:32m=\033[m' * 27)
        print('Vocês \033[1:31mEMPATARAM!!!')
    elif pc == 'Papel':
        print('O computador jogou \033[1:34m{}\033[m'.format(pc))
        print('Você jogou \033[1:33m{}\033[m'.format(op))
        print('\033[1:32m=\033[m' * 27)
        print('Você \033[1:31mPERDEU!!!')
    elif pc == 'Tesoura':
        print('O computador jogou \033[1:34m{}\033[m'.format(pc))
        print('Você jogou \033[1:33m{}\033[m'.format(op))
        print('\033[1:32m=\033[m' * 27)
        print('Você \033[1:31mGANHOU!!!')

elif op == 2:
    op = 'Papel'
    if pc == 'Papel':
        print('O computador jogou \033[1:34m{}\033[m'.format(pc))
        print('Você jogou \033[1:33m{}\033[m'.format(op))
        print('\033[1:32m=\033[m' * 27)
        print('Vocês \033[1:31mEMPATARAM!!!')
    elif pc == 'Tesoura':
        print('O computador jogou \033[1:34m{}\033[m'.format(pc))
        print('Você jogou \033[1:33m{}\033[m'.format(op))
        print('\033[1:32m=\033[m' * 27)
        print('Você \033[1:31mPERDEU!!!')
    elif pc == 'Pedra':
        print('O computador jogou \033[1:34m{}\033[m'.format(pc))
        print('Você jogou \033[1:33m{}\033[m'.format(op))
        print('\033[1:32m=\033[m' * 27)
        print('Você \033[1:31mGANHOU!!!')

elif op == 3:
    op = 'Tesoura'
    if pc == 'Tesoura':
        print('O computador jogou \033[1:34m{}\033[m'.format(pc))
        print('Você jogou \033[1:33m{}\033[m'.format(op))
        print('\033[1:32m=\033[m' * 27)
        print('Vocês \033[1:31mEMPATARAM!!!')
    elif pc == 'Pedra':
        print('O computador jogou \033[1:34m{}\033[m'.format(pc))
        print('Você jogou \033[1:33m{}\033[m'.format(op))
        print('\033[1:32m=\033[m' * 27)
        print('Você \033[1:31mPERDEU!!!')
    elif pc == 'Papel':
        print('O computador jogou \033[1:34m{}\033[m'.format(pc))
        print('Você jogou \033[1:33m{}\033[m'.format(op))
        print('\033[1:32m=\033[m' * 27)
        print('Você \033[1:31mGANHOU!!!')

else:
    pygame.init()
    pygame.mixer.music.load('errou.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
    sleep(2)
    print('\033[1:31mOPÇÃO INVÁLIDA!!!\033[m Tente novamente.')







