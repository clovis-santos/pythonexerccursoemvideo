#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

total = contproduto = menor = conta = 0
barato = ''

print('\033[1:33m=\033[m' * 35)
print('\033[1:31m          LOJÃO DO CLOVÃO\033[m')
print('\033[1:33m=\033[m' * 35)

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))

    print('\033[1:35m-\033[m' * 35)

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    print('\033[1:35m-\033[m' * 35)

    total += preco

    if preco > 1000:
        contproduto += 1

    conta += 1

    if conta == 1 or preco < menor:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome

    if cont == 'N':
        break
print(f'O total gasto na compra é R${total:.2f}')

print(f'{contproduto} produtos custam mais de R$1.000.')

print(f'O produto mais barato foi {barato} que custa R${menor:.2f}.')
