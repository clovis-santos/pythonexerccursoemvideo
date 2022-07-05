#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Palmeiras.

times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense',
         'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará',
         'Corinthians', 'Atlético Goianiense', 'Bahia', 'Sport', 'Fortaleza EC',
         'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')

#print('\nOs 5 primeiros colocados do Brasileirão de 2020 foram: ', end='')
#for c in range(0,5):
 #   print('\033[1:31m', times[c], '\033[m', end='')
 #   print('\033[1:33m->\033[m', end='')
#print(' \033[1:34mLibertadores\033[m')

print(f'\nOs 5 primeiros colocados do Brasileirão de 2020 foram: \033[1:31m{times[0:5]}\033[m')

#print('\nOs 4 últimos colocados do Brasileirão de 2020 foram: ', end='')
#for i in range(19,15,-1):
 #   print('\033[1:31m', times[i], '\033[m', end='')
  #  print('\033[1:33m->\033[m', end='')
#print(' \033[1:34mRebaixados\033[m\n')

print(f'\nOs 4 últimos colocados do Brasileirão de 2020 foram: \033[1:31m{times[-4:]}\033[m')

print('\nOs 20 times do Brasileirão em ordem alfabética:', end='')
print('\033[1:36m', ', '.join(sorted(times)),'\033[m')

#for cont in range(0, len(times)):
 #   if times[cont] == 'Palmeiras':
  #      print(f'\nO \033[1:32mPalmeiras\033[m está na posição \033[1:31m{cont+1}\033[m\n')

print(f'\nO \033[1:32mPalmeiras\033[m está na posição \033[1:31m{times.index("Palmeiras")+1}ª\033[m\n')

time = str(input('Qual time deseja saber a classificação? '))
for cont in range(0, len(times)):
    if times[cont] == time:
        print(f'\nO time do \033[1:34m{time}\033[m ficou em \033[1:31m{cont+1}º\033[m lugar da classificação')

