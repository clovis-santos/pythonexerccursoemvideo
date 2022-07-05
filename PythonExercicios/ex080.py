#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco
# valores numéricos e cadastre-os em uma lista, já na posição correta de
# inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

''' Minha solução
valores = []

for cont in range(5):
    valor = int(input('Digite um valor: '))
    for c, i in enumerate(valores):
        if valor < i:
            valores.insert(c, valor)
            break
    else:
        valores.append(valor)

print(f'\n\033[1:31mA lista ordenada é\033[m \033[1:34m{valores}\033[m')
'''

# Solução Guanabara

lista = []
for c in range(0,5):
    n = int(input('Diigite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')



