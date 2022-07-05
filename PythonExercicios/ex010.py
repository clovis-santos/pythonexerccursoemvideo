#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dólares ela pode comprar.

di = float(input('Quanto dinheiro você tem em sua carteira? R$'))
dol = di / 3.27

print('Com R${:.2f} eu consigo comprar US${:.2f}'.format(di, dol))

