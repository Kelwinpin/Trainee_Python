i = 0

conjunto = []
conjuntoQuadratico = []

print('Entre com 10 números para serem elevados ao quadrado:')

while i < 10:
    num = int(input())

    conjunto.append(num)

    i = i + 1

print(conjunto)

i = 0

while i < len(conjunto):
    conjuntoQuadratico.append(conjunto[i]**2)
    i = i + 1

print(conjuntoQuadratico)
