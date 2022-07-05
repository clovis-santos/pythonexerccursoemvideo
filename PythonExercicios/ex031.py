#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Qual a distância da sua viagem?: '))

if dist <= 200:
    pre = dist * 0.50
else:
    pre = dist * 0.45

#pre = dist * 0.50 if dist <= 200 else dist * 0.45

print('Para sua viagem de {}kms você irá pagar R${:.2f} pela passagem.'.format(dist, pre))
