#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e
# do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

opost = float(input('Digite o comprimento do cateto oposto: '))
adjac = float(input('Digire o comprimento do cateto adjacente: '))
hip = (opost ** 2 + adjac ** 2) ** (1/2)
print('Com o comprimento do cateto oposto {} e o comprimento do cateto adjacente {} '
     'temos o comprimento da hipotenusa {:.2f}.'.format(opost, adjac, hip))


'''import math

opost = float(input('Digite o comprimento do cateto oposto: '))
adjac = float(input('Digite o comprimento do cateto adjacente: '))

print('Com o comprimento do cateto oposto {} e o comprimento do cateto adjacente {} '
     'temos o comprimento da hipotenusa {:.2f}.'.format(opost, adjac, math.hypot(opost, adjac)))'''


'''from math import hypot

opost = float(input('Digite o comprimento do cateto oposto: '))
adjac = float(input('Digite o comprimento do cateto adjacente: '))

print('Com o comprimento do cateto oposto {} e o comprimento do cateto adjacente {} '
      'temos o comprimento da hipotenusa {:.2f}.'.format(opost, adjac, hypot(opost, adjac)))'''
