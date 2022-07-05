#Exercício Python 076: Crie um programa que tenha uma tupla única
# com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('\033[1:33m-\033[m' * 40)

titulo = 'LISTAGEM DE PREÇOS'

print('\033[1:31m',titulo.center(36),'\033[m')

print('\033[1:33m-\033[m' * 40)

produtos = ('Maça', 10.50, 'Uva', 15, 'Banana', 5.99, 'Ovo', 12, 'Arroz', 20.75)

subtitulo1 = 'Produtos'
subtitulo2 = 'Preço'
subtitulo3 = '|'

print('\033[1:34m',subtitulo1.center(10),subtitulo3.center(16), subtitulo2.center(10),'\033[m')

print('\033[1:33m-\033[m' * 40)

for i, j in zip(range(0, len(produtos), 2), range(1, len(produtos), 2)):
   print(f'{produtos[i]:.<30}R${produtos[j]:>6.2f} ')

print('\033[1:33m-\033[m' * 40)








