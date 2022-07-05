#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela
# é um palíndromo, desconsiderando os espaços.
#Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA,
# O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

def palindromo(frase):
    frase = frase.lower()

    if ' ' in frase:
        semcarac = ' ,.;:?!-'
        texto = [c for c in frase if c not in semcarac]
    else:
        texto = frase
    inicio = 0
    fim = len(texto)-1
    for i in range(len(texto)//2):
        if texto[inicio] != texto[fim]:
            return False
            inicio = inicio + 1
            fim = fim - 1
        return True


frase = str(input('Digite a frase: '))

pali = palindromo(frase)

if pali == True:
    print('A Frase digitada é um Palindromo!!!')
else:
    print('A Frase digita não é um Palindromo!!!')



