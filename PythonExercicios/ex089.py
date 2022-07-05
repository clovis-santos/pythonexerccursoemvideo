#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e
# guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.

''' Minha Solução
aluno = []
lista = []

while True:
    aluno.append(str(input('Nome do aluno: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    lista.append(aluno[:])
    aluno.clear()

    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
c = 0
print('\033[1:38m-\033[m'*50)
print(f'\n\033[1:31m{"Num.":<8}{"Nome":<12}{"Média":<4}\033[m')
print('\033[1:33m=\033[m'*30)
for p in lista:
    print(f'\033[1:34m{c:<8}\033[m\033[1:35m{p[0]:<12}\033[m\033[1:36m{(p[1] + p[2])/ 2:.2f}\033[m')
    c += 1
print('\033[1:33m=\033[m' * 30)
print()
while True:
    a = int(input('Quer mostrar as notas de qual aluno? (999 interrompe): '))
    if a == 999:
        break
    print(f'\nNotas de \033[1:35m{lista[a][0]}\033[m foram \033[1:36m{lista[a][1]}\033[m e \033[1:36m{lista[a][2]}\033[m')
    print()
print()
print('\033[1:33m*\033[m'*10, end='')
print('\033[1:31m FIM! \033[m',end='')
print('\033[1:33m*\033[m'*10)
'''

# Solução Guanabara

ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"Nº.":<8}{"NOME":<9}`{"MÉDIA":>8}')
print('-' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<8}{a[0]:<9}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')


