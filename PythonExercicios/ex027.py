#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.

nome = str(input('Digite seu nome completo: ')).strip()

di = nome.split()

print('O primeiro nome é: {}'.format(di[0]))
print('O último nome é: {}'.format(di[-1]))
