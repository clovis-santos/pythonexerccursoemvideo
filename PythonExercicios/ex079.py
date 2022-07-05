#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
# será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

''' Minha solução
valores = []

while True:
    val = int(input('Digite um valor: '))
    if val in valores:
        print(f'\n\033[1:34mO valor {val} não será adicionado na lista, já existe!\033[m')
    else:
        valores.append(val)

    cont = ' '
    while cont not in 'SN':
        cont = str(input('\nDeseja continuar? [S/N]: ')).strip().upper()[0]
        print('\n',end='')
    if cont == 'N':
        break
valores.sort()
print('\033[1:35m-\033[m' * 60)
print(f'\033[1:31mOs valores digitados em ordem crescente foram\033[m \033[1:33m{valores}\033[m')
print('\033[1:35m-\033[m' * 60)
'''

# Solução Guanabara

numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!!!')
    else:
        print('Valor duplicado! Não vou adicionar...')

    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')






