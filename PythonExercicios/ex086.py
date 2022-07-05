#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha
# com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

''' Minha Solução
matriz = []
linha = []

for i in range(3):
    for c in range(3):
        linha.append(int(input(f'Digite um valor para [{i},{c}]: ')))
    matriz.append(linha[:])
    linha.clear()
print(matriz[0])
print(matriz[1])
print(matriz[2])
'''

# Solução Guanabara

matriz = [[0,0,0], [0,0,0], [0,0,0]]
for lin in range(0,3):
    for col in range(0,3):
        matriz[lin][col] = int(input(f'Digite um valor para [{lin}, {col}]: '))
print('-=' * 30)
for lin in range(0,3):
    for col in range(0,3):
        print(f'[{matriz[lin][col]:^5}]', end='')
    print()






