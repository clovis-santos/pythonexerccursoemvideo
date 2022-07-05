#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = soma = cont = 0
print('Digite um número ou 999 para Sair - ', end=' ')
n = int(input('Número: '))
while n != 999:
    soma += n
    cont += 1
    print('\nDigite um número ou 999 para Sair - ', end=' ')
    n = int(input('Número: '))

print('\n\033[1:31mForam digitados\033[m \033[1:33m{}\033[m \033[1:31mnúmeros e a soma deles é\033[m \033[1:33m{}\033[m\033[1:31m.'.format(cont, soma))
