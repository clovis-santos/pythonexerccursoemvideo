#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a
# razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Digite o primeiro Termo de uma PA: '))

print('\033[1:33m*\033[m'*40)

razao = int(input('Digite a Razão de uma PA: '))
ultimo = termo + (11-1) * razao

print('\033[1:33m*\033[m'*115)

print('\033[1:31mCom o Termo inicial\033[m \033[1:34m{}\033[m \033[1:31me a Razão\033[m \033[1:34m{}\033[m\033[1:31m, temos os 10 primeiros Termos de uma PA:\033[m'.format(termo, razao), end=' ')

for c in range(termo, ultimo, razao):
    print('\033[1:35m', c , end=' ' '\033[m')
