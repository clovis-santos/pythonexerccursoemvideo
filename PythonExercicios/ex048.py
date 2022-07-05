#Exercício Python 048: Faça um programa que calcule a soma entre todos os números ímpares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0

for c in range(1, 501, 2):
    if (c % 3) == 0:
        cont = cont + 1
        soma = soma + c

print(' A soma de todos os números \033[1:33m{}\033[m múltiplos de 3 no intervalo de 1 e 500 é: \033[1:33m{}\033[m.'.format(cont, soma) )