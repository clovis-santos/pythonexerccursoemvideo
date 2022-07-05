#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
# quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

''' Minha Solução

dici = dict()
nome = str(input('Nome do jogador: '))
part = int(input(f'Quantas partidas {nome} jogou? '))
dici['nome'] = nome
lista = list()

for c in range(1, part+1):
    lista.append(int(input(f"Quantos gols na partida {c}? ")))
soma = sum(lista)
dici['gols'] = lista
dici['total'] = soma

print('\033[1:33m-=\033[m' * 30)

print(dici)

print('\033[1:33m-=\033[m' * 30)

print(f"O campo nome tem o valor {dici['nome']}.")
print(f"O campo gols tem o valor {dici['gols']}.")
print(f"O campo total tem o valor {dici['total']}.")

print('\033[1:33m-=\033[m' * 30)

print(f"O jogador {dici['nome']} jogou {part} partidas.")

for i in range(0, part):
    print(f'    => Na partida {i+1}, fez {lista[i]} gols.')

print(f"Foi um total de {dici['total']}.")

'''

# Solução Guanabara

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i+1}, fez {v} gols. ')
print(f"Foi um total de {jogador['total']} gols.")