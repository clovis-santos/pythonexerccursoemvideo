#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

''' Minha Solução

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

print(f'\033[1:31mForam digitados\033[m \033[1:33m{len(valores)}\033[m \033[1:31mnúmeros\033[m')

valores.sort(reverse=True)

print(f'\n\033[1:34mA lista de valores de forma decrescente é\033[m \033[1:33m{valores}\033[m')

if 5 in valores:
    print(f'\n\033[1:35mO valor 5 está na lista\033[m')

else:
    print(f'\n\033[1:35mO número 5 não está na lista\033[m')
'''

# Solução Guanabara

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')







