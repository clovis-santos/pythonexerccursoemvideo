#Exercício Python 006: Crie um algoritmo que leia um número e
# mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
dob = n * 2
tri = n * 3
qua = n**(1/2)
print('O dobro do número {} é: {}\nO triplo do número {} é: {}\nA raiz quadrada do número {} é: {:.2f}'.format(n, dob, n, tri, n, qua))

print('O dobro do número {} é: {}\nO triplo do número {} é: {}\nA raiz quadrada do número {} é: {:.2f}'.format(n, (n*2), n, (n*3), n, (n**(1/2))))

