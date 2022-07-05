#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em
# um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

n = randint(0, 10)

num = int(input('Tente descobrir o número escolhido pelo computador entre 0 e 10: '))

print('PROCESSANDO...')
sleep(1)

cont = 1

while num != n:
    print('Você Errou!!!')
    cont = cont + 1
    num = int(input('Tente novamente acertar entre 0 e 10: '))
    print('PROCESSANDO...')
    sleep(3)

print('Você venceu o desafio!!! Precisou de {} tentativas para acertar.'.format(cont))
