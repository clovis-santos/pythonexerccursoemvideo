#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

''' Minha Solução

matriz = []
linha = []
somapar = somacol2 = maior = 0

for i in range(3):
    for c in range(3):
        linha.append(int(input(f'Digite um valor para [{i},{c}]: ')))
        if linha[c] % 2 == 0:
            somapar += linha[c]
        if c == 2:
            somacol2 += linha[c]
    matriz.append(linha[:])
    linha.clear()

print('-=' * 30)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('-=' * 30)
maior = max(matriz[1])
print(f'A soma dos valores Pares digitados é {somapar}')
print(f'A soma dos valores digitados na terceira coluna é {somacol2}')
print(f'O maior valor da segunda linha é {maior}')
'''

# Solução Guanabara

matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = maior = scol = 0
for lin in range(0,3):
    for col in range(0,3):
        matriz[lin][col] = int(input(f'Digite um valor para [{lin}, {col}]: '))
print('-=' * 30)
for lin in range(0,3):
    for col in range(0,3):
        print(f'[{matriz[lin][col]:^5}]', end='')
        if matriz[lin][col] % 2 == 0:
            spar += matriz[lin][col]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for lin in range(0,3):
    scol += matriz[lin][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for col in range(0,3):
    if col == 0 or matriz[1][col] > maior:
        maior = matriz[1][col]
print(f'O maior valor da segunda linha é {maior}')


