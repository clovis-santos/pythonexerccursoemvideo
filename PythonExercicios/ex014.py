#Exercício Python 014: Escreva um programa que converta uma temperatura digitando
# em graus Celsius e converta para graus Fahrenheit.

cel = float(input('Digite a temperatura em graus Celsius: '))
#fah = cel * 1.8 + 32

fah = ((9 * cel) / 5) + 32

print('Após a conversão de {} graus Celsius temos {:.2f} graus Fahrenheit'.format(cel, fah))