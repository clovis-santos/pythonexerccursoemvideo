#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

from random import choice, randint

cont = 0

while True:

    lista = ['Par', 'Impar']
    comp = choice(lista)
    print(f'\033[1:31mO computador falou {comp}\033[m')

    if comp == 'Par':
        print('\033[1:34mEu falei Impar\033[m')
        eu = 'Impar'
        n = randint(0, 10)
        #print(n)
        eunum = int(input('Qual seu número de 0 a 10? '))
        result = (n + eunum)
        print('\033[1:33m-=\033[m' * 20)
        if (result % 2) == 0:
            print('\033[1:31mO resultado foi Par. O computador Ganhou!!!\033[m')
            break
        else:
            print('\033[1:34mO resultado foi Impar. Você Ganhou!!!\033[m')
            cont += 1

    else:
        print('\033[1:34mEu falei Par\033[m')
        eu = 'Par'
        n = randint(0, 10)
        #print(n)
        eunum = int(input('Qual seu número de 0 a 10? '))
        result = (n + eunum)
        print('\033[1:33m-=\033[m' * 20)
        if (result % 2) == 0:
            print('\033[1:34mO resultado foi Par. Você Ganhou!!!\033[m')
            cont += 1
        else:
            print('\033[1:31mO resultado foi Impar. O computador Ganhou!!!\033[m')
            break
    print('\033[1:33m-=\033[m' * 20)
print('\033[1:33m-=\033[m' * 22)
print(f'\033[1:36mGAME OVER - Você obteve {cont} vitórias consecutivas!!!\033[m')


