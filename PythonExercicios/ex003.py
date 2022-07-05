#Exercício Python 003: Crie um programa que leia dois números e mostre a soma entre eles.

numero1 = int (input('Primeiro número = '))
numero2 = int (input('Segundo número = '))
soma = numero1 + numero2

print('A soma é:',soma)

#print('A soma entre', numero1, 'e', numero2, 'é:', soma)

print('A soma entre {} e {} é {}'.format(numero1, numero2, soma))
