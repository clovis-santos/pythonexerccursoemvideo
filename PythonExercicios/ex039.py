#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anonasc = int(input('Digite o ano do seu nascimento: '))

anoatual = date.today().year

idade = anoatual - anonasc

if idade < 18:
    print('Ainda não chegou a hora de se alistar você tem \033[33m{} \033[manos, faltam \033[31m{} \033[manos para o alistamento.'.format(idade, 18-idade))

elif idade == 18:
    print('Você deve se alistar pois está com \033[32m{}\033[m anos que é a idade correta para o alistamento.'.format(idade))

else:
    print('Você deve se alistar pois está com \033[34m{}\033[m anos, já passou \033[31m{}\033[m anos da idade do alistamento.'.format(idade, idade-18))


