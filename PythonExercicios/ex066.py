#Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

s = qtd = 0
while True:
    n = int(input('Digite um número ou [999] para Sair: '))
    if n == 999:
        break
    s += n
    qtd += 1
print(f'A soma dos {qtd} números digitados é {s}')
