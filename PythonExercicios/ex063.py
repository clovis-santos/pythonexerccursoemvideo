#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

#Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

n = int(input('Quantos termos de uma Sequência de Fibonacci deseja mostrar? '))

cont = 3
ultimo = 1
penultimo = 0
termo = 0

print('\033[1:31m', termo, '\033[m' '\033[1:33m->\033[m', '\33[1:31m', ultimo, '\33[m' '\033[1:33m->\033[m', end=' ')

while cont <= n:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    cont += 1
    print('\033[1:31m', termo, '\033[m''\033[1:33m->\033[m', end=' ')
print('\033[1:34mFIM\033[m')





