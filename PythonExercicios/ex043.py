#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está com o IMC \033[35m{:.2f}\033[m, portanto está \033[1:35mABAIXO\033[m do Peso.'.format(imc))

elif 18.5 >= imc < 25:
    print('Você está com o IMC \033[32m{:.2f}\033[m, portanto está no \033[1:32mPESO IDEAL.'.format(imc))

elif 25 >= imc < 30:
    print('Você está com o IMC \033[33m{:.2f}\033[m, portanto está com \033[1:33mSOBRE PESO.'.format(imc))

elif 30 >= imc < 40:
    print('Você está com o IMC \033[36m{:.2f}\033[m, portanto está com \033[1:36mOBESIDADE.'.format(imc))

else:
    print('Você está com o IMC \033[31m{:.2f}\033[m, portanto está com \033[1:31mOBESIDADE MÓRBIDA.'.format(imc))









