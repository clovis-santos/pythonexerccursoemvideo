#Exercício Python 008: Escreva um programa que leia um valor em metros e
# o exiba convertido em centímetros e milímetros.

met = float(input('Digite um valor: '))
cent = met * 100
mil = met * 1000

print('A medida de {} metros equivale a {:.0f} centrímetros e a {:.0f} milímetros.'.format(met, cent, mil))
