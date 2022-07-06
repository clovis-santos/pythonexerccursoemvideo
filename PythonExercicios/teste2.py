compras =[]

resp = "s"

while resp == "s":
    compras.append(input("Digite o item da Lista: "))
    resp = input("Deseja continuar - s para Sim ou n pra Não: ")
for x in compras:
    if x == "banana":
        print("Encontrei a banana!!!")
    else:
        print("Não encontrei a banana!!!")
        


#Mais algumas alterações para testar o Revert na aula de Git/GitHub