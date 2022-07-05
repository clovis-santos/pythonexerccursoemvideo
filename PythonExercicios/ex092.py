#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de
# trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
# além da idade, com quantos anos a pessoa vai se aposentar.

''' Minha Solução

from datetime import date
dici = dict()
nome = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
cart = int(input('Carteira de Trabalho (0 não tem): '))
anoatual = date.today().year
idade = anoatual - ano

dici['nome'] = nome
dici['idade'] = idade
dici['ctps'] = cart

if cart != 0:
    contra = int(input('Ano de contratação: '))
    sal = float(input('Salário: R$'))
    dici['ano de contratação'] = contra
    dici['salário'] = sal
    contri = 35 - (anoatual - dici['ano de contratação'])
    dici['aposentadoria'] = idade + contri

print('\033[1:31m-=\033[m' * 20)

for c, v in dici.items():
    print(f'  ** {c} tem o valor {v}')

'''

# Solução Guanabara

from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 25)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')