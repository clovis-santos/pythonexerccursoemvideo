#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
# de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Qual a largura da parede em metros? '))
alt = float(input('Qual a altura da parede em metros? '))
area = larg * alt
tinta = area / 2

print('Para pintar uma area de {} metros quadrados você precisa de {} litros de tinta.'.format(area, tinta))




