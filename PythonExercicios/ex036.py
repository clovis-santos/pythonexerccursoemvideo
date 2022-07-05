#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa R$'))
salario = float(input('Qual o salário do comprador R$'))
anos = int(input('Em quantos anos irá pagar? '))

prest = casa / (anos * 12)
salmax = salario * 0.30

if prest <= salmax:
    print('Seu empréstimo foi aprovado com a parcela no valor de \033[34mR${:.2f}'.format(prest))

else:
    print('\033[31mSeu empréstimo não foi aprovado porque ultrapassou 30% do valor do seu salário.')
