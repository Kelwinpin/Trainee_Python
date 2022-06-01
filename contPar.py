vetor = []
i = 0

print('Digite dez números para contar os números pares:')
contPar=0
while i < 10:
    num = int(input())

    vetor.append(num)

    if num % 2 == 0:
        contPar = contPar + 1
    i = i + 1

print('A quantidade de valores pares é de ' + str(contPar))
