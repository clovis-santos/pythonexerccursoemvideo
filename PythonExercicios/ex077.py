#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


palavras = ('Gratuito', 'Proibido', 'Rubrica', 'Recorde', 'Menu')

for c in palavras:
    print(f'\nNa palavra \033[1:31m{c.upper()}\033[m temos ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print('\033[1:33m',letra,'\033[m', end='')
    print('vogais', end='')

