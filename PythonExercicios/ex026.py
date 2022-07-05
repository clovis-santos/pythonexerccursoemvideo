#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e
# mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e
# em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()

print('A letra *A* aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra *A* apareceu a primeira vez na posição {} da frase.'.format(frase.find('A')+1))
print('A letra *A* apareceu a ultima vez na posição {} da frase.'.format(frase.rfind('A')+1))
