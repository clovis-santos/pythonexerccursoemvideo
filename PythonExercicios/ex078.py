#Exercício Python 078: Faça um programa que leia 5 valores numéricos e
# guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.
'''Minha solução
valores = []
maior = []
menor = []

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print(f'Os números digitados da lista foram {valores}')

for c, v in enumerate(valores):
    if v == max(valores):
        maior.append(c)
    if v == min(valores):
        menor.append(c)
print(f'O menor número da lista foi {min(valores)} que está na posição {menor}')
print(f'O maior número da lista foi {max(valores)} que está na posição {maior}')
'''
# Solução Guanabara

listanum =[]
maior = 0
menor = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para Posição {c}: ')))
    if c == 0:
        maior =  menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]

print('=-' * 30)
print(f'Você digitou os valores {listanum}')

print(f'O maior valor digitado foi {maior} nas posições ', end='')

for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print()

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
print()



