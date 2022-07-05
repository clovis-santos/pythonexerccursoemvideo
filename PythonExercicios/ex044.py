#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

print('='*20, '\033[1:34mSupermercado CSS\033[m','='*20 )
print('\033[33m*\033[m'*60)

preco = float(input('Qual o preço das compras: R$'))

print('\033[33m*\033[m'*28)

print('\033[1:31mEscolha a forma de pagamento\033[m')

print('\033[33m*\033[m'*60)

print('Digite 1 para à vista dinheiro/cheque: 10% de Desconto')
print('Digite 2 para à vista no cartão: 5% de Desconto')
print("Digite 3 para parcelar em até 2x no cartão: Preço Normal")
print("Digite 4 para parcelar em 3x ou mais no cartão: 20% de Juros")

print('\033[33m*\033[m'*60)

op = int(input('Qual opção: '))

if op == 1:
    pnovo = preco - (preco * 0.10)
    print('\033[36m*\033[m' * 60)
    print('Sua compra de \033[1:31mR${}\033[m, você irá pagar \033[1:31mR${}\033[m.'.format(preco, pnovo))

elif op == 2:
    pnovo = preco - (preco * 0.05)
    print('\033[36m*\033[m' * 60)
    print('Sua compra de \033[1:31mR${}\033[m, você irá pagar \033[1:31mR${}\033[m.'.format(preco, pnovo))

elif op == 3:
    pnovo = preco
    parcelado = pnovo / 2
    print('\033[36m*\033[m' * 60)
    print('Sua compra de \033[1:31mR${}\033[m, você irá pagar \033[1:31m2\033[m parcelas de \033[1:31mR${}\033[m, sendo o total de \033[1:31mR${}\033[m.'.format(preco, parcelado, pnovo))

elif op == 4:
    parc = int(input('Quantas parcelas? '))
    pnovo = preco + (preco * 0.20)
    parcelado = pnovo / parc
    print('\033[36m*\033[m' * 60)
    print('Sua compra de \033[1:31mR${}\033[m, você irá pagar \033[1:31m{}\033[m parcelas de \033[1:31mR${}\033[m, sendo o total de \033[1:31mR${}\033[m.'.format(preco, parc, parcelado, pnovo))

else:
    print('\033[1:31mOPÇÃO INVÁLIDA!!!\033[m Digite novamente a opção de pagamento.')


