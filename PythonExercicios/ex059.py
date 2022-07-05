#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

op = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

while op != 5:
    print('\033[1:31mQual operação deseja realizar com os valores?\033[m')
    print('\033[1:32m[ 1 ] Somar\033[m')
    print('\033[1:33m[ 2 ] Multiplicar\033[m')
    print('\033[1:34m[ 3 ] Maior\033[m')
    print('\033[1:35m[ 4 ] Novos números\033[m')
    print('\033[1:36m[ 5 ] Sair\033[m')
    op = int(input('\033[1:37mOpção: \033[m'))

    while op < 1 or op > 5:
        op = int(input('\nOpção Inválida!!! Digite novamente a opção: '))

    if op == 1:
        soma = n1 + n2
        print('\n\033[1:34mA soma dos valores {} e {} é\033[m \033[1:31m{}\033[m'.format(n1, n2, soma))

    elif op == 2:
        mult = n1 * n2
        print('\n\033[1:34mO resultado da multiplicação dos valores {} e {} é\033[m \033[1:31m{}\033[m'.format(n1, n2, mult))

    elif op == 3:
        if n1 > n2:
            maior = n1
            print('\n\033[1:34mO maior valor é\033[m \033[1:31m{}\033[m'.format(maior))
        elif n2 > n1:
            maior = n2
            print('\n\033[1:34mO valor maior é\033[m \033[1:31m{}\033[m'.format(maior))
        else:
            print('\n\033[1:34mOs valores são iguais.\033[m')
    elif op == 4:
        n1 = int(input('\nDigite um novo valor: '))
        n2 = int(input('Digite outro valor: '))

    print('\033[1:38m=-=\033[m' * 18)


print('\n\033[1:31mFIM!!!\033[m')

