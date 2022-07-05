#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km
# percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos KMs você percorreu com o carro ? '))
dias = int(input('Você alugou o carro por quantos dias ? '))

pagar = (dias * 60) + (km * 0.15)

print('Você irá pagar pelo(s) {:.0f} dia(s) de aluguel do carro e pelos {} KMs rodados o valor total de R${:.2f}'.format(dias, km, pagar))
