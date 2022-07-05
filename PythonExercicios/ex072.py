#Exercício Python 072: Crie um programa que tenha uma tupla totalmente
# preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
            'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
            'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
            'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    while True:
        n = int(input('\nDigite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('\n\033[1:31mNúmero inválido!!!\033[m')

    print(f'Você digitou o número \033[1:33m{contagem[n]}\033[m')
    cont = str(input('\n\033[1:36mDeseja continuar? [S/N]: \033[m'))
    if cont in 'Nn':
        print('\n\033[1:31mFIM!!!\033[m')
        break



