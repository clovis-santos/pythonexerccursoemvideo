#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

contid = contsexo = contmul = 0
while True:
    print('\033[1:31m        CADASTRE UMA PESSOA\033[m')
    print('\033[1:36m-=\033[m' * 20)
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

    print('\033[1:33m-=\033[m' * 20)

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    print('\033[1:33m-=\033[m' * 20)
    if idade > 18:
        contid += 1

    if sexo == 'M':
        contsexo += 1

    if sexo == 'F' and idade < 20:
        contmul += 1

    if cont == 'N':
        break
print(f'{contid} pessoa(s) tem mais de 18 anos.')
print('\033[1:35m-=\033[m' * 20)
print(f'Foram cadastrados {contsexo} Homens.')
print('\033[1:35m-=\033[m' * 20)
print(f'{contmul} Mulhere(s) tem menos de 20 anos.')
