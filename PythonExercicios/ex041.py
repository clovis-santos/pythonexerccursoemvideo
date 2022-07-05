#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

from datetime import date

anonasc = int(input('Digite o ano do seu nascimento: '))

anoatual = date.today().year

idade = anoatual - anonasc

if idade <= 9:
    print('Você tem \033[32m{}\033[m anos sua categoria é \033[31mMIRIM.'.format(idade))

elif idade <= 14:
    print('Você tem \033[32m{}\033[m anos sua categoria é \033[33mINFANTIL.'.format(idade))

elif idade <= 19:
    print('Você tem \033[32m{}\033[m anos sua categoria é \033[34mJÚNIOR.'.format(idade))

elif idade <= 25:
    print('Você tem \033[32m{}\033[m anos sua categoria é \033[35mSÊNIOR.'.format(idade))

else:
    print('Você tem \033[32m{}\033[m anos sua categoria é \033[36mMASTER.'.format(idade))


