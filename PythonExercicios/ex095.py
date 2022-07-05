#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

''' Minha Solução

dici = dict()
lista = list()
gols = list()
somagols = 0

while True:
    nome = str(input('Nome do jogador: '))
    part = int(input(f'Quantas partidas {nome} jogou? '))
    dici['nome'] = nome
    dici['partidas'] = part

    if dici['partidas'] > 0:
        for c in range(1, dici['partidas']+1):
            quantgols = int(input(f"Quantos gols na partida {c}? "))
            somagols += quantgols
            gols.append(quantgols)
    dici['gols'] = gols.copy()
    dici['total'] = somagols
    lista.append(dici.copy())
    dici.clear()
    gols.clear()
    somagols = 0

    print('\033[1:33m-=\033[m' * 17)

    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
    print('\033[1:33m-=\033[m' * 17)

print('\033[1:34m-\033[m' * 45)

print(f'\033[1:31m{"cod.":<8}{"nome":<9}{"gols":>8}{"total":>17}\033[m')
print('\033[1:34m-\033[m' * 45)
for pos, v in enumerate(lista):
    print(f'{pos:<5} {v["nome"]:<14} {v["gols"]!s:<15s} {v["total"]:<20}')
print('\033[1:33m-=\033[m' * 25)
while True:
    pergunta2 = int(input('Mostrar dados de qual jogador? '))
    while pergunta2 > len(lista)-1 and pergunta2 != 999:
        print(f'Erro! Não existe jogador com o código {pergunta2}! Tente novamente')
        print('\033[1:33m-\033[m' * 60)
        pergunta2 = int(input('Mostrar dados de qual jogador? '))
    if pergunta2 == 999:
        break

    print(f'\n\033[31m-- LEVANTAMENTO DO JOGADOR {lista[pergunta2]["nome"]}:\033[m')
    print()
    for c in range(0, len(lista[pergunta2]['gols'])):
        print(f'    No jogo {c+1} fez {lista[pergunta2]["gols"][c]} gol(s).')
    print('\033[1:35m-\033[m' * 50)
print()
print('<<  VOLTE SEMPRE  >>')


'''

# Solução Guanabara

time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')

