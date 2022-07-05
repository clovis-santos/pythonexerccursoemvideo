#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e
# mostre seu novo salário, com 15% de aumento.

sal = float(input('Digite o salário do funcionário R$'))
#nsal = sal + sal * 0.15

nsal = sal + (sal * 15 / 100)

print('Após o aumento de 15% o novo salário do funcionário é R${}'.format(nsal))

print('O salário atual do funcionário é R${:.2f}, com o aumento de 15% ficará R${:.2f}'.format(sal, nsal))