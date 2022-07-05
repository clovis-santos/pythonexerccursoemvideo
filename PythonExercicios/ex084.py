#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

'''Minha solução
lista1 = []
lista2 = []
peso = []
cont = 0
while True:
    lista1.append(str(input('Nome: ')))
    lista1.append(float(input('Peso: ')))
    lista2.append(lista1[:])
    peso.append(lista1[1])
    lista1.clear()
    cont += 1
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'\nForam cadastradas \033[1:31m{cont}\033[m pessoas na lista')
print(f'\nO maior peso foi de \033[1:34m{max(peso)}kg\033[m. Peso de ', end='')
for p in lista2:
    if p[1] == max(peso):
        print(f'\033[1:33m{p[0]}\033[m ', end='')
print(f'\nO menor peso foi de \033[1:34m{min(peso)}kg\033[m. Peso de ', end='')
for p in lista2:
    if p[1] == min(peso):
        print(f'\033[1:33m{p[0]}\033[m ', end='') '''

# Solução Guanabara

temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()

    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()





