#Exercício Python 047: Crie um programa que mostre na tela todos os números
# pares que estão no intervalo entre 1 e 50.

print('Números: ', end='' '\033[1:31m')
for c in range(2, 51, 2):
    #print('Números: \033[1:31m{}\033[m'.format(c))
    print( c, end=' ')

