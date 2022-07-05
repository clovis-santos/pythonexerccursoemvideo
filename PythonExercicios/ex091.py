#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

''' Minha Solução
from random import randint
from time import sleep

jogos = dict()
print('\033[1:33m-=\033[m' * 15)
print('\033[1:31m      Valores sorteados:\033[m')
print('\033[1:33m-=\033[m' * 15)
for j in range(1, 5):
    jogos[f'jogador{j}'] = randint(1,6)

for c, v in jogos.items():
    print(f'   O {c} tirou {v}')
    sleep(1)

print('\033[1:33m-=\033[m' * 16)
print('\033[1:34m     Ranking dos jogadores:\033[m')
print('\033[1:33m-=\033[m' * 16)

ord_dict = sorted(jogos.items(), key=lambda t: t[1], reverse=True)

for chave, valor in enumerate(ord_dict):
    print(f'{chave+1}º lugar: {valor[0]} com {valor[1]} pontos')
    sleep(1)

'''

# Solução Guanabara

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
        'jogador3': randint(1, 6), 'jogadir4': randint(1, 6)}

ranking = dict()

print('\033[1:31m     Valores sorteados:\033[m')
print('\033[1:33m-\033[m' * 30)
for k, v in jogo.items():
    print(f'  {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('\033[1:33m-=\033[m' * 15)
print('\033[1:34m ==  RANKING DOS JOGADORES  == \033[m')
print('\033[1:33m-=\033[m' * 15)
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
