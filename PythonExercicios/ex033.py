#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.****

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

#lista = [n1, n2, n3]
#print('O maior número é {}'.format(max(lista)))
#print('O menor número é {}.format(min(lista)))
'''
maior = n1
menor = n1

if n1 < n2:
    maior = n2
    if maior < n3:
        maior = n3

if n1 > n2:
    menor = n2
    if menor > n3:
        menor = n3
print('O maior número é {}.'.format(maior))
print('O menor número é {}.'.format(menor))
'''
menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor número é {}.'.format(menor))
print('O maior número é {}.'.format(maior))




