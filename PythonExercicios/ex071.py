#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


cont50 = cont20 = cont10 = cont1 = 0

valor = int(input('Qual valor deseja sacar? R$ '))

while True:
    while valor >= 50:
        cont50 += 1
        valor -= 50

    while valor >= 20:
        cont20 += 1
        valor -= 20

    while valor >= 10:
        cont10 += 1
        valor -= 10

    while valor >= 1:
        cont1 += 1
        valor -= 1
    break

print(f'\033[1:31mNo seu saque serão entregues {cont50} nota de R$50,00\033[m')
print(f'\033[1:33mNo seu saque serão entregues {cont20} nota de R$20,00\033[m')
print(f'\033[1:34mNo seu saque serão entregues {cont10} nota de R$10,00\033[m')
print(f'\033[1:36mNo seu saque serão entregues {cont1} nota de R$1,00\033[m')




