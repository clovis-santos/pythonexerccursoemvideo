#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.


termo = int(input('Digite o primeiro Termo de uma PA: '))

print('\033[1:33m*\033[m'*40)

razao = int(input('Digite a Razão de uma PA: '))

ultimo = 0

print('\033[1:33m*\033[m' * 115)

print(
        '\033[1:31mCom o Termo inicial\033[m \033[1:34m{}\033[m \033[1:31me a Razão\033[m \033[1:34m{}\033[m\033[1:31m, temos os 10 primeiros Termos de uma PA:\033[m'.format(
            termo, razao), end=' ')

while ultimo < 10:
    proximo = termo + (ultimo * razao)
    ultimo = ultimo + 1

    print('\033[1:35m', proximo, end=' ' '\033[m')



