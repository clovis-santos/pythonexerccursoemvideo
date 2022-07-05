#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor
# valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continuar = 'S'
soma = cont = maior = menor = 0

while continuar == 'S':
    n = int(input('\nDigite um número: '))
    soma += n
    cont += 1

    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    continuar = str(input('\nDigite [ S ] Continuar ou [ N ] Sair: ')).strip().upper()
media = soma / cont

print('\n\033[1:31mA Média entre os\033[m \033[1:34m{}\033[m \033[1:31mnúmeros digitados é\033[m \033[1:33m{}\033[m\033[m.'.format(cont, media))
print('\n\033[1:31mO Maior número digitado foi\033[m \033[1:33m{}\033[m.'.format(maior))
print('\n\033[1:31mO Menor número digitado foi\033[m \033[1:33m{}\033[m.'.format(menor))




