#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente.

''' Minha Solução
lista = []
listapar = []
listaimp = []

while True:
    valores = int(input('Digite um número: '))

    if valores in lista:
        print('Este número já existe na lista!')
    else:
        lista.append(valores)

        if (valores % 2) == 0:
            listapar.append(valores)
        else:
            listaimp.append(valores)

    cont = ' '
    while cont not in 'SN':
        cont = str(input('\nDeseja continuar? [S/N]: ')).strip().upper()[0]
        print('\n', end='')
    if cont == 'N':
        break

print('\033[1:36m-\033[m' * 45)
print(f'\033[1:31mA lista inteira é\033[m \033[1:33m{lista}\033[m')
print('\033[1:36m-\033[m' * 45)
print(f'\033[1:34mA lista só com os números Pares\033[m \033[1:33m{listapar}\033[m')
print('\033[1:36m-\033[m' * 45)
print(f'\033[1:35mA lista só com os números Ímpares\033[m \033[1:33m{listaimp}\033[m')
print('\033[1:36m-\033[m' * 45)
'''


# Solução Guanabara

num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de Pares é {pares}')
print(f'A lista de Ímpares é {impares}')





