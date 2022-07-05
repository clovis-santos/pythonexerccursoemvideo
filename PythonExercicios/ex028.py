#Exercício Python 028: Escreva um programa que faça o computador "pensar"
# em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
# o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

n = randint(0, 5)

num = int(input('Tente descobrir o número escolhido pelo computador entre 0 e 5: '))

print('PROCESSANDO...')
sleep(3)

if num == n:
    print('Você venceu o desafio!!!')
else:
    print('Você perdeu o desafio!!! O computador pensou no número {}'.format(n))
