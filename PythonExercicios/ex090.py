#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando
# também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

''' Minha Solução

dic = dict()

dic['nome'] = str(input('Nome: '))
dic['media'] = float(input(f"Média de {dic['nome']}: "))

print('\033[1:31m-=\033[m' * 20)

print(f"Nome é igual a {dic['nome']}")
print(f"Média é igual a {dic['media']}")

if dic['media'] < 5:
    print(f'Situação é igual a Reprovado')

elif dic['media'] >= 5 and dic['media'] < 7:
    print(f'Situação é igual a Recuperação')

elif dic['media'] >= 7:
    print(f'Situação é igual a Aprovado')

'''

# Solução Guanabara

aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))

print('\033[1:31m-=\033[m' * 20)

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'

elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'

else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')


