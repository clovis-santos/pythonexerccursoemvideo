#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite seu salário R$'))

if sal > 1250:
    novosal = sal + (sal * 0.10)
else:
    novosal = sal + (sal * 0.15)

print('Após o aumento seu novo salário é R${:.2f}'.format(novosal))

