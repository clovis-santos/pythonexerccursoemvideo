#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar
# mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.


termo = int(input('Digite o primeiro Termo de uma PA: '))

print('\033[1:33m*\033[m'*40)

razao = int(input('Digite a Razão de uma PA: '))

ultimo = 0

print('\033[1:33m*\033[m' * 115)

print('\033[1:31mCom o Termo inicial\033[m \033[1:34m{}\033[m \033[1:31me a Razão\033[m \033[1:34m{}\033[m\033[1:31m, temos os 10 primeiros Termos de uma PA:\033[m'.format(
                termo, razao), end=' ')

while ultimo < 10:
    proximo = termo + (ultimo * razao)
    ultimo = ultimo + 1

    print('\033[1:35m', proximo, '->', end=' ' '\033[m')
print('\033[1:33mPausa\033[m')

cont = 1

while cont != 0:
    c = 0
    cont = int(input('\nDeseja mostrar mais termos? ou \033[1:34m[ 0 ] Sair\033[m : '))
    while c < cont:
        proximo = proximo + razao
        c += 1
        ultimo += 1
        print('\033[1:35m', proximo, '->', end=' ' '\033[m')

    if cont != 0:
        print('\033[1:33mPausa\033[m')

print('Progressão finalizada com \033[1:31m{}\033[m termos mostrados.'.format(ultimo), '\033[1:33m->->->\033[m', end=' ')

print('\033[1:31mFIM!\033[m')
