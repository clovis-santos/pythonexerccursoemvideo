#Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido
# quando o número solicitado for negativo.

while True:
    tabuada = int(input('Qual a tabuada deseja mostrar? '))
    print('\033[1:33m-=\033[m' * 16)
    if tabuada <= 0:
        break
    for c in range(1, 11):
        print(f'{tabuada} x {c} = {tabuada * c}')
    print('\033[1:33m-=\033[m' * 16)
    print(' ')

print('\033[1:31mFIM!!!\033[m')