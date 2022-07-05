#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).****
#- Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()

print('O nome em maiúsculo é {}'.format(nome.upper()))
print('O nome em minúsculo é {}'.format(nome.lower()))

#di = nome.split()
#ad = ''.join(di)

#print('O nome {} tem {} letras ao todo'.format(nome, len(ad)))
#print('O primeiro nome é {} e tem {} letras'.format(di[0], len(di[0])))

print('O nome {} tem {} letras ao todo'.format(nome, len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras'.format(nome.find(' ')))

