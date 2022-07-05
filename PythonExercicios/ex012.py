#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e
# mostre seu novo preço, com 5% de desconto.

preco = float(input("Informe o preço do produto: R$"))
#novopre = preco - preco * 0.05

novopre = preco - (preco * 5 / 100)

print('Após o desconto de 5% o novo preço do produto é R${:.2f}'.format(novopre))

print('O preço do produto é R${:.2f}, com o desconto de 5% ficará R${:.2f}'.format(preco, novopre))