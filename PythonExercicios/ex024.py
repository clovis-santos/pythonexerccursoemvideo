#Exercício Python 024: Crie um programa que leia o nome de uma cidade
# diga se ela começa ou não com o nome "SANTO".

#cidade = str(input('Digite o nome da sua cidade: ')).upper()
#di = cidade.split()
#print('SANTO' in di[0])

cidade = str(input('Digite o nome da sua cidade: ')).strip().upper()
print(cidade[:5] == 'SANTO')
