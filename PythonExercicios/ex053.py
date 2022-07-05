#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela
# é um palíndromo, desconsiderando os espaços.
#Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA,
# O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]'''

if inverso == junto:
    print('\033[1:31mTemos um Palindromo!')
else:
    print('\033[1:34mNão temos um Palindromo!')

