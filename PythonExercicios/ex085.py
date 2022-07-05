#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

''' Minha Solução

lista = []
listapar = []
listaimpar = []

for cont in range(1,8):
    valor = int(input(f'Digite o {cont}º valor: '))
    if (valor % 2) == 0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)
    listapar.sort()
    listaimpar.sort()
lista.append(listapar[:])
print('-=' * 30)
print(f'Os valores Pares digitados foram: {lista}')
lista.clear()
lista.append(listaimpar[:])
print(f'Os valores Ímpares digitados foram: {lista}')
'''

# Solução Guanabara

num = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}°. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')




