#Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

veloc = float(input('Digite a velocidade do carro: '))

if veloc > 80:
    print('Você foi multado pois ultrapassou a velocidade permitida de 80km/h')
    ac = veloc - 80
    multa = ac * 7
    print('Você ultrapassou {}km/h, vai pagar de multa R${:.2f}.'.format(ac, multa))
