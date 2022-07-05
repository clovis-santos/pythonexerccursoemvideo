#Exercício Python 005: Faça um programa que leia um número Inteiro e
# mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
ant = n - 1
suc = n + 1
print('O número antecessor de {} é: {} e seu sucessor é: {}'.format(n, ant, suc))

print('O número antecessor de {} é: {} e seu sucessor é: {}'.format(n, (n-1), (n+1)))