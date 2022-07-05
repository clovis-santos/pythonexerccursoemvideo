#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número para conversão: '))

print('Digite 1 para converter o número para Binário')
print('Digite 2 para conventer o número para Octal')
print("Digite 3 para converter o número para Hexadecimal")

op = int(input('Sua opção: '))

if op == 1:
    num = bin(n) [2:]
    base = 'Binário'
    print('O número \033[34m{}\033[m após convertido para \033[31m{}\033[m ficou \033[1:32m{}\033[m.'.format(n, base, num))

elif op == 2:
    num = oct(n) [2:]
    base = 'Octal'
    print('O número \033[34m{}\033[m após convertido para \033[31m{}\033[m ficou \033[1:32m{}\033[m.'.format(n, base, num))

elif op == 3:
    num = hex(n) [2:]
    base = 'Hexadecimal'
    print('O número \033[34m{}\033[m após convertido para \033[31m{}\033[m ficou \033[1:32m{}\033[m.'.format(n, base, num))

else:
    print('Você digitou uma opção inválida!!! Tente novamente.')

