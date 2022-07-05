#Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número: '))

print('\033[1:33m*\033[m'*22)

print('\033[1:31mA Tabuada do número\033[m \033[1:34m{}\033[m:'.format(n))

print('\033[1:33m*\033[m'*22)

for c in range(1, 11, 1):
    print('\033[1:32m{}\033[m \033[1:35mx\033[m \033[1:32m{:2}\033[m \033[1:35m=\033[m \033[1:36m{}\033[m'.format(n, c, n * c))

