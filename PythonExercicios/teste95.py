cont = 0
time = []
jogador = {}
gols = []
while True:
    jogador['Nome'] = str(input('Digite o nome do jogador: '))
    jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    if jogador['Partidas'] > 0:
        for c in range(0, jogador['Partidas']):
            qgols = int(input(f'  Quantos gols na {c+1}ª partida? '))
            cont += qgols
            gols.append(qgols)
    jogador['Gols'] = gols.copy()
    jogador['Total'] = cont
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    cont = 0
    while True:
        pergunta = str(input('Quer continuar? [S/N]: ')).upper()
        if pergunta == 'S' or pergunta == 'N':
            break
        print('Erro! Digite apenas "S" ou "N".')
    if pergunta == 'N':
        break
print('='*50)
print(f'{"COD":<5} {"NOME":<15} {"GOLS":<15} {"TOTAL":<15}')
for pos, v in enumerate(time):
    print(f'{pos:<5} {v["Nome"]:<15} {v["Gols"]!s:<15s} {v["Total"]:<15}')
print('='*50)
while True:
    pergunta2 = int(input('Mostrar dados de qual jogador? [999 para parar]: '))
    while pergunta2 > len(time)-1 and pergunta2 != 999:
        print('Erro! Digite o número correto:')
        pergunta2 = int(input('Mostrar dados de qual jogador? [999 para parar]: '))
    if pergunta2 == 999:
        break
    print(f'--LEVANTAMENTO DO JOGADOR {time[pergunta2]["Nome"]}:'.upper())
    for c in range(0, len(time[pergunta2]['Gols'])):
        print(f'    No jogo {c+1} fez {time[pergunta2]["Gols"][c]} gol(s).')
    print('='*50)
print()
print('Acabou.')