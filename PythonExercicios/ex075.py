#Exercício Python 075: Desenvolva um programa que leia quatro valores
# pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

'''tupla = ()
lista = []
for c in range(4):
    n = int(input('Insira um valor: '))
    lista.append(n)
tupla = tuple(lista)
contn9 = tupla.count(9)
if contn9 != 0:
    print(f'O número 9 apareceu {contn9} vez(es) nessa tupla. ')
else:
    print('Não há número 9 nessa tupla')

if 3 in tupla:
    print(f'O número 3 apareceu {tupla.count(3)} vez(es), sendo a primeira vez na posição {tupla.index(3)}.')
else:
    print('Não há número 3 nessa tupla')

print('Nessa tupla temos os números pares: ', end='')

for i in range(len(tupla)):
    if tupla[i] % 2 == 0:
        print(tupla[i], ' ', end='')'''


tupla = (int(input('insira o primero valor: ')),
         int(input('insira o segundo valor: ')),
         int(input('insira o terceiro valor: ')),
         int(input('insira o quarto valor: ')))

print(f'\nVocê digitou os valores {tupla}')

print(f'\nO valor 9 apareceu \033[1:34m{tupla.count(9)}\033[m vez(es)')

if 3 in tupla:
    print(f'\nO valor 3 apareceu na \033[1:33m{tupla.index(3)+1}ª\033[m posição')
else:
    print('\n\033[1:31mO valor 3 não apareceu nessa tupla\033[m')

print(f'\nOs valores pares foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print('\033[1:33m',n,'\033[m', end='')
















