lista = []
i = 0

input('Entre com um valor:')
while i < 8:
    num = int(input())
    lista.append(num)
    i = i + 1

print(lista)
escolhaX = int(input('Escolha um valor entre 0 e 7:'))
escolhaY = int(input('Escolha um valor entre 0 e 7:'))

if escolhaX > len(lista) or escolhaX == len(lista):
    print('Posição não existente no vetor para a escolha X')
elif escolhaY > len(lista) or escolhaY == len(lista):
    print('Posição não existente no vetor para a escolha Y')
else:
    soma = lista[escolhaX]+lista[escolhaY]
    print(str(lista[escolhaX])+'+'+str(lista[escolhaY])+'='+ str(soma))
